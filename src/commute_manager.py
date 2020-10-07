# python modules ---------------------
import logging
import sys
import configparser
from pathlib import Path

# user modules ---------------------
import Email.email_manager as email_manager
import Lib.error_manager as error_manager
from Commute.bike import bike as bikeClass
from Commute.car import car as carClass
from Commute.train import train as trainClass


# Globals ---------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Private functions ---------------------
def checkEnvironment():
    if not sys.version_info.major == 3 and sys.version_info.minor >= 5:
        logger.critical("You are using Python %s.%s."\
                        ,sys.version_info.major, sys.version_info.minor)
        logger.critical("At least python 3.5 is required. Exiting ...")
        sys.exit(1)

def readConfigs():
    config = configparser.ConfigParser()
    configPath = (Path(__file__) / ".." / ".." / "user_config.ini").resolve()
    config.read(configPath)
    return config

def initializeEmail(config):
    email = email_manager.email(config["EMAIL"]["ADDRESS"], \
                                config["EMAIL"]["PASSWORD"])
    email.setupEmailServer(config["EMAIL"]["PORT"])
    return email

def initializeCommuter(config):
    commuters = []
    if "BIKE" in config:
        bike = bikeClass(config["ROUTE"], config["BIKE"])
        commuters.append(bike)
    if "TRAIN" in config:
        train = trainClass(config["TRAIN"])
        commuters.append(train)
    if "CAR" in config:
        car = carClass(config["ROUTE"], config["CAR"], config["GENERAL"]["GOOGLE_API_KEY"])
        commuters.append(car)
    print(commuters)
    return commuters  

def calculateCommutes(commuters):
    for commuter in commuters:
        commuter.calculateCommute()
    return commuters

def getDefaultCommputer(commutersResolved, defaultCommuter):
    for commuter in commutersResolved:
        if commuter.name == defaultCommuter:
            return commuter

def generateSummary(commuters, defaultCommuter):
    if not commuters:
        logger.error("Failed to create commuter summary because the list of cummuters was empty")
    summary = ""
    summary += "A threshold of " + defaultCommuter + " is expected to be violated.\n"
    for commuter in commuters:
        summary += commuter.name + ":" + "\n"
        for treshold in commuter.tresholds:
            summary += "Treshold" + treshold.name + ": " + treshold.treshold + "\n"
            summary += "Estimation: " + treshold.name + ": " + treshold.estimation +"\n"
    return summary

if __name__ == "__main__":
    checkEnvironment()
    config = readConfigs()
    email = initializeEmail(config)
    commutersInit = initializeCommuter(config)
    commutersResolved = calculateCommutes(commutersInit)
    defaultCommuter = config["GENERAL"]["DEFAULT_COMMUTER"]
    #if getDefaultCommputer(commutersResolved, defaultCommuter).isTresholdViolated:
    if True:
        summaryString = generateSummary(commutersResolved, defaultCommuter)
        email.sendEmail(summaryString, "Commute warning")
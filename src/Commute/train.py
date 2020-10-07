# Web scraping can be done by a wide range of python modules, with the most common one beeing 'beautifull soup'.
# Web automation is done almost exclusively by the 'Selenium' python package that already comes with a scraper.
# Web automation always requires both a browser and an additional driver tool. The driver tool can be a 
# browser plugin, a python module or a local installation. 
# Some of the tutorials use firefox, yet most of them prefer chromium.
# 
#   Choosen automation setup: Chromium + chromium-chromedriver
#
#   install: https://www.youtube.com/watch?v=4TuawlLrWaY
#   usage: https://www.youtube.com/watch?v=QPp0UrefaZo
#   run headless: https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programmatically-in-selenium-with-python
#
#   Website to scrape: 'https://reiseauskunft.bahn.de/bin/query.exe/dn?protocol=https:'

import logging

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Commute.commute import commuteClass
from Lib.helpers import treshold

logger = logging.getLogger(__name__)


class train(commuteClass):
    def __init__(self, config):
        self.name = "TRAIN"
        self._TRAIN_STATION_START = config["TRAIN_STATION_START"]
        self._TRAIN_STATION_DESTINATION = config["TRAIN_STATION_DESTINATION"]
        self._TRAIN_ID = config["TRAIN_ID"]
        tresholds = []
        tresholds.append(treshold("TRESHOLD_LATENESS", config["TRESHOLD_LATENESS"]))
        super().__init__(tresholds)
        return

    def calculateCommute(self):
        #searchBox.send_keys(Keys.RETURN)
        binary = r'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        options = Options()
        # reenable to run headless
        # options.set_headless(headless=True)
        options.binary = binary
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = True #optional
        driver = Firefox(firefox_options=options, capabilities=cap, executable_path="C:\\Users\\lukas\\Documents\\Skripte\\geckodriver.exe")
        driver.get("https://reiseauskunft.bahn.de/bin/query.exe/dn?protocol=https:")
        searchTrainstationStart = driver.find_element_by_id("locS0")
        searchTrainstationStart.send_keys(self._TRAIN_STATION_START)
        searchTrainstationDestination = driver.find_element_by_id("locZ0")
        searchTrainstationDestination.send_keys(self._TRAIN_STATION_DESTINATION)
        searchButton = driver.find_element_by_id("searchConnectionButton")
        searchButton.click()
        try:
            i = 0
            results = []
            while(i < 3):
                resultBody = WebDriverWait(driver, 10).until(
                             EC.presence_of_element_located((By.ID, "overview_updateC1-" + str(i))))
                results.append(resultBody)
                i += 1
        finally:
            pass
        for result in results:
            # check if the result is suitable
            time = result.find_elements_by_class_name("time")[0].text
            duration = result.find_elements_by_class_name("duration.lastrow")[0].text
            trainId = result.find_elements_by_class_name("products.lastrow")[0].text
            changges = result.find_elements_by_class_name("changes.lastrow")[0].text
            if changes != "0":
                continue
            if duration >= self._TRESHOLD_DURATION:
                continue
            timeStart = ..
            timeDelayedStart = ..
            currentTime = ..
            if timeStart - currentTime > 1h:
                continue
            
        driver.quit()
        return

    def getCommuteSummary(self):
        return

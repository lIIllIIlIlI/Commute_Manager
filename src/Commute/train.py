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
        return

    def getCommuteSummary(self):
        return

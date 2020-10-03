import logging

from Commute.commute import commuteClass
from Lib.helpers import treshold

logger = logging.getLogger(__name__)


class bike(commuteClass):
    def __init__(self, route, config):
        self.name = "BIKE"
        self._START_COORDINATES = route["START_COORDINATES"]
        self._DESTINATION_COORDINATES = route["DESTINATION_COORDINATES"]
        tresholds = []
        tresholds.append(treshold("TRESHOLD_RAIN_PROBABILITY", \
                                 config["TRESHOLD_RAIN_PROBABILITY"]))
        tresholds.append(treshold("TRESHOLD_HEADWIND", \
                                 config["TRESHOLD_HEADWIND"]))
        super().__init__(tresholds)
        return

    def calculateCommute(self):
        return

    def getCommuteSummary(self):
        return
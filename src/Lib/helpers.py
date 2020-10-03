import logging

logger = logging.getLogger(__name__)


class treshold:
    def __init__(self, name, treshold, estimation=""):
        self.name = name
        self.treshold = treshold
        self.estimation = estimation
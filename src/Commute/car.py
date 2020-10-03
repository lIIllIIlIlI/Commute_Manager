# stolen code from 'kiteco/python-youtube-code' 

import logging
try:
    import requests
except:
    # TODO: Report error
    pass

from Commute.commute import commuteClass
from Lib.helpers import treshold

logger = logging.getLogger(__name__)

class car(commuteClass):
    def __init__(self, route, config):
        self.name = "CAR"
        self._START_COORDINATES = route["START_COORDINATES"]
        self._DESTINATION_COORDINATES = route["DESTINATION_COORDINATES"]
        tresholds = []
        tresholds.append(treshold("TRESHOLD_TRAVEL_DURATION", \
                                 config["TRESHOLD_TRAVEL_DURATION"]))
        super().__init__(tresholds)
        return

    def calculateCommute(self):
        return

    def getCommuteSummary(self):
        return

# # home address input
# home = input("Enter a home address\n") 
  
# # work address input
# work = input("Enter a work address\n") 
  
# # base url
# url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

# # get response
# r = requests.get(url + "origins=" + home + "&destinations=" + work + "&key=" + api_key) 
 
# # return time as text and as seconds
# time = r.json()["rows"][0]["elements"][0]["duration"]["text"]       
# seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
  
# # print the travel time
# print("\nThe total travel time from home to work is", time)

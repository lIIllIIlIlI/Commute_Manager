# stolen code from 'kiteco/python-youtube-code' 

import logging
import re
try:
    import requests
except:
    # TODO: Report error
    pass

from Commute.commute import commuteClass
from Lib.helpers import treshold

logger = logging.getLogger(__name__)

class car(commuteClass):
    def __init__(self, route, config, apiKey):
        self.name = "CAR"
        self._apiKey = apiKey
        self._start = route["START_COORDINATES"]
        self._destination = route["DESTINATION_COORDINATES"]
        self.tresholds = []
        self.tresholds.append(treshold("TRESHOLD_TRAVEL_DURATION", \
                                 config["TRESHOLD_TRAVEL_DURATION"]))
        super().__init__(self.tresholds)
        return

    def calculateCommute(self):
        url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial"
        requestUrl = url + "&origins=" + self._start + "&destinations=" + \
            self._destination + "&key=" + self._apiKey
        response = requests.get(requestUrl)
        estimatedTravelTime = response.json()["rows"][0]["elements"][0]["duration"]["text"] 
        estimatedTravelTime = re.search(r'(\d+)', estimatedTravelTime).group(0)
        self.tresholds[0].estimation = estimatedTravelTime
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

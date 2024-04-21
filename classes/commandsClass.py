import datetime
import geocoder
import os


class Commands:
    def __init__(self):
        pass

    def whatIsTheTime(self):
        timeNow = datetime.datetime.now()
        return "{}, the time is: {:%H:%M.%S}".format(os.getlogin(), timeNow)
        # return "{}, the time is: {:%I %M%p}".format("Dom", timeNow)

    def whatIsTheWeather(self):
        g = geocoder.ip('me')
        print(g.city)

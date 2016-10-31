import requests


class Adaptor():

    def __init__(self):
        pass

    def rate(self, answer):
        """ gets the answer as a text and return an integer value as a score """
        pass

    def get(self, url):
        return requests.get(url)

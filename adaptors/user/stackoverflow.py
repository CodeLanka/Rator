from adaptors.Adaptor import Adaptor
import re


class StackoverflowAdaptor(Adaptor):

    def __init__(self):
        pass

    def username(self, answer):
        r = self.get('https://api.stackexchange.com/2.2/users/'+answer+'?order=desc&sort=reputation&site=stackoverflow')
        j = r.json()
        return j['items'][0]['reputation']

    def url(self, answer):
        if answer == "":
            return 0
        else:
            username = re.search(r"http[s]?://stackoverflow.com/users/([a-z0-9]*)", answer).group(1)
            return self.username(username)
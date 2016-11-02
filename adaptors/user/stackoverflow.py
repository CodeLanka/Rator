import math
import json

from adaptors.Adaptor import Adaptor
import re


class StackoverflowAdaptor(Adaptor):

    def __init__(self):
        pass

    def url(self, answer):
        return self.rate(answer)

    def username(self, answer):
        return self.rate(answer)

    def rate(self, answer):
        if answer == "":
            return 0
        else:
            userid = self.get_userid(answer)
            return self.get_score(userid)

    def get_score(self, answer):
        if answer == None:
            return 0
        else:
            r = self.get('https://api.stackexchange.com/2.2/users/'+str(answer)+'?order=desc&sort=reputation&site=stackoverflow')
            j = r.json()
            badges = j['items'][0]['badge_counts']
            return self.do_score_calculation(j['items'][0]['reputation'], badges['bronze'], badges['silver'], badges['gold'])

    def get_userid(self, answer):
        if re.match("^\d+$", answer):
            return answer
        else:
            username = re.search(r"http[s]?://stackoverflow.com/users/([0-9]*)/[0-9a-zA-Z]*", answer).group(1)
            return username

    def do_score_calculation(self, reputation, bronze_badges, silver_badges, gold_badges):
        multiplier = (gold_badges / 2) + (silver_badges / 3) + (bronze_badges / 5)
        score = math.ceil(reputation * (1 + multiplier))
        return score

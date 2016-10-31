import math

from adaptors.Adaptor import Adaptor
import re


class StackoverflowAdaptor(Adaptor):

    def __init__(self):
        pass

    def rate(self, answer):
        return self.url(answer)

    def username(self, answer):
        r = self.get('https://api.stackexchange.com/2.2/users/'+str(answer)+'?order=desc&sort=reputation&site=stackoverflow')
        j = r.json()
        # print(j['items'][0]['reputation'])
        print(j['items'][0]['badge_counts'])
        badges = j['items'][0]['badge_counts']
        return self.get_score(j['items'][0]['reputation'], badges['bronze'], badges['silver'], badges['gold'])

    def url(self, answer):
        if answer == "":
            return 0
        else:
            username = re.search(r"http[s]?://stackoverflow.com/users/([0-9]*)/[0-9a-zA-Z]*", answer).group(1)
            return self.username(username)

    def get_score(self, reputation, bronze_badges, silver_badges, gold_badges):
        multiplier = (gold_badges / 2) + (silver_badges / 3) + (bronze_badges / 5)
        score = math.ceil(reputation * (1 + multiplier))
        return score

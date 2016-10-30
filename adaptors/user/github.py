import math
from datetime import datetime

from adaptors.Adaptor import Adaptor
import re


class GithubAdaptor(Adaptor):

    def __init__(self):
        pass

    def rate(self, answer):
        return self.username(answer)

    def username(self, answer):
        print(answer)
        r = self.get('https://api.github.com/users/'+answer)
        j = r.json()
        #print(j)
        return self.get_score(j['public_repos'], j['created_at'], j['updated_at'], j['followers'], j['following'])


    def url(self, answer):
        if answer == "":
            return 0
        else:
            username = re.search(r"http[s]?://github.com/([a-zA-Z0-9]*)", answer).group(1)
            return self.username(username)

    def get_score(self, repos, joined_date, updated_date, followers, following):
        repo_score = 50 * ( 1 - 1 / (repos + 1))
        date_diff = datetime.strptime(updated_date, "%Y-%m-%dT%H:%M:%SZ") - datetime.strptime(joined_date, "%Y-%m-%dT%H:%M:%SZ")

        active_period = math.ceil(abs(date_diff).days / 30)
        date_score = 30 * (1 - (1 / active_period))
        follower_score = 10 * (1 - (1 / (followers + 1)))
        following_score = 10 * (1 - (1 / (following + 1)))
        print(repos,repo_score,active_period, date_score,followers,follower_score, following,following_score)
        return repo_score + date_score + follower_score + following_score


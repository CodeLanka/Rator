from __future__ import division
import math
from datetime import datetime
import os


from adaptors.Adaptor import Adaptor
import re
import requests
import time



class GithubAdaptor(Adaptor):

    def __init__(self):
        pass

    def username(self, answer):
        return self.rate(answer)

    def url(self, answer):
        return self.rate(answer)

    def rate(self, answer):
        userid = self.get_userid(answer)
        if userid == "":
            return 0
        else:
            return self.get_score(userid)

    def get_score(self, answer):
        try:
            if answer == "":
                return 0
            else:
                r = self.get('https://api.github.com/users/'+answer)
                j = r.json()

                limit_remaining = int(r.headers['X-RateLimit-Remaining'])
                if limit_remaining < 2:
                    self.sleep_till_reset(r.headers['X-RateLimit-Reset'])
                print(j)

                return self.do_score_calculation(j['public_repos'], j['created_at'], j['updated_at'], j['followers'], j['following'])
        except:
            return 0

    def get_userid(self, answer):
        if re.match("^\w+$", answer):
            return answer
        elif re.match(r"https?://\w+\.com/(\w+)/?", answer):
            return re.search(r"https?://\w+\.com/(\w+)", answer).group(1)
        else:
            return ""

    def do_score_calculation(self, repos, joined_date, updated_date, followers, following):
        repo_score = 50 * ( 1 - 1 / (repos + 1))
        date_diff = datetime.strptime(updated_date, "%Y-%m-%dT%H:%M:%SZ") - datetime.strptime(joined_date, "%Y-%m-%dT%H:%M:%SZ")

        active_period = math.ceil(abs(date_diff).days / 30)
        date_score = 30 * (1 - (1 / active_period))
        follower_score = 10 * (1 - (1 / (followers + 1)))
        following_score = 10 * (1 - (1 / (following + 1)))
        return repo_score + date_score + follower_score + following_score

    def get(self, url):
        return requests.get(url, auth=(os.environ.get("GITHUB_USERNAME"), os.environ.get("GITHUB_PASSWORD")))

    def sleep_till_reset(self, reset_timestamp):
        sleep_duration = float(reset_timestamp) - time.time()
        print("Program sleep till : ", time.ctime(int(reset_timestamp)))
        time.sleep(sleep_duration)
        print("Reset complete")






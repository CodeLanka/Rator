from adaptors.Adaptor import Adaptor
import re


class GithubAdaptor(Adaptor):

    def __init__(self):
        pass

    def username(self, answer):
        print(answer)
        r = self.get('https://api.github.com/users/'+answer)
        j = r.json()
        print(j)
        return j['public_gists'] + j['public_repos']*2

    def url(self, answer):
        if answer == "":
            return 0
        else:
            username = re.search(r"http[s]?://github.com/([a-z0-9]*)", answer).group(1)
            return self.username(username)
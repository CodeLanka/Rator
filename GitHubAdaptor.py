from Adaptor import Adaptor


class GitHubAdaptor(Adaptor):

    def __init__(self):
        pass

    def rate(self, answer):
        r = self.get('https://api.github.com/users/'+answer)
        j = r.json()
        print(j)
        return j['public_gists'] + j['public_repos']*2
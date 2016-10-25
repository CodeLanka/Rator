from Adaptor import Adaptor


class GitHubAdaptor(Adaptor):

    def __init__(self):
        pass

    def rate(self, answer):
        r = self.get('https://api.github.com/user/'+answer)
        r.json()
        return 100

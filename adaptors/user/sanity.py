from adaptors.Adaptor import Adaptor



class SanityAdaptor(Adaptor):

    def __init__(self):
        pass

    def verify(self, answer):
        return 0

    def why(self, answer):
        return len(answer.split(' '))

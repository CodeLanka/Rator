from adaptors.Adaptor import Adaptor


class SanityAdaptor(Adaptor):

    def __init__(self):
        pass

    def why(self, answer):
        return -10 if len(answer.split()) < 3  else 0

    def verify(self, answer):
        return 0


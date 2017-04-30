from adaptors.Adaptor import Adaptor



class SanityAdaptor(Adaptor):

    def __init__(self):
        pass

    def why(self, answer):
        return ( len(answer.split()) < 3 )?-10:0

    def verify(self, answer):

import sys
class Outil(object):
    def __init__(self):
        self.moi = self.__class__
        self.path = sys.path[0]
        self.filename = __file__

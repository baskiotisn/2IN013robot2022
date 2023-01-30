
class Vec2D(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def mul(self, v):
        self.x *= v.x
        self.y *= v.y

class PolyLine2D(object):
    def __init__(self):
        self.sommets = []
    def add(self,p):
        self.sommets.append(p)
    def len(self):
        return len(self.sommets)
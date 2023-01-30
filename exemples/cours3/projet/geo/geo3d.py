from .geo2d import Vec2D
class Vec3D(Vec2D):
    def __init__(self,x,y,z):
        super(Vec3D,self).__init__(self,x,y)
        self.z = z
    def add(self,v):
        super(Vec3D,self).add(v)
        self.z+=v.z
    def mul(self,v):
        super(Vec3D,self).mul(v)
        self.z *= v.z

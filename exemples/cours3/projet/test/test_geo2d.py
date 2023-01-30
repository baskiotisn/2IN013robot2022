import unittest
from  geo import Vec2D,PolyLine2D
class TestVec2D(unittest.TestCase):
    def setUp(self):
        self.p = Vec2D(1,1)
        self.deux = Vec2D(2,2)
    def test_point(self):
        self.assertEqual(self.p.x,1)
        self.assertEqual(self.p.y,1)
    def test_add(self):
        self.p.add(self.p)
        self.assertEqual(self.p.x,2)
        self.assertEqual(self.p.y,2)
    def test_mul(self):
        self.p.mul(self.deux)
        self.assertEqual(self.p.x, 2)
        self.assertEqual(self.p.y, 2)

class TestPolyLine2D(unittest.TestCase):
    def setUp(self):
        self.line = PolyLine2D()
        self.line.add(Vec2D(1,1))
        self.line.add(Vec2D(2,2))
    def test_len(self):
        self.assertEqual(self.line.len(),2)

if __name__=='__main__':
    unittest.main()

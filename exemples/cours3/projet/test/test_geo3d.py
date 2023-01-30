import unittest
from geo import Vec3D


class TestVec3D(unittest.TestCase):
    def setUp(self):
        self.p = Vec3D(1, 1,2 )
        self.deux = Vec3D(2, 2,1)

    def test_point(self):
        self.assertEqual(self.p.x, 1)
        self.assertEqual(self.p.y, 1)
        self.assertEqual(self.p.z, 1)

    def test_add(self):
        self.p.add(self.p)
        self.assertEqual(self.p.x, 2)
        self.assertEqual(self.p.y, 2)
        self.assertEqual(self.p.z, 2)

    def test_mul(self):
        self.p.mul(self.deux)
        self.assertEqual(self.p.x, 2)
        self.assertEqual(self.p.y, 2)
        self.assertEqual(self.p.z, 1)



if __name__ == '__main__':
    unittest.main()

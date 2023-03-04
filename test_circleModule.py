import unittest
from circleModule import Circle

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle1 = Circle(2)
        self.circle2 = Circle(5)
        self.circle3 = Circle(7)

    def test_radius(self):
        self.assertEqual(self.circle1.radius, 2)
        self.assertEqual(self.circle2.radius, 5)
        self.assertEqual(self.circle3.radius, 7)

    def test_circumference(self):
        self.assertEqual(self.circle1.circumference(), 12.56)
        self.assertEqual(self.circle2.circumference(), 31.400000000000002)
        self.assertEqual(self.circle3.circumference(), 43.96)
    
    def test_print_circumference(self):
        myCirc1 = self.circle1.circumference()
        myCirc2 = self.circle2.circumference()
        myCirc3 = self.circle3.circumference()
        self.assertEqual(myCirc1, 12.56)
        self.assertEqual(myCirc2, 31.400000000000002)
        self.assertEqual(myCirc3, 43.96)



if __name__ == '__main__':
    unittest.main()
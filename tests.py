import unittest
import math
import circle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_area_first(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_second(self):
        res = circle.area(10)
        self.assertEqual(res, 100 * math.pi)

    def test_perimeter_first(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_second(self):
        res = circle.perimeter(10)
        self.assertEqual(res, 20 * math.pi)

class SquareTestCase(unittest.TestCase):
    def test_area_first(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_area_second(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_perimeter_first(self):
        res = square.perimeter(0)
        self.assertEqual(res, 5)

    def test_perimeter_second(self):
        res = square.perimeter(25)
        self.assertEqual(res, 100)

class TriangleTestCase(unittest.TestCase):
    def test_area_first(self):
        res = triangle.area(0, 10)
        self.assertEqual(res, 0)

    def test_area_second(self):
        res = triangle.area(10, 5)
        self.assertEqual(res, 25)

    def test_perimeter_first(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_second(self):
        res = triangle.perimeter(10, 20, 30)
        self.assertEqual(res, 60)
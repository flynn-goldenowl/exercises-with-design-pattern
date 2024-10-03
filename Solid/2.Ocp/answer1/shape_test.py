import unittest
import math
from shape import Circle, Rectangle, Triangle, Square

class TestShapes(unittest.TestCase):
    
    def test_circle_area(self):
        circle = Circle(radius=3)
        expected_area = math.pi * 3**2
        self.assertAlmostEqual(circle.calculate_area(), expected_area)

    def test_rectangle_area(self):
        rectangle = Rectangle(height=4, width=5)
        expected_area = 4 * 5
        self.assertEqual(rectangle.calculate_area(), expected_area)

    def test_triangle_area(self):
        triangle = Triangle(length=6)
        expected_area = 0.5 * 6**2
        self.assertEqual(triangle.calculate_area(), expected_area)

    def test_square_area(self):
        square = Square(length=6)
        expected_area = 6**2
        self.assertEqual(square.calculate_area(), expected_area)


if __name__ == "__main__":
    unittest.main()

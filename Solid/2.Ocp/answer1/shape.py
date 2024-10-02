import math

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        super().__init__()

        self.radius = radius

    def calculate_area(self) -> float:
        return math.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, height: float, width: float) -> None:
        super().__init__()

        self.height = height
        self.width = width

    def calculate_area(self) -> float:
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, length: float) -> None:
        super().__init__()

        self.length = length

    def calculate_area(self) -> float:
        return 0.5 * self.length**2

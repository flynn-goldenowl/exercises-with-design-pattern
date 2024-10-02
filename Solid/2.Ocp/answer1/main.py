from shape import Circle, Rectangle, Triangle

if __name__ == "__main__":
    shapes = [Circle(5), Rectangle(4, 5), Triangle(3)]

    print([s.calculate_area() for s in shapes])

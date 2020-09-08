from math import pi

from geometric_tool.figures import Circle, Rectangle, Square, Triangle


def test_circle_perimeter():
    # given
    name = "circulito"
    radius = 2
    circle = Circle(name, radius)

    # when
    perimeter = circle.calculate_perimeter()

    # then
    expected_perimeter = 2 * pi * radius
    assert perimeter == expected_perimeter


def test_circle_area():
    # given
    name = "circulito"
    radius = 2
    circle = Circle(name, radius)

    # when
    area = circle.calculate_area()

    # then
    expected_area = pi * radius**2
    assert area == expected_area


def test_triangle_perimeter():
    # given
    name = "triangulito"
    side1 = 3
    side2 = 2
    side3 = 4
    triangle = Triangle(name, side1, side2, side3)

    # when
    perimeter = triangle.calculate_perimeter()

    # then
    expected_perimeter = side1 + side2 + side3
    assert perimeter == expected_perimeter


def test_triangle_area():
    # given
    name = "triangulito"
    side1 = 3
    side2 = 2
    side3 = 4
    triangle = Triangle(name, side1, side2, side3)

    # when
    area = triangle.calculate_area()

    # then
    s = (side1 + side2 + side3) / 2
    expected_area = (s * (s - side1) * (s - side2) * (s - side3))**0.5
    assert area == expected_area


def test_square_perimeter():
    # given
    name = "cuadradito"
    side = 5
    square = Square(name, side)

    # when
    perimeter = square.calculate_perimeter()

    # then
    expected_perimeter = side * 4
    assert perimeter == expected_perimeter


def test_square_area():
    # given
    name = "cuadradito"
    side = 5
    square = Square(name, side)

    # when
    area = square.calculate_area()

    # then
    expected_area = side**2
    assert area == expected_area


def test_rectangle_perimeter():
    # given
    name = "rectangulito"
    side1 = 5
    side2 = 10
    rectangle = Rectangle(name, side1, side2)

    # when
    perimeter = rectangle.calculate_perimeter()

    # then
    expected_perimeter = side1 * 2 + side2 * 2
    assert perimeter == expected_perimeter


def test_rectangle_area():
    # given
    name = "rectangulito"
    side1 = 5
    side2 = 10
    rectangle = Rectangle(name, side1, side2)

    # when
    area = rectangle.calculate_area()

    # then
    expected_area = side1 * side2
    assert area == expected_area

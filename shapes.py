import math

def circle(radius: float) -> float:
    return (22 / 7) * (radius ** 2)

def triangle(a: float, b: float, c: float) -> float:
    s = (a + b + c) / 2
    # Heron's formula for area of a triangle
    area = (s * (s - a) * (s - b) * (s - c))
    return area ** 0.5

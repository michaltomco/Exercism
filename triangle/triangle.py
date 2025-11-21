def equilateral(sides):
    return is_triangle(sides) and (sides[0] == sides[1] == sides[2])


def isosceles(sides):
    return is_triangle(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def scalene(sides):
    return is_triangle(sides) and (sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2])

def is_triangle(sides):
    sorted_sides = sorted(sides)
    return sorted_sides[2] < sorted_sides[0] + sorted_sides[1]
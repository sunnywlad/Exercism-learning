def is_triangle(sides):
    [s1, s2, s3] = sides
    return all(s > 0 for s in sides) and (
        s1 + s2 > s3 and
        s2 + s3 > s1 and
        s1 + s3 > s2
    )

def equilateral(sides):
    return is_triangle(sides) and (
        sides[0] == sides[1] == sides[2]
    )


def isosceles(sides):
    [s1, s2, s3] = sides
    return is_triangle(sides) and (
        s1 == s2 or s1 == s3 or s2 == s3
    )


def scalene(sides):
    [s1, s2, s3] = sides
    return is_triangle(sides) and (
        s1 != s2 and s1 != s3 and s2 != s3
    )

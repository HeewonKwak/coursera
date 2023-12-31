from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', 'x y')

def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def brute_force_closest_pair(points):
    min_distance_squared = float("inf")

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist_squared = distance_squared(points[i], points[j])
            min_distance_squared = min(min_distance_squared, dist_squared)

    return min_distance_squared

def strip_closest(points, strip, min_distance_squared):
    strip.sort(key=lambda point: point.y)

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j].y - strip[i].y) ** 2 < min_distance_squared:
            dist_squared = distance_squared(strip[i], strip[j])
            min_distance_squared = min(min_distance_squared, dist_squared)
            j += 1

    return min_distance_squared

def minimum_distance_squared_naive(points):
    n = len(points)

    if n <= 3:
        return brute_force_closest_pair(points)

    points.sort()

    mid = n // 2
    left_half = points[:mid]
    right_half = points[mid:]

    left_closest = minimum_distance_squared_naive(left_half)
    right_closest = minimum_distance_squared_naive(right_half)

    min_distance_squared = min(left_closest, right_closest)
    
    strip = [point for point in points if abs(point.x - points[mid].x) ** 2 < min_distance_squared]
    strip_min_distance_squared = strip_closest(points, strip, min_distance_squared)

    return min(strip_min_distance_squared, min_distance_squared)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared_naive(input_points))))

from sys import stdin
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    segments.sort(key=lambda x: (x.end,x.start))
    end = -1
    for s in segments:
        if end == -1:
            end = s.end
        else:
            if end < s.start:
                points.append(end)
                end = s.end
    points.append(end)
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

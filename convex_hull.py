from math import atan2, degrees
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"x:{self.x};y:{self.y}"

    def __str__(self):
        return f"x:{self.x};y:{self.y}"


def find_bottom_right_point(points: [Point]):
    bottom_right = points[0]
    for i in range(1, len(points)):
        if points[i].y < bottom_right.y:
            bottom_right = points[i]
        elif points[i].y == bottom_right.y and points[i].x > bottom_right.x:
            bottom_right = points[i]
    return bottom_right


def calculate_slopes(bottom_right_point: Point, points: [Point]):
    slopes = {}
    for point in points:
        delta_x = point.x - bottom_right_point.x
        delta_y = point.y - bottom_right_point.y
        theta_radians = atan2(delta_y, delta_x)
        slopes[point] = degrees(theta_radians)
    return slopes


def build_convex_hull(points: [Point]):
    convex_hull = [points[0], points[1]]
    for i in range(2, len(points)):
        add_point_to_convex_hull(convex_hull, points[i])
    return convex_hull


def add_point_to_convex_hull(convex_hull: [Point], point: Point):
    area = (convex_hull[-1].x - convex_hull[-2].x) * (point.y - convex_hull[-2].y) \
           - (convex_hull[-1].y - convex_hull[-2].y) * (point.x - convex_hull[-2].x)
    if area >= 0:
        convex_hull.append(point)
    else:
        convex_hull.pop()
        add_point_to_convex_hull(convex_hull, point)


if __name__ == '__main__':
    test_points = [
        Point(0, 0),
        Point(1, 2),
        Point(2, 5),
        Point(-1, 3),
        Point(4, 9),
        Point(3, 2),
        Point(-5, -3),
        Point(7, -5),
    ]
    br = find_bottom_right_point(test_points)
    point_slopes = calculate_slopes(br, test_points)
    print(br)
    sorted_points = list(map(lambda x: x[0], sorted(point_slopes.items(), key=lambda item: item[1])))
    ch = build_convex_hull(sorted_points)
    plt.plot(list(map(lambda point: point.x, test_points)), list(map(lambda point: point.y, test_points)), 'o')
    x_values = list(map(lambda point: point.x, ch))
    x_values.append(ch[0].x)
    y_values = list(map(lambda point: point.y, ch))
    y_values.append(ch[0].y)
    plt.plot(x_values, y_values, '--')
    plt.show()

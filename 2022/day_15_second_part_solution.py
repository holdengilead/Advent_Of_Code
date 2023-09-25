"""
Day 15. https://adventofcode.com/2022/day/15
"""

import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int


@dataclass
class Sensor:
    x: int
    y: int
    distance: int

    def possible(self, p: Point) -> bool:
        return abs(self.x - p.x) + abs(self.y - p.y) > self.distance

    def get_border_points(self) -> set[Point]:
        points = set()
        for i in range(self.distance + 2):
            points.add(Point(self.x + (self.distance + 1 - i), self.y + i))
            points.add(Point(self.x - (self.distance + 1 - i), self.y + i))
            points.add(Point(self.x + (self.distance + 1 - i), self.y - i))
            points.add(Point(self.x - (self.distance + 1 - i), self.y - i))
        return points


def main(name_file: str) -> None:
    """
    Main function.
    """
    with open(name_file, encoding="utf-8") as file:
        sensors: list[Sensor] = []
        for line in file:
            _, _, x_sensor, y_sensor, *_, x_beacon, y_beacon = line.split()
            x_sensor = int(x_sensor.split("=")[1][:-1])
            x_beacon = int(x_beacon.split("=")[1][:-1])
            y_sensor = int(y_sensor.split("=")[1][:-1])
            y_beacon = int(y_beacon.split("=")[1])
            distance_b = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)
            sensors.append(Sensor(x=x_sensor, y=y_sensor, distance=distance_b))

        for sensor in sorted(sensors, key=lambda x: x.distance):
            print(sensor)
            points: set[Point] = sensor.get_border_points()
            for point in points:
                if 0 <= point.x <= 4000000 and 0 <= point.y <= 4000000:
                    if all(sensor.possible(point) for sensor in sensors):
                        print(f"Found the distress beacon at ({point.x}, {point.y}).")
                        print(f"The tuning frequency is {point.x * 4000000 + point.y}")
                        sys.exit()


if __name__ == "__main__":
    main("day_15_input.txt")

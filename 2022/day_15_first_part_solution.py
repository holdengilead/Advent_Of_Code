"""
Day 15. https://adventofcode.com/2022/day/15
"""


def main(name_file: str, row: int) -> None:
    """
    Main function.
    """
    with open(name_file, encoding="utf-8") as file:
        impossible_positions = set()
        for line in file:
            _, _, x_sensor, y_sensor, *_, x_beacon, y_beacon = line.split()
            x_sensor = int(x_sensor.split("=")[1][:-1])
            x_beacon = int(x_beacon.split("=")[1][:-1])
            y_sensor = int(y_sensor.split("=")[1][:-1])
            y_beacon = int(y_beacon.split("=")[1])
            distance_b = abs(x_sensor - x_beacon) + abs(y_sensor - y_beacon)
            if abs(y_sensor - row) <= distance_b:
                rang = distance_b - abs(y_sensor - row)
                impossible_positions.update(range(x_sensor - rang, x_sensor + rang))
        print(f"The number of empty positions is: {len(impossible_positions)}")


if __name__ == "__main__":
    main("day_15_input.txt", 2_000_000)

from collections import defaultdict


def process_input(filename):
    """Acquire input data"""
    with open(filename) as file:
        input = file.read().splitlines()

    scanners = []

    for line in input:
        if line[0:3] == "---":
            words = line.split(" ")
            scanner = int(words[2])
            scans = []
        elif len(line) == 0:
            scanners.append(scans)
        else:
            beacon = line.split(",")
            beacon = list(map(int, beacon))
            scans.append(tuple(beacon))
    scanners.append(scans)
    return scanners


def detect_scanners():
    """Find matching scanners"""
    global known_beacons
    known_beacons = set(scanner_beacons[0])
    scanners_to_find = set(range(1, len(scanner_beacons)))
    scanner_coord = [(0, 0, 0)] * (len(scanner_beacons) + 1)

    while len(scanners_to_find):
        scanners_this_pass = set(scanners_to_find)
        for scanner in scanners_this_pass:
            # print 'Checking scanner', scanner
            rotation, translation = find_matches(scanner)
            if rotation < 0:
                # print 'No match found for scanner', scanner
                continue

            # Add transformed beacons in scanner to known_beacons
            scanners_to_find.remove(scanner)
            print(f"Scanner {scanner} is at {translation} with rotation {rotation}")
            for beacon in scanner_beacons[scanner]:
                known_beacons.add(transform(beacon, rotation, translation))
            # print 'Now know', len(known_beacons), 'beacons'
            scanner_coord[scanner] = translation
    print()
    print(f"There are {len(known_beacons)} beacons")

    max_distance = find_max_distance(scanner_coord)
    print(f"Largest Manhattan distance is {max_distance}")
    return


def find_matches(scanner):
    """Find rotation & translation for a scanner"""
    global known_beacons
    for rotation in range(24):
        translation = find_rotation(scanner, rotation)
        if translation:
            return rotation, translation
    return -1, -1


def find_rotation(scanner, rotation):
    """Return translation if this rotation is a match"""
    global known_beacons
    matches = defaultdict(int)

    for beacon_0 in known_beacons:
        x0, y0, z0 = beacon_0
        for beacon_s in scanner_beacons[scanner]:
            xs, ys, zs = transform(beacon_s, rotation)
            dx, dy, dz = x0 - xs, y0 - ys, z0 - zs
            matches[dx, dy, dz] += 1

    best_match = max(matches.values())
    if best_match < 12:
        return

    # print 'Scanner', scanner, 'matched', best_match, 'beacons'
    translation = matches.keys()[matches.values().index(best_match)]
    return translation


def transform(coordinates, rotation, translation=(0, 0, 0)):
    """Transform coordinates using rotation and then apply translation"""
    x, y, z = coordinates
    dx, dy, dz = translation

    # apply rotation

    # Face forward
    if rotation == 0:
        tx, ty, tz = x, y, z
    elif rotation == 1:
        tx, ty, tz = -y, x, z
    elif rotation == 2:
        tx, ty, tz = -x, -y, z
    elif rotation == 3:
        tx, ty, tz = y, -x, z

    # Face left
    elif rotation == 4:
        tx, ty, tz = z, y, -x
    elif rotation == 5:
        tx, ty, tz = z, x, y
    elif rotation == 6:
        tx, ty, tz = z, -y, x
    elif rotation == 7:
        tx, ty, tz = z, -x, -y

    # Face back
    elif rotation == 8:
        tx, ty, tz = -x, y, -z
    elif rotation == 9:
        tx, ty, tz = -y, -x, -z
    elif rotation == 10:
        tx, ty, tz = x, -y, -z
    elif rotation == 11:
        tx, ty, tz = y, x, -z

    # Face right
    elif rotation == 12:
        tx, ty, tz = -z, y, x
    elif rotation == 13:
        tx, ty, tz = -z, x, -y
    elif rotation == 14:
        tx, ty, tz = -z, -y, -x
    elif rotation == 15:
        tx, ty, tz = -z, -x, y

    # Face up
    elif rotation == 16:
        tx, ty, tz = x, z, -y
    elif rotation == 17:
        tx, ty, tz = -y, z, -x
    elif rotation == 18:
        tx, ty, tz = -x, z, y
    elif rotation == 19:
        tx, ty, tz = y, z, x

    # Face down
    elif rotation == 20:
        tx, ty, tz = x, -z, y
    elif rotation == 21:
        tx, ty, tz = y, -z, -x
    elif rotation == 22:
        tx, ty, tz = -x, -z, -y
    elif rotation == 23:
        tx, ty, tz = -y, -z, x

    else:
        print(f"Rotation {rotation} not recognized")

    # apply translation
    tx, ty, tz = tx + dx, ty + dy, tz + dz

    return (tx, ty, tz)


def find_max_distance(scanner_coord):
    """Find largest Manhattan distanc"""
    max_distance = 0
    for a in scanner_coord:
        for b in scanner_coord:
            if a >= b:
                continue
            max_distance = max(max_distance, manhattan_distance(a, b))
    return max_distance


def manhattan_distance(a, b):
    """Find largest Manhattan distance"""
    ax, ay, az = a
    bx, by, bz = b
    dx = abs(ax - bx)
    dy = abs(ay - by)
    dz = abs(az - bz)
    distance = dx + dy + dz
    return distance


# -----------------------------------------------------------------------------------------

filename = "day_19.txt"
# filename = 'sample.txt'

scanner_beacons = process_input(filename)

detect_scanners()

# First Part

# Lo he hecho a ojo.

# Second Part
from copy import deepcopy


def is_ordered(rooms):
    for room, occupants in rooms.items():
        if None in occupants or room * 4 != "".join(occupants):
            return False
    return True


def can_go(pos_hall, room, hall_situation):
    for i in range(min(pos_hall[1], room) + 1, max(pos_hall[1], room)):
        if (0, i) in hall_situation and not hall_situation[(0, i)] is None:
            return False  # Existe obstáculo en el pasillo.
    return True


hallway = {
    (0, 0): None,
    (0, 1): None,
    (0, 3): None,
    (0, 5): None,
    (0, 7): None,
    (0, 9): None,
    (0, 10): None,
}

columns = {"A": 2, "B": 4, "C": 6, "D": 8}

energy = {"A": 1, "B": 10, "C": 100, "D": 1000}

rooms = {
    "A": ["C", "D", "D", "B"],
    "B": ["A", "C", "B", "A"],
    "C": ["B", "B", "A", "D"],
    "D": ["D", "A", "C", "C"],
}
min_energy = 42275

burrow = [(rooms, hallway, 0)]
while burrow:
    # burrow.sort(key=lambda x: x[2], reverse=True)
    situation = burrow.pop()
    # print("Situación a estudiar:")
    # print(situation)
    # input()
    print(len(burrow))
    if situation[2] < min_energy:
        if is_ordered(situation[0]):
            print(f"He encontrado una solución con menos coste --> {situation[2]}.")
            min_energy = situation[2]
            input('Press any key to continue...')
        else:
            for pos, bug in situation[1].items():
                if bug:
                    for pos_room in (3, 2, 1, 0):
                        if not situation[0][bug][pos_room] and can_go(
                            pos, columns[bug], situation[1]
                        ):
                            new_rooms = deepcopy(situation[0])
                            new_rooms[bug][pos_room] = bug
                            new_hallway = situation[1].copy()
                            new_hallway[pos] = None
                            new_energy = situation[2] + energy[bug] * (
                                pos_room + 1 + abs(columns[bug] - pos[1])
                            )
                            burrow.append((new_rooms, new_hallway, new_energy))
                            # print("Situación nueva al mover un bicho a su columna")
                            # print((new_rooms, new_hallway, new_energy))
                            # input()
                            break
                            # print(len(burrow))
                        elif situation[0][bug][pos_room] != bug:
                            break
            for room in situation[0]:
                for i in range(4):
                    if situation[0][room][i] and room * (4 - i) != "".join(
                        situation[0][room][i:]
                    ):
                        for pos_in_hall, elem_in_that_position in situation[1].items():
                            if not elem_in_that_position and can_go(
                                pos_in_hall, columns[room], situation[1]
                            ):
                                new_hallway = situation[1].copy()
                                new_hallway[pos_in_hall] = situation[0][room][i]
                                new_rooms = deepcopy(situation[0])
                                new_rooms[room][i] = None
                                new_energy = situation[2] + energy[
                                    situation[0][room][i]
                                ] * (i + 1 + abs(columns[room] - pos_in_hall[1]))
                                burrow.append((new_rooms, new_hallway, new_energy))
                                # print(len(burrow))
                                # print("Situación nueva al mover un bicho al pasillo")
                                # print((new_rooms, new_hallway, new_energy))
                                # input()
                        break
                    if situation[0][room][i] and room * (4 - i) == "".join(
                        situation[0][room][i:]
                    ):
                        break

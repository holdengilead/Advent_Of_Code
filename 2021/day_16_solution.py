hxdc = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

# FIRST PART
# total = 0


# def read_package(bits):
#     global total
#     version, bits = int(bits[:3], 2), bits[3:]
#     print(f"The version is {version}")
#     total += version
#     type_id, bits = int(bits[:3], 2), bits[3:]
#     if type_id == 4:
#         block, bits = bits[:5], bits[5:]
#         while block[0] == "1":
#             block, bits = bits[:5], bits[5:]
#         if int(bits, 2) == 0:
#             return ""
#         else:
#             return bits
#     else:
#         length_type_id, bits = bits[0], bits[1:]
#         if length_type_id == "0":
#             length_in_bits, bits = int(bits[:15], 2), bits[15:]
#         else:
#             num_subpackets, bits = int(bits[:11], 2), bits[11:]
#         return bits


# with open("day_16.txt") as f:
#     for _ in range(1):
#         transmission = "".join((hxdc[n] for n in f.readline().strip()))
#         while transmission:
#             transmission = read_package(transmission)

#         print(total)


index = 0
bits = None


def read_package():
    global index, bits

    __ = bits[index : index + 3]
    index += 3
    type_id = int(bits[index : index + 3], 2)
    index += 3
    if type_id == 4:
        block = bits[index : index + 5]
        index += 5
        aux = block[1:]
        while block[0] == "1":
            block = bits[index : index + 5]
            index += 5
            aux += block[1:]
        return int(aux, 2)
    length_type_id = bits[index : index + 1]
    index += 1
    length_in_bits, num_subpackets = None, None
    if length_type_id == "0":
        length_in_bits = int(bits[index : index + 15], 2)
        index += 15
    else:
        num_subpackets = int(bits[index : index + 11], 2)
        index += 11
    result = []
    while (length_in_bits) or (num_subpackets):
        aux_index = index
        result.append(read_package())
        if num_subpackets:
            num_subpackets -= 1
        else:
            length_in_bits -= index - aux_index
    if type_id < 4:
        if type_id == 0:
            return sum(result)
        if type_id == 1:
            prod = 1
            for elem in result:
                prod *= elem
            return prod
        if type_id == 2:
            return min(result)
        return max(result)
    aux = result[0] - result[1]
    if (
        (aux < 0 and type_id == 6)
        or (aux == 0 and type_id == 7)
        or (aux > 0 and type_id == 5)
    ):
        return 1
    return 0


with open("day_16.txt") as f:
    for _ in range(1):
        index = 0
        bits = "".join((hxdc[n] for n in f.readline().strip()))
        print(read_package())

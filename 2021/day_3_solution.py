num_numbers = 0
count_ones = dict()
gamma = 0
epsilon = 0
with open("day_3.txt", "r", encoding="utf-8") as diagnostic:
    for number in diagnostic:
        num_numbers += 1
        for pos, bit in enumerate(reversed(list(number.strip()))):
            if bit == "1":
                count_ones[pos] = count_ones.get(pos, 0) + 1
for i in range(max(count_ones) + 1):
    if count_ones[i] > num_numbers // 2:
        gamma += 2 ** i
    else:
        epsilon += 2 ** i

print(f"The solution to the first part is: {gamma * epsilon}")

print("*-*" * 35)


def get_most_common(numbers, position):
    num_1 = 0
    num_0 = 0
    for n in (number[position] for number in numbers):
        if n == "1":
            num_1 += 1
        else:
            num_0 += 1
    if num_1 >= num_0:
        return "1"
    return "0"


def get_least_common(numbers, position):
    num_1 = 0
    num_0 = 0
    for n in (number[position] for number in numbers):
        if n == "1":
            num_1 += 1
        else:
            num_0 += 1
    if num_0 <= num_1:
        return "0"
    return "1"


numbers_oxygen = [number.strip() for number in open("day_3.txt", "r", encoding="utf-8")]
numbers_co2 = numbers_oxygen[:]
for i in range(len(numbers_oxygen[0])):
    most_common = get_most_common(numbers_oxygen, i)
    numbers_oxygen = [number for number in numbers_oxygen if number[i] == most_common]
    if len(numbers_oxygen) == 1:
        break

for i in range(len(numbers_co2[0])):
    least_common = get_least_common(numbers_co2, i)
    numbers_co2 = [number for number in numbers_co2 if number[i] == least_common]
    if len(numbers_co2) == 1:
        break

print(
    f"The solution to the second part is: {int(numbers_oxygen[0], 2) * int(numbers_co2[0], 2)}"
)

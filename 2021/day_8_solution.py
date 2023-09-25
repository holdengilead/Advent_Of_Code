total = 0
with open("day_8.txt", "r", encoding="utf-8") as file:
    for line in file:
        segments = dict()
        numbers = dict()
        all_ten, to_decode = line.strip().split(" | ")
        all_ten = all_ten.split(" ")
        numbers[1] = (n for n in all_ten if len(n) == 2).__next__()
        numbers[7] = (n for n in all_ten if len(n) == 3).__next__()
        numbers[4] = (n for n in all_ten if len(n) == 4).__next__()
        numbers[8] = (n for n in all_ten if len(n) == 7).__next__()
        segments["a"] = set(numbers[7]).difference(set(numbers[1])).pop()
        segments["c"] = set(numbers[7]).intersection(set(numbers[1]))
        segments["f"] = segments["c"]
        segments["b"] = set(numbers[4]).difference(set(numbers[1]))
        segments["d"] = segments["b"]
        segments["e"] = (
            set("abcdefg")
            .difference(segments["a"])
            .difference(segments["c"])
            .difference(segments["b"])
        )
        segments["g"] = segments["e"]
        two_three_five = [n for n in all_ten if len(n) == 5]
        if (
            len(set(two_three_five[0]).intersection(set(two_three_five[1]))) == 4
            and len(set(two_three_five[0]).intersection(set(two_three_five[2]))) == 4
        ):
            numbers[3] = two_three_five[0]
        elif (
            len(set(two_three_five[1]).intersection(set(two_three_five[0]))) == 4
            and len(set(two_three_five[1]).intersection(set(two_three_five[2]))) == 4
        ):
            numbers[3] = two_three_five[1]
        else:
            numbers[3] = two_three_five[2]
        segments["d"] = segments["d"].intersection(set(numbers[3])).pop()
        segments["b"] = segments["b"].difference(set(segments["d"])).pop()
        segments["g"] = segments["g"].intersection(set(numbers[3])).pop()
        segments["e"] = segments["e"].difference(set(segments["g"])).pop()
        two_three_five.remove(numbers[3])
        if len(set(two_three_five[0]).intersection(segments["e"])) == 1:
            numbers[2] = two_three_five[0]
            numbers[5] = two_three_five[1]
        else:
            numbers[2] = two_three_five[1]
            numbers[5] = two_three_five[0]
        zero_six_nine = [n for n in all_ten if len(n) == 6]
        if len(set(zero_six_nine[0]).intersection(segments["d"])) == 0:
            numbers[0] = zero_six_nine[0]
        elif len(set(zero_six_nine[1]).intersection(segments["d"])) == 0:
            numbers[0] = zero_six_nine[1]
        else:
            numbers[0] = zero_six_nine[2]
        zero_six_nine.remove(numbers[0])
        if len(set(zero_six_nine[0]).intersection(segments["e"])) == 0:
            numbers[9] = zero_six_nine[0]
        else:
            numbers[9] = zero_six_nine[1]
        zero_six_nine.remove(numbers[9])
        numbers[6] = zero_six_nine.pop()
        for i in range(10):
            numbers[i] = "".join(sorted(numbers[i]))
        mapping = dict()
        for k, v in numbers.items():
            mapping[v] = str(k)
        total += int("".join(mapping["".join(sorted(n))] for n in to_decode.split()))

print(total)

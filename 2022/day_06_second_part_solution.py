datastream = open("day_06_input.txt").readline().strip()

for i in range(len(datastream)):
    if len(set(datastream[i : i + 14])) == 14:
        print(i + 14)
        break

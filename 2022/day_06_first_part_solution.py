datastream = open("day_06_input.txt").readline().strip()

for i in range(len(datastream)):
    if len(set(datastream[i : i + 4])) == 4:
        print(i + 4)
        break

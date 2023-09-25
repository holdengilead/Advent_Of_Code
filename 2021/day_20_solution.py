lights = {".": "0", "#": "1"}


def get_square(x, y, values, step):
    aux = ""
    for inc_x in range(-1, 2):
        for inc_y in range(-1, 2):
            aux += values.get((x + inc_x, y + inc_y), str((step - 1) % 2))
    return int(aux, 2)


pixels = {}
with open("day_20.txt") as f:
    enhancement = f.readline().strip()
    line = f.readline()
    for i in range(100):
        line = f.readline().strip()
        for j, value in enumerate(line):
            pixels[(i, j)] = lights[value]

for step in range(1, 51):
    print(step)
    new_pixels = {}
    for i in range(0 - step, 100 + step):
        for j in range(0 - step, 100 + step):
            new_pixels[(i, j)] = lights[enhancement[get_square(i, j, pixels, step)]]

    pixels = new_pixels

print(sum(map(int, pixels.values())))

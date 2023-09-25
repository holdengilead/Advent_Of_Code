# SEGUNDA PARTE

# 16   --> Ese es el mínimo numero para el cual su sumatorio llega a 135
# 156  --> Más de esto te pasas en 'x' en un único paso.
# -102 --> Valor mínimo que puede tener y para el caso de un único paso.
# 200  --> En la primera parte ví que la mayor altura es 101, así que pongo 200 para asegurar

possible = 0
for x in range(16, 156):
    print(f"X --> {x}")
    for y in range(-102, 200):
        pos = [0, 0]
        vel = [x, y]
        while True:
            pos[0], pos[1] = pos[0] + vel[0], pos[1] + vel[1]
            if vel[0] > 0:
                vel[0] -= 1
            vel[1] -= 1
            if (135 <= pos[0] <= 155) and (-102 <= pos[1] <= -78):
                possible += 1
                break
            if pos[1] < -102:
                break
print(possible)

# PRIMERA PARTE
# max_height = 0
# for i in range(10000):
#     pos = [0, 0]
#     vel = [16, i]
#     heights = []
#     while True:
#         pos[0], pos[1] = pos[0] + vel[0], pos[1] + vel[1]
#         heights.append(pos[1])
#         # print(f"Position |===>  {pos}")
#         if vel[0] > 0:
#             vel[0] -= 1
#         vel[1] -= 1
#         # print(f"Velocity |===>  {vel}")
#         # input()
#         if (135 <= pos[0] <= 155) and (-102 <= pos[1] <= -78):
#             # print(
#             #     f"Llega al target, con velocidad inicial {(16, i)} y una maxima altura de {max(heights)}"
#             # )
#             if max(heights) > max_height:
#                 print(
#                     f"Llega al target, con velocidad inicial {(16, i)} y una maxima altura de {max(heights)}"
#                 )
#                 max_height = max(heights)
#             break
#         if pos[1] < -102:
#             # print(f"No llega al target, con velocidad inicial de {(16, i)}")
#             break

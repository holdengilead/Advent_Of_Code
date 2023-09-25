# dice = list(range(1, 101)) * 100
# board = [0] + list(range(1, 11)) * 100
# index = 0
# players = ("1", "2")
# player = 0
# pos = {"1": 4, "2": 2}
# scores = {"1": 0, "2": 0}
# while max(scores.values()) < 1000:
#     pos[players[player]] = board[sum(dice[index : index + 3]) + pos[players[player]]]
#     index += 3
#     scores[players[player]] += pos[players[player]]
#     player = (player + 1) % 2
# print(index, scores)

# Second Part


class Game:
    def __init__(self, universes, scores, positions, player) -> None:
        self.universes = universes
        self.scores = scores
        self.positions = positions
        self.player = player


outcomes = {9: 1, 8: 3, 7: 6, 6: 7, 5: 6, 4: 3, 3: 1}


board = [0] + list(range(1, 11)) * 100
dirac = [Game(universes=1, scores=(0, 0), positions=(4, 2), player=0)]
wins = [0, 0]
while dirac:
    print(len(dirac), wins)
    game = dirac.pop()
    for sum_dice, num_universes in outcomes.items():
        new_pos = board[game.positions[game.player] + sum_dice]
        new_score = game.scores[game.player] + new_pos
        if new_score > 20:
            wins[game.player] += game.universes * num_universes
        else:
            aux_positions = [None, None]
            aux_positions[(game.player - 1) % 2] = game.positions[(game.player - 1) % 2]
            aux_positions[game.player] = new_pos
            aux_scores = [None, None]
            aux_scores[(game.player - 1) % 2] = game.scores[(game.player - 1) % 2]
            aux_scores[game.player] = new_score
            dirac.append(
                Game(
                    universes=game.universes * num_universes,
                    scores=aux_scores,
                    positions=aux_positions,
                    player=(game.player + 1) % 2,
                )
            )

print(f"Wins: {wins}")

# if game.scores[(game.player - 1) % 2] > 20:
#     wins[(game.player - 1) % 2] += 1
# else:
#     for sum_dice in range(3, 10):
#         aux_positions = [None, None]
#         aux_positions[(game.player - 1) % 2] = game.positions[(game.player - 1) % 2]
#         aux_positions[game.player] = board[game.positions[game.player] + sum_dice]
#         aux_scores = [None, None]
#         aux_scores[(game.player - 1) % 2] = game.scores[(game.player - 1) % 2]
#         aux_scores[game.player] = (
#             game.scores[game.player] + aux_positions[game.player]
#         )
#         outcomes.append(
#             Game(
#                 scores=aux_scores,
#                 positions=aux_positions,
#                 player=(game.player + 1) % 2,
#             )
#         )

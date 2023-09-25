import sys

instructions = []
with open("day_24.txt") as f:
    while instruction := f.readline().strip():
        instructions.append(instruction)

i = 99999999999999
while i > 9999999999999:
    # print(i)
    dec = 1
    for j in range(14):
        if i % (10 ** (j + 1)) == int("1" * (j + 1)):
            dec += 10 ** j
        else:
            break

    monad = list(reversed(str(i)))
    variables = {"w": 0, "x": 0, "y": 0, "z": 0}
    for _, instruction in enumerate(instructions):
        aux = instruction.split(" ")
        if len(aux) == 2:
            variables[aux[1]] = int(monad.pop())
        else:
            try:
                op2 = int(aux[2])
            except ValueError:
                op2 = variables[aux[2]]
            if aux[0] == "add":
                variables[aux[1]] += op2
            elif aux[0] == "mul":
                variables[aux[1]] *= op2
            elif aux[0] == "div" and op2 != 0:
                variables[aux[1]] = variables[aux[1]] // op2
            elif aux[0] == "div" and op2 == 0:
                print("ERROR div por 0")
                input()
            elif aux[0] == "mod" and op2 > 0 and variables[aux[1]] >= 0:
                variables[aux[1]] = variables[aux[1]] % op2
            elif aux[0] == "mod" and op2 <= 0 and variables[aux[1]] < 0:
                print("MOD incorrecto")
                input()
            elif aux[0] == "eql":
                if variables[aux[1]] == op2:
                    variables[aux[1]] = 1
                else:
                    variables[aux[1]] = 0
    if variables["z"] == 0:
        print(f"HE ENCONTRADO EL NUMERO: {i}")
        sys.exit()
    i -= dec


# The input is a set of instructions repeated 14 times. The repetitions differ
# only in three places, marked below as {DIV}, {CHECK}, and {OFFSET}:
#     inp w
#     mul x 0
#     add x z
#     mod x 26
#     div z {DIV}
#     add x {CHECK}
#     eql x w
#     eql x 0
#     mul y 0
#     add y 25
#     mul y x
#     add y 1
#     mul z y
#     mul y 0
#     add y w
#     add y {OFFSET}
#     mul y x
#     add z y
# It is very important to notice the following characteristics:
# - Each such series of instructions resets w, x, and y. Only z's value persists
#   from one such grouping to the next.
# - {DIV} is always either 1 or 26, determined by whether {CHECK} is positive or
#   negative respectively.
# - If {CHECK} is positive, it's always greater than 9.
# - There are an equal number of repetitions where {CHECK} is positive as there
#   are where it is negative (seven of each).
# We can interpret this code as performing the following:
# - Read an input.
# - Check the condition: input == (z % 26) + {CHECK}.
# - If {CHECK} is negative (or equivalently, {DIV} is 26), set z = z / 26.
# - If the condition is met, do nothing further.
# - Otherwise, set z = 26 * z + input + {OFFSET}
# Note here that if {CHECK} is positive, then it is impossible for the condition
# to be met, since we noticed that positive {CHECK} is always greater than 9 but
# the largest possible input we can read is 9.
# Because the operations on z all involve multiplying, dividing, or modding by 26,
# we can think of z as being treated like a stack of "digits" in a base-26 number.
# With this mental model, the above description becomes as follows:
# - If {CHECK} is positive, push (input + {OFFSET}) onto the stack.
# - If {CHECK} is negative, pop from the stack. If the popped value plus {CHECK}
#   does not equal the input, then push (input + {OFFSET}) onto the stack.
# - After all instructions have run, we are successful if the stack is empty.
# There are the same number of positive and negative {CHECK}s, we have the same
# number of push and pop instructions. If we want to end with an empty stack, we
# can't allow any of the pops to re-push, so must be sure that the condition
# (popped_value == input + {OFFSET}) is met on every single pop.
# The values of {CHECK},{OFFSET} for the 14 sets in my problem input are:
#     15, 13
#     10, 16
#     12, 2
#     10, 8
#     14, 11
#     -11, 6
#     10, 12
#     -16, 2
#     -9, 2
#     11, 15
#     -8, 1
#     -8, 10
#     -10, 14
#     -9, 10
# so translated to the mental model above, this is the following:
#     PUSH input[0] + 13
#     PUSH input[1] + 16
#     PUSH input[2] + 2
#     PUSH input[3] + 8
#     PUSH input[4] + 11
#     POP. Must have input[5] == popped_value - 11
#     PUSH input[6] + 12
#     POP. Must have input[7] == popped_value - 16
#     POP. Must have input[8] == popped_value - 9
#     PUSH input[9] + 15
#     POP. Must have input[10] == popped_value - 8
#     POP. Must have input[11] == popped_value - 8
#     POP. Must have input[12] == popped_value - 10
#     POP. Must have input[13] == popped_value - 9
# By playing out the stack operations, we arrive at the following requirements for
# all pops to succeed:
#     input[5] = input[4]
#     input[7] = input[6] - 4
#     input[8] = input[3] - 1
#     input[10] = input[9] + 7
#     input[11] = input[2] - 6
#     input[12] = input[1] + 6
#     input[13] = input[0] + 4
# From here, it is trivial to choose digits to create the largest number
# satisfying these requirements. For example, the second rule:
#     input[7] = input[6] - 4
# means that the sixth digit should be 9 and the seventh digit should be 5 (counting
# digits from left to right 0-indexed). Each rule gives us two of the fourteen
# digits, so the seven rules give the largest possible number: 53999995829399.
# Finding the smallest number is equivalent, e.g the same rule tells us that the
# sixth digit should be 5 and the seventh digit should be 1. This gives us the
# smallest possible number: 11721151118175.

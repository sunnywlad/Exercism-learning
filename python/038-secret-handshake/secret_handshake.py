SECRET_ACTIONS = [line.split(' = ')[1] for line in '''00001 = wink
00010 = double blink
00100 = close your eyes
01000 = jump'''.splitlines()]

def commands(binary_str):
    actions = []
    binary_act = binary_str[1:]
    binary_act = binary_act[::-1]
    for index, binary in enumerate(binary_act):
        if binary == '1':
            actions.append(SECRET_ACTIONS[index])
    if binary_str[0] == '1':
        actions.reverse()
    return actions

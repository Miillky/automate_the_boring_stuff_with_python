# Comma Code.

spam = ['apples', 'bannanas', 'tofu', 'cats']

def list_joiner(list):
    #Take a list and print it as an Oxford comma havint sentence.
    count = 0
    joined = ''
    while count < len(list) - 2:
        joined += list[count] + ', '
        count += 1
    joined += list[-2] + ' and '
    joined += list[-1] + '.'
    return joined

print(list_joiner(spam))

# Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for x in range(len(grid[0])):
    for y in range(len(grid)):
        print(grid[y][x], end="")
    print()
def print_puzzle(puzzle):
    # puzzle = [[a, b, c, d, e], [f, g, h, i, j], ...]
    for row in puzzle:
        print("-" * (len(row) * 5 - len(row) + 1))
        print("/ ", end = '')
        for char in row:
            print(char + " / ", end = '')
        print()
    print("-" * (len(row) * 5 - len(row) + 1))


test = [
    ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['A', 'B', 'C', 'D', 'E',],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C']
]
print_puzzle(test)
        

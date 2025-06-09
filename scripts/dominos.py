def calculate_domino_pieces(x):
    domino_set = set()
    for i in range(x + 1):
        for j in range(i, x + 1):
            domino_set.add((i, j))
    return domino_set, len(domino_set)

x = int(input("Valor de x: "))
domino_set, num_pieces = calculate_domino_pieces(x)

print(f"\nO número de peças neste conjunto é {num_pieces}")
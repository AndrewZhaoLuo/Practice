
largest = 0
for a in range(1, 100000):
    for b in range(1, 100000):
        appearProduct = [False] * 10

        a_c = a
        b_c = b
        while a_c < 0:
            appearProduct
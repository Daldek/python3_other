'''
Wyszukiwanie binarne.
Sprawdz czy wartosc n jest na posortowanej liscie P.
'''

P = [-124, -99, -50, -28, -3, 1, 2, 3, 7, 14, 27, 54, 85, 324, 456, 657, 999]

n = eval(input())
left = 0  # index [0]
right = len(P) - 1  # index [-1]

while left <= right:
    middle = (left + right) // 2  # dzielnie przy uzyciu "//" to floor division, zwraca tylko czesc calkowita
    if P[middle] == n:
        print(f"Znaleziono {n}")
        break  # przerwanie petli while
    elif P[middle] < n:
        left = middle + 1
    else:
        right = middle - 1
else:
    print(f"{n} nie ma na liscie")

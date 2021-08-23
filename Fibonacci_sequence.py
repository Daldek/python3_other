'''
Obliczenie kolejnych wartosci ciagu Fibonacciego
'''

# rekurencja
def fibonacci_r(n):  # O(2^n)
    if n <= 1:
        return n
    return fibonacci_r(n-1) + fibonacci_r(n-2)

# liniowe
def fibonacci_l(n):  # O(n)
    p, d = 0, 1
    for _ in range(n):  # "_" oznacza, ze nie interesuje nas ta zmienna
        p, d = d, p + d
    return p

print(fibonacci_r(9))
print(fibonacci_l(10))

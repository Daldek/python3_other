'''
Program, ktory wypisuje dla kolejnych liczb z zakresu od 1 do n:
"Fizz" - dla podzielnych przez 3
"Buzz" - dla podzielnych przez 5
"FizzBuzz" - dla podzielnych przez 3 i przez 5
dla pozostałych wartości ma wypisać aktualnie analizowaną liczbę
'''

def FizzBuzz(n):
    for num in range(1, n + 1):
        if num % (3*5) == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(str(num))

FizzBuzz(15)

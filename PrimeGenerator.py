user_range = eval(input("Podaj zakres wartosci liczbowych do zbadania "))

try:
    int(user_range)
except:
    print("Invalid input")
    exit()

# user_range = int(user_range)
primes = []
counter = 0

for tested_value in range(2, user_range + 1):
    # print("Tested value is " + str(tested_value))
    for testing_value in range(2, tested_value + 1):
        if tested_value % testing_value == 0:
            counter += 1
        # print("Testing value is " + str(testing_value))
        # print("Counter value is " + str(counter))

    if counter == 1:
        primes.append(tested_value)

    counter = 0

print(primes)

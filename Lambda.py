'''
Lambda, czyli funkcja anonimowa.
'''

lambda x : x+2

def increase_value(x):
    return x+2

'''
Powyzsza funkcja "increase_value" robi to samo co lambda powyzej
'''

L = [('Anna', 82), ('Robert', 33), ('Artur', 40)]
# sortowaniu wg 2. elementu tupli
L_sorted = sorted(L, key=lambda x : x[1])
print(L_sorted)

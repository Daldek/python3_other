'''
List comprehension, czyli wyrazenia listowe. Przyklady uzycia.
Jest to alternatywa dla petli for, pozwalajaca uniknac nadmiernego rozpisywania kodu.
D1 to dict comprehension
Nie ma prostej motody tworzenia tupli w sposob analogiczny
https://stackoverflow.com/questions/16940293/why-is-there-no-tuple-comprehension-in-python
'''

L = [1, 2, 3, 4, 5, 6]

L1 = [x for x in range(5)]
L2 = [x**2 for x in L]
L3 = [x for x in L if x % 2 == 0]
L4 = ["Parzysta" if x % 2 == 0 else "Nieparzysta" for x in range(5)]
L5 = [(x, x+10) for x in L]  # tutaj tworzymy tuple zagniezdzona w liscie
D1 = {x:x % 2 == 0 for x in L}

print(L1)
print(L2)
print(L3)
print(L4)
print(L5)
print(D1)

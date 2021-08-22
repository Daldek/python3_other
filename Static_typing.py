'''
Python jest jezykiem dynamicznie typowanym, jednak wykorzystujac biblioteke
mypy, mozemy wprowadzic typowanie statyczne i sprawdzic kod pod katem bledow
Do sprawdzenia poprawnosci nalezy zainstalowac 'mypy' oraz 'typed-ast'
Nastepnie zamaist 'python <nazwa pliku>' uruchmiamy kod wpisujac 'mypy <nazwa pliku>'
'''

# Przyklad typowanie dynamicznego
a = 5  # zmienna a jest typu int
print(type(a))
a = 'piec'  # teraz zmiennej a przypisujemy wartosc str
print(type(a))
a = [1, 2, 3, 4, 5]  # po czym zmieniamy typ na liste
print (type(a))

# Wprowadzenie typowania statycznego
from typing import List  # aby używać type hints należy zainstalować i zaimportować bibliotekę typing

''' funkcja spell_it_out oczekuje, ze pobrana zmienna "word"
bedzie typu str oraz, ze zwroci liste stringow
'''
def spell_it_out(word: str) -> List[str]:
    return list(word)

''' Teraz tworzymy kolejna funkcje, ktora bedzie niezgodna z wytycznymi
zawartmi w definicji funkcji'''
def spell_it_wrong(word: str) -> List[str]:
    return 5

spell_it_out("Python")
spell_it_wrong(1)

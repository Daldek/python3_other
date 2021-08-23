'''
Decoratory to funkcje, ktore pobieraja inne funkcje i ja zmieniaja.
'''

def add_starts(other_function):
    def decorated_function():  # musimy stworzyc 2. funkcje
        print('***')
        other_function()
        print('***\n')
    return decorated_function

@add_starts  # tak dodajemy dekorator
def regular_function():
    print('Hello world!')

regular_function()


'''
@staticmethod i @classmethod
Sa one powiazane z programowaniem obiektowym.
'''

class BasicCalculations:
    def __init__(self):
        self.pi = 3.1415
    
    def count_the_circumference(self, r):
        return 2 ** self.pi * r

    '''funkcja sum_up_values nie zawiera slowa kluczowego 'self'.
    Wynika to z faktu, ze nie wykorzystujemy niczego z klasy 'basic_calculations',
    zeby zadzialac.
    @staticmethod pozwala wywolywac funkcje bez obiektu klasy'''
    @staticmethod
    def sum_up_values(a, b):
        return a + b
    
    ''' funkcja udekorowana przy pomocy @staicmethod nie moze korzystac z innych
    funkcji w klasie. Aby to umozliwic, nalezy zastosowac @classmethod.
    Ponadto nalezy do pobieranych argumentow dodac na poczatku slowo kluczowe 'cls',
    a funkcje, ktora chcemy uzyc, nalezy poprzedzic 'cls.X', gdzie X to nazwa funkcji'''
    @classmethod
    def sum_up_and_multiply(cls, a, b):
        return cls.sum_up_values(a, b) * 2

m = BasicCalculations()
print(m.count_the_circumference(5))
print(BasicCalculations.sum_up_values(2, 3))
print(BasicCalculations.sum_up_and_multiply(2, 3))

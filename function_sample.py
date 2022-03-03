# Hozz létre egy is_even nevű függvényt
# amely True-t ad vissza, ha a paraméterként megadott
# érték páros, egyéb esetben False-t adjon vissza

def is_even(a):
    if a % 2 == 0:
      return True
    else:
        return False

print(is_even(2))
print(is_even(0))
print(is_even(3))

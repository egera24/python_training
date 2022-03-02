# Literál - érték
print (5) # Egész szám
print (100_000)

print (3.14) # Lebegőpontos literál

print ("Hello World")
print ('Hello World')

employee_name = "John Doe" # az employee_name a változó neve (kisbetű mindig)
print (employee_name) # Mikor a változó nevére hivatkozok, akkor a változó előre definiált értékét adja vissza. Ha fentebb a változó neve változik, akkor mindenhol máshol is változtatni kell, hiszen arra hivatkozunk. Vagy lehet nyomni shift+F6 bil kombót, és átírja nekünk mindenhol.

age = 30
print (age)
age = 31
print (age) # Mivel két változónk van age névvel, így a későbbi felülírja a régit és az újat írja ki.

color_of_eye = "blue"
print(color_of_eye)

color_of_eye_of_john = color_of_eye

print(color_of_eye_of_john)

type(5) # Megadja az 5 típusát. viszont itt nincs kiíratva

print(type(5)) # Ezzel már ki van íratva. Integer=egész szám

print(type(3.14)) # float - lebegőpontos szám
print(type("Hello")) # string - karakterlánc

age = 32

print(type(age)) # Ekkor azt nézi meg, hogy a változó milyen értékre hivatkozik és annak milyen a típusa, ez esetben integer

age = "harminckettő"

print(type(age)) # Itt pedig már string a típusa

# literálok, változóknak - van típusa - Python típusos nyelv
# változóknál a típus változhat - dinamikusan típusos nyelv
# a legfrissebb python-ban behozták a type hint -et. Ez nem változtat a kódon, viszont a programban ha az érték fölé viszem a kurzort, akkor kijelzi, hogy oda alapvetően más típusú értéket szántak.

salary: int = 200
print(salary)

salary = "kétszáz"

print(salary)




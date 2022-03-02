# Írj egy programot, ami bekérdezi elsőzör a nevedet.
# name_repeater.py
# Majd bekérdezi, hogy hánszor írja ki
# Írja ki ennyiszer a nevedet.
# Szorgalmi feladat: írd ki a név elé, hogy éppen hanyadjára kerül kiírásra.

# John Doe
# 2
# 0 John Doe
# 1 John Doe

name=input("Kérlek add meg a neved!")
count=input("Hányszor írjam ki a neved?")
for i in range (0, int(count)):
    print(str(i+1) + " " + name)

# vagy

name=input("Kérlek add meg a neved!")
count=input("Hányszor írjam ki a neved?")
for i in range (0, int(count)):
    print(str(i+1), name)
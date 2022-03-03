# Kérjük be a felhasználótól a nevét, ha üres, akkor írjuk ki, hogy nem lehet üres értéket megadni.
# És kérjük be még egyszer.
# Ha nem üres, írjuk ki, hogy köszönöm!

name = ""
while name == "":
name=input("Kérjük adja meg nevét!")
if name == "":
    print("Nem lehet üres értéket megadni")
print("Udvozollek " + name)








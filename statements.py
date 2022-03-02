print(5 * 6)
print(5 + 6)
print(3 / 2)
print(3 - 2)
print(5 * 6 + 12)
print(1 + 2 * 3)
print((1 + 2) * 3)

print("alma" + "korte") #konkatenálás - összefűzés

# Mi van ha össze akarsz adni egy stringet és egy int-et?  - nem lehetséges a végrehajtás
# Mi van fordítva, ha intet és stringet akarsz összeadni? - nem lehetséges a végrehajtás
# Mi van, ha egy stringből ki akarsz vonni egy másikat? - nem lehetséges a végrehajtás
# Mi van, ha egy stringet megszorzol egy másik stringgel? - nem lehetséges a végrehajtás
# Mi van, ha egy stringet megszorzol egy int-tel? - az int-nek megfelelően egymás után beteszi a stringet: pl. almaalmaalma


# name = "John Doe"
# message = "A name valtozo tipusa" + type(name) - ezt nem engedy mert a type class típusú és ezért nem megy a kontkatenáció. String-é kell konvertálni a str() beépített függvénnyel
# print(message)

name = "John Doe"
message = "A name valtozo tipusa: " + str(type(name))
print(message)

#kifejezések végrehajtása: kiértékelés

print(len("Hello"))
length_of_hello = len("Hello")

# hozzatok létre egy változót, hogy órák száma: hours. Értéke legyen először 5.
# hozzatok létre egy másik változót, aminek a neve: minutes. Ez tartalmazza, hogy ez előző változó szorzása 60-al
# írjuk ki, hogy 3 óra az 180 perc. A számok helyén az hours és minutes változók legyenek.

hours = 3
minutes = hours * 60
print(str(hours) + " óra az " + str(minutes) + " perc")

message = str(hours)
message = message + " óra az " # újra lefuttatja a message változót és felülírja azt.
print(message)

# Hozzatok létre egy word nevű változót és adjátok neki értékül egy nagyon hosszú szót.
# Számoljátok ki a hosszát
# A ... szó pontosan .... karakter hosszú.

word = "elkelkáposztásítottátok"
len(word)
print(len(word))

print("Az " + word + " szó pontosan " + str(len(word)) + " karakter hosszú.")

print(5 // 2) # ötben a kettő megvan 2-szer
print(5 % 2) # és maradék az 1


# Írjatok egy get_max nevű függvényt,
# aminek paraméterül át lehet adni két lebegőpontos számot,
# és adja vissza a kettő közül a nagyobbat

# def get_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b
#
# print(get_max(6.8, 6.8))


# Írjatok egy beszédes print_square függvényt,
# ami paraméterül kap két egész számot.
# Rajzoljon ki egy ekkora téglalapot csillagokból.

# def print_square(width: int, height: int) -> None:
#     full_row = width * "*"
#     print(full_row)
#     center_row = "*" + (width - 2) * " " + "*"
#     for i in range(0, height - 2):
#         print(center_row)
#     print(full_row)
#
#
# print_square(7,6)


# Írjatok egy függvényt, ami paraméterül megkapja a szavak listáját,
# és visszaadja ezeket összefűzve,
# de mindegyiket gondolatjel között

def repeat_words_with_hyphens(words: list) -> str:
    result = ""
    for word in words:
        result += "-" + word + "-"
    return result

print(repeat_words_with_hyphens("alma", "korte", "meggy"))





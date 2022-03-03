# # Függvény definíciója:
# def print_employee_data(name, age):
#     # DRY: don't repeate yourself
#     print("Az alkalmazott neve: ", name)
#     print("Az alkalmazott eletkora:", age)
#
#
# print_employee_data("John", 10)
# print_employee_data("Jack", 20)
# print_employee_data("Jane", 30)
# print("End")
#
#
# # Feladat: Írjatok egy függvényt, amely vár két darab számot (a,b) és kiírja az összegüket.
#
# def print_sum_of_numbers(a, b):
#     print(int(a)+int(b))
#
# print_sum_of_numbers(1, 6)
#
# # Kérjétek be a függvényen kívül a két számot
# # és a bekért értékekkel hívjátok meg a print_sum függvényt
# value1 = int(input("Adj meg egy számot"))
# value2 = int(input("Adj meg egy másik számot"))
# print_sum(value1, value2)


# Írjatok egy sum_list függvényt, amely paraméterül kap egy listás
# És kiírja a konzolra a listában szereplő számok összegét
numbers = [1, 2, 5, 8]


def sum_list(numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)





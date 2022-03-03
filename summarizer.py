# Kérd be a felhasználótól, hogy hány számot szeretne megadni
# 3
# Kérj be tőle pont annyi számot, mint amit az előbb megadott
# Összegezzük a felhasználó által megadott CSAK pozitív számokat.
#3
#4
#-2
# Eredmény: 7

count = int(input("Hány számot szeretnél megadni?"))
sum = 0
for i in range(count):
    number = int(input("Add meg a(z) " + str(i+1) +". számot"))
    print("A megadott szám: ", number)
    if number > 0:
        sum += number
        print("Részösszeg: ", sum)
print("Végső összeg: ", sum)


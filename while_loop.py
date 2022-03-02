# logikai = boolean
# két értéke lehet: True, False - literál

are_you_a_boy = True
print(are_you_a_boy)

is_13_lower_than_15 = False
print(is_13_lower_than_15)

print(type(is_13_lower_than_15))

# összehasonlító operátorok

result = 10 < 20
print(result)

result = 10 > 20
print(result)

result = 10 >= 20
print(result)

result = 10 == 20
print(result)

result = 10 == 10
print(result)

print("alma" == "alma")
print ("alma" == "körte")

while False:
    print("Hello ciklus")

# Végtelen ciklus
#while True:
    #print("Hello vegtelen")

count = 0
while count < 10:
    print("Hello " + str(count))
    count = count + 1





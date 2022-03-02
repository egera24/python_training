# Írj egy programot, ami a for ciklus használatával az alábbi szöveget írja ki
# Az év egyik hónapja január.
# Az év egyik hónapja február.



for month in ["Januar", "Februar", "Marcius"]:
    print("Az ev egyik honapja " + str(month) + ".")

# ha azt akarjuk, hgoy számozza is:


count = 1
for month in ["Januar", "Februar", "Marcius"]:
    print("Az ev " + str(count) + ". honapja " + str(month) + ".")
    count += 1


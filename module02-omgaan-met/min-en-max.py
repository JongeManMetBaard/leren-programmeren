a = int(input("Typ het gewenste getal in: "))
b = int(input("Typ nogmaals het gewenste getal in: "))

if a > b:
    max = a
    print("a is het grootste getal:", max)

elif a < b:
    min = a
    print("a is het kleinste getal:", min)

# else:
#     print("a en b zijn even groot")
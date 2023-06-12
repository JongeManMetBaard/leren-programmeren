# while True:
#     try:
#         getal = int(input("voer een getal in: "))
#     except ValueError:
#         print("voer een getal in sukkelaar")
#     else:
#         break

# number = 2.705
# formatted_number = f"{number:.2f}"
# print(formatted_number)  # Output: 2.70

# Ali Goutsal pizzaCalculator

# prijzen
small = 14.99
medium = 16.49
large = 19.99

# functie om een geldig geheel getal te verkrijgen van de gebruiker
def getIntegerInput(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Dat is geen geldig geheel getal. Probeer het opnieuw.")

# keuze
small_pizza = getIntegerInput("Hoeveel small pizza's wilt u? ")
medium_pizza = getIntegerInput("Hoeveel medium pizza's wilt u? ")
large_pizza = getIntegerInput("Hoeveel large pizza's wilt u? ")

# berekening totaal prijs
small_total_price = small_pizza * small
medium_total_price = medium_pizza * medium
large_total_price = large_pizza * large

# Totale kosten bestelling
total_price_order = small_total_price + medium_total_price + large_total_price

# bon
print("+------------------+------------------+")
print("|     Afmeting     |      Aantal      |")
print("+------------------+------------------+")
print("|      Small       |      {:>4d}        |".format(small_pizza))
print("|      Medium      |      {:>4d}        |".format(medium_pizza))
print("|      Large       |      {:>4d}        |".format(large_pizza))
print("+------------------+------------------+")
print("|   Totale kosten  |   € {:>7.2f}   |".format(total_price_order))
print("+------------------+------------------+")

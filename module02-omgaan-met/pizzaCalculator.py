# Ali Goutsal pizzaCalculator

# prijzen
small = 14.99
medium = 16.49
large = 19.99

# keuze

def getInteger():
    while True:
        try:
            small_pizza = getInteger(int(input("Hoeveel small pizza's wilt u? ")))
            medium_pizza = getInteger(int(input("Hoeveel medium pizza's wilt u? ")))
            large_pizza = int(input("Hoeveel large pizza's wilt u? "))
            break
        except ValueError:
            print("Dat is geen nummer")

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
print("|      Small       |       ",   small_pizza,"        |")
print("|      Medium      |       ",  medium_pizza,"        |")
print("|      Large       |       ",   large_pizza,"        |")
print("+------------------+------------------+")
print("|   Totale kosten  |     €",   total_price_order,"     |")
print("+------------------+------------------+")
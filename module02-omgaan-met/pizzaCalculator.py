# Ali Goutsal pizzaCalculator

# prijzen
small = 14.99
medium = 16.49
large = 19.99

# vraag geldige getalwaarde aan gebruiker
def getInteger(amount):
    while True:
        try:
            aantal = int(input(amount))  
            return aantal
        except ValueError:
            print("Dat is geen nummer")

# keuze
small_pizza = getInteger("Hoeveel small pizza's wilt u? ")
medium_pizza = getInteger("Hoeveel medium pizza's wilt u? ")
large_pizza = getInteger("Hoeveel large pizza's wilt u? ")
    
# berekening totaal prijs
small_total_price = small_pizza * small
medium_total_price = medium_pizza * medium
large_total_price = large_pizza * large

# Totale kosten bestelling
total_price_order = small_total_price + medium_total_price + large_total_price
formatted_number = f"{total_price_order:.2f}"

# bon
print("+------------------+------------------+")
print("|     Afmeting     |      Aantal      |")
print("+------------------+------------------+")
print("|      Small       |       ",   small_pizza,"        |")
print("|      Medium      |       ",  medium_pizza,"        |")
print("|      Large       |       ",   large_pizza,"        |")
print("+------------------+------------------+")
print("|   Totale kosten  |     €",   formatted_number,"     |")
print("+------------------+------------------+")
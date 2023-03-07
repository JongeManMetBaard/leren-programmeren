geel = input("Is de kaas geel? ")
if geel == "nee":
    schimmel = input("Heeft de kaas blauwe schimmel? ")
    if schimmel == "nee":
        korst = input("Heeft de kaas een korst? ")
        if korst == "nee":
            print("Mozzarella")
        elif korst == "ja":
            print("Camembert")
    elif schimmel == "ja":
        korst = input("Heeft de kaas een korst? ")
        if korst == "nee":
            print("Foume d'Ambert")
        elif korst == "ja":
            print("Blue de Rochbaron")
if geel == "ja":
    gaten = input("Zitter er gaten in? ")
    if gaten == "nee":
        steen = input("Is de kaas hard als steen? ")
        if steen == "nee":
            print("Goudse Kaas")
        if steen == "ja":
            print("Parmigiano Reggiano")
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur? ")
        if duur == "nee":
            print("Leerdammer")
        if duur == "ja":
            print("Emmenthaler")
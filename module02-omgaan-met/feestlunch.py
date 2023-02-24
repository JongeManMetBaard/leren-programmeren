croissantjes = int(input("Hoeveel croissantjes wilt u? "))
stokbroden = int(input("Hoeveel strokbroden wilt u? "))
kortingsbonnen = int(input("Hoeveel kortingsbonnen heeft u? "))

croissantjes_prijs = int(input("Hoeveel kost de croissantjes? "))
stokbroden_prijs = int(input("Hoeveel kost de stokbroden? "))
kortingsbonnen_prijs = int(input("Hoeveel korting? "))

berekening = croissantjes * croissantjes_prijs + stokbroden * stokbroden_prijs - kortingsbonnen * kortingsbonnen_prijs

print("'De feestlunch kost je bij de bakker" , berekening , "cent voor de", croissantjes , "croissantjes en de",
stokbroden , "stokbroden als de" , kortingsbonnen , "kortingsbonnen nog geldig zijn!'")
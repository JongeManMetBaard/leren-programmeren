toegangsticket = int(input("Hoeveel kost de toegangsticket? "))
vip_vr_gameseat = int(input("Hoeveel kost de VIP-VR-GameSeat? "))

aantal_mensen = int(input("Hoeveel mensen? "))
minuten_VR = int(input("Voor hoeveel minuten in de VIP-VR-GameSeat? "))

berekening = toegangsticket * aantal_mensen + vip_vr_gameseat * (minuten_VR / 5)
bedrag_in_cent = int(berekening)

print("'Dit geweldige dagje-uit met", aantal_mensen ,"mensen in de speelhal met", minuten_VR, "minuten VR kost je maar",
bedrag_in_cent ,"cent'")
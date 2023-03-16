diploma = input("Bent u in bezit van een Diploma MBO-4 ondernemen? J/N ")
rijbewijs = input("Heeft u een geldig Vrachtwagen rijbewijs? J/N ")
hoed = input("Heeft u een hoge hoed? J/N ")
geslacht = input("Bent u een man of vrouw? man/vrouw ")
if geslacht == "man":
    snor = input("Heeft u een snor? J/N ")
    if snor == "J":
        snorlengte = int(input("Hoe lang is uw snor in hele cm? "))
elif geslacht == "vrouw":
    kleur_haar = input("Wat voor kleurhaar heeft u? ")
    haarlengte = int(input("Hoe lang is uw haren in hele cm? "))
lengte = int(input("Wat is uw lichaamslengte in hele cm? "))
gewicht = int(input("Wat is uw lichaamsgewicht in hele kg? "))
certificaat = input('Heeft u een Certificaat "Overleven met gevaarlijk personeel?" J/N ')
dieren_dressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
jongleren = int(input("Hoeveel jaar ervaring heeft u met jongleren? "))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acobatiek? "))

if (diploma == "J") and (rijbewijs == "J") and (hoed == "J") and (geslacht == "man" and snor == "J" and snorlengte > 10 or geslacht == "vrouw" and kleur_haar == "rood" and haarlengte > 20) and (lengte > 150 and lengte < 220) and (gewicht > 90 and gewicht < 120) and (certificaat == "J") and (dieren_dressuur > 4 or jongleren > 5 or acrobatiek > 3):
    print("U bent aangenomen")
else:
    print("Sorry")
while True:
    try:
        getal = int(input("voer een getal in: "))
    except ValueError:
        print("voer een getal in sukkelaar")
    else:
        break
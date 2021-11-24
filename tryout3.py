def persoon(naam:str, leeftijd:int):
    print(f"Dag {naam}, uw bent {leeftijd} jaar oud.")
while True:
    naam = str(input("Wat is uw naam >>> "))
    if naam  == "break":
        break
    leeftijd = int(input("Wat is uw leeftijd >>> "))
    if leeftijd == "break":
        break
    persoon(naam, leeftijd)
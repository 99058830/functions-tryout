def persoon(naam:str, leeftijd:int):
    print(f"Dag meneer/mevrouw {naam}, uw leeftijd is {leeftijd}.")
while True:
    naam = input("Wat is uw naam >>> ")
    if naam  == "break":
        break
    leeftijd = input("Wat is uw leeftijd >>> ")
    if leeftijd == "break":
        break
    persoon(naam, leeftijd)
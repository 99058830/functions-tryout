import time

def einde():
  print('Je bent helaas af gegaan, probeer het opnieuw!')

def uitgang():
    print('Je hebt de uitgang gevonden, snel naar huis!')

def a():
    print('Je hebt voor keuze A gekozen!')
    time.sleep(3)

def b():
    print('=|--->Je hebt voor keuze B gekozen!')
    time.sleep(3)

print ("""Welkom in dit enge doolhof, maak je geen zorgen je komt heelhuids thuis.
""")

print ("""Gaat u links af of rechts af?
A. Links af
B. Rechts af""")
keuze = input(">>> ").lower()
if keuze == "a":
    a()
    print ("Onthoudt deze code. 5453")
    print ("Je komt een keypad tegen, voer een code in")
    keuze = input(">>> ").lower()
    if keuze == "5453":
        print ("Er gaat een deur open, ik denk dat de code goed is!")
        print ("""Gaat u links af of rechts af?
        A. Links af
        B. Rechts af""")
        keuze = input(">>> ").lower()
        if keuze == "a":
            a()
            uitgang()
        elif keuze == "b":
            b()
            einde()
    else:
        print ("Er gaat een valluik open!")
        print ("Game-over | Begin opnieuw.")
elif keuze == "b":
    b()
    print ("""Je ziet twee tools liggen, welke pak je?
    A. Zwaard
    B. Compas""")
    keuze = input(">>> ").lower()
    if keuze == "a":
        a()
        print ("""Je ziet een monster, ga je het gevecht aan of ga je vragen of je er langs mag.
        A. Gevecht
        B. Vragen of je er langs mag""")
        keuze = input(">>> ").lower()
        if keuze == "a":
            a()
            einde()
        elif keuze == "b":
            b()
            print ("Hij laat je er langs!")
            uitgang()
    elif keuze == "b":
        b()
        print ("""Gaat u links af of rechts af?
        A. Links af
        B. Rechts af""")
        keuze = input(">>> ").lower()
        if keuze == "a":
            a()
            einde()
        elif keuze == "b":
            b()
            uitgang()
else:
    einde()
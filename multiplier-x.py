def Multiplier():
    Getal = int(input('Van welk getal wilt u de tafel zien? >>>'))
    for i in range(1, 11):
        print(Getal, 'x', i, '=', Getal*i)
   
Multiplier()
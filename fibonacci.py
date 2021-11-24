keer = int(input("Hoe veel keer? "))
nummer1, nummer2 = 0, 1 
telling = 0
while telling < keer: 
    print(nummer1) 
    alle = nummer1 + nummer2
    nummer1 = nummer2 
    nummer2 = alle 
    telling += 1
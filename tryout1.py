def HelloWorld(hoeveel):
    for i in range(1, hoeveel+1):
        print(f'{i}.Hello World!')
HelloWorld(int(input('Hoeveel >>> ')))
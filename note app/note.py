notatka = []
dalej = True 

while dalej == True:
    print("Co dzisiaj?\n")
    do = input("1. Przejrzyj zapisane notatki\n2. Stwórz nową notatkę\n")
    if do == 1:
        print(notatka)
        wroc = input("\nAby wrócić wciśnij 1\n")
        if wroc == 1:
            break
    elif do == 2:
        notatka = input("Wpisz tekst notatki:\n")


    wyjdz = input("Aby wyjść wpisz 0\n")
    if wyjdz == 0:
        dalej = False
        break
    



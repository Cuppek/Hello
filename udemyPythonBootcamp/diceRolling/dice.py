import random
i = "y"
while i == "y": 
    y = int(input("Wpisz ilość rzutów kostką:\n"))
    for number in range(y):
        x = random.randint(1,6)
        print("\n-----\n")
        if x == 1:
            print("  1  ")
        elif x == 2:
            print("  2  ")
        elif x == 3:
            print("  3  ")
        elif x == 4:
            print("  4  ")
        elif x == 5:
            print("  5  ")
        elif x == 6:
            print("  6  ")
        print("\n-----")
    i = input("Czy chcesz rzucać dalej? Wpisz n aby zamknąć lub y aby kontynuować.\n")
    if i == "n":
        break
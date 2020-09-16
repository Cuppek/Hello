def div(a,b):
    if(b  == 0):
        return print("nie możliwe")
    else:
        c = a/b
        return print(c)

    
a = input("1: ")
b = input("2: ")

div(int(a),int(b))
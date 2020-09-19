"""
def add(x, y):
    z = x + y
    return print(z)

a = int(input("1 liczba: "))
b = int(input("2 liczba: "))
add(a,b)
"""

def temp(c):
    f = (9/5) * c + 32
    return print(f)

c = int(input("Wpisz temperaturę w stopniach Celcjusza: "))

temp(c)

def leng(m, s):
    h = m/60+s/3600
    return print(h)

m = int(input("Wpisz liczbę minut: "))
s = int(input("Wpisz liczbę sekund: "))

leng(m,s)
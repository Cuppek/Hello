import json
data = json.load(open(r"C:\Users\milos\Desktop\Hello\udemyPythonBootcamp\dictionaries\data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("Nie ma takiego słowa")

word = input("Wpisz słowo: ")
output = translate(word)


print(output)
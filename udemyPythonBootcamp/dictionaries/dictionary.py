import json
from difflib import get_close_matches
data = json.load(open(r"C:\Users\milos\Desktop\Hello\udemyPythonBootcamp\dictionaries\data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("miałeś na myśli %s?" %get_close_matches(word, data()))
        decide = input("\nWciśnij t jeżeli tak lub n jeżeli nie")
        if decide == "y":
            return data[get_close_matches(word, data())]
        elif decide == "n":
            return("Nie ma takiego słowa")
    else:
        print("Nie ma takiego słowa2")

word = input("Wpisz słowo: ")
output = translate(word)


print(output)


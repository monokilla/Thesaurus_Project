import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(f"Did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes or N if no: ")
        if yn == "Y" or "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or "n":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")


print(translate(word))

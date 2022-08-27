import nltk
from nltk.tokenize import word_tokenize
import random

tarot = {1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14:	"Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

spread = {}
rand1 = random.randint(1, 22)
rand2 = random.randint(1, 22)
rand3 = random.randint(1, 22)

spread["past"] = tarot.get(rand1)

while (rand1 == rand2 or rand2 == rand3 or rand1 == rand3 or rand2 <= 0 or rand2 > 22 or rand3 <= 0 or rand3 > 22):
    rand2 = random.randint(1, 22)
    rand3 = random.randint(1, 22)

spread["present"] = tarot.get(rand2)
spread["future"] = tarot.get(rand3)

for key, value in spread.items():
    print("Your " + key + " is the " + str(value) + " card.")

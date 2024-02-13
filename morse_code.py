"""
Obtain basic morse code alphabet
"""

from bs4 import BeautifulSoup
import pprint


def swap_keys_values(dictionary):
    """Swap keys and values in the dictionary"""
    swapped_dict = {value: key for key, value in dictionary.items()}
    return swapped_dict


extra_char = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "|"
}

# html file with basic morse code from "https://www.morsecode-translator.com/morse-code-alphabet"
with open("morse_code.html") as ms:
    input_file = ms.read()

soup = BeautifulSoup(input_file, "html.parser")

tags = soup.find_all("table", class_="w-full")

# create dictionary with characters parsed from html file
alphabet = {}

for tag in tags:
    tag_text = tag.text
    characters = tag_text.split("    ")

    for character in characters:
        if character.strip() != "":
            if character.strip()[0] in ("A", "("):
                alphabet[character.split(" ")[0].strip()] = character.split(" ")[1].strip()
            else:
                alphabet[character.split("  ")[0].strip()] = character.split("  ")[1].strip()

# add missing numbers to alphabet dictionary + extra character for spaces
alphabet.update(extra_char)

# copy complete and formatted alphabet for text encoding and create dictionary in the morse_alphabet.py
pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
pp.pprint(alphabet)

# copy complete and formatted alphabet for text decoding and create dictionary in the morse_alphabet.py
pp.pprint(swap_keys_values(alphabet))

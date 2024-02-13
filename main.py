from morse_alphabet import MORSE_ALPHABET_ENCODE, MORSE_ALPHABET_DECODE
from graphics import MAIN_THEME, INSTRUCTIONS


def continue_to_translate():
    """
    Continue to translate, if input message equals 'y' -> yes
    """
    next_message = input("Do you want to continue? Write 'y' or 'n'\n").lower()
    if next_message == 'y':
        translate_message()
    else:
        quit()


def encode_message(input_message):
    """
    Encode latin characters into the morse code
    """
    encoded_message = " ".join([MORSE_ALPHABET_ENCODE[char] for char in input_message.upper()])
    return encoded_message


def decode_message(input_message):
    """
    Decode morse code into the latin characters
    """
    decoded_message = "".join([MORSE_ALPHABET_DECODE[char] for char in input_message.split(" ")])
    return decoded_message.title()


translator_functions = {
    "encode": encode_message,
    "decode": decode_message
}


def translate_message():
    """
    Translate message from latin to morse code or vice-versa
    """
    translation_direction = input("Write what you want to do: 'encode' or 'decode' the message? (write 'q' to quit)\n").lower()
    if translation_direction in ("encode", "decode"):
        message_to_translate = input(f"Write your message to {translation_direction}:\n").upper()
        try:
            translated_message = translator_functions[translation_direction](message_to_translate)
        except KeyError:
            print("Invalid input, try again!")
            translate_message()
        else:
            print(f"Your {translation_direction}d message: {translated_message}")
            continue_to_translate()
    elif translation_direction == "q":
        quit()
    else:
        print("Wrong option, try again!")
        return translate_message()


if __name__ == "__main__":
    print(MAIN_THEME)
    print(INSTRUCTIONS)
    translate_message()

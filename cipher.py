import random


def encryption_mapping():
    encryption_mapping = {
        'a': '', 'b': '', 'c': '', 'd': '', 'e': '', 'f': '', 'g': '', 'h': '',
        'i': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'o': '', 'p': '',
        'q': '', 'r': '', 's': '', 't': '', 'u': '', 'v': '', 'w': '', 'x': '',
        'y': '', 'z': ''
    }
    # letters = list("abcdefghijklmnopqrstuvwxyz")
    letters = list(range(1,27))
    for letter in encryption_mapping.keys():
        random_letter = random.choice(letters)
        encryption_mapping[letter] = f"{random_letter}"
        letters.remove(random_letter)
    return encryption_mapping


if  __name__ == "__main__":
    print(encryption_mapping())

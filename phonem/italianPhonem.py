import random
import re

VOWELS = 'AEIOUY'
CONSONANTS = f"^{VOWELS}"
V = f"[{VOWELS}]"
C = f"[{CONSONANTS}]"

SUBSTITUTIONS = [
    [fr"([^{VOWELS}S])\1/g", r"\1"], # Removes double consonnant except S
    ["^Z", "DS"],
    ["Z", "TS"],
    ["C(?=[AOU])", "K"],
    ["CH(?=[IE])", "K"],
    ["G(?=[IE])", "J"],
    ["^H", ""],
    [f"(?<={V})S(?={V})", "Z"]
]


def italianPhonem(name):
    code = name.upper()

    for substitution in SUBSTITUTIONS:
        pattern, replacement = substitution

        if pattern.endswith("/g"):
            pattern = pattern[:-2]

        code = re.sub(pattern, replacement, code)

    return code


AUGMENTATIONS = [
    [f"(?<={V})Z(?={V})", ["S"]],
    [f"^({V})", [r"\1", r"H\1"]],
    ["J(?=[IE])", ["J", "G"]],
    ["K(?=[IE])", ["K", "CH"]],
    ["K(?=[AOU])", ["K", "C"]],
    ["TS", ["TS", "Z"]],
    ["^DS", ["DS", "Z"]],
    [f"([TM])", [r"\1", r"\1\1"]]
]



def italianInversePhonem(name:str):
    code = name.upper()

    for substitution in AUGMENTATIONS:
        pattern, replacement = substitution

        code = re.sub(pattern, replacement[random.randint(0, len(replacement)-1)], code)

    return code
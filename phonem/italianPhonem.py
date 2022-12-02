import re

VOWELS = 'AEIOUY'
CONSONANTS = f"^{VOWELS}"
V = f"[{VOWELS}]"
C = f"[{CONSONANTS}]"

SUBSTITUTIONS = [
    [fr"([^{VOWELS}S])\1/g", r"\1"], # Removes double consonnant except S
    ["^Z", "DS"],
    ["Z/g", "TS"], # Removes double consonnant except S
    ["C(?=[AOU])/g", "K"],
    ["CH(?=[IE])/g", "K"],
    ["G(?=[IE])/g", "J"],
    ["^H", ""],
    [f"(?<={V})S(?={V})/g", "Z"]
]


def italianPhonem(name):

    code = name.upper()

    for substitution in SUBSTITUTIONS:
        pattern, replacement = substitution

        if pattern.endswith("/g"):
            pattern = pattern[:-2]

        code = re.sub(pattern, replacement, code)

    return code

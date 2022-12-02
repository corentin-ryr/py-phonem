import re
import random

def translation(first, second):
    index = {}

    if len(first) != len(second):
        raise ValueError('talisman/helpers#translation: given strings don\'t have the same length.')

    for i in range(len(first)):
        index[first[i]] = second[i]

    return index

def squeeze(target):
    if len(target) == 0: return ""
    squeezed = [target[0]]

    for i in range(1, len(target)):
        if target[i] != target[i - 1]:
            squeezed.append(target[i])

    return "".join(squeezed)


SUBSTITUTIONS2 = [
    [r"([LT])\1", r"\1"],
    ["(?:SC|SZ|CZ)/g", "C"],
    ["(?:PF|PH)/g", "V"],
    ["QU/g", "KW"],
    ["^Y", "J"],
    ["CHS", "KS"],
    ["C(?=[ÄEIÖ])", "TS"],
    ["C(?=[^ÄEIH])", "K"],
    ["(?<=[AOU])CH", "R"],
    ["UE", "Y"],
    ["AE", "E"],
    ["OE", "Ö"],
    ["E[IY]", "AY"],
    ["EU", "OY"],
    ["AU", "A§"],
    ["OU", "§"],
    ["DT?$", "T"],
    ["Z", "TS"],
    ["CK", "K"],
]


TRANSLATION2 = translation(
  'QÇÑßFÁÀÂÃÅÄÆÉÈÊËIÌÍÎÏÜÝ§ÚÙÛÔÒÓÕØ',
  'CCNSVAAAAAEEEEEEYYYYYYYUUUUOOOOÖ'
)

ACCEPTABLE_LETTERS2 = set('ABCDLMNORSUVWXYÖETGKJP')

def germanPhonem(name):

    code = name.upper()

    for substitution in SUBSTITUTIONS2:
        pattern, replacement = substitution

        if pattern.endswith("/g"):
            pattern = pattern[:-2]

        code = re.sub(pattern, replacement, code)
  
	    # print(pattern)
        # print(code)
        # print()

    translatedCode = ''
    for letter in code:
        translatedCode += TRANSLATION2[letter] if letter in TRANSLATION2 else letter
    
    translatedCode = squeeze(translatedCode)

    code = ''
    for letter in translatedCode:
        if letter in ACCEPTABLE_LETTERS2:
            code += letter

    return code


AUGMENTATIONS = [
    ["(?<!A)U", ["OU"]],
    ["Y", ["I", "Ü"]],
    ["OY", ["EU"]],
    ["E", ["AE", "E"]],
    ["AY", ["EI", "EY", "AY"]],
    ["Ö", ["OE", "Ö"]],
    ["KW", ["QU", "KW"]],
    ["C", ["CH", "SCH"]],
    ["K(?=[^EYÖ])", ["C", "K", "CK"]],
    ["K(?=[S])", ["KS", "CHS"]],
    ["C?K", ["K", "CK"]],
    ["(?<=[AOU])R", ["CH", "R"]],
    ["TS(?=[^EYÖ])", ["Z", "TS"]],
    ["TS(?=[EYÖ])", ["Z", "TS", "C"]],
    ["(?<![ST])S(?![SC])", ["S", "ß"]],
    ["T$", ["T", "D", "DT"]],
    ["V", ["V", "F"]],
    ["^J", ["J", "Y"]],
    [r"([LFBT])", [r"\1", r"\1\1"]]
]



def germanInversePhonem(name:str):
    code = name.upper()

    for substitution in AUGMENTATIONS:
        pattern, replacement = substitution

        if pattern.endswith("/g"):
            pattern = pattern[:-2]

        code = re.sub(pattern, replacement[random.randint(0, len(replacement)-1)], code)

    return code
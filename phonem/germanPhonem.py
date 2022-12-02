import re


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


SUBSTITUTIONS = [
    ["(?:SC|SZ|CZ|TZ|TS)/g", "C"],
    ["KS/g", "X"],
    ["(?:PF|PH)/g", "V"],
    ["QU/g", "KW"],
    ["UE/g", "Y"],
    ["AE/g", "E"],
    ["OE/g", "Ö"],
    ["E[IY]/g", "AY"],
    ["EU/g", "OY"],
    ["AU/g", "A§"],
    ["OU/g", "§"],
]
SUBSTITUTIONS2 = [
    ["(?:SC|SZ|CZ|TZ|TS)/g", "C"],
    ["KS/g", "X"],
    ["(?:PF|PH)/g", "V"],
    ["QU/g", "KW"],
    ["^Y", "J"],
    ["CHS/g", "KS"],
    ["C(?=[ÄEI])/g", "TS"],
    ["C(?=[^ÄEIH])/g", "K"],
    ["(?<=[AOU])CH/g", "R"],
    ["UE/g", "Y"],
    ["AE/g", "E"],
    ["OE/g", "Ö"],
    ["E[IY]/g", "AY"],
    ["EU/g", "OY"],
    ["AU/g", "A§"],
    ["OU/g", "§"],
    ["DT?$", "T"],
    ["Z/g", "TS"],
    ["CK/g", "K"],
]

TRANSLATION = translation(
  'ZKGQÇÑßFWPTÁÀÂÃÅÄÆÉÈÊËIJÌÍÎÏÜÝ§ÚÙÛÔÒÓÕØ',
  'CCCCCNSVVBDAAAAAEEEEEEYYYYYYYYUUUUOOOOÖ'
)

TRANSLATION2 = translation(
  'ZQÇÑßFÁÀÂÃÅÄÆÉÈÊËIÌÍÎÏÜÝ§ÚÙÛÔÒÓÕØ',
  'CCCNSVAAAAAEEEEEEYYYYYYYUUUUOOOOÖ'
)

ACCEPTABLE_LETTERS = set('ABCDLMNORSUVWXYÖ')
ACCEPTABLE_LETTERS2 = set('ABCDLMNORSUVWXYÖETWGKJP')

def germanPhonem(name):

    code = name.upper()

    for substitution in SUBSTITUTIONS2:
        isGlobal = False
        pattern, replacement = substitution

        if pattern.endswith("/g"):
            pattern = pattern[:-2]
            isGlobal = True

        newCode = re.sub(pattern, replacement, code)
        if isGlobal:
            while newCode != code:
                code = newCode
                newCode = re.sub(pattern, replacement, code)
	    
        code = newCode
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

INVERSETRANSLATIONS = {
    "V": ["V", "F", "W"],
    "C": ["C", "Z","K","G","Q"],
    "S": ["S", "ß"],
    "B": ["B", "P"],
    "D": ["D", "T"],
    "Y": ["Y", "I", "J"]
}

AUGMENTATIONS = [
    ["(?<!A)U/g", ["OU"]],
    ["OY/g", ["EU"]],
    ["AY/g", ["EI", "EY"]],
    ["Ö/g", ["OE"]],
    ["E/g", ["AE"]],
    ["KW/g", ["QU"]],
    ["KW/g", ["QU"]]
]



def germanInversePhonem(name:str):
    pass
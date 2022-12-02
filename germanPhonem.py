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

TRANSLATION = translation(
  'ZKGQÇÑßFWPTÁÀÂÃÅÄÆÉÈÊËIJÌÍÎÏÜÝ§ÚÙÛÔÒÓÕØ',
  'CCCCCNSVVBDAAAAAEEEEEEYYYYYYYYUUUUOOOOÖ'
)

ACCEPTABLE_LETTERS = set('ABCDLMNORSUVWXYÖ')

def phonem(name):

    code = name.upper()

    for substitution in SUBSTITUTIONS:
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

    translatedCode = ''
    for letter in code:
        translatedCode += TRANSLATION[letter] if letter in TRANSLATION else letter
    
    translatedCode = squeeze(translatedCode)

    code = ''
    for letter in translatedCode:
        if letter in ACCEPTABLE_LETTERS:
            code += letter

    return code
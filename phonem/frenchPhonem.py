import re
from pydash.strings import deburr

VOWELS = 'AEIOUY'
CONSONANTS = f"^{VOWELS}"
V = f"[{VOWELS}]"
C = f"[{CONSONANTS}]"


RULES = {
	# Vowels & vowel clusters
	'V-1': ["E?AU/g", 'O'],
	'V-2': ["(?:E?AU|O)LT$", 'O'],
	'V-3': ["E?AUT$", 'O'],
	'V-4': ["E?AUX$", 'O'],
	'V-5': ["(?:E?AU|O)LX$", 'O'],
	'V-6': ["E?AUL?D$", 'O'],
	'V-7': ["([^G])AY$", '\\1E'],
	'V-8': ["EUX$", 'EU'],
	'V-9': [fr"EY(?=$|{C})", 'E'],
	'V-10': [fr"(^|{C})Y|Y({C}|$)", '\\1I\\2'],
	'V-11': [fr"({V})I(?={V})", '\\1Y'],
	'V-12': [fr"({V})ILL", '\\1Y'],
	'V-13': ["OU(?=I(?!LL)|[AEOU])/g", 'W'],
	'V-14': [fr"({V})\1", '\\1'],

	# Nasals
	'V-15': [fr"[AE]M(?=[{CONSONANTS}N](?!$))", 'EN'],
	'V-16': [fr"OM(?=[{CONSONANTS}N])", 'ON'],
	'V-17': [fr"AN(?={C})", 'EN'],
	'V-18': [fr"(?:AIM|AIN|EIN)(?={C}|$)", 'IN'],
	'V-19': ["(?:BORNE?|BOURNE?|BURNE)$", 'BURN'],
	'V-20': [fr"(?:^IM|IM(?={C}))(?=[{CONSONANTS}N])", 'IN'],

	# Consonants & consonant clusters
	'C-1': ["BV/g", 'V'],
	'C-2': [fr"({V})C(?=[EIY])", '\\1SS'],
	'C-3': ["([^CX])C(?=[EIY])/g", '\\1S'],
	'C-4': ["^C(?=[EIY])", 'S'],
	'C-5': ["^C(?=[AOU])", 'K'],
	'C-6': [fr"({V})C$", '\\1K'],
	'C-7': [fr"C(?=[{CONSONANTS}CH])", 'K'],
	'C-8': ["CC(?=[AOU])/g", 'K'],
	'C-9': ["CC(?=[EIY])/g", 'X'],
	'C-10': ["G(?=[EIY])/g", 'J'],
	'C-11': ["GA(?=I?[MN])/g", 'G§'], # The paper is inconsistent so I cheated.
	'C-12': ["(?:GEO|GEAU)/g", 'JO'],
	'C-13': [fr"GNI(?={V})", 'GN'],
	'C-14': ["(^|[^CPS])H/g", '\\1'],
	'C-15': ["JEA/g", 'JA'],
	'C-16': [fr"^MAC(?={C})", 'M§'], # The paper is inconsistent so I cheated.
	'C-17': ["^MC", 'M§'],
	'C-18': ["PH/g", 'F'],
	'C-19': ["QU/g", 'K'],
	'C-20': ["^SC(?=[EIY])", 'S'],
	'C-21': ["(.)SC(?=[EIY])/g", '\\1SS'],
	'C-22': ["(.)SC(?=[AOU])/g", '\\1SK'],
	'C-23': ["SH/g", 'CH'],
	'C-24': ["TIA$", 'SSIA'],
	'C-25': ["([AIOUY])W/g", '\\1'],
	'C-26': ["X[CSZ]/g", 'X'],
	'C-27': [fr"(?:Z(?={V})|({C})Z(?={C}))", '\\1S'],
	'C-28': [fr"(?:([{CONSONANTS}CLS])\1|(C)C(?!{V})|({C}S)S|(.S)S(?!{V})|([^I]L)L)", r'\1\2\3\4\5'],
	'C-28-bis': ["ILE$", 'ILLE'],
	'C-29': [fr"(?:(ILS)|([CS]H)|([MN]P)|(R[CFKLNSX])|({C}){C})$", r'\1\2\3\4\5'],
	'C-30': ["^(?:SINT?|SAINT?|SEIN|SEIM|CINQ?)", 'ST-'],
	'C-31': ["^SAINTE", 'STE-'],
	'C-32': ["^ST(?!E)", 'ST-'],
	'C-33': ["^STE", 'STE-']
}

ORDERED_RULES = [
  'V-14', 'C-28', 'C-28-bis', # START
  'C-12',
  'C-9',
  'C-10',
  'C-16',
  'C-17',
  'C-20',
  'C-2', 'C-3', 'C-7',
  'V-2', 'V-3', 'V-4', 'V-5', 'V-6',
  'V-1',
  'C-14',
  'C-11',
  'C-33', 'C-32', 'C-31', 'C-30', # SAINT
  'V-15', 'V-17', 'V-18',
  'V-7', 'V-8', 'V-9', 'V-10', 'V-11', 'V-12', 'V-13', 'V-16', 'V-19', 'V-20', # V
  'C-1', 'C-4', 'C-5', 'C-6', 'C-8', 'C-13', 'C-15', 'C-18', # C
  'C-19', 'C-21', 'C-22', 'C-23', 'C-24', 'C-25', 'C-26', 'C-27', # C
  'C-29', # END
  'V-14', 'C-28', 'C-28-bis' # ONCE AGAIN
]

FIXING_RULES = [
  ["G§/g", 'GA'],
  ["M§/g", 'MAC']
]

ORDERED_RULES = list(map(lambda key:  RULES[key], ORDERED_RULES))
ORDERED_RULES += FIXING_RULES


def frenchPhonem(name:str):
	code = deburr(name).upper()
	code = re.sub("[^A-Z]", "", code)

	# Applying rules in order
	for rule in ORDERED_RULES:
		isGlobal = False
		pattern, replacement = rule

		if pattern.endswith("/g"):
			pattern = pattern[:-2]
			isGlobal = True

		newCode = re.sub(pattern, replacement, code)
		if isGlobal:
			while newCode != code:
				code = newCode
				newCode = re.sub(pattern, replacement, code)

		code = newCode

	return code

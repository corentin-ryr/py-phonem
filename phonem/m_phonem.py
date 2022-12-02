from phonem.frenchPhonem import frenchPhonem
from phonem.germanPhonem import germanPhonem, germanInversePhonem
from phonem.italianPhonem import italianPhonem

def phonem(name:str, lang:str):
    languages = {"fr", "de", "it"}
    if lang not in languages:
        raise ValueError(f"Language should be one of {languages}")

    if lang == "fr":
        return frenchPhonem(name)
    if lang == "de":
        return germanPhonem(name)
    if lang == "it":
        return italianPhonem(name)

def inversePhonem(name:str, lang:str):
    languages = {"fr", "de", "it"}
    if lang not in languages:
        raise ValueError(f"Language should be one of {languages}")

    if lang == "fr":
        raise NotImplementedError()
    if lang == "de":
        return germanInversePhonem(name)
    if lang == "it":
        raise NotImplementedError()
    
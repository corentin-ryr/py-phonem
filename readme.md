# Phonetic encoding and inverse phonetic encoding

This project contains algorithms to generate the phonetic encoding of words in three languages: French, German and Italian.
It also contains a reverse phonetic encoding that can generate a new word with a similar pronunciation.

## Phonetic encoding

Phonetic encoding is an algorithm to transform a word into a shorter word that has the same pronunciation (e.g. "EDOUARD" to "EDWAR"). The algorithm is different for each language as it accounts for the specifics of that language's pronunciation.

Two words with the same pronunciation are likely to have the same encoding. (e.g. 'MEIER' -> 'MEYER' and 'MEILLER' -> 'MEYER')

## Reverse phonetic encoding

The reverse algorithm is stochastic. It generates a new word from a phonetic encoding. The reverse encoding has a similar pronunciation and the encoding of the reverse encoding is the initial encoding (e.g. "OBY" -reverse-> "OBBI" -encoding-> "OBY")


## Usage

You can get the phonetic encoding by using the `phonem` method and you can generate a new word by using the `inversePhonem` method.

```py
from phonem import phonem, inversePhonem

name = "typisch"
pho = phonem(test[0], "de")
inversepho = inversePhonem(pho, "de")
```

# References

This project is a translation and extension of [Talisman](https://github.com/Yomguithereal/talisman), a Javascript library (it includes encoding for german and french).
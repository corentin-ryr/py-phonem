from germanPhonem import phonem


tests = [
    ['', ''],
    ['müller', 'MYLR'],
    ['schmidt', 'CMYD'],
    ['schneider', 'CNAYDR'],
    ['fischer', 'VYCR'],
    ['weber', 'VBR'],
    ['meyer', 'MAYR'],
    ['wagner', 'VACNR'],
    ['schulz', 'CULC'],
    ['becker', 'BCR'],
    ['hoffmann', 'OVMAN'],
    ['schäfer', 'CVR'],
    ['mair', 'MAYR'],
    ['bäker', 'BCR'],
    ['schaeffer', 'CVR'],
    ['computer', 'COMBUDR'],
    ['pfeifer', 'VAYVR'],
    ['pfeiffer', 'VAYVR']
]

for test in tests:
    pho = phonem(test[0])

    if pho != test[1]:
        print(pho)
        print(f"Should be: {test[1]}")
        print()
    else:
        print(f"OK: {test[0]}")
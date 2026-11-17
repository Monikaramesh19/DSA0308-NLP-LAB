def plural_fsm(word):
    if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        state = 'ES'
    elif word.endswith('y') and word[-2] not in 'aeiou':
        state = 'IES'
    else:
        state = 'S'

    if state == 'ES':
        return word + 'es'
    elif state == 'IES':
        return word[:-1] + 'ies'
    else:
        return word + 's'

words = ['cat', 'box', 'bus', 'baby', 'church', 'dog']

print("Singular\tPlural")
for word in words:
    print(word, "\t\t", plural_fsm(word))
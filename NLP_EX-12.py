
grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Det', 'N']],
    'VP': [['V', 'NP']],
    'Det': [['the']],
    'N': [['cat'], ['mouse']],
    'V': [['chased']]
}

def earley_parse(sentence):
    words = sentence.split()
    chart = [set() for _ in range(len(words) + 1)]

    chart[0].add(('S0', ('S',), 0, 0))

    for i in range(len(chart)):
        changed = True

        while changed:
            changed = False

            for state in list(chart[i]):
                lhs, rhs, dot, start = state

                if dot < len(rhs):
                    symbol = rhs[dot]

                    if symbol in grammar:
                        for rule in grammar[symbol]:
                            new_state = (symbol, tuple(rule), 0, i)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                    elif i < len(words) and words[i] == symbol:
                        chart[i + 1].add(
                            (lhs, rhs, dot + 1, start)
                        )

                else:
                    for old in list(chart[start]):
                        old_lhs, old_rhs, old_dot, old_start = old

                        if old_dot < len(old_rhs) and old_rhs[old_dot] == lhs:
                            new_state = (
                                old_lhs, old_rhs, old_dot + 1, old_start
                            )
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

    return ('S0', ('S',), 1, 0) in chart[len(words)]

sentence = "the cat chased the mouse"

if earley_parse(sentence):
    print("Sentence is accepted by Earley Parser")
else:
    print("Sentence is rejected by Earley Parser")
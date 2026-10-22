def finite_automaton(string):
    state = 0
    for ch in string:
        if ch == 'a':
            state = 1
        elif ch == 'b' and state == 1:
            state = 2
        else:
            state = 0
    return state == 2
strings = ["ab", "aab", "abab", "abc", "ba", "abb"]
for s in strings:
    if finite_automaton(s):
        print(s, "-> Accepted")
    else:
        print(s, "-> Rejected")

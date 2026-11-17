import re

def parse(expression):
    expression = expression.strip()

    pattern = r'^(forall|exists)\s+([a-zA-Z]+)\s*\((.+)\)$'

    match = re.match(pattern, expression, re.IGNORECASE)

    if match:
        quantifier = match.group(1)
        variable = match.group(2)
        predicate = match.group(3)

        print("Valid FOPC Expression")
        print("Quantifier:", quantifier)
        print("Variable:", variable)
        print("Predicate:", predicate)

    elif re.match(r'^[A-Z][a-zA-Z]*\([a-zA-Z, ]+\)$', expression):
        print("Valid FOPC Expression")
        print("Predicate:", expression)

    else:
        print("Invalid FOPC Expression")

expression = "forall x (Human(x))"

parse(expression)

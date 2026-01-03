#!/usr/bin/python3
#automated_theorem_prover.py

def negate(literal):
    if literal.startswith("~"):
        # If the literal is negated (starts with '~'), remove the '~' to get its positive form
        return literal[1:]
    else:
        # If the literal is positive, add '~' to negate it
        return "~" + literal


def make_clause(*literals):
    return frozenset(literals)

def resolve(c1, c2):
    resolvents = set()
    for l in c1:
        nl = negate(l)
        if nl in c2:
            resolvent = (c1 | c2) - {l, nl}
            resolvents.add(resolvent)
    return resolvents


def resolution_prover(clauses):
    clauses = set(clauses)
    while True:
        new_clauses = set()
        clause_list = list(clauses)

        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):
                resolvents = resolve(clause_list[i], clause_list[j])
                if frozenset() in resolvents:
                    return True
                new_clauses |= resolvents

        if new_clauses.issubset(clauses):
            return False

        clauses |= new_clauses


if __name__ == "__main__":
    # Example: (A ∨ B), ¬A, ¬B => contradiction

    clauses = {
        make_clause("A", "B"),
        make_clause("~A"),
        make_clause("~B")
    }

    result = resolution_prover(clauses)
    if result:
      print("Theorem proven")
    else:
      print("Theorem not proven")

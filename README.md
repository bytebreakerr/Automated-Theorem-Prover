This project uses the resolution principle to implement a basic automated theorem prover for propositional logic. In order to prove a theorem by refutation, the prover ascertains whether a given set of logical clauses entails a contradiction.

Clause normal form (CNF), in which each clause is a disjunction of literals, is used to express logical statements. Negation is explicitly represented, and literals are modeled as strings. By removing complementary literals from pairs of clauses, the system repeatedly applies the resolution rule to create new clauses. A logical contradiction is found and the theorem is deemed proven if the resolution process yields the empty clause.

Clarity and educational value are prioritized over performance in this implementation. It illustrates the fundamental principles of automated reasoning, such as literal negation, clause representation, resolvent generation, and iterative resolution. While

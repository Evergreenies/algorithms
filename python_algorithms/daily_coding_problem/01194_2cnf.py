"""
A Boolean formula can be said to be satisfiable if there is a way to 
assign truth values to each variable such that the entire formula 
evaluates to true.

For example, suppose we have the following formula, where the symbol 
¬ is used to denote negation:

(¬c OR b) AND (b OR c) AND (¬b OR c) AND (¬c OR ¬a)

One way to satisfy this formula would be to let a = False, b = True, 
and c = True.

This type of formula, with AND statements joining tuples containing 
exactly one OR, is known as 2-CNF.

Given a 2-CNF formula, find a way to assign truth values to satisfy 
it, or return False if this is impossible.
"""


from collections import defaultdict
from typing import DefaultDict


def is_satisfy_2cnf_brute_force(formula: list[tuple]) -> bool:
    variables = set(list(literal for clause in formula for literal in clause))
    num_variables = len(variables)

    for assignement in range(2**num_variables):
        thruth_values = {
            variable: (assignement >> index) & 1
            for index, variable in enumerate(variables)
        }

        if all(any(thruth_values[literal] for literal in clause) for clause in formula):
            return True

    return False


def build_graph(formula: list[tuple]) -> DefaultDict:
    implication_graph = defaultdict(set)
    for clause in formula:
        literal1, literal2 = clause
        implication_graph[negation(literal2)].add(literal1)

    return implication_graph


def negation(literal: str) -> str:
    return literal[1:] if literal[0] == "!" else f"!{literal}"


def is_satisfy_2cnf_implication_graph(formula: list[tuple]) -> bool:
    graph: DefaultDict[str, set[str]] = build_graph(formula)
    for current_node, neighbors in graph.items():
        if current_node in neighbors:
            return False

    return True


if __name__ == "__main__":
    assert (
        is_satisfy_2cnf_brute_force(
            [("!c", "b"), ("b", "c"), ("!b", "c"), ("!b", "!a")]
        )
        is True
    )
    assert (
        is_satisfy_2cnf_implication_graph(
            [("!c", "b"), ("b", "c"), ("!b", "c"), ("!b", "!a")]
        )
        is True
    )

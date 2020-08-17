from parglare import Parser, Grammar

grammar = r"""
E: E '+' E  {left, 1}
 | E '-' E  {left, 1}
 | E '*' E  {left, 2}
 | E '/' E  {left, 2}
 | E '^' E  {right, 3}
 | '(' E ')'
 | number;

terminals
number: /\d+(\.\d+)?/;
"""

file_name = "entrada.pg"

actions = {
    "E": [lambda _, n: n[0] + n[2],
          lambda _, n: n[0] - n[2],
          lambda _, n: n[0] * n[2],
          lambda _, n: n[0] / n[2],
          lambda _, n: n[0] ** n[2],
          lambda _, n: n[1],
          lambda _, n: n[0]],
    "number": lambda _, value: float(value),
}

g = Grammar.from_file(file_name)
parser = Parser(g, debug=True)

result = parser.parse("34 + 4.6")

print("Result = ", result)
from parglare import Parser, Grammar

file_name = "entrada.pg"

g = Grammar.from_file(file_name)
parser = Parser(g, debug=True)

result = parser.parse("34 + 4.6")

print("Result = ", result)

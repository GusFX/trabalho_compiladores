from parglare import Parser, Grammar

# arquivo de entrada no formato padrão recomendado pela biblioteca
file_name = "entry.pg"

g = Grammar.from_file(file_name)
parser = Parser(g, debug=True)

result = parser.parse("34 + 4.6")

print("Result = ", result)

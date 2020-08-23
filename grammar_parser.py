from parglare import Parser, Grammar
# arquivo de entrada no formato padrão recomendado pela biblioteca
import pgFile as pgfile
import inputFile as inputfile


def main():
    fileName = 'entry.pg'
    grammar = inputfile.readGrammarFile('gramatica.txt')
    pgfile.createPgFile(fileName, grammar)

    g = Grammar.from_file(fileName)
    parser = Parser(g, debug=True, debug_colors=True)

    result = parser.parse("abcaa")

    print("Result = ", result)

if __name__ == '__main__':
    main()
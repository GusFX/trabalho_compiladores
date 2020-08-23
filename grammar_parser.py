from parglare import Parser, Grammar
# arquivo de entrada no formato padrão recomendado pela biblioteca
import pgFile as pgfile
import inputFile as inputfile


def main():
    file_name = 'entry.pg'
    grammar = inputfile.readGrammarFile('gramatica.txt')
    #pgfile.createPgFile(file_name)

    #g = Grammar.from_file(file_name)
    #parser = Parser(g, debug=True, debug_colors=True)

    #result = parser.parse("34 + 4.6")

    #print("Result = ", result)

if __name__ == '__main__':
    main()
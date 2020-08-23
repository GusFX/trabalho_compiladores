def readGrammarFile(name): 
    grammar_file = open(name ,"r")
    lines = grammar_file.readlines()
    data = []
    for i in range(len(lines) - 1): 
        array_line = lines[i].split('[')
        if i == 0 or i == 1: 
            data.append(readTerminals(array_line[1]))
        elif i == 2: 
            data.append(readProductionRules(array_line[1]))
    data.append(readInitialTerminal(lines[len(lines) - 1]))
    print(data)

def readTerminals(array_line):
    array_line = filterString(array_line)
    return array_line.split(',')

def readProductionRules(array_line):
    array_line = filterString(array_line)
    array_line = array_line.split(',')
    production_list = {}
    for production in array_line:
        production = production[1:len(production)- 1]
        production = production.split('>')
        production_list[production[0]] = separateProductionRule(production[1])
    return production_list

def readInitialTerminal(array_line):
    array_line = array_line.replace(" ", "")
    index = array_line.find('=')
    if(index < 0): 
        print('Entrada não está no formato reconhecido!')
        exit(1)
    return array_line[index + 1:index + 2]

def filterString(string): 
    end_index = string.find(']')
    if(end_index < 0): 
        print('Entrada não está no formato reconhecido!')
        exit(1)
    return (string[0: end_index]).replace(" ", "")

# cria o array dos resultados de cada terminal
def separateProductionRule(productionResults):
    return productionResults.split('|')
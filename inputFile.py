def readGrammarFile(name): 
    grammarFile = open(name ,"r")
    lines = grammarFile.readlines()
    data = []
    for i in range(len(lines) - 1): 
        arrayLine = lines[i].split('[')
        if i == 0 or i == 1: 
            data.append(readTerminals(arrayLine[1]))
        elif i == 2: 
            data.append(readProductionRules(arrayLine[1]))
    data.append(readInitialTerminal(lines[len(lines) - 1]))
    print(data)

def readTerminals(arrayLine):
    arrayLine = filterString(arrayLine)
    return arrayLine.split(',')

def readProductionRules(arrayLine):
    arrayLine = filterString(arrayLine)
    arrayLine = arrayLine.split(',')
    productionList = {}
    for production in arrayLine:
        production = production[1:len(production)- 1]
        production = production.split('>')
        productionList[production[0]] = separateProductionRule(production[1])
    return productionList

def readInitialTerminal(arrayLine):
    arrayLine = arrayLine.replace(" ", "")
    index = arrayLine.find('=')
    if(index < 0): 
        print('Entrada não está no formato reconhecido!')
        exit(1)
    return arrayLine[index + 1:index + 2]

def filterString(string): 
    endIndex = string.find(']')
    if(endIndex < 0): 
        print('Entrada não está no formato reconhecido!')
        exit(1)
    return (string[0: endIndex]).replace(" ", "")

# cria o array dos resultados de cada terminal
def separateProductionRule(productionResults):
    return productionResults.split('|')
def createPgFile(name, grammar):
    
    nonTerminals, terminals, productions, initialState = grammar
    gramStr = ""

    with open(name, "w+") as pg:
        for nt in nonTerminals:
            for prod in productions[nt]:
                gramStr += f'{nt}:\t'
                gramStr += separeteSymbols(prod)
                gramStr += f';\n'


        gramStr += f'\nterminals\n'


        for term in terminals:
            gramStr += f'{term}: "{term}";\n'
        
        pg.write(gramStr)

def separeteSymbols(production):
    separetedProd = ""
    for p in production:
        separetedProd += f'{p} ' 
    return(separetedProd[0:-1])
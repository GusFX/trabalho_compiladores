# trabalho_compiladores

Trabalho final da disciplina de compiladores

Membros do grupo: Dênes Vargas e Gustavo Felix

### Parser de Expressões Regulares
Para este trabalho utilizamos a biblioteca Parglare, com suporte à linguagem Python.

O código le o arquivo entryER.pg que contém a gramática solicitada no trabalho e ao executar o arquivo grammar_parser.py o mesmo será lido e então ficará em loop solicitando entradas a serem validadas.

##### funcionalidade extra

Ao descomentar as três linhas da main no arquivo grammar_parser.py, pode-se gerar um arquivo .pg a partir de uma gramática qualquer, realizando os seguintes passos:

O código lê a gramática desejada de um arquivo texto (gramatica.txt) e, em seguida, a converte para um arquivo do tipo "pg" (que deve ser setado na main), reconhecido pela biblioteca. Em seguida, essa gramática é validada. Se estiver correta, uma entrada é solicitada ao usuário da expressão que se deseja validar.

### Instalação
Para a instalação em um ambiente linux, seguem-se os seguintes passos

1. Instalação do Python
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3.6
```
2. Instalação do Pip
```
sudo apt-get install python3-pip
```
3. Instalação do Parglare
```
sudo pip3 install parglare
```
### Execução
Para executar o programa, basta executar o arquivo "grammar_parser.py"
```
python3 grammar_parser.py
```

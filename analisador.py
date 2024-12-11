from tabulate import tabulate
import ply.lex as lex

# Lista de tokens
tokens = [
    "RESERVED",
    "TYPE",
    "CLASS",
    "PROPERTY",
    "INDIVIDUAL",
    "DATATYPE",
    "INTEGER",
    "SYMBOL",
    "NAMESPACEID"
]

# Palavras reservadas específicas
reserved_words = {
    "SOME": "RESERVED",
    "ALL": "RESERVED",
    "VALUE": "RESERVED",
    "MIN": "RESERVED",
    "MAX": "RESERVED",
    "EXACTLY": "RESERVED",
    "THAT": "RESERVED",
    "NOT": "RESERVED",
    "AND": "RESERVED",
    "OR": "RESERVED",
    "some": "RESERVED",
    "all": "RESERVED",
    "value": "RESERVED",
    "min": "RESERVED",
    "max": "RESERVED",
    "exactly": "RESERVED",
    "that": "RESERVED",
    "not": "RESERVED",
    "and": "RESERVED",
    "or": "RESERVED",
}

types = {
    "Class:": "TYPE",
    "EquivalentTo:": "TYPE",
    "Individuals:": "TYPE",
    "SubClassOf:": "TYPE",
    "DisjointClasses:": "TYPE",
}
## 
def t_SYMBOL(t):
    r"[\[\]\{\}=\,\"\(\)><,]"
    symbol_table.append({
      "Lexema": t.value,
      "Token": "Símbolo",
      "Linha": t.lineno
    })
    return t

def t_TYPE(t):
    r'\b(Class|EquivalentTo|Individuals|SubClassOf|DisjointClasses|):'
    symbol_table.append({
        "Lexema": t.value,
        "Token": "TYPE",
        "Linha": t.lineno
    })
    token_counts["TYPE"] += 1
    return t

def t_RESERVED(t):
    r'\b(SOME|ALL|VALUE|MIN|MAX|EXACTLY|THAT|NOT|AND|OR|some|all|value|min|max|exactly|that|not|and|or)\b'
    symbol_table.append({
        "Lexema": t.value,
        "Token": "RESERVED",
        "Linha": t.lineno
    })
    token_counts["RESERVED"] += 1
    return t

def t_CLASS(t):
    r'\b[A-Z][a-zA-Z0-9_]*\b'
    symbol_table.append({
        "Lexema": t.value,
        "Token": "CLASS",
        "Linha": t.lineno
    })
    token_counts["CLASS"] += 1
    return t

def t_PROPERTY(t):
    r'\b([a-z]+[a-zA-Z0-9_]+|has[A-Za-z]+|is[A-Za-z]+Of|[a-z][a-zA-Z]*)\b'
    symbol_table.append({
        "Lexema": t.value,
        "Token": "PROPERTY",
        "Linha": t.lineno
    })
     #Contador de tokens
    token_counts["PROPERTY"] += 1
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    symbol_table.append({
        "Lexema": str(t.value),
        "Token": "Inteiro",
        "Linha": t.lineno
    })
     #Contador de tokens
    token_counts["INTEGER"] += 1
    return t

def t_NAMESPACEID(t):
    r'\b(xsd|rdf|owl):[a-zA-Z][a-zA-Z0-9_]*\b'
    symbol_table.append({
        "Lexema": t.value,
        "Token": "Namespace ID",
        "Linha": t.lineno
    })
    #Contador de tokens
    token_counts["NAMESPACEID"] += 1
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

##Ignora espaços em branco e tabulações
t_ignore = ' \t'

def t_error(t):
    symbol_table.append({
        "Lexema": t.value[0],
        "Token": "Caractere Inválido",
        "Linha": t.lineno
    })
   
    token_counts["INVALID"] += 1
    t.lexer.skip(1)

lexer = lex.lex()

# Lista para armazenar os símbolos
symbol_table = []


token_counts = {
    "TYPE": 0,
    "RESERVED": 0,
    "CLASS": 0,
    "PROPERTY": 0,
    "INTEGER": 0,
    "NAMESPACEID": 0,
    "INVALID": 0
}

def process_file(file_path):
    # Abre o arquivo e lê o conteúdo
    with open(file_path, 'r') as file:
        input_text = file.read()

    # Processa o conteúdo do arquivo com o lexer
    lexer.input(input_text)
    
    while tok := lexer.token():
        pass

    symbol_list = [[entry["Lexema"], entry["Token"], entry["Linha"]] for entry in symbol_table]    

    print(tabulate(symbol_list, headers=["Lexema", "Token", "Linha"], tablefmt="fancy_grid"))
    
    print("\nQuantidade de tokens por tipo:")
    for token_type, count in token_counts.items():
        print(f"{token_type}: {count}")

if __name__ == "__main__":
    # Caminho para o arquivo de texto a ser analisado
    file_path = '/home/douglasly/Analisador_Lexico/texto.txt'  
    process_file(file_path)

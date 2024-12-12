# Analisador Léxico
O analisador em questão faz uma análise léxica de um código fonte, identificando e classificando os tokens presentes no código. Ele percorre todo o texto, reconhecendo palavras reservadas, inteiros, propriedades, identificando quando se trata de um tipo de dado, dentre outras propriedades. Sendo útil na validação de códigos mais simples ou como base para a construção de um analisador sintático.

## Sumário

1. [Instalação](#instalação)
2. [Utilização](#utilização)
3. [Exemplos](#exemplos)



# Tecnologias utilizadas
1. Python 3.0
2. Bibliotecas (ply e tabulate)
3. Visual Studio Code
   
# Instalação
Passos para instalar o projeto:
1. Faça o clone ou o download do repositório;
2. Certifique de ter o Phyton instalado em sua máquina

    Caso não possua, execute a instalação do Phyton3.0
      
```ruby
sudo apt install python3.10
```   
4. Instale as dependências:

```ruby
    pip install ply tabulate
```
   ---------------------
# Estrutura do repositório
/analisador_lexico
   ├── texto.txt            # Arquivo de exemplo para análise
   ├── analisador.py        # Script principal
   ├── README.md            # Este arquivo


# Utilização

1. Abra o arquivo 'analisador.py';
2. No campo 'file_path' adicione o caminho do arquivo txt a ser analisado, como ilustrado no trecho de código abaixo:

```ruby
  if __name__ == "__main__":
    # Caminho para o arquivo de texto a ser analisado
    file_path = 'caminho_do_arquivo.txt'  
    process_file(file_path)
```

4. Após a modificação do path, basta executar o analisador

```
   python3 analisador.py
```

# Exemplo prático

Se utilizar o seguinte conteúdo no arquivo .txt

```
Pizza that
hasTopping some MozzarellaTopping and
hasTopping some TomatoTopping and
hasTopping only (MozzarellaTopping orTomatoTopping)
```

Após a execução o sistema retornará uma saída no seguinte formato:
   
![Captura de tela de 2024-12-11 20-33-55](https://github.com/user-attachments/assets/d911488a-e0ac-4d38-9703-e6ca54936c8e)

O analisador disponibiliza o Lexema, o Token, linha de ocorrência e a quantidade de ocorrências de cada Token

# Ajustes no código

Se precisar adicionar ou modificar alguma propriedade dos tokens reconhecidos, você pode criar novas regras léxicas, modificar as expressões regulares existentes ou alterar a classificação dos tokens. 






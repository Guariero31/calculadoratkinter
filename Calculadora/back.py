# Função para dividir a expressão em números e operador
def split(expressao, delimitador):
    resultado = []  # Cria uma lista vazia para armazenar os números e o operadores

    # Verifica se a expressao esta vazia. Se for vazia, retorna a expressão
    if not expressao:
        return [expressao]

    # Verifica se o delimitador não foi fornecido
    # Se não for fornecido, assume-se uma string vazia como delimitador
    if not delimitador:
        delimitador = ''

    start = 0  #Variável para armazenar a posição inicial de cada número na expressão

    # Percorre cada caractere (char) na expressão juntamente com seu índice (index)
    for index, char in enumerate(expressao):
        # Verifica se o caractere atual é um dos operadores ('+', '-', 'x', '/', '!', '^', '%', 'Mod')
        if char in ('+', '-', 'x', '/', '!', '^', '%', 'M', '!'):
            # Se encontrou um operador, atualiza o delimitador para o caractere encontrado
            # e adiciona o número anterior à lista de resultados.
            resultado.append(expressao[start:index])
            delimitador = char
            start = index + 1

    # Após o loop, adiciona o último número encontrado e o delimitador à lista de resultados.
    resultado.append(expressao[start:])
    resultado.append(delimitador)

    return resultado

# Função da calculadora
def calculadora(expressao):
    # Divide a expressão em números e operador usando a função split()
    res = split(expressao, None)

    num1 = float(res[0])  # Obtém o primeiro número da lista e o converte para um valor numérico (float)
    num2 = float(res[1])  # Obtém o segundo número da lista e o converte para um valor numérico (float)

    # Realiza o cálculo com base no operador presente na posição 2 da lista
    if res[2] == '+':
        return num1 + num2
    elif res[2] == '-':
        return num1 - num2
    elif res[2] == 'x':
        return num1 * num2
    elif res[2] == '/':
        return num1 / num2
    elif res[2] == '^':
        return num1 ** num2
    elif res[2] == '%':
        return num1 * (num2 / 100)
    elif res[2] == 'M':
        return num1 % num2

def fatorial(expressao):
    res = split(expressao, None)

    num1 = float(res[0])

    if res[2] == '!':
        i = 1 
        contador = num1
        while contador > i:
            contador -= 1
            num1 = contador * num1
        return num1
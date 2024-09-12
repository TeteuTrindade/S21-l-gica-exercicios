def fatorial_iterativo(n):
    """
    Calcula o fatorial de um número usando abordagem iterativa.
    
    :param n: Número inteiro para o qual o fatorial será calculado.
    :return: Fatorial de n.
    """
    resultado = 1 # Inicializa o resultado com 1 (o valor inicial do fatorial)
    for i in range(1, n + 1): # Loop para multiplicar o resultado por cada número de 1 até n
        resultado *= i # Multiplica o resultado atual por i
    return resultado # Devolve um valor de uma função e encerra sua execução.

def main():
    """
    Função principal que interage com o usuário para obter um número e calcular o fatorial.
    """
    try: # Tenta executar um bloco de código onde erros podem ocorrer.
        numero = int(input("Digite um número inteiro para calcular o fatorial: ")) # Solicita ao usuário para digitar um número

        if numero < 0: # Verifica se o número é não-negativo
            print("O fatorial não é definido para números negativos.")
        else:
            resultado = fatorial_iterativo(numero) # Calcula o fatorial
            print(f"O fatorial de {numero} é {resultado}.") # Imprime o resultado
    
    except ValueError: # Captura e trata erros que ocorrem no bloco try.
        print("Por favor, insira um número inteiro válido.")

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
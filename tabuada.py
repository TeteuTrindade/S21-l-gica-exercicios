"""
TABUADA
"""

while True: # Enquanto for verdadeiro
    numero = int(input("Digite um número para ver a tabuada (0 para sair): ")) # Fala para digitar um número inteiro.
    if numero == 0: # Se digitar o número 0.
        break # O programa para.
    for i in range(1, 11): 
        """
        A variável i significa o intervalo numérico da range que inicía de 
        zero até o ultimo número correspondente ao intervalo da range.
        """
        print(f"{numero} x {i} = {numero * i}") # Faz a multiplicação e imprime o resultado
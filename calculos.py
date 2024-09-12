"""
CALCULADORA SIMPLES
"""
while True: # Enquanto a condição for verdadeira.
    print("Escolha a operação: ") # Mostra que você deverá escolhar uma operação matemática.
    print("1. Soma") # Aqui você escolherá a operação de soma.
    print("2. Subtração") # Aqui você escolherá a operação de subtração.
    print("3. Multiplicação") # Aqui você escolherá a operação de multiplicação.
    print("4. Divisão") # Aqui você escolherá a operação de divisão.
    print("0. Sair") # Aqui você poderá sair.
    
    escolha = input("Digite o número da operação desejada: ") # Aqui você escolherá a operação.
    
    if escolha == '0': # Se digitar o número 0.
        break # O sistema para.
    
    num1 = float(input("Digite o primeiro número: ")) # O primeiro número da conta, poderá ser decimal.
    num2 = float(input("Digite o segundo número: ")) # O segundo número da conta, poderá ser decimal.
    
    if escolha == '1': # Se a sua escolha for 1.
        print(f"Resultado: {num1 + num2}") # O resultado será a soma da variável num1 com a num2.
    elif escolha == '2': # Se a sua escolha for 2.
        print(f"Resultado: {num1 - num2}") # O resultado será a subtração da variável num1 com a num2.
    elif escolha == '3': # Se a sua escolha for 3.
        print(f"Resultado: {num1 * num2}") # O resultado será a multiplicação da variável num1 com a num2.
    elif escolha == '4': # Se a sua escolha for 4.
        if num2 == 0: # Se o segundo número for 0.
            print(f"Resultado: {num1 / num2}") # O resultado será a divisão da variável num1 com a num2.
        else: # Aparecerá a seguinte informação
            print("Erro: Divisão por zero!") # Aparecerá erro se o segundo número for 0.
    else: # Caso a escolha não seja existente.
        print("Escolha inválida!") # Aparecerá que a escolha é inválida.
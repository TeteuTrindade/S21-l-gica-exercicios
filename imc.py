def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC).
    
    :param peso: Peso da pessoa em quilogramas.
    :param altura: Altura da pessoa em metros.
    :return: IMC calculado.
    """
    imc = peso / (altura ** 2)  # Aplica a fórmula do IMC
    return imc

def classificar_imc(imc):
    """
    Classifica o IMC de acordo com as categorias padrão.
    
    :param imc: IMC calculado.
    :return: Categoria do IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    """
    Função principal que interage com o usuário para calcular e classificar o IMC.
    """
    try:
        # Solicita ao usuário para inserir o peso e a altura
        peso = float(input("Digite o seu peso em kg: "))
        altura = float(input("Digite a sua altura em metros: "))

        # Verifica se a altura é maior que zero
        if altura <= 0:
            print("A altura deve ser maior que zero.")
            return

        # Calcula o IMC
        imc = calcular_imc(peso, altura)
        # Classifica o IMC
        classificacao = classificar_imc(imc)

        # Imprime o resultado
        print(f"O seu IMC é {imc:.2f}. Classificação: {classificacao}.")
    
    except ValueError:
        # Captura e trata o erro se o usuário não inserir um número válido
        print("Por favor, insira valores numéricos válidos.")

# Executa a função principal se o script for executado diretamente
if __name__ == "__main__":
    main()
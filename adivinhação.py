import random

numero_sorteado = random.randint(1, 50) # Será escolhido um número de 1 a 50.
tentativas = 5 # Você tem 5 tentativas para acertar.

while tentativas > 0: # Enquanto a tentativas for maior que 0.
    palpite = int(input("Adivinhe um número de 1 a 10: ")) # Você poderá dar um palpite para acertar.
    
    if palpite == numero_sorteado: # Se o palpite for o mesmo número sorteado.
        print("Parabéns, você acertou!") # Aparecerá "Parabéns, você acertou".
        break # E o sistema para.
    elif palpite > numero_sorteado: # Se o palpite for maior do que o número sorteado.
        print("O número é menor.") # Aparecerá que o número sorteado é menor.
    else: # Caso o contrário.
        print("O número é maior.") # Aparecerá que o número sorteado é maior.
    
    tentativas -= 1 # Toda vez que errar, perderá uma tentativa.

if tentativas == 0: # Se tiver 0 tentativas restantes.
    print(f"Você perdeu! O número era {numero_sorteado}.") # Aparecerá que você perdeu e apresentará o número sorteado.
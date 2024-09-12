notas = []
while True: # Enquanto for verdadeiro.
    nota = float(input("Digite a nota do aluno (ou -1 para sair): ")) 
    """
    Digite a nota do aluno, ou digite -1 para sair.
    """
    if nota == -1: # Se a nota digitada for -1.
        break # O sistema para.
    notas.append(nota) # Apresentará os números acumulados.

media = sum(notas) / len(notas) # Irá fazer a média das notas.

print(f"Média do aluno: {media:.2f}") # Aparecerá a média do aluno.

if media >= 7: # Se a média for maior ou igual a 7.
    print("Aluno Aprovado!") # O aluno foi aprovado.
elif 5 <= media < 7: # Se a nota for entre 5 e 7.
    print("Aluno em Recuperação!") # O aluno estará de recuperação.
else: # Caso o contrário.
    print("Aluno Reprovado!") # O aluno será reprovado.
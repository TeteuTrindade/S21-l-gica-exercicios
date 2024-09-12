def main():
    """
    Função principal que coleta os dados dos alunos, calcula a média da turma
    e classifica cada aluno como Aprovado ou Reprovado.
    """
    alunos = [] # Lista para armazenar o nome dos alunos.
    notas = [] # Lista para armazenar as notas dos alunos.
    
    # Solicita o nome e a nota de 5 alunos.
    for i in range(5):
        print(f"\nAluno {i + 1}:") # Exibe o número do aluno (1 a 5).
        nome = input("Digite o nome do aluno: ") # Solicita o nome do aluno.
        
        while True: # Enquanto for verdadeiro.
            try:
                nota = float(input("Digite a nota do aluno (0 a 10): ")) # Solicita a nota e converte para float.
                if 0 <= nota <= 10: # Verifica se a nota está entre 0 e 10.
                    break # O sistema para.
                else:
                    print("Nota deve estar entre 0 e 10. Tente novamente.") # Mensagem de erro se a nota estiver fora do intervalo.
            except ValueError:
                print("Entrada inválida. Digite um número válido.") # Mensagem de erro se a entrada não for um número.
        
        alunos.append((nome, nota)) # Itera sobre cada aluno na lista de alunos.
        notas.append(nota) # Adiciona a nota à lista de notas.
    
    # Calcula a média da turma.
    media_turma = sum(notas) / len(notas)
    
    # Exibe a média da turma.
    print(f"\nMédia da turma: {media_turma:.2f}")
    
    # Classifica e exibe o status de cada aluno.
    print("\nClassificação dos alunos:")
    for nome, nota in alunos: # Itera sobre cada aluno na lista de alunos.
        if nota >= 7: # Verifica se a nota é maior ou igual a 7.
            status = "Aprovado" # Define o status como "Aprovado".
        else: # Caso o contrário.
            status = "Reprovado" # Define o status como "Reprovado".
        
        print(f"{nome}: Nota = {nota:.2f}, Status = {status}") # Exibe o nome, a nota e o status do aluno

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    main() # Executa a função principal

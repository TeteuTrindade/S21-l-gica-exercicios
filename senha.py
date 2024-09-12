"""
Digite a senha correte
"""
senha_correta = "segurança123" # A senha correta é "segurança123".

while True : # Enquanto for verdadeiro. 
    senha = input("Digite a senha correta:") # Digite a senha.
    if senha == senha_correta: # Se a senha digitada for igual a senha correta.
        print("Acesso permitido") # Aparecerá "Acesso permitido".
        break # E o sistema irá parar.
    else: # Caso o contrario.
        print("Senha incorreta") # Aparecerá que a senha está incorreta.
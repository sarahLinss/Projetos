while True: 
    senha =  input("Digite uma senha forte com no mínimo 8 caracteres")
    if len(senha) >= 8 and any(char.isdigit() for char in senha) and any(char.isalpha() for char in senha):
        print("Senha criada com sucesso")
        break
    else:
        print("Sua senha não atende os requisitos. Tente novamente")
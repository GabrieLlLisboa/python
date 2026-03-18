senha = "oi"
seja = "Seja bem vindo ao sistema de login"

while True:
    seja = "Seja bem vindo ao sistema de login"
    resposta = input("Digite a senha: ")

    if resposta == senha:
        print("Acesso Permitido")
        print(seja)
        break
    else:
        print("Senha Incorreta. Tente novamente.")
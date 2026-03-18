while True:
    print("\n=== CALCULADORA ===")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Sair")
    
    opcao = input("\nEscolha uma opção: ")
    
    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    
    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    
    elif opcao == "3":
        print("Encerrando programa...")
        break
    
    else:
        print("Opção inválida")
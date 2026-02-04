# Escreva um algoritmo em Python que leia uma opção escolhida
#   pelo usuário e faça as seguintes rotinas:

print("1 - Número ímpar ou par")
print("2 - Qual o valor maior")
print("3 - Calcular o dobro do valor")
continuar = "s"
while continuar == "s":
    situacao = int(input("Escolha a situação: "))
    match situacao:
        case 1:
            print("1 - Número ímpar ou par")
            numero = int(input("Digite o número: "))
            if numero % 2 == 0:
                print(f"O número {numero} é par")
            else:
                print(f"O número {numero} é ímpar")
        case 2:
            print("2 - Qual o valor maior")
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))

            if num1 > num2:
                print(f"O número {num1} é maior que o número {num2}")
            elif num2 > num1:
                print(f"O número {num2} é maior que o número {num1}")
            else:
                print("Opção inválida.")
        case 3:
            print("3 - Calcule o dobro do valor")
            numero = int(input("Digite um valor: "))
            dobro = numero * 2
            print(f"O dobro do {numero} é {dobro}")
    continuar = input("Você deseja continuar? (s/n)").lower().strip() # strip apaga todos os espaços
    if continuar != "s":
        print("Programa Encerrado")
        break # Interrompe a linha de comando
    
código antigo

print("Escolha uma opção")
print("1 - Verificar se um numero é par ou impar")
print("2 - verifique o número")
print("\n3 - calcular o dobro de um valor")
opcao = int(input("Digite a opção desejada: "))
match opcao:
    case 1:
        print(" 1 - par ou ímpar")
        numero = int(input("Escolha um número:"))
        if numero %2 == 0:
            print("O numero é par.")
        else:
            print("o numero é impar.") 
    case 2:
        print(" 2 - Verifique o número")
        numero1 = int(input("Escolha o 1º número:"))
        numero2 = int(input("Escolha o 2º número:"))
        if numero1 > numero2:   
            print(f"{numero1} é maior.")
        elif numero1 < numero2:
            print(f"{numero2} é maior.")
        else:
            print ("Os números são iguais.")
    case 3:
        print(" 3 - Dobro")
        n = int(input("Escolha o 1° numero: ")) 
        print(f"O dobro do número é: {n*2}") 
    case _:
        print('Opção inválida')      


código novo

print("\nOpções")
print("1 - Par ou ímpar")
print("2 - Verifique o número")
print("3 - DObro\n")
continuar = "s"
while continuar == "s":
    op = int(input("Escolha uma opção: "))
    match op:
        case 1:
            print(" 1 - Par ou ímpar")
            numero = int(input("Escolha um número: "))
            if numero %2 == 0:
                print("o número é par.")
            else:
                print("o número é ímpar.")
        case 2:
            print(" 2 - Verifique o número")
            numero1 = int(input("Escolha o 1º número: "))
            numero2 = int(input("Escolha o 2º número: "))
            if numero1 > numero2:
                print(f"{numero1} é maior.")
            elif numero1 < numero2:
                print(f"{numero2} é maior.")
            else:
                print("Os números são iguais.")
        case 3:
            print(" 3 - Dobro")
            n  = int(input("Escolha o 1º número: "))
            print(f"O dobro do número é: {n*2}")
        case _:
            print("Opção inválida")
    continuar = input("Deseja continuar?(s/n) ").lower().strip()
    if continuar != "s":
        print("Programa Encerrado")
        break #interromper a linha de comando do case


código antigo 2

nome = input("Nome: ")
p1 = float(input("Prova 01: "))
p2 = float(input("Prova 02: "))
    
md = (p1+p2)/2
if md >= 7:
    resultado = "Aprovado"
elif md >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"\nNome: {nome}")
print(f"Prova 01: {p1}")
print(f"Prova 02: {p2}")
print(f"Média: {md:.1f}")
print(f"Resultado: {resultado}")


nome = input("Nome: ")
while True:
    p1 = float(input("Prova 01 (0,0 e 10,0): ").replace(",","."))
    if p1 >= 0.0 and p1 <= 10.0:
        break # Interrompe a linha de comando
    else:
        print("Nota inválida! Digite o valor entre 0,0 e 10,0")
while True:
    p2 = float(input("Prova 02: "))
    if p2 >= 0.0 and p2 <= 10.0:
        break # Interrompe a linha de comando
    else:
        print("Nota inválida! Digite o valor entre 0,0 e 10,0")
    
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
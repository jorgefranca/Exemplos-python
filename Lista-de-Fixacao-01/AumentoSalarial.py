# Escrever um programa que calcule um aumento de 15% para um salário de R$ 750,00

#salario = 750.00
#bonus = 15    # em porcentagem
salario = float(input("Digite o salario: "))
bonus = int(input("bonus em porcentagem: "))

acrescimo = (bonus/100) * salario

novoSalario = salario + acrescimo

print("-------------------------")
print("Salario: R$ ", salario)
print("Adiconal: R$ ", acrescimo)
print("Novo Salario: R$", novoSalario)
print("-------------------------")
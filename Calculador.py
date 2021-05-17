# calculadora simples

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

op = input("operacao(Ex.: +, -, *, /): ")

if op == '+':
    resultado = num1 + num2
elif op == '-':
    resultado = num1 - num2
elif op == '*':
    resultado = num1 * num2
elif op == '/':
    #fazer a verificacao do num2=0
    resultado = num1 / num2
else:
    resultado = ''
    print("Operacao invalida")

if resultado != '':
    print(f"Resultado = {resultado:.5f}")

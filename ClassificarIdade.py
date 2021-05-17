#classificar de acordo com a idade
'''
idade = 65
print("---------------")
print("")
if idade <= 12:
    print("Criança")
else:
    if idade <= 18:
        print("Adolescente")
    else:
        if idade <= 59:
            print("Adulto")
        else:
            print("idoso")
print("----------------")
'''

idade = int(input("Digite sua idade: "))

print("---------------")
print("")
if idade <= 12:
    print("Criança")
elif idade <= 18:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("idoso")
print("----------------")
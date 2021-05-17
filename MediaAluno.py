'''
FAZER:
media do aluno

se media >= 7.0, o aluno foi aprovado
se media estiver entre 5 e 6.9, aluno em recuperação
se media < 5.0, aluno reprevado

se media>=7.0
    escreva("Aprovado")
senao
    escreva("reprovado")
----------------------------------------------------------

#CÓDIGO 1

media = float(input("Digite sua media: "))

print("--------------")

if media >= 7.0: 
    print("Aluno Aprovado!")
else:
    if media < 5.0:
        print("Aluno reprovado!")
    else:
        print("Aluno em recuperacao")
print("--------------")
'''
#CÓDIGO 2

media = float(input("Digite sua media: "))

print("--------------")

if media >= 7.0: 
    print("Aluno Aprovado!")
# 5.0<= media < 7.0
elif media>=5.0 and media < 7.0:
    print("Aluno em recuperacao!")
else:
    print("Aluno reprovado")
print("--------------")
# Aula 01
# --------------------------------
# Conteúdo: 
# operações lógicas 
# operadores relacionais

a = 10
b = 5

#operadores relacionais sempre retornam um valor booleano(True ou False)
print( a >= b ) # 'a' é maior ou igual a 'b'?
print( a == b ) # 'a' é igual a 'b'?
print( a != b ) # 'a' é diferente de 'b'?
print( a >= a ) # 'a' é maior ou igual a 'a'?

#operadores lógicos (and, or, not)
#and
print("-------OPERADOR AND--------")
print("true AND true: ",True and True)
print("false AND true: ",False and True)
print("true AND false: ",True and False)
print("false AND false: ",False and False)
#or
print("-------OPERADOR OR---------")
print("true OR true: ", True or True)
print("false OR true: ", False or True)
print("true OR false: ", True or False)
print("false OR false: ", False or False)
#not
print("-------OPERADOR NOT--------")
print("NOT true: ", not True)
print("NOT false: ", not False)
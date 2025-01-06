# operações básicas
num1 = 5
num2 = 12.7
u = -5
p = 17
r = 12.3 

# printa o tipo
print(type(num1))
print(type(num2))

# posso mudar o tipo da var
vira_float = float(num1)
print(vira_float)
print(type(vira_float))

# inclusive strings -> porém a string deve conter apenas números
xic_cafes_hoje = "235"

strtoint = int(xic_cafes_hoje)       # converte "235" para 235
strtofloat = float(xic_cafes_hoje)   # converte "235" para 235.0

print(type(strtoint)) 
print(type(strtofloat))  

print(strtoint, strtofloat)

# caso específico -> não é possível converter str float para int
#a = int("105.7") -> errado
# o certo é
a = int(float("105.7"))
print(type(a))
print(a)

# algumas funções

# retorna módulo
print(abs(u))

# retorna exponencial
print(pow(u,u))

# arredonda para o mais próximo
print(round(r))

import math

# arredonda para baixo
print(math.floor(r))

# arredonda para baixo
print(math.ceil(r))


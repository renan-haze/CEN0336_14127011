#Importando bibliotecas que serão importante para o código
import sys
import math

#Aplicando às variáveis comandos que fazem um link entre o usuário e o script
a = sys.argv[1]
b = sys.argv[2]

#Condição uar números maiores ou iguais a 500
#Essa condição acontece caso o que o usuário fornece os dados corretos
if int(a) & int(b) <= 500:
    print("your numbers are correct!")
    X = math.sqrt(int(a))
    Y = math.sqrt(int(b))
    Z = math.sqrt(int(a+b))
    print (int(Z))

#Caso o usuário forneça os dados errados, tal mensagem irá aparecer
else:
    print("the numbers must be less than 500")


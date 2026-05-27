from time import sleep
from random import randint

# INICIO
print("Eu sou o mestre da adivinhação...")
sleep(1)
print("Tente acertar o número que estou pensando entre 0 e 10!!")
sleep(1)

# VARIAVEIS
sorteado = randint(0,10)
tentativas = 1

# ENTRADA
num = int(input("Tente acertar o número: "))
while num != sorteado:
    num = int(input("Número errado. Tente de novo!! "))
    if num > sorteado:
        print("Foi muito!!. O número é menor viu!!")
    elif num < sorteado:
        print("Foi pouco!!. O número é maior viu!! ")
    tentativas += 1

# SAIDA
print(f"Você acertou!!!. O número era {sorteado}, como sabia? Foram {tentativas} tentativas!!")


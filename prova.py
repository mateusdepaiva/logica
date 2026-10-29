'''
nu_candi = int(input("qual numero?: "))
no_candi = input("coloque noome do candidato: ")
print(f"numero do candidato: {nu_candi}")
print(f"nome do candidato: {no_candi}")
print("cargo: Presidente")

escolha = int(input("qual dia? [1][2][3] "))
if escolha == 1:
    print("sexta-feira = bola")
elif escolha == 2:
    print("sabado = cinema")
elif escolha == 3:
    print("domingo = zoologico")
else:
    print("escolha invalida")
'''
import random
nu = [random.randint(1,100) for _ in range(10)]
 int(nu)
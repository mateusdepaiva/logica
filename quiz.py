while True:
 ponto = 0

 res1 = input("qual é o nome do robô que foi enviado a marte? ")
 if res1 == "rover":
     print("correto: +1 ponto")
     ponto = ponto + 1
 else:
     print("incorreto: rover")

 if ponto < 1:
    cont = input("continuar y/n: ")
    if cont == "y":
        continue
    else:
        break

 res2 = input("qual o nome do sateleti natural da terra? ")
 if res2 == "lua":
     print("correto +1 ponto")
     ponto = ponto + 1
 else:
     print("incorreto: lua")

 if ponto < 2:
    cont = input("continuar y/n: ")
    if cont == "y":
        continue
    else:
        break


 res3 = input("qual é o nome da entidade que assombra o minecraft desde sua beta? ")
 if res3 == "herobrine":
     print("correto +1 ponto")
     ponto = ponto + 1
 else:
     print("incorreto: herobrine")

 if ponto < 3:
    cont = input("continuar y/n: ")
    if cont == "y":
        continue
    else:
        break

 res4 = input("em minecraft qual é o comando que da items para o jogador?(sem simbolu) ")
 if res4 == "give":
     print("correto +1 ponto")
     ponto = ponto + 1
 else:
     print("incorreto: give")

 if ponto < 4:
    cont = input("continuar y/n: ")
    if cont == "y":
        continue
    else:
        break

 res5 = input("qual é o nome do ouriço com poderes psiquicos que veio do futuro em sonic06?(primeiro nome) ")
 if res5 == "silver":
     print("correto +1 ponto")
     ponto = ponto + 1
 else:
     print("incorreto: silver")

 if ponto < 5:
    cont = input("continuar y/n: ")
    if cont == "y":
        continue
    else:
        break
 
 print(f"ponto:{ponto}")

 cont = input("continuar y/n: ")
 if cont == "y":
    continue
 else:
    break

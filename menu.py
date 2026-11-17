print("=== menu ===")
print("1 - ver mensagem")
print("2 - sair")
opcao = input("escolha: ")
match opcao:
    case "1":
        print("bem-vindo")
    case "2":
        oo = input("quer fechar? y/n: ")
        match oo:
            case "y":
                print("encerrando...")
            case "n":
                
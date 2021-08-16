while True:
    try:
        password = 2002
        a = int(input())
        if password == a:
            print("Acesso Permitido")
            break
        else:
            print("Senha Invalida")

    except EOFError:
        break

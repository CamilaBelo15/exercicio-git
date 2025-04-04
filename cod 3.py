def verificar_maiusculas():
    try:
        texto = input("Digite uma string: ")

        if not texto.isupper():
            raise ValueError(
                "Erro: A string contém letras minúsculas ou outros caracteres que não são letras maiúsculas.")

        print("A string contém apenas letras maiúsculas.")

    except ValueError as erro:
        print(erro)


verificar_maiusculas()

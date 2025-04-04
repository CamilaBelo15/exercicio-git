def dividir_por_dez():
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero == 0:
            raise ZeroDivisionError("Erro: divisão por zero não é permitida.")
        resultado = 10 / numero
        print(f"Resultado da divisão: {resultado}")
    except ZeroDivisionError as e:
        print(e)
    except ValueError:
        print("Erro: por favor, digite um número inteiro válido.")

dividir_por_dez()

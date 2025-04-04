
class NumeroImparError(Exception):
    def __init__(self, numero):
        super().__init__(f"Erro: o número {numero} é ímpar. Por favor, digite um número par.")

def verificar_numero_par():
    try:
        numero = int(input("Digite um número inteiro: "))

        if numero % 2 != 0:
            raise NumeroImparError(numero)

        print(f"O número {numero} é par.")

    except NumeroImparError as e:
        print(e)
    except ValueError:
        print("Erro: entrada inválida. Certifique-se de digitar um número inteiro.")


verificar_numero_par()

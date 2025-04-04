class ComprimentoDiferenteError(Exception):
    def __init__(self, mensagem="As strings possuem comprimentos diferentes!"):
        super().__init__(mensagem)


def verificar_comprimento():
    try:
        string1 = input("Digite a primeira string: ")
        string2 = input("Digite a segunda string: ")

        if len(string1) != len(string2):
            raise ComprimentoDiferenteError()

        print("As strings têm o mesmo comprimento!")

    except ComprimentoDiferenteError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    verificar_comprimento()

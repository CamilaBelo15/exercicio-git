import pandas as pd
import os

arquivo_excel = "notas.xlsx"

nome = input("Informe seu nome: ")
n1 = input("Informe a N1: ")
n2 = input("Informe a N2: ")
n3 = input("Informe a N3: ")

dados_novos = pd.DataFrame([[nome, n1, n2, n3]], columns=["Nome", "N1", "N2", "N3"])


if os.path.exists(arquivo_excel):
    df_existente = pd.read_excel(arquivo_excel)
    df_final = pd.concat([df_existente, dados_novos], ignore_index=True)
else:

    df_final = dados_novos

df_final.to_excel(arquivo_excel, index=False)

print(f"Dados salvos em {arquivo_excel}")


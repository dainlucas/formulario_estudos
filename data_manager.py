import pandas as pd
import os

def salvar_dados(dicionario_de_dados):
    arquivo = "reports/dados_estudos.csv"
    os.makedirs("reports", exist_ok=True)
    df = pd.DataFrame([dicionario_de_dados])
    df.to_csv(arquivo, mode='a', index=False, header=not os.path.exists(arquivo))
    return True

def carregar_dados():
    arquivo = "reports/dados_estudos.csv"
    if os.path.exists(arquivo):
        return pd.read_csv(arquivo)
    return None

def remover_ultimo_registro():
    arquivo = "reports/dados_estudos.csv"
    if os.path.exists(arquivo):
        df = pd.read_csv(arquivo)
        if not df.empty:
            # Remove a última linha (index -1)
            df = df[:-1]
            df.to_csv(arquivo, index=False)
            return True
    return False
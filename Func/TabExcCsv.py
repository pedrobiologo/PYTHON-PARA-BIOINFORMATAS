import pandas as pd

def Arch_types(caminho):
    if str(caminho).endswith("xlsx"):
        df = pd.read_excel(caminho)
    elif str(caminho).endswith("tabular"):
        df = pd.read_table(caminho, sep="\t")
    elif str(caminho).endswith("csv"):
        df = pd.read_csv(caminho)
    return df

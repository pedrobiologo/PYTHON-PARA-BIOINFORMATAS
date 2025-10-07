import pandas as pd
import os

os.chdir(r"C:\Users\leand\TCC\TCC data\EdgeR")

df_bruto = pd.read_table(r"C:\Users\leand\TCC\TCC data\EdgeR\EdgeMmu_Anurans_NumReadsFiltered.tabular", sep="\t")
referencia = pd.read_excel(r"C:\Users\leand\TCC\TCC data\Especies\Mmu\referencia\IdsAnotadasComProteinas.xlsx")
for index, row in df_bruto.iterrows():
    valor = row["logFC"]
    cpm = row["logCPM"]
    df_bruto.loc[index, "CPM"] = 2**cpm
    if valor >0:
        df_bruto.loc[index, "FC"] = 2**valor
    else:
        df_bruto.loc[index, "FC"] = (1/(2**valor))*-1
referencia.rename(columns={'sseqid': 'GeneID'}, inplace=True)
referencia.drop_duplicates(subset = ["GeneID"], keep="first", inplace=True)
df_bruto_anotaded = pd.merge(df_bruto, (referencia[["GeneID", "stitle"]]), on="GeneID", how="left", )
print(df_bruto.columns)

df_DEG = df_bruto_anotaded[df_bruto_anotaded["FDR"] < 0.05]

df_DEG_UP = df_DEG[df_DEG["logFC"] > 0]
df_DEG_UP.sort_values(by="logFC", ascending=False, inplace=True)
df_DEG_DOWN = df_DEG[df_DEG["logFC"] < 0]
df_DEG_DOWN.sort_values(by="logFC", ascending=True, inplace=True)

with pd.ExcelWriter("FCEdgeMmu_Anurans_NumReadsFiltered.xlsx") as writer:

    df_bruto_anotaded.to_excel(writer, sheet_name="Bruto", index=False)
    df_DEG.to_excel(writer, sheet_name="Diferencialmente expressos", index=False)

    df_DEG_UP.to_excel(writer, sheet_name="Up regulated", index=False)
    df_DEG_DOWN.to_excel(writer, sheet_name="Down regulated", index=False)
    print("Tabela feita com sucesso")
# list_up = ["MaisExpressos: "]

# list_down = ["Menos Expressos:"]
# for index, row in df_DEG_UP.iterrows():
#     list_up.append(row["GeneID"])

# for index, row in df_DEG_DOWN.iterrows():
#     list_down.append(row["GeneID"])

# for c in list_up:
#     with open("IdsDEG.txt", "a") as arch:
#         arch.write(c)
#         arch.write(" ")

# with open("IdsDEG.txt", "a") as arch:
#     arch.write("\n\n\n\n")

# for c in list_down:
#     with open("IdsDEG.txt", "a") as arch:
#         arch.write(c)
#         arch.write(" ")

#df.to_excel(r"EdgeAnuransOrfs_MmuSorted_TPM.xlsx", index=False, index_label=False)


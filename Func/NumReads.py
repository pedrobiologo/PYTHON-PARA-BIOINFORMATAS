import pandas as pd
import os

os.chdir(r'D:\\UFPE\\GRADUAÇÃO\\TCC\\AMOSTRAS\\ANOTAÇÃO SEM HEADCROP\\')
list_arch = []
for c in os.listdir():
    list_arch.append(c)

#Entrada do arquivo do clorotalonil CTL55
dfs = {}
print("ATENÇÃO: Para as amostras de clorotalonil, utilize o código 'CTL + o código da amostra'\nPara os veículos/controles, utilize 'VH + o código do veículo.")
for c in list_arch:
    print("-"*20)
    caminho = c
    print(c)
    print("-"*20)
    name = input("Qual o nome da sua amostra ou código?\n")
    if caminho.endswith(".tabular"):
        df = pd.read_table(caminho, sep="\t") #Lê o arquivo tabular e atribui a variável
    elif caminho.endswith(".xlsx"):
        df = pd.read_excel(caminho)
    #contador = f"df{i}"
    df1 = df.drop(["Length", "EffectiveLength", "TPM"], axis=1)
    df1.columns = ["Name", f"NumReads {name}"]
    dfs[name] = df1
    print("\n","\n")
    #[f'df{i}']

#print(dfs.keys())
keys_df = list(dfs.keys())
print(keys_df)
keys_CTL = []
keys_VH = []

for c in keys_df:
    if "CTL" in c:
        keys_CTL.append(c)

print(keys_CTL)
for c in keys_df:
    if "VH" in c:
        keys_VH.append(c)

print(keys_VH)
print("Fazendo a junção de todos...")
df_final = pd.merge(dfs[keys_df[0]], dfs[keys_df[1]], on="Name")
for key in list(dfs.keys())[2:]:
    df_final = pd.merge(df_final, dfs[key], on="Name")
print("Finalizado\n")

print("Começando a formação do Clorotalonil")
df_finalCTL = pd.merge(dfs[keys_CTL[0]], dfs[keys_CTL[1]], on="Name")
print("Finalizado :D\n")

df_finalVH = pd.merge(dfs[keys_VH[0]], dfs[keys_VH[1]], on="Name")
for key in keys_VH[2:]:
    df_finalVH = pd.merge(df_finalVH, dfs[key], on="Name")

print("Iniciando a exportação...\n")
df_final.to_excel(r'D:\\UFPE\\GRADUAÇÃO\\TCC\\AMOSTRAS\\NumReads SEM HEADCROP\\NumReadsTodos_Sem_Headcrop.xlsx', index=False, index_label=False)
df_finalCTL.to_excel(r'D:\\UFPE\\GRADUAÇÃO\\TCC\\AMOSTRAS\\NumReads SEM HEADCROP\\NumReadsCTL_Sem_Headcrop.xlsx', index=False, index_label=False)
df_finalVH.to_excel(r'D:\\UFPE\\GRADUAÇÃO\\TCC\\AMOSTRAS\\NumReads SEM HEADCROP\\NumReadsVH_Sem_Headcrop.xlsx', index=False, index_label=False)
print('CTL + VH')
print('-'*80)
print(df_final.head(5))
print('-'*80)
print('CTL')
print(df_finalCTL.head(5))
print('VH')
print('-'*80)
print(df_finalVH.head(5))
print('-'*40)
print('Exportação concluída com êxito.')
print('-'*40)
import seaborn as sb
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def MEGA_file(matriz):
    #MEGA
    with open('matriz.meg', 'a') as arc:
        nome = input('Qual o nome da matriz? ')
        arc.write('#MEGA\n')
        arc.write(f'!Title: Matriz Correlação{nome};\n')
        arc.write('!Format DataType=Distance DataFormat=UpperRight;\n\n')
        spcs = []
        for c in matriz.columns:
            spcs.append(c)
            especie = '#'+c+'\n'
            arc.write(especie)
        arc.write('\n')
        
        for c in spcs:
            param = False
            valores = reversed(list(matriz.loc[c]))
            print(valores)
            for c in valores:
                if c == 1:
                    break
                local = valores
                values = str(c)+" "
                arc.write(values)
                
            arc.write("\n")

os.chdir(r'D:\\UFPE\\GRADUAÇÃO\\TCC\\AMOSTRAS\\NumReads SEM HEADCROP')

df = pd.read_excel('NumReadsTodos_Sem_Headcrop.xlsx')
df = df.set_index(['Name'])
print(df)
df = df.corr()
print(df)
matriz = df.where(np.triu(np.ones(df.shape)).astype(bool))
print(matriz)
#matriz.to_excel("MatrizNumRead_Sem_Headcrop.xlsx", index=False, index_label=False)
MEGA_file(matriz)


plot = sb.heatmap(df, annot=True)
plt.show()
print('Cabosse')

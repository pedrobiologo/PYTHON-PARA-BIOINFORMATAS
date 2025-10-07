import pandas as pd
import os

os.chdir(r"D:\\UFPE\\GRADUAÇÃO\\TCC\\AMOSTRAS\\CTL SEM HEADCROP\\SRR2078356 SEM HEADCROP")
df = pd.read_table(r'SRR2078356.tabular', sep='\t', decimal='.')
df = df[["Name","NumReads"]]
df.rename(columns={'NumReads':'NumReads CTL56'}, inplace=True)
df.to_csv(r'SRR2078356_tratado.tabular', sep='\t', index=False)
print('Concluído com êxito.')
import tkinter as tk
from tkinter import filedialog
import sys

def selecionar_pasta():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    
    # Abre a janela de seleção de diretório
    diretorio = filedialog.askdirectory(
        title="Selecione a pasta desejada",
        mustexist=True  # Só permite selecionar diretórios existentes
    )
    
    if diretorio:  # Se um diretório foi selecionado
        print(f"Diretório selecionado: {diretorio}")
        return diretorio
    else:
        print("Nenhum diretório foi selecionado")
        sys.exit() #Parada do código
        return None

def explorador_de_arquivos(tiposarquivos=[("Excel", "*.xlsx"), ("Tabular", "*.tabular"), ("Csv", "*.csv")], titulo="selecione seu arquivo"):
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    #Abre uma caixa de diálogo do arquivo:
    file_path = filedialog.askopenfilename(filetypes=tiposarquivos, title=titulo)

    #Verifica se foi inserido um caminho válido:    
    if file_path:
        print(f"Arquivo selecionado: {file_path}")  # Imprime o caminho do arquivo selecionado
        return (file_path) #Retorna o caminho
    
    #Verifica se foi inserido um caminho inválido:
    else:
        print("Arquivo não selecionado, tente novamente :(")
        sys.exit() #Parada do código


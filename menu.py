import tkinter as tk
from tkinter import filedialog
import os
import shutil


janela = tk.Tk()
janela.title("Cleaning Menu")
janela.geometry("350x300")
janela.config(bg="black")


label = tk.Label(
    janela,
    text="Cleaning Menu",
    font=("Consolas", 16, "bold"),
    fg="white",
    bg="black"
)
label.pack(pady=20)

pasta_selecionada = None


def voltar_texto():
    label.config(text="Cleaning Menu")


def clicar():
    janela.destroy()


def selecionar_pasta():
    global pasta_selecionada
    pasta = filedialog.askdirectory()

    if pasta:
        espaco_libertado = apagar_ficheiros(pasta)  # Chama a função para apagar os arquivos e obter o espaço libertado
        label.config(text=f"Espaço libertado: {espaco_libertado / (1024 * 1024):.2f} MB")  # Exibe em MB

        
        janela.after(2000, voltar_texto)


def apagar_ficheiros(pasta):
    espaco_total = 0  
    for arquivo in os.listdir(pasta):
        caminho_arquivo = os.path.join(pasta, arquivo)
        try:
            if os.path.isfile(caminho_arquivo):  
                espaco_total += os.path.getsize(caminho_arquivo)  
                os.remove(caminho_arquivo)  
            elif os.path.isdir(caminho_arquivo):
                shutil.rmtree(caminho_arquivo)  
        except Exception as e:
            print(f"Erro ao apagar {caminho_arquivo}: {e}")
    return espaco_total  

def limpar_temp():
    espaco_libertado = apagar_temp() 
    label.config(text=f"Espaço libertado: {espaco_libertado / (1024 * 1024):.2f} MB")

    janela.after(2000, voltar_texto)

def apagar_temp():
    temp_path = r"C:\Windows\Temp"
    espaco_total = 0 

    if os.path.exists(temp_path):
        for arquivo in os.listdir(temp_path):
            caminho_arquivo = os.path.join(temp_path, arquivo)

            try:
                if os.path.isfile(caminho_arquivo):
                    espaco_total += os.path.getsize(caminho_arquivo) 
                    os.remove(caminho_arquivo)
                elif os.path.isdir(caminho_arquivo):
                    shutil.rmtree(caminho_arquivo)
            except Exception as e:
                print(f"Erro ao apagar {caminho_arquivo}: {e}")

        return espaco_total  

    else:
        return 0 


def on_hover(botao, cor):
    botao.config(bg=cor)

def on_leave(botao, cor):
    botao.config(bg=cor)


estilo_botao = {
    "font": ("Arial", 12, "bold"),
    "fg": "white",
    "bg": "#333",
    "activebackground": "#555",
    "activeforeground": "white",
    "bd": 0,
    "relief": "flat",
    "width": 20,
    "height": 2
}

botao_pasta = tk.Button(janela, text="Selecionar Pasta", command=selecionar_pasta, **estilo_botao)
botao_pasta.pack(pady=10)
botao_pasta.bind("<Enter>", lambda event: on_hover(botao_pasta, "#555"))
botao_pasta.bind("<Leave>", lambda event: on_leave(botao_pasta, "#333"))

botao_limpar_temp = tk.Button(janela, text="Limpar Temp", command=limpar_temp, **estilo_botao)
botao_limpar_temp.pack(pady=10)
botao_limpar_temp.bind("<Enter>", lambda event: on_hover(botao_limpar_temp, "#555"))
botao_limpar_temp.bind("<Leave>", lambda event: on_leave(botao_limpar_temp, "#333"))

botao_sair = tk.Button(janela, text="Sair", command=clicar, **estilo_botao)
botao_sair.pack(pady=10)
botao_sair.bind("<Enter>", lambda event: on_hover(botao_sair, "#900"))
botao_sair.bind("<Leave>", lambda event: on_leave(botao_sair, "#333"))

janela.mainloop()
import tkinter as tk
from tkinter import filedialog
import PIL.Image

def selecionar_imagem():
    caminho = filedialog.askopenfilename(title="Selecionar Imagem")
    if caminho:
        entry_caminho.delete(0, tk.END)
        entry_caminho.insert(0, caminho)

def selecionar_local_salvar():
    local_salvar = filedialog.askdirectory(title="Selecionar Local para Salvar")
    if local_salvar:
        entry_salvar.delete(0, tk.END)
        entry_salvar.insert(0, local_salvar)

def criar_icone():
    try:
        caminho_imagem = entry_caminho.get()
        local_salvar = entry_salvar.get()

        icone = PIL.Image.open(caminho_imagem)
        largura, altura = icone.size
        corte = largura if largura <= altura else altura
        icone = icone.crop(((largura - corte) // 2, (altura - corte) // 2, (largura + corte) // 2, (altura + corte) // 2)).resize((256, 256))
        icone.save(local_salvar+'/icone.ico', format='ICO', sizes=[(256, 256)], quality=95)
        print('Concluído!')
    except Exception as e:
        print('Erro:', e)

# Criar a janela principal
root = tk.Tk()
root.title("Criador de Ícones")

# Criar e posicionar os widgets
label_caminho = tk.Label(root, text="Caminho da Imagem:")
label_caminho.grid(row=0, column=0, padx=5, pady=5)
entry_caminho = tk.Entry(root, width=50)
entry_caminho.grid(row=0, column=1, padx=5, pady=5)
botao_buscar = tk.Button(root, text="Buscar", command=selecionar_imagem)
botao_buscar.grid(row=0, column=2, padx=5, pady=5)

label_salvar = tk.Label(root, text="Local para Salvar:")
label_salvar.grid(row=1, column=0, padx=5, pady=5)
entry_salvar = tk.Entry(root, width=50)
entry_salvar.grid(row=1, column=1, padx=5, pady=5)
botao_local = tk.Button(root, text="Buscar", command=selecionar_local_salvar)
botao_local.grid(row=1, column=2, padx=5, pady=5)

botao_criar = tk.Button(root, text="Criar Ícone", command=criar_icone)
botao_criar.grid(row=2, column=1, padx=5, pady=5)

# Iniciar o loop da aplicação
root.mainloop()

import tkinter as tk

# nome = input('Digite seu nome: ')

janela = tk.Tk()
janela.title('janela nome, esse e o nome da janela :D')
janela.geometry('500x500')

texto = tk.Label(janela, text=f"INSIRA SEU NOME")
texto.pack()

def resposta_botao():
    nome = entrada_texto.get()
    texto['text'] = f'o {nome} apertou aqui ow'

entrada_texto = tk.Entry(janela)
entrada_texto.pack()
tk.Button(janela, text="botaoao", command=resposta_botao).pack()

# class Application:
#     def __init__(self, master=None):
#         pass

# Application(janela)
janela.mainloop()

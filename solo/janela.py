import tkinter as tk

contas = [
    ('lan', '123'),
    ('aleale', 'ale123')
]

# nome = input('Digite seu nome: ')

janela = tk.Tk()
janela.title('Login')
janela.geometry('400x300')

tk.Label(janela, text='user').pack()
usuario_entry = tk.Entry(janela)
usuario_entry.pack()

tk.Label(janela, text='password').pack()
senha_entry = tk.Entry(janela)
senha_entry.pack()

def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    if (usuario, senha) in contas:
        mensagem_label['text'] = "logado"
    else:
        mensagem_label['text'] = 'credenciais invalidas'

tk.Button(janela, text='login', command=login).pack()

mensagem_label = tk.Label(janela, text='')
mensagem_label.pack()



# texto = tk.Label(janela, text=f"INSIRA SEU NOME")
# texto.pack()

# def resposta_botao():
#     nome = entrada_texto.get()
#     texto['text'] = f'o {nome} apertou aqui ow'

# entrada_texto = tk.Entry(janela)
# entrada_texto.pack()
# tk.Button(janela, text="botaoao", command=resposta_botao).pack()

# class Application:
#     def __init__(self, master=None):
#         pass

# Application(janela)

janela.mainloop()

#    _____                                            .___
#   / ___ \  _________________  ________    ____    __| _/
#  / / ._\ \/  ___/\___   /\  \/  /\__  \  /    \  / __ | 
# <  \_____/\___ \  /    /  >    <  / __ \|   |  \/ /_/ | 
#  \_____\ /____  >/_____ \/__/\_ \(____  /___|  /\____ | 
#               \/       \/      \/     \/     \/      \/ 

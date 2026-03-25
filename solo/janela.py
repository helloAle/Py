import tkinter as tk

contas = [
    ('lan', '123'),
    ('ale', 'ale')
]


janela = tk.Tk()
janela.title('Login')
janela.geometry('400x300')

# LOGIN

pagina_login = tk.Frame(janela)
pagina_login.pack()

tk.Label(pagina_login, text='user').pack()
usuario_entry = tk.Entry(pagina_login)
usuario_entry.pack()

tk.Label(pagina_login, text='password').pack()
senha_entry = tk.Entry(pagina_login)
senha_entry.pack()

# FUNÇÃO DE LOGIN

def login():
    usuario = usuario_entry.get()
    senha = senha_entry.get()
    if (usuario, senha) in contas:
        pagina_login.pack_forget()
        pagina_sistema.pack()
    else:
        mensagem_label['text'] = 'credenciais invalidas'

tk.Button(pagina_login, text='login', command=login).pack()

mensagem_label = tk.Label(pagina_login, text='')
mensagem_label.pack()

# SISTEMA

pagina_sistema = tk.Frame()
tk.Label(pagina_sistema, text='Bienvenido!').pack()

# JANELA

janela.mainloop()


#    _____                                            .___
#   / ___ \  _________________  ________    ____    __| _/
#  / / ._\ \/  ___/\___   /\  \/  /\__  \  /    \  / __ | 
# <  \_____/\___ \  /    /  >    <  / __ \|   |  \/ /_/ | 
#  \_____\ /____  >/_____ \/__/\_ \(____  /___|  /\____ | 
#               \/       \/      \/     \/     \/      \/ 

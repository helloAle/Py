import tkinter as tk
import sqlite3
import hashlib

# ================== BANCO DE DADOS ==================

conexao = sqlite3.connect("teste.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
)
""")

conexao.commit()

# ================== JANELA ==================

janela = tk.Tk()
janela.title('Sistema')
janela.geometry('400x300')

# ================== FUNÇÕES ==================

def ir_para_registro():
    pagina_login.pack_forget()
    pagina_registro.pack()

def ir_para_login():
    pagina_registro.pack_forget()
    pagina_login.pack(fill="both", expand=True)

def logout():
    pagina_sistema.pack_forget()
    pagina_login.pack()
# -------- REGISTER --------

def register():
    usuario = usuario_registro_entry.get()
    senha = senha_registro_entry.get()

    if usuario == "" or senha == "":
        mensagem_registro.config(text="Preencha todos os campos", fg="red")
        return

    try:
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        cursor.execute(
            "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
            (usuario, senha_hash)
        )
        conexao.commit()

        mensagem_registro.config(text="Usuário registrado!", fg="green")

        usuario_registro_entry.delete(0, tk.END)
        senha_registro_entry.delete(0, tk.END)

    except sqlite3.IntegrityError:
        mensagem_registro.config(text="Usuário já existe!", fg="red")

# -------- LOGIN --------

def login():
    usuario = usuario_login_entry.get()
    senha = senha_login_entry.get()

    if usuario == "" or senha == "":
        mensagem_login.config(text="Preencha todos os campos", fg="red")
        return

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?",
        (usuario, senha_hash)
    )

    resultado = cursor.fetchone()

    if resultado:
        pagina_login.pack_forget()
        pagina_sistema.pack()
    else:
        mensagem_login.config(text="Credenciais inválidas", fg="red")

# ================== LOGIN ==================

pagina_login = tk.Frame(janela)

tk.Label(pagina_login, text='Login').pack()

tk.Label(pagina_login, text='User').pack()
usuario_login_entry = tk.Entry(pagina_login)
usuario_login_entry.pack()

tk.Label(pagina_login, text='Password').pack()
senha_login_entry = tk.Entry(pagina_login, show="*")
senha_login_entry.pack()

mensagem_login = tk.Label(pagina_login, text='')
mensagem_login.pack()

tk.Button(pagina_login, text='Login', command=login).pack()
tk.Button(pagina_login, text='Ir para registro', command=ir_para_registro).pack()

# ================== REGISTRO ==================

pagina_registro = tk.Frame(janela)

tk.Label(pagina_registro, text='Registro').pack()

tk.Label(pagina_registro, text='User').pack()
usuario_registro_entry = tk.Entry(pagina_registro)
usuario_registro_entry.pack()

tk.Label(pagina_registro, text='Password').pack()
senha_registro_entry = tk.Entry(pagina_registro, show="*")
senha_registro_entry.pack()

mensagem_registro = tk.Label(pagina_registro, text='')
mensagem_registro.pack()

tk.Button(pagina_registro, text='Registrar', command=register).pack()
tk.Button(pagina_registro, text='Voltar para login', command=ir_para_login).pack()

# ================== SISTEMA ==================

pagina_sistema = tk.Frame(janela)

tk.Label(pagina_sistema, text='Tudo certo! Você entrou no sistema 😎').pack()

tk.Button(pagina_sistema, text='Logout', command=logout).pack()


# ================== INICIO ==================

pagina_login.pack()

janela.mainloop()

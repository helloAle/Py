import customtkinter as ctk
import sqlite3
import hashlib

# ================== CONFIG ==================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ================== BANCO ==================

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

janela = ctk.CTk()
janela.title("Sistema")
janela.geometry("400x300")

# ================== FUNÇÕES ==================

def ativar_enter_login():
    janela.bind("<Return>", lambda e: login())

def ativar_enter_registro():
    janela.bind("<Return>", lambda e: register())

def ir_para_registro():
    pagina_login.pack_forget()
    pagina_registro.pack(fill="both", expand=True)
    ativar_enter_registro()

def ir_para_login():
    pagina_registro.pack_forget()
    pagina_sistema.pack_forget()
    pagina_login.pack(fill="both", expand=True)
    ativar_enter_login()

def logout():
    pagina_sistema.pack_forget()
    pagina_login.pack(fill="both", expand=True)
    ativar_enter_login()

# ================== REGISTER ==================

def register():
    usuario = usuario_registro_entry.get()
    senha = senha_registro_entry.get()

    if usuario == "" or senha == "":
        mensagem_registro.configure(text="Preencha todos os campos", text_color="red")
        return

    try:
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        cursor.execute(
            "INSERT INTO usuarios (usuario, senha) VALUES (?, ?)",
            (usuario, senha_hash)
        )
        conexao.commit()

        mensagem_registro.configure(text="Usuário registrado!", text_color="green")

        usuario_registro_entry.delete(0, "end")
        senha_registro_entry.delete(0, "end")

    except sqlite3.IntegrityError:
        mensagem_registro.configure(text="Usuário já existe!", text_color="red")

# ================== LOGIN ==================

def login():
    usuario = usuario_login_entry.get()
    senha = senha_login_entry.get()

    if usuario == "" or senha == "":
        mensagem_login.configure(text="Preencha todos os campos", text_color="red")
        return

    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?",
        (usuario, senha_hash)
    )

    if cursor.fetchone():
        pagina_login.pack_forget()
        pagina_sistema.pack(fill="both", expand=True)
    else:
        mensagem_login.configure(text="Credenciais inválidas", text_color="red")

# ================== LOGIN UI ==================

pagina_login = ctk.CTkFrame(janela)

ctk.CTkLabel(pagina_login, text="Login").pack(pady=10)

usuario_login_entry = ctk.CTkEntry(pagina_login, placeholder_text="Usuário")
usuario_login_entry.pack(pady=5)

senha_login_entry = ctk.CTkEntry(pagina_login, placeholder_text="Senha", show="*")
senha_login_entry.pack(pady=5)

mensagem_login = ctk.CTkLabel(pagina_login, text="")
mensagem_login.pack()

ctk.CTkButton(pagina_login, text="Login", command=login).pack(pady=5)
ctk.CTkButton(pagina_login, text="Ir para registro", command=ir_para_registro).pack()

# ================== REGISTRO ==================

pagina_registro = ctk.CTkFrame(janela)

ctk.CTkLabel(pagina_registro, text="Registro").pack(pady=10)

usuario_registro_entry = ctk.CTkEntry(pagina_registro, placeholder_text="Usuário")
usuario_registro_entry.pack(pady=5)

senha_registro_entry = ctk.CTkEntry(pagina_registro, placeholder_text="Senha", show="*")
senha_registro_entry.pack(pady=5)

mensagem_registro = ctk.CTkLabel(pagina_registro, text="")
mensagem_registro.pack()

ctk.CTkButton(pagina_registro, text="Registrar", command=register).pack(pady=5)
ctk.CTkButton(pagina_registro, text="Voltar", command=ir_para_login).pack()

# ================== SISTEMA ==================

pagina_sistema = ctk.CTkFrame(janela)

ctk.CTkLabel(pagina_sistema, text="Bem-vindo 😎").pack(pady=20)
ctk.CTkButton(pagina_sistema, text="Logout", command=logout).pack()

# ================== START ==================

pagina_login.pack(fill="both", expand=True)
ativar_enter_login()

janela.mainloop()

import tkinter as tk

nome = input('Digite seu nome: ')

J=janela = tk.Tk()
janela.title('janela nome, esse e o nome da janela :D')
janela.geometry('500x500')

tk.Label(janela, text=f"oi, {nome} :D").pack()

# class Application:
#     def __init__(self, master=None):
#         pass

# Application(janela)
janela.mainloop()

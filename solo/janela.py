import tkinter as tk # importei a biblioteca e apelidei como tk neeeee

root = tk.Tk()      #  Tk() cria a janela //  root é a variavel que ta guardando a janela :P
                    # entao a variavel que guarda a janela ta recebendo a biblioteca criando a janela

class Application:  # criando a classe da aplicação :P
    def __init__(self, master=None):    # __init__ é o contrutor e self é o proprio objeto, master(janela)
        pass        # faz nada

Application(root)   # A CLASSE Application ESTÁ CRIANDO UM OBJETO e recebendo (root) [root possui a janeta]
root.mainloop()     # Mantem rodando :P

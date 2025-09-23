# eu não utilizei IA para a criação da calculadora, creditos ao https://youtu.be/i24MxljM-Bw?si=pvPNiHRTJqH8sW4l
# Ia utilizada somente para construção de comentarios para melhor entendimento do que esta sendo realizado

from tkinter import * # importei todas as funções, classes e constantes da tkinter (tkinter é usado para criar interfaces graficas no python)
from tkinter import ttk # importa o modulo ttk da biblioteca tkinter, que fornece widgets temáticos para criar interfaces gráficas mais modernas e estilizadas.

#===========cores===========#
cor1 = "#222222" # preto
cor2 = "#feffff" # branco
cor3 = "#2f6183" # azul
cor4 = "#FFAB40" # laranja
#===========================#

#====================================Frames=================================#

janela = Tk() # Cria uma janela principal usando a classe Tk() da biblioteca tkinter
janela.title("Calculadora") # Define o título da janela principal como "Calculadora"
janela.geometry("235x318") # Define o tamanho da janela principal para 235 pixels de largura e 318 pixels de altura
janela.config(bg=cor1) # Configura a cor de fundo da janela principal para a cor definida em cor1 (preto)

frame_tela = Frame(janela, width=235, height=50, bg=cor3) # Cria um frame (container) dentro da janela principal com largura de 235 pixels, altura de 50 pixels e fundo azul
frame_tela.grid(row=0, column=0) # Posiciona o frame na grade da janela principal na linha 0 e coluna 0

frame_corpo = Frame(janela, width=235, height=268) # Cria outro frame dentro da janela principal com largura de 235 pixels, altura de 268 pixels e fundo branco
frame_corpo.grid(row=1, column=0) # Posiciona este frame na grade da janela principal na linha 1 e coluna 0

# variavel todos os valores
todos_valores = '' # Inicializa a variável todos_valores como uma string vazia para armazenar os valores inseridos na calculadora


# criando função

def entrar_valores(event):

    global todos_valores # Declara que a variável todos_valores é global, permitindo que seja acessada e modificada dentro da função

    todos_valores = todos_valores + str(event) # Recebe o valor do botão pressionado e armazena na variável todos_valores

    #passando valor para tela
    valor_texto.set(todos_valores) # Atualiza o valor exibido na tela da calculadora com o conteúdo atualizado de todos_valores

#função para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores) # Usa a função eval() para avaliar a expressão matemática armazenada em todos_valores e calcular o resultado
    
    valor_texto.set(str(resultado)) # Atualiza o valor exibido na tela da calculadora com o resultado calculado

#função limpar tela

def limpar_tela():
    global todos_valores # Declara que a variável todos_valores é global, permitindo que seja acessada e modificada dentro da função
    todos_valores = "" # Reseta a variável todos_valores para uma string vazia, limpando a expressão atual
    valor_texto.set("") # Atualiza o valor exibido na tela da calculadora para uma string vazia

#====================================Label=================================#
valor_texto = StringVar() # Cria uma variável de string chamada valor_texto para armazenar o texto exibido na calculadora

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify='right', font=('Ivy 18'), bg=cor3, fg=cor2) # Cria um label dentro do frame_tela que exibe o valor da variável valor_texto, com várias configurações de estilo
app_label.place(x=0, y=0) # Posiciona o label dentro do frame_tela na coordenada (0,0)

#====================================Botões=================================#

b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) # Cria um botão "C" dentro do frame_corpo que chama a função limpar_tela quando clicado, com várias configurações de estilo
b_1.place(x=0, y=0) # Posiciona o botão "C" no frame_corpo na coordenada (0,0)

b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=53)

b_5 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=53)

b_6 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=53)

b_7 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=53)

b_8 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=106)

b_9 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=106)

b_10 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=106)

b_11 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=106)

b_12 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=159)

b_13 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=159)

b_14 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=159)

b_15 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=159)

b_16 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=11, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=212)

b_17 = Button(frame_corpo, command=lambda: entrar_valores(','), text=",", width=5, height=2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=212)

b_18 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=212)



janela.mainloop() # Inicia o loop principal da interface gráfica, que mantém a janela aberta e responde a eventos do usuário


#    _____                                            .___
#   / ___ \  _________________  ________    ____    __| _/
#  / / ._\ \/  ___/\___   /\  \/  /\__  \  /    \  / __ | 
# <  \_____/\___ \  /    /  >    <  / __ \|   |  \/ /_/ | 
#  \_____\ /____  >/_____ \/__/\_ \(____  /___|  /\____ | 

#               \/       \/      \/     \/     \/      \/ 


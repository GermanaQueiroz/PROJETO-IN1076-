from tkinter import*
import random
import time
import datetime
import sqlite3
import banco

janela = Tk()

janela.title("Ética")
janela["bg"]="black"
janela.configure(background = "gray")

#Criando o frame do topo
Top = Frame(janela, width=200, height=200)
Top.pack(side=TOP)

#Criando o frame da esquerda
Left = Frame(janela, width=800, height=900)
Left.pack(side=LEFT)

#Criando o frame da direita
Right = Frame(janela, width=300, height=240)
Right.pack(side=RIGHT)
Right.configure(background='white')

img = PhotoImage(file=r"C:\Users\germa\OneDrive\Bureau\Python\Python - Interface\RegistroInformações\0_Bl64HQR_5P1IdC0h.png")
label_imagem = Label(Right, image=img).pack()

#Inserindo Label para o titulo do sistema
lblTitulo = Label(Top, font=('arial', 20, 'bold'), text="Registro de informações", width=75)
lblTitulo.grid(row=0, column=0)

#Inserindo Label para as perguntas do sistema

lblperguntas = Label(Left,font=('arial', 11, 'bold'), text="1- Qual é o nome completo?")
lblperguntas.grid(row=0, column=0)

lblperguntas = Label(Left,font=('arial', 11, 'bold'), text="2- Qual é o sexo?")
lblperguntas.grid(row=2, column=0)

lblperguntas = Label(Left,font=('arial', 11, 'bold'), text="3- Qual é a faixa étaria?")
lblperguntas.grid(row=6, column=0)

lblperguntas = Label(Left,font=('arial', 11, 'bold'), text="4- Qual é o estado civil?")
lblperguntas.grid(row=12, column=0)

lblperguntas = Label(Left,font=('arial', 11, 'bold'), text="5- Quanto é o tempo de experiência de trabalho?")
lblperguntas.grid(row=17, column=0)

lblperguntas = Label(Left,font=('arial', 11, 'bold'), text="6- Qual é o Email?")
lblperguntas.grid(row=22, column=0)


#Declaração de variaveis

tb_txtNome=StringVar()
tb_txtNome.set(" ")

tb_txtOutros1=StringVar()
tb_txtOutros1.set(" ")

tb_txtEmail=StringVar()
tb_txtEmail.set(" ")

tb_txtidade=StringVar()
tb_txtidade.set(" ")

tb_varcheck21 = StringVar()
tb_varcheck21.set("0")

tb_varcheck22 = StringVar()
tb_varcheck22.set("0")

tb_varcheck28 = StringVar()
tb_varcheck28.set("0")

tb_varcheck29 = StringVar()
tb_varcheck29.set("0")

tb_varcheck30 = StringVar()
tb_varcheck30.set("0")

tb_varcheck32 = StringVar()
tb_varcheck32.set("0")

tb_varcheck33 = StringVar()
tb_varcheck33.set("0")

tb_varcheck34 = StringVar()
tb_varcheck34.set("0")

tb_varcheck35 = StringVar()
tb_varcheck35.set("0")

#Codigo do botão sair

def iExit():
    janela.destroy()
    return

#Codigo do botão enviar


def var_states():

    print ("Qual é o nome completo:"+tb_txtNome.get())
    print ("Masculino:%s, \nFeminino: %s"%(tb_varcheck21.get(),tb_varcheck22.get()))
    print ("Qual é a idade:"+tb_txtidade.get())
    print ("Solteiro:%s, \nCasado: %s, \nDivorciado: %s"%(tb_varcheck28.get(),tb_varcheck29.get(),tb_varcheck30.get()))
    print ("Outros:"+tb_txtOutros1.get())
    print ("0 - 5 anos:%s, \n6 - 10 anos: %s, \n11 - 20 anos:%s, n\Acima de 21 anos:%s" %(tb_varcheck32.get(),tb_varcheck33.get(), tb_varcheck34.get(), tb_varcheck35.get()))
    print ("Qual é o e-mail:"+tb_txtEmail.get())
    print ("Enviar")

def gravarDados():
    if tb_txtNome.get()!="":
        vnome=tb_txtNome.get()
        vsexo=tb_varcheck21.get()
        vsexo=tb_varcheck22.get()
        vidade=tb_txtidade.get()
        vestadocivil=tb_varcheck28.get()
        vestadocivil=tb_varcheck29.get()
        vestadocivil=tb_varcheck30.get()
        vestadocivil=tb_txtOutros1.get()
        vtempotrabalho=tb_varcheck32.get()
        vtempotrabalho=tb_varcheck33.get()
        vtempotrabalho=tb_varcheck34.get()
        vtempotrabalho=tb_varcheck35.get()
        vemail=tb_txtEmail.get()
        vquery="INSERT INTO Usuarios2 (Nome, Sexo, Sexo, Idade, EstadoCivil,EstadoCivil,EstadoCivil,EstadoCivil,Tempotrabalho,Tempotrabalho,Tempotrabalho,Tempotrabalho, Email) VALUES('"+vnome+"','"+vsexo+"','"+vsexo+"','"+vidade+"','"+vestadocivil+"','"+vestadocivil+"','"+vestadocivil+"','"+vestadocivil+"','"+vtempotrabalho+"','"+vtempotrabalho+"','"+vtempotrabalho+"','"+vtempotrabalho+"','"+vemail+"')"                         
        banco.dml(vquery)
        tb_txtNome.delete(0, END)
        tb_txtidade.delete(0, END)
        tb_txtOutros1.delete(0, END)
        tb_txtEmail.delete(0, END)
        print("Dados Gravados")
    else:
        print("ERRO")
    

#criação de objetos e componentes

Entrega = Checkbutton(Left, text = "Masculino\t",variable = tb_varcheck21, onvalue=1,offvalue=0,font=('arial', 10, 'bold')).grid(row=3, stick=W)
Entrega = Checkbutton(Left, text = "Feminino\t",variable = tb_varcheck22, onvalue=1,offvalue=0,font=('arial', 10, 'bold')).grid(row=4, stick=W)
Entrega = Checkbutton(Left, text = "Solteiro\t",variable = tb_varcheck28, onvalue=1,offvalue=0,font=('arial', 10, 'bold')).grid(row=13, stick=W)
Entrega = Checkbutton(Left, text = "Casado\t",variable = tb_varcheck29, onvalue=1,offvalue=0,font=('arial', 10, 'bold')).grid(row=14, stick=W)
Entrega = Checkbutton(Left, text = "Divorciado\t", variable = tb_varcheck30, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=15, stick=W)
Entrega = Checkbutton(Left, text = "0 - 5 anos\t", variable = tb_varcheck32, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=18, stick=W)
Entrega = Checkbutton(Left, text = "6 - 10 anos\t", variable = tb_varcheck33, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=19, stick=W)
Entrega = Checkbutton(Left, text = "11 - 20 anos\t", variable = tb_varcheck34, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=20, stick=W)
Entrega = Checkbutton(Left, text = "Acima de 21 anos\t", variable = tb_varcheck35, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=21, stick=W)


#Criação de caixa de texto para obtenção dos dados dos participantes

tb_txtNome = Entry(Left, font = ('arial', 11), bd = 2, width = 50, justify ='left', state=NORMAL, textvariable=tb_txtNome)
tb_txtNome.grid(row=0, column = 1)

tb_txtidade = Entry(Left, font = ('arial', 11), bd = 2, width = 50, justify ='left', state=NORMAL, textvariable=tb_txtidade)
tb_txtidade.grid(row=6, column = 1)

tb_txtOutros1 = Entry(Left, font = ('arial', 11), bd = 2, width = 50, justify ='left', state=NORMAL, textvariable=tb_txtOutros1)
tb_txtOutros1.grid(row=16, column = 1)

tb_txtEmail = Entry(Left, font = ('arial', 11), bd = 2, width = 50, justify ='left', state=NORMAL, textvariable=tb_txtEmail)
tb_txtEmail.grid(row=22, column = 1)

#Criação de botão para enviar informações

cmdEnviar = Button(Left, padx=16, pady=1, bd=2, fg='black', font=('arial', 12, 'bold'), width= 5, text="Enviar", command=var_states).grid(row=23, column=0)
cmdGravar = Button(Left, padx=16, pady=1, bd=2, fg='black', font=('arial', 12, 'bold'), width= 5, text="Registrar", command=gravarDados).grid(row=24, column=0)
cmdSair = Button(Left, padx=16, pady=1, bd=2, fg='black', font=('arial', 12, 'bold'), width= 5, text="Sair", command=iExit).grid(row=24, column=1)


#Fechamento do programa
janela.mainloop()


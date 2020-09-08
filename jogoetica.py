#Importando as bibliotecas necessarias
from tkinter import*
from tkinter import ttk
import random
import time
import datetime

    
#Importando o objeto da tela
janela = Tk()

janela.title("Ética")
janela["bg"]="black"
janela.configure(background = "white")

#Criando o frame do topo
Top = Frame(janela, width=100, height=100)
Top.pack(side=TOP)

#Criando o frame da esquerda
Left = Frame(janela, width=750, height=640)
Left.pack(side=LEFT)

#Criando o frame da direita
Right = Frame(janela, width=750, height=640)
Right.pack(side=RIGHT)
Right.configure(background='white')


#Inserindo Label para o titulo do sistema
lblTitulo = Label(Top, font=('arial', 20, 'bold'), text="Certificação ética", width=80)
lblTitulo.grid(row=0, column=0)


#Declaração de variaveis 


varcheck1 = IntVar()
varcheck1.set("0")

varcheck2 = IntVar()
varcheck2.set("0")

varcheck3 = IntVar()
varcheck3.set("0")

varcheck4 = IntVar()
varcheck4.set("0")

varcheck5 = IntVar()
varcheck5.set("0")

varcheck6 = IntVar()
varcheck6.set("0")

varcheck7 = IntVar()
varcheck7.set("0")

varcheck8 = IntVar()
varcheck8.set("0")

varcheck9 = IntVar()
varcheck9.set("0")

varcheck10 = IntVar()
varcheck10.set("0")

varcheck11= IntVar()
varcheck11.set("0")

varcheck12= IntVar()
varcheck12.set("0")

varcheck13= IntVar()
varcheck13.set("0")

varcheck14= IntVar()
varcheck14.set("0")

varcheck15 = IntVar()
varcheck15.set("0")

varcheck16 = IntVar()
varcheck16.set("0")


perguntas = StringVar()
perguntas.set("1- Os desenvolvedores são treinados pela empresa com capacitação sobre temas de ética e integridade?")

perguntas1 = StringVar()
perguntas1.set("2- Os desenvolvedores são punidos por não cumprirem as leis do código de ética na elaboração de um programa?")

perguntas2 = StringVar()
perguntas2.set("3- Existe algum canal de comunicação com a empresa para que os desenvolvedores tirem dúvidas sobre questões éticas?")

perguntas3 = StringVar()
perguntas3.set("4- Os programas são desenvolvidos de acordo com o código de ética ou código de conduta estabelecido pela empresa?")

perguntas4 = StringVar()
perguntas4.set("5- A finalidade do sistema desenvolvido é informada aos desenvolvedores?")

perguntas5 = StringVar()
perguntas5.set("6- Os funcionários possuem autonomia no desenvolvimento de projetos na empresa?")

perguntas6 = StringVar()
perguntas6.set("7- Existem testes que procuram verificar e validar os conceitos éticos utilizados?")


#Funções para botões

#Codigo do botão sair

def iExit():
    janela.destroy()
    return

def enviar():
    
    if varcheck1.get()==1:
        print("Questão 1: Correta")
    else:
        print("")
        
    if varcheck2.get()==1:
        
        print("Questão 1: Errado")
    else:
        print("")

    if varcheck3.get()==1:
        print("Questão 2: Correta")
    else:
        print("")
        
    if varcheck4.get()==1:
        
        print("Questão 2: Errado")
    else:
        print("")

    if varcheck5.get()==1:
        print("Questão 3: Correta")
    else:
        print("")
        
    if varcheck6.get()==1:
        
        print("Questão 3: Errado")
    else:
        print("")

    if varcheck7.get()==1:
        print("Questão 4: Correta")
    else:
        print("")
        
    if varcheck8.get()==1:
        
        print("Questão 4: Errado")
    else:
        print("")

    if varcheck9.get()==1:
        print("Questão 5: Correta")
    else:
        print("")
        
    if varcheck10.get()==1:
        
        print("Questão 5: Errado")
    else:
        print("")

    if varcheck11.get()==1:
        print("Questão 6: Correta")
    else:
        print("")
        
    if varcheck12.get()==1:
        
        print("Questão 6: Errado")
    else:
        print("")

    if varcheck13.get()==1:
        print("Questão 7: Correta")
    else:
        print("")
        
    if varcheck14.get()==1:
        
        print("Questão 7: Errado")
    else:
        print("")

def resultados():

    a=int(varcheck1.get()==1)
    b=int(varcheck2.get()==0)
    c=int(varcheck3.get()==1)
    d=int(varcheck4.get()==0)
    e=int(varcheck5.get()==1)
    f=int(varcheck6.get()==0)
    g=int(varcheck7.get()==1)
    h=int(varcheck8.get()==0)
    i=int(varcheck9.get()==1)
    j=int(varcheck10.get()==0)
    k=int(varcheck11.get()==1)
    l=int(varcheck12.get()==0)
    m=int(varcheck13.get()==1)
    n=int(varcheck14.get()==0)
    resultado = ((a+b+c+d+e+f+g+h+i+j+k+l+m+n)/14)*100
    lb_resultado= Label(Right,font = ('arial', 20), bd = 2, width = 10, text=f'{"%.2f" %resultado}').grid(row=10, column=0)
    result = Label(Right, font = ('arial', 16), bd = 2, width = 10, text='Resultado').grid(row=5, column=0)

    if resultado >= 70: print ("Aderente:",resultado)
    else: print("Não-aderente:",resultado)

#def limpar():
    

#criação de objetos e componentes


Entrega = Checkbutton(Left, text = "Sim\t", variable = varcheck1, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=1, stick=W)
Entrega = Checkbutton(Left, text = "Não\t", variable = varcheck2, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=2, stick=W)
Entrega = Checkbutton(Left, text = "Sim\t", variable = varcheck3, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=4, stick=W)
Entrega = Checkbutton(Left, text = "Não\t", variable = varcheck4, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=5, stick=W)    
Entrega = Checkbutton(Left, text = "Sim\t", variable = varcheck5, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=7, stick=W)
Entrega = Checkbutton(Left, text = "Não\t", variable = varcheck6, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=8, stick=W)
Entrega = Checkbutton(Left, text = "Sim\t", variable = varcheck7, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=10, stick=W)
Entrega = Checkbutton(Left, text = "Não\t", variable = varcheck8, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=11, stick=W)
Entrega = Checkbutton(Left, text = "Sim\t", variable = varcheck9, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=13, stick=W)
Entrega = Checkbutton(Left, text = "Não\t", variable = varcheck10, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=14, stick=W)
Entrega = Checkbutton(Left, text = "Sim\t", variable = varcheck11, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=16, stick=W)
Entrega = Checkbutton(Left, text = "Não\t", variable = varcheck12, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=17, stick=W)
Entrega = Checkbutton(Left, text = "Sim\t", variable = varcheck13, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=19, stick=W)
Entrega = Checkbutton(Left, text = "Não\t", variable = varcheck14, onvalue=1,offvalue=0, font=('arial', 10, 'bold')).grid(row=20, stick=W)




#Criação de caixa de texto para lado das questões da certificação

txtProduto = Entry(Left, font = ('arial', 11), bd = 2, width = 110, justify ='left', state=NORMAL, textvariable=perguntas)
txtProduto.grid(row=0, column = 0)

txtProduto = Entry(Left, font = ('arial', 11), bd = 2, width = 110, justify ='left', state=NORMAL, textvariable=perguntas1)
txtProduto.grid(row=3, column = 0)

txtProduto = Entry(Left, font = ('arial', 11), bd = 2, width = 110, justify ='left', state=NORMAL, textvariable=perguntas2)
txtProduto.grid(row=6, column = 0)

txtProduto = Entry(Left, font = ('arial', 11), bd = 2, width = 110, justify ='left', state=NORMAL, textvariable=perguntas3)
txtProduto.grid(row=9, column = 0)

txtProduto = Entry(Left, font = ('arial', 11), bd = 2, width = 110, justify ='left', state=NORMAL, textvariable=perguntas4)
txtProduto.grid(row=12, column = 0)

txtProduto = Entry(Left, font = ('arial', 11), bd = 2, width = 110, justify ='left', state=NORMAL, textvariable=perguntas5)
txtProduto.grid(row=15, column = 0)

txtProduto = Entry(Left, font = ('arial', 11), bd = 2, width = 110, justify ='left', state=NORMAL, textvariable=perguntas6)
txtProduto.grid(row=18, column = 0)



#Botões para a área de resultados

cmdEnviar= Button(Left, padx=16, pady=1, bd=2, fg='red', font=('arial', 12, 'bold'), width= 5, text="Enviar", command=enviar).grid(row=20,column = 0)

cmdSair = Button(Left, padx=16, pady=1, bd=2, fg='black', font=('arial', 12, 'bold'), width= 5, text="Sair", command=iExit).grid(row=21,column=1)

cmdResultado = Button (Left, padx=20, pady=1, bd=2, fg='black', font=('arial', 12, 'bold'), width= 5, text="Resultados", command=resultados).grid(row=21, column=0)

cmdLimpar = Button(Left, padx=20, pady=1, bd=2, fg='black', font=('arial', 12, 'bold'), width= 5, text="Limpar").grid(row=20, column=1)


#Fechamento do sistema
janela.mainloop()


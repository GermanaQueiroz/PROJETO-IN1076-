from tkinter import*

janela = Tk()

janela.title("Janela Principal")
janela["bg"]="gray"


lb1 = Label(janela, text="Email")
lb2 = Label(janela, text="Senha")

txt1 = Entry(janela, width=50)
txt2 = Entry(janela, width=50)

btn = Button(janela, text = "Login")
btn1 = Button(janela, text = "Recuperar senha")

lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
txt1.grid(row=0, column=1)
txt2.grid(row=1, column=1)

btn.grid(row=2, column=0)
btn1.grid(row=2, column=1)


#posicionamento e tamanho da janela
#L x A + ME + MT
janela.geometry("600x750+0+0")


janela.mainloop()

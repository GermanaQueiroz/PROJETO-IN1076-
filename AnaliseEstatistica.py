import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

x = pd.read_excel(r"C:\Users\germa\OneDrive\Bureau\Python\Python - Interface\Questionarioética\Dadosjogoetica.xlsx")

print(x.head())
print(x.describe())

#Distribuição da Idade

#Gerando um histograma

x.Idade.hist(bins=60)

plt.xlabel("Idade")
plt.ylabel("Numero de profissionais")
plt.title("Distribuição de Idade")
plt.show()

#Distribuição do sexo

x.Sexo.hist(bins=5)

plt.xlabel("Sexo")
plt.ylabel("Numero de profissionais")
plt.title("Distribuição por sexo")
plt.show()


#Grafico de pizza

plt.pie(x["Idade"], labels=x["Nome"], autopct="%1.0f%%")
plt.title("Distribuição do sexo")
plt.show()

#Distribuição por tempo de trabalho

x.Tempo.hist(bins=60)
plt.xlabel("Tempo")
plt.ylabel("Numero de profissionais")
plt.title("Distribuição por tempo de trabalho")
plt.show()




import matplotlib.pyplot as plt
#Para fazer gráficos em 3d
from mpl_toolkits.mplot3d import axes3d
import numpy as np

#Criando o gráfico eixo x e eixo y correspondente
plt.plot([8,6,4,4,5,6,7,8,9,10],[1,4,7,8,10,25,62,82,96,100],label='Sala 1',color='green',linestyle='--')
plt.plot([1,2,3,4,5,6,7,8,9,18],[1,4,7,8,10,25,62,82,96,100],label='Sala 2',color='red',linestyle='dotted')
#Colocando legenda
plt.ylabel('Aluno')
plt.xlabel('Nota')
plt.title('Relação Id Aluno X Nota')
#Iniciando a janela
plt.legend()
plt.show()
#criando gráficos de barras e comparando
x = [1,3,5,7]
y=[2,5,8,10]
x2= [2,4,6,8]
y2=[5,6,8,7]
plt.bar(x,y,color='Green',label='Quantos malucos de doidos têm 1')
plt.bar(x2,y2,color='Red',label='Quantos malucos de doidos têm 2')
plt.title('Doido Maluco')
plt.ylabel('Doido')
plt.xlabel('Maluco')
plt.legend()
plt.show()
#Criando gráficos de dispersão
x=[1,1,1.5,2,2]
y=[3,3.5,4,4.5,5]
plt.scatter(x,y,color='yellow',marker='*')
plt.plot(x,y,color='black')
#Gráficos maluco
x = [1,2,3,4]
y= [2,3,4,5]
xp = [1,1,1.5,2,2]
yp = [3,3.5,4,4.5,5]
xp1 = [3,3,3.5,4,2]
yp1 = [2,2.5,3,3.5,2]
plt.plot(x,y)
plt.scatter(xp,yp)
plt.scatter(xp1,yp1)
#Gráficos de Pizza ou Setores
label = ['Floresta','Deserto']
dados=[60,40]
fig, ax=plt.subplots()
ax.pie(dados,labels=label,autopct='%1.1f%%')
#Gráficos em 3D
fig = plt.figure()
ax = fig.gca(projection="3d")
x,y,z = axes3d.get_test_data(0.9)
graf = ax.plot_wireframe(x,y,z)
plt.show()




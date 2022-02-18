# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:26:52 2017

@author: Laura
"""


import numpy as np

import math
from math import sqrt
import matplotlib.pylab as plt
import matplotlib.pyplot as pl


## Tomei como referencia um exercicio do livro do H. Moyses N. 
##(um dos primeiros da parte de gravitacao)

G = 6.6739*10**(-11)
#### em kg
M = 7.23*10**22
m = 50.

## Esse raio determina o numero de 
## iteracoes. Entao, para testar, 
## por um valor menor (17, por exemplo). 
## Caso contrario, o grafico 
## ira demorar muito para aparecer

#### Em km
R = 1738.

#### Valor qualquer para U(R)

UR = 200.
### h eh o incremento dos pontos e r a lista de possiveis raios
h = 0.5        
r = np.arange(0.0,10.*R + h,h)




##################### Potencial U)r)

def U(t,R,G,M,m):
### potencial para t menor que o raio do corpo    
    if t < R:
        saida = UR + (G*M*m*t**2)/(2*R**3) - (G*M*m)/(2*R)
    else:
### potencial para t maior ou igual ao raio do corpo
        saida = -(G*M*m)/(t)
    
    return saida    
        


#################### Forca = - gradU     
        
def F(G,M,m,t):
    if t >= R:
### forca para t maior ou igual ao raio do corpo
        saida = -(G*m*M)/(t**2)
    else:
### forca para t menor que o raio do corpo
        saida = 0
    return saida



########### definindo a matriz do potencial e a matriz da forca
    
Ur = np.zeros(len(r))
Fgrad = np.zeros(len(r))


########### definindo alguns contadores para auxiliar
########### na legenda dos graficos
cont1=0
cont2=0
cont3=0


########### Calculando o potencial
print '\nPotencial gravitacional associado a distancia entre a Lua e um corpo orbitando ao seu redor\n'
for t in r:
    Ur = U(t,R,G,M,m)
    if t%100==0:  ### os pontos pulam de 100 em 100 para
                  ### diminuir o tempo de processamento
    ### grafico para t>=R
        if (t >= R):
            ### plotando e "pintando" o grafico em t >= R
            pl.plot(t,Ur,'r^')
            ### esse contador ajuda a plotar a legenda1
            ### para que ela apareca apenas uma vez
            if cont1==0:
                cont1=1
                ### legenda1 para t>=R
                plt.plot(t,Ur,'r^',label='Raio > ou = ao raio da Lua')
            ### nomeando os eixos
            pl.ylabel(Ur'Potencial')
            pl.xlabel(Ur'Raio')
            ### titulo do grafico
            plt.title('Potencial gravitacional = U')
    ### grafico para t<R
        else:
            ### esse contador ajuda a plotar a legenda2
            ### para que ela apareca apenas uma vez
            if cont2==0:
                cont2=1
                ### legenda2 para t<R
                plt.plot(t,Ur,'go',label='Raio < raio da Lua')
            ### plotando e "pintando" o grafico em t<R
            pl.plot(t,Ur,'go')
    ### mostrando a legenda e salvando a imagem em postscript
    if t==10*R:
        plt.legend()
        pl.savefig('Ur.png')


### mostrando o primeiro grafico
plt.show()


########## Calculando a forca
print '\nForca associada ao Gradiente do potencial\n'
for t in r:
    Fgrad = F(G,M,m,t)
    if t%100==0:### os pontos pulam de 100 em 100 para
                ### diminuir o tempo de processamento
        ### titulo do grafico        
        plt.title('Forca = Gradiente de U')
        ### nomeando os eixos
        pl.ylabel(Ur'Gradiente')
        pl.xlabel(Ur'Raio')
        ### plotando e "pintando" o grafico da forca
        pl.plot(t,Fgrad,'o',color='blue')
        ### esse contador ajuda a plotar a legenda2
        ### para que ela apareca apenas uma vez
        if cont3==0:
            cont3=1
            ### legenda3 para o gradiente
            pl.plot(t,Fgrad,'o',color='blue',label='Grad U')
    ### mostrando a legenda e salvando a imagem em postscript
    if t==10*R:
        plt.legend()
        pl.savefig('Fgrad.png')


### mostrando o segundo grafico
plt.show()




############## De Gravitacao para oscilacoes ############
### oscilacoes forcadas amortecidas



### Estou em duvida quanto a esse grafico!!





### "peteleco" inicial
f0= 5.
### frequencia natural do sistema
w0= 11.
### ro/massa
gama= 2.
### contador para auxiliar na legenda
cont4=0
### massa em kg
massa= 10.
### pulo da frequancia e vetor de frequencias
c = 0.5
w =np.arange(1.,10 + c,c)
### vetor do tempo
tempo = np.arange(0.0,10,0.5)



########## funcao da oscilacao

def X(f0,massa,gama,w0,w):
    amplit=(f0*math.cos(w*t - math.atan(gama*w/(w0**2-w**2)))/(massa*sqrt((w0**2-w**2)**2-(gama**2)*(w**2))))
    return amplit


### matriz da oscilacao
Xt=np.zeros(len(w))


print "\nOscilacoes\n"
### Calculando a funcao
for t in tempo:
    for x in w:
        Xt= X(f0,massa,gama,w0,x)
        ### titulo do grafico       
        plt.title('Oscilacao forcada')
        ### nomeando os eixos
        pl.ylabel(Ur'Amplitude')
        pl.xlabel(Ur'Frequencia')
        ### plotando e "pintando" o grafico da oscilacao
        pl.plot(x,Xt,'go')
        ### esse contador ajuda a plotar a legenda4
        ### para que ela apareca apenas uma vez
        if cont4==0:
            cont4=1
            ### legenda4 para a amplitude
            pl.plot(x,Xt,'go',label='Amplitude(w)')
        ### mostrando a legenda e salvando a imagem em postscript
        if x==10:
            plt.legend()
            pl.savefig('Amplitude.png')


### mostrando o terceiro grafico
plt.show()

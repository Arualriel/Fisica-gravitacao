# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 13:26:52 2017

@author: Laura
"""


import numpy as np

import matplotlib.pyplot as plt


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
R = 17#38.

#### Valor qualquer para U(R)

UR = 200.

h = 0.5        
r = np.arange(0.0,10.*R + h,h)


##################### Potencial U)r)


def U(t,R,G,M,m):    
    if t < R:
        saida = UR + (G*M*m*t**2)/(2*R**3) - (G*M*m)/(2*R)
    else:
        saida = -(G*M*m)/(t)
    
    return saida    
        
#################### Forca = - gradU     
        
def F(G,M,m,t):
    if t > R:
        saida = -(G*m*M)/(t**2)
    else:
        saida = 0
    return saida

Ur = np.zeros(len(r))

Fgrad = np.zeros(len(r))
print '\nPOTENCIAL\n'
raio=U(R,R,G,M,m)
for t in r:
    Ur = U(t,R,G,M,m)
    if t > R:
        plt.plot(t,Ur,'r--')
        plt.ylabel(Ur'Potencial')
        plt.xlabel(u 'Raio')
        plt.xlim(0,10*R)
    else:
        plt.plot(t,Ur,'b-')
        plt.ylabel(Ur'Potencial')
        plt.xlabel(u 'Raio')
        plt.xlim(0,10*R)
        if r==R:
            plt.annotate(t'r = R',(R,raio),(R+1,raio+1))

plt.show()

print '\nF = - GRAD U\n'

for t in r:
    Fgrad = F(G,M,m,t)
    plt.scatter(t,Fgrad)



plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 13:22:57 2015

@author: Ricardo
"""

import matplotlib.pylab as plt
from scipy import misc
import numpy as np
    
def main():
    #carga una imagen cualquiera
    l = misc.imread('C:\Users\Ricardo\Desktop\digimon.gif', flatten=1)
    #flatten = 1 convierte las capas de color en una sola capa en escala de grises
    #l = misc.lena()
    plt.subplot(3,1,1)
    #añade una etiqueta
    plt.ylabel("Imagen Original")
    plt.imshow(l,cmap='gray')
    
    (ren,col) = np.shape(l)
    
    print ("Dimensiones: %d x %d") % (col, ren)
    
    n = np.zeros((ren,col))
    c = np.zeros((ren,col))
    n = 255 - l
    """
    for i in range(ren):
        for j in range(col):
            n[i,j] = 255- l[i,j]
    """
    plt.subplot(3,1,2)
    plt.ylabel("Negativo")
    plt.imshow(n,cmap='gray')
    
    p = input("Probabilidad para contaminar:")
    
    for i in range(ren):
        for j in range(col):
            #np.random.rand() devuelve un número aleatorio procedente de una distribución
            #uniforme en el intervalo [0,1). Se multiplica * 100 para obtener un 100%
            if np.random.rand() * 100 <= p:
                if np.random.randint(2) == 0:
                    c[i,j]=0
                else:
                    c[i,j]=255
            else:
                c[i,j]=l[i,j]
    plt.subplot(3,1,3)
    plt.ylabel("Contaminada\n Al %.2f" % (p) + "%")
    plt.imshow(c,cmap='gray')
    plt.show()
    
if __name__ == "__main__":
    main()

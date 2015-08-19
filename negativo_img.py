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
    plt.subplot(2,1,1)
    #añade una etiqueta
    plt.ylabel("Imagen Original")
    plt.imshow(l,cmap='gray')
    
    (ren,col) = np.shape(l)
    
    print ("Dimensiones: %d x %d") % (col, ren)
    
    n = np.zeros((ren,col))
    n = 255 - l
    """
    for i in range(ren):
        for j in range(col):
            n[i,j] = 255- l[i,j]
    """
    plt.subplot(2,1,2)
    plt.ylabel("Negativo")
    plt.imshow(n,cmap='gray')
    plt.show()
    
if __name__ == "__main__":
    main()

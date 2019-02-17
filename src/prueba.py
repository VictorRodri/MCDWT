# Bibliotecas requeridas para este software.
import cv2
import argparse
import time
import numpy as np
from PIL import Image

# Mostrar en consola que este programa iniciará su ejecución.
print("Iniciando programa...")

# Abrir y cargar la imagen del disco.
imagen = cv2.imread("/home/victor/Documentos/MCDWT/src/imagennegropuntoblanco.jpg")

# Convertir la imagen a escala de grises.
#imagenbn = imagen.convert('L')

# Si la imagen se trabaja a color, 'datopixel' obtendrá los valores BGR del píxel XY en cuestión de la imagen.
# Si la imagen se trabaja en blanco y negro (BN), 'datopixel' obtendrá el valor entero del píxel XY en cuestión de la imagen.
#datopixel = imagen.getpixel((x, y))

print("Siendo 0 la subbanda LL, 1 la LH, 2 la HL y 3 la HH.")

# Leer y analizar todos los píxeles de la imagen.
def vectorial(imagen, x, y):

    for i in range(0, 4):
        print("Subbanda", i)
        # Leer y cargar en 'm' las distintas subbandas (cuadrantes) de la imagen, píxel a píxel (filas, columnas).
        if i == 0:
            m = imagen[:250, :250] # subbanda LL de arriba-izquierda.
        if i == 1:
            m = imagen[250:, :250] # subbanda LH de arriba-derecha.
        if i == 2:
            m = imagen[:250, 250:] # subbanda HL de abajo-izquierda.
        if i == 3:
            m = imagen[250:, 250:] # subbanda HH de abajo-derecha.

        # Obtener en matrices las componentes BGR de todos los píxeles de la imagen.
        mB = m[:, :, 2]
        mG = m[:, :, 1]
        mR = m[:, :, 0]
                
        # Elevar al cuadrado cada dato BGR de la imagen.
        mB2 = mB*mB
        mG2 = mG*mG
        mR2 = mR*mR

        # Realizar la sumatoria acumulativa de cada BGR al cuadrado de la imagen.
        sumB = np.sum(mB2)
        sumG = np.sum(mG2)
        sumR = np.sum(mR2)

        # Sumar las anteriores tres componentes entre sí ('sumB', 'sumG' y 'sumR'), para obtener la sumatoria total de los valores de las tres componentes RGB entre sí de todos los píxeles al cuadrado de la imagen.
        sumaBGR = sumR+sumG+sumB

        # Mostrar en consola la 'sumaBGR' de la imagen calculada previamente (ver instrucción anterior).
        print(sumaBGR)

        # Guardar en distintas variables los resultados de las 'sumaBGR' de las subbandas (cuadrantes) de la imagen.
        if i == 0:
            HH = sumaBGR # subbanda HH de abajo-derecha.
        if i == 1:
            LL = sumaBGR # subbanda LL de arriba-izquierda.
        if i == 2:
            LH = sumaBGR # subbanda LH de arriba-derecha.
        if i == 3:
            HL = sumaBGR # subbanda HL de abajo-izquierda.

            print("LL/HH =", LL/HH)
            print("LH/HH =", LH/HH)
            print("HL/HH =", HL/HH)

# Llamar a la función definida 'vectorial(imagen, x, y)', siendo 'imagen' la imagen a tratar, y XY las coordenadas de la esquina superior izquierda de la imagen (es el píxel exacto donde comenzará su tratamiento).
vectorial(imagen, 0, 0)
    
# Mostrar en consola que este programa finalizó su ejecución.
print("Programa terminado.")

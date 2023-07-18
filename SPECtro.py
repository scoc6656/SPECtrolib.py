#Este va a ser el main, aquí va nuestro código cuando esté completo
#mientras hay que trabajar en branch
#Creamos una función para desempaquetar los datos que vienen en archivo fits (flexible image transport system)
#denominada open_file

import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


#Función para abrir el archivo fits
def open_fits(data_file):
    
    """
    DESCRIPCIÓN
    Ésta función recibe como argumento un archivo en formato fits ("data_file") para devolvernos el archivo desempaquetado
    con la longitud ya calculada con los parámetros de header que está en los datos. 
    
    OUTPUTS
    retorna la variable "longitud" que representa
    el flujo del espectro de luz, la variable "data" que son los datos que entrega el archivo y por último la variable "header" 
    que representa el encabezado asociado a los datos, en ese orden respectivamente. 

    EJEMPLO
    Para que la función nos retorne esos valores debemos crear 3 variables a las que le asignemos estos outputs, es decir, hacer
    la asignación: longitud,data,header = open_fits('file')
    """
    
    with fits.open(data_file) as set_data:
        header = set_data[0].header
        data = set_data[0].data
        
    pix1 = header['CRVAL1']
    delta = header['CDELT1']
    num = header['NAXIS1']
    pixeles = pix1 + delta * num
    longitud = np.linspace(pix1, pixeles, num, endpoint = False)
    
    return (longitud, data, header)


#Creamos una función para graficar el espectro y un recorte de este 
def slicing_plot(a,b):
    """
    DESCRIPCIÓN
    La funcion sirve para hacer un recorte en el gráfico de los datos, dando como opción de que el usario indique sus 
    maximos y minimos para el espectro que desea graficar.

    OUTPUT
    Nos devuelve un gráfico recortado del espectro en longitud vs flujo normalizado.
    
    USO 
    slicing_plot(a,b)
    a: deben ser los datos de longitud
    b: deben ser los datos en sí mismos
    El código pide 2 inputs
    min:  es el limite inferior en x
    max: es el límite superior en x
    """
    xmin= int(input('indique el xmin para su gráfico: '))
    xmax= int(input('indique el xmax para su gráfico: '))
    #ploteo de los datos ya recortados    
    %matplotlib qt
    plt.figure(figsize=(18,6))
    plt.plot(a,b)
    plt.ylabel('$Normalized flux$')
    plt.xlabel('$Angstroms$')
    plt.grid('on')
    plt.xlim(xmin,xmax)
    plt.show()
  

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
    Ésta función recibe como argumento un archivo en formato fits ("data_file") y retorna la variable "longitud" que representa
    el flujo del espectro de luz, la variable "data" que son los datos que entrega el archivo y por último la variable "header" 
    que representa el encabezado asociado a los datos, en ese orden respectivamente. 
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
    """la funcion sirve para hacer un recorte en el plot de los datos, dando como opción de que el usario indique sus maximos y minimos
          especificos a realizar"""
    xmin= int(input('indique el xmin para su gráfico: '))
    xmax= int(input('indique el xmax para su gráfico: '))
    #ploteo de los datos ya recortados    
    
    plt.figure(figsize=(18,6))
    plt.plot(a,b)
    plt.ylabel('$Normalized flux$')
    plt.xlabel('$Angstroms$')
    plt.grid('on')
    plt.xlim(xmin,xmax)
    plt.show()
  

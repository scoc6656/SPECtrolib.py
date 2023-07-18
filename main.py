#Este va a ser el main, aquí va nuestro código cuando esté completo
#mientras hay que trabajar en branch
#Creamos una función para desempaquetar los datos que vienen en archivo fits (flexible image transport system)
#denominada open_file

from astropy.io import fits
import matplotlib.pyplot as plt 
def open_file(data_file):
  """La función data file nos ayuda a desempaquetar el header y el array o imagen que contiene
     los datos de formato fits, para ello debemos insertar en la función un archivo fits"""
  with fits.open(data_file) as data:
    header = data[0].header
    file = data[0].data
    return(header, file)

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
  

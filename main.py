#Este va a ser el main, aquí va nuestro código cuando esté completo
#mientras hay que trabajar en branch
#Creamos una función para desempaquetar los datos que vienen en archivo fits (flexible image transport system)
#denominada open_file
def open_file(data_file):
  """La función data file nos ayuda a desempaquetar el header y el array o imagen que contiene
     los datos de formato fits, para ello debemos insertar en la función un archivo fits"""
  with fits.open(data_file) as data:
    header = data[0].header
    file = data[0].data
    return(header, file)

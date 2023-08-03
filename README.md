# SPECtro.py
SPECtro.py tiene como propósito aportar una serie de funciones principalmente enfocada en el área de la espectrocopia, con el fin de agilizar el trabajo con datos espectrales. Entre las herramientas encontramos la normalización de datos, gráficos de espectros y la etiqueta de líneas de absorción presentes. 
Entre las dependencias del código se encuentran astropy.oi, matplotlib y numpy.

Disponible para la version Python 3.10.11

En este repositorio podran encontrar las siguentes funciones: open_fits, data_normalization, slicing_plot y labels.

La función open_fits lo que hace es leer el archivo en formato fits y entregar tres variables:  header, contiene la información que permite reconstruir el muestreo del flujo. La variable data es una extensión que contiene un array con estos flujos. Por último, longitud es la reconstrucción de la longitud de onda (o flujo) a partir del header y data.

La siguiente función es data_normalization y se divide en tres secciones:
model_fit busca un polinomio entre los grados 1 y 5 que mejor se ajuste a los datos y elige el que tenga menor diferencia entre los datos reales y la predicción del modelo.
sigma_clip recibe los parámetros de longitud y data para realizar un recorte de los datos asociado al ruido.
Se aplican estas dos funciones primero sigma_clip de forma iterativa hasta cumplir 10 veces, luego model_fit para encontrar un polinomio mejor ajustado debido al recorte del ruido y finalmente se divide la variable data entre el polinomio evaluado en la longitud para de esta manera entregar los datos normalizados.

La función slicing_plot genera un gráfico de una parte del espectro especificada por el usuario, el cual se genera mediante un recorte de los datos.

Por último labels es una función que a partir de un valor de ancho equivalente que ingrese el usuario, un valor mínimo y máximo de longitud de onda, grafica los datos con etiquetas de elementos químicos asociados a las líneas de absorción.


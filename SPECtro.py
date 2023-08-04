#Este va a ser el main, aquí va nuestro código cuando esté completo
#mientras hay que trabajar en branch
#Creamos una función para desempaquetar los datos que vienen en archivo fits (flexible image transport system)
#denominada open_file

import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

class load:
    def __init__(self, data_file):
        self.data_file = data_file
        self.longitud, self.data, self.header = self.open_fits()


    def open_fits(self):

        """
        Ésta función lee el archivo y entrega los datos de longitud de onda, los datos y el header respectivamente.

        """

        with fits.open(self.data_file) as set_data:
            header = set_data[0].header
            data = set_data[0].data

        pix1 = header['CRVAL1']
        delta = header['CDELT1']
        num = header['NAXIS1']
        pixeles = pix1 + delta * num
        longitud = np.linspace(pix1, pixeles, num, endpoint=False)

        return longitud, data, header


    def model_fit(self, longitud, data):

        """
        Ésta función recibe como argumentos la longitud del espectro y el set de datos asociado para buscar un modelo
        polinomial que se ajuste a los datos.

        """

        polynomials = []
        MSEs = []

        for grade in range(1, 6):
            model = np.poly1d(np.polyfit(longitud, data, grade))
            mse = np.sqrt( (1/len(data)) * np.sum( (data - model(longitud)) ** 2) )
            polynomials.append(model)
            MSEs.append(mse)

        index = MSEs.index(min(MSEs))
        return polynomials[index]



    def sigma_clip(self, longitud, data):

        """
        Ésta función recibe como argumentos la longitud del espectro y el set de datos asociado para buscar un modelo
        polinomial que se ajuste a los datos.

        """

        mean = np.mean(data)
        std = np.std(data)
        sigma = 2

        threshold_upper = mean + sigma * std
        threshold_lower = mean - sigma * std

        clipped_data = []
        clipped_longitud = []
        for i in range(len(data)):
            if threshold_lower <= data[i] <= threshold_upper:
                clipped_data.append(data[i])
                clipped_longitud.append(longitud[i])

        return clipped_longitud, clipped_data



    def normalized_data(self):

        """
        Ésta función normaliza los datos espectrales.

        """

        clip_longitud = self.longitud
        clip_data = self.data

        for i in range(11):
            clip_longitud, clip_data = self.sigma_clip(clip_longitud, clip_data)

        normalization = (self.data / self.model_fit(clip_longitud, clip_data)(self.longitud))

        plt.figure(figsize=(20, 6))
        plt.plot(self.longitud, normalization)
        plt.xlabel(r"Angstroms ($\mathrm{\AA}$)", fontsize=14)
        plt.ylabel("Normalized Flux", fontsize=14)
        plt.grid()

        return normalization



    def labels(self, eqw, min_wavelength, max_wavelength):

        """
        Ésta función recibe como argumentos el ancho equivalente que desee el usuario (eqw), el mínimo y máximo de longitud de onda
        que se desea graficar, hay que tener en cuenta que estos datos tienen que coincidir con los rangos de longitud presentes en
        los datos de estudio.

        """

        opticalLabels = np.genfromtxt("opticalLines_EQW_giant.dat", dtype=None, encoding=None, unpack=True, usecols=(0, 1, 2), skip_header=1)
        wavelength = opticalLabels[0]
        chemical_element = opticalLabels[1]
        equivalent_width = opticalLabels[2]

        # Filtrar las filas según la condición ingresada por el usuario
        indices_cumplen_condicion = []
        for i in range(len(equivalent_width)):
            if equivalent_width[i] >= eqw and min_wavelength <= wavelength[i] <= max_wavelength:
                indices_cumplen_condicion.append(i)

        # Crear listas con los índices que cumplen la condición para cada columna
        wavelength_filtrada = [wavelength[i] for i in indices_cumplen_condicion]
        chemical_element_filtrada = [chemical_element[i] for i in indices_cumplen_condicion]
        equivalent_width_filtrada = [equivalent_width[i] for i in indices_cumplen_condicion]

        # Crear el gráfico
        plt.figure(figsize=(20, 6))
        plt.plot(self.longitud, self.normalized_data())

        # Marcar los puntos y etiquetarlos
        for j, name in enumerate(chemical_element_filtrada):
            plt.annotate(name, xy = (wavelength_filtrada[j], 1.1), xytext = (wavelength_filtrada[j], 1.22 + 0.08),
                         arrowprops = dict(arrowstyle = "simple", color = "#A872DB", lw = 1.25),
                         fontsize = 12, weight="bold", ha = "left", va="top")

        # Personalizar el gráfico
        plt.xlabel(r"Angstroms ($\mathrm{\AA}$)", fontsize = 14)
        plt.ylabel("Flux", fontsize = 14)
        plt.title("Gráfico con elementos etiquetados", fontsize = 14)
        plt.xlim(min_wavelength, max_wavelength)
        plt.grid(True)

        # Mostrar el gráfico
        plt.show()
  

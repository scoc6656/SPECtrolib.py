import numpy as np



def data_normalization(longitud, data):
    
    """
    Está función recibe como argumentos la longitud del espectro, conocido también como flujo, y el set de datos asociados para
    luego retornar un gráfico de data en función de la longitud pero con los datos normalizados.
    """
    
    def model_fit(longitud, data):
        
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
        return (polynomials[index])

    def sigma_clip(longitud, data):
        
        """
        Ésta función recibe como argumentos la longitud del espectro y el set de datos asociados para realizar un recorte de
        los mismos, el cual podría considerarse como el ruido asociado.
        """
        
        # Calcula la media y la desviación estándar
        mean = np.mean(data)
        std = np.std(data)
        sigma = 2

        # Define el umbral de corte superior e inferior
        threshold_upper = mean + sigma * std
        threshold_lower = mean - sigma * std

        # Realiza el recorte sigma   
        clipped_data = []
        clipped_longitud = []
        for i in range(len(data)):
            if threshold_lower <= data[i] <= threshold_upper:
                clipped_data.append(data[i])
                clipped_longitud.append(longitud[i])
    
        return(clipped_longitud, clipped_data)

    clip_longitud = longitud
    clip_data = data

    for i in range(11):
        clip_longitud, clip_data = sigma_clip(clip_longitud, clip_data)
    normalization = (data / model_fit(clip_longitud, clip_data)(longitud))
    return(normalization)
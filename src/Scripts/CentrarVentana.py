def CentrarVentana(ventana, ancho, alto):
    # Cálculos para el centrado de la ventana
    Ancho_Ventana = ventana.winfo_screenwidth()
    Alto_Ventana = ventana.winfo_screenheight()

    Coordenada_X = int((Ancho_Ventana / 2) - (ancho / 2))
    Coordenada_Y = int((Alto_Ventana / 2) - (alto / 2))

    # Redimensionar Ventana
    return ventana.geometry(
        "{}x{}+{}+{}".format(ancho, alto, Coordenada_X, Coordenada_Y)
    )

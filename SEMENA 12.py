def calcular_temperatura_promedio(ciudades_temperaturas):
    """
    Calcula el promedio de temperatura de cada ciudad.

    Parámetros:
    ciudades_temperaturas (dict): Un diccionario donde las claves son los nombres de las ciudades
                                  y los valores son listas de temperaturas semanales.

    Retorna:
    dict: Un diccionario con las ciudades como claves y su temperatura promedio como valores.
    """
    promedios = {}

    for ciudad, temperaturas in ciudades_temperaturas.items():
        # Calcula el promedio sumando las temperaturas y dividiéndolo entre el número de semanas
        promedio = sum(temperaturas) / len(temperaturas)
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso
ciudades_temperaturas = {
    'Ciudad A': [20, 22, 23, 21],  # Temperaturas de Ciudad A en 4 semanas
    'Ciudad B': [18, 19, 21, 20],  # Temperaturas de Ciudad B en 4 semanas
    'Ciudad C': [25, 26, 27, 24]  # Temperaturas de Ciudad C en 4 semanas
}

promedios = calcular_temperatura_promedio(ciudades_temperaturas)

# Mostrar los resultados
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperatura en {ciudad} es {promedio:.2f}°C")


# Definición de los datos de temperatura: Ciudades, Días de la semana, Semanas
# Ejemplo: 3 ciudades, 7 días por semana, 4 semanas
temperaturas = [
    [   # Pedernales ( Ciudad 1)
        [20, 22, 21, 19, 18, 20, 21],  # Semana 1
        [21, 23, 22, 20, 19, 21, 22],  # Semana 2
        [22, 24, 23, 21, 20, 22, 23],  # Semana 3
        [23, 25, 24, 22, 21, 23, 24]   # Semana 4
    ],
    [   # Santo Domingo ( Ciudad 2 )
        [15, 16, 15, 14, 13, 15, 16],  # Semana 1
        [16, 17, 16, 15, 14, 16, 17],  # Semana 2
        [17, 18, 17, 16, 15, 17, 18],  # Semana 3
        [18, 19, 18, 17, 16, 18, 19]   # Semana 4
    ],
    [   # Manta ( Ciudad 3 )
        [25, 26, 25, 24, 23, 25, 26],  # Semana 1
        [26, 27, 26, 25, 24, 26, 27],  # Semana 2
        [27, 28, 27, 26, 25, 27, 28],  # Semana 3
        [28, 29, 28, 27, 26, 28, 29]   # Semana 4
    ]
]

# Calcula y muestra el promedio de temperaturas para cada ciudad y semana
for ciudad_index in range(len(temperaturas)):
    for semana_index in range(len(temperaturas[ciudad_index])):
        suma_temperaturas = 0
        for dia in temperaturas[ciudad_index][semana_index]:
            suma_temperaturas += dia
        promedio = suma_temperaturas / len(temperaturas[ciudad_index][semana_index])
        print(f"Promedio de temperaturas para Ciudad {ciudad_index + 1} en Semana {semana_index + 1}: {promedio:.2f}°C")

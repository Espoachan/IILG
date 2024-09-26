import csv
import os

def obtener_siguiente_combinacion(ultima):
    if ultima == 'ZZ':
        return 'AAA'  # Puedes cambiar esto si necesitas más combinaciones
    if ultima[-1] != 'Z':
        return ultima[:-1] + chr(ord(ultima[-1]) + 1)
    else:
        return obtener_siguiente_combinacion(ultima[:-1] + 'Z')

def agregar_combinar_csv(nombre_archivo):
    # Verifica si el archivo existe
    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Combinación', 'Significado'])  # Encabezados

    # Leer el archivo CSV y obtener la última combinación
    with open(nombre_archivo, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        filas = list(reader)

    if filas:
        ultima_combinacion = filas[-1]['Combinación']
    else:
        ultima_combinacion = 'AA'  # Inicializa con 'AA' si está vacío

    # Obtener la siguiente combinación
    siguiente_combinacion = obtener_siguiente_combinacion(ultima_combinacion)
    print(f'La siguiente combinación es: {siguiente_combinacion}')

    # Pedir al usuario el significado
    significado = input('Introduce el significado para la combinación: ')

    # Agregar al CSV
    with open(nombre_archivo, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([siguiente_combinacion, significado])

    print(f'Combinación {siguiente_combinacion} agregada con éxito.')

# Ejecutar la función
agregar_combinar_csv('IILG.csv')

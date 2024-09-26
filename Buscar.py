import csv

def buscar_significado(codigo):
    # Abrir el archivo CSV en modo lectura
    with open('IILG.csv', mode='r', encoding='utf-8') as archivo_csv:
        lector_csv = csv.reader(archivo_csv)
        
        # Recorrer las filas del archivo
        for fila in lector_csv:
            if fila[0] == codigo:  # Verificar si el código coincide
                return fila[1]  # Retornar el significado
    
    return "Código no encontrado."  # Mensaje si no se encuentra el código

def main():
    codigo = input("Introduce el código que deseas buscar: ").strip().upper()
    significado = buscar_significado(codigo)
    print(f"El significado de {codigo} es: {significado}")

if __name__ == "__main__":
    main()

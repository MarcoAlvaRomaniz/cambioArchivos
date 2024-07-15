import os
import pandas as pd

folder = os.path.dirname(os.path.abspath(__file__))
print("Estamos en :",folder)

# Ruta de la carpeta con los archivos
input_folder = folder
# Ruta donde quiero que se generen
output_folder = folder + '/excel'

# Crear la carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Codificaciones comunes a probar
encodings = ['utf-8', 'latin-1', 'ISO-8859-1', 'cp1252']

# Procesar cada archivo en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.csv'):
        # Construir las rutas completas de los archivos
        csv_path = os.path.join(input_folder, filename)
        excel_path = os.path.join(output_folder, filename.replace('.csv', '.xlsx'))
        
        print("CSV PATH:", csv_path)
        print("EXCEL PATH:", excel_path)

        for encoding in encodings:
            try:
                # Intentar leer el archivo CSV con la codificación especificada
                archivo = pd.read_csv(csv_path, encoding=encoding)
                # Guardar como archivo Excel
                archivo.to_excel(excel_path, index=False)
                print(f"Archivo convertido con la codificación {encoding}: {excel_path}")
                break  # Salir del bucle si se lee correctamente
            except Exception as e:
                print(f"Error al procesar el archivo {csv_path} con la codificación {encoding}: {e}")


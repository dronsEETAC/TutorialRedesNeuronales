import os

nombre_objeto = 'caballo'

carpeta_imagenes_train = 'YOLOv5Dataset/images/train'
carpeta_etiquetas_train = 'YOLOv5Dataset/labels/train'

carpeta_imagenes_val = 'YOLOv5Dataset/images/val'
carpeta_etiquetas_val = 'YOLOv5Dataset/labels/val'

# Obtener la lista de archivos en la carpeta
archivos = os.listdir(carpeta_imagenes_train)

# Iterar sobre cada archivo en la carpeta
for archivo in archivos:
    # Comprobar si el archivo es una imagen
    if archivo.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        # Ruta completa de la imagen



        # Nombre del archivo de texto donde se escribirá el resultado
        nombre_archivo_txt = os.path.splitext(archivo)[0] + '.txt'
        ruta_archivo_txt = os.path.join(carpeta_etiquetas_train, nombre_archivo_txt)

        # Escribir el tamaño de la imagen en el archivo de texto
        with open(ruta_archivo_txt, 'w') as f:
            f.write("0 0.5 0.5 1 1\n")




archivos = os.listdir(carpeta_imagenes_val)

# Iterar sobre cada archivo en la carpeta
for archivo in archivos:
    # Comprobar si el archivo es una imagen
    if archivo.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        # Ruta completa de la imagen



        # Nombre del archivo de texto donde se escribirá el resultado
        nombre_archivo_txt = os.path.splitext(archivo)[0] + '.txt'
        ruta_archivo_txt = os.path.join(carpeta_etiquetas_val, nombre_archivo_txt)

        # Escribir el tamaño de la imagen en el archivo de texto
        with open(ruta_archivo_txt, 'w') as f:
            f.write("0 0.5 0.5 1 1\n")


nombre_archivo = "YOLOv5Dataset/dataset.yaml"
contenido_yalm = """
names:
  0: """ + nombre_objeto + """
path: ../YOLOv5Dataset
train: ./images/train/
val: ./images/val/
"""
with open(nombre_archivo, 'w') as f:
        f.write(contenido_yalm)

print("Fin")

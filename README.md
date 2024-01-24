# Tutorial Redes Neuronales
El fichero best_lata.pt contiene la configuración de una red neuronal entrenada por Yolov5 para reconocer latas de bebidas (Coca Cola, Fanta, etc.)    
El script detect.py usa el fichero de configuración .pt para detectar el objeto correspondiente en el stream de video. Es necessario importar las librerías que se indican en el propio script.      
El script downloadCOCO.py permite descargar imágenes etiquetadas de los datasets de la base de datos COCO (consultar en https://cocodataset.org). En el script hay que editar el tipo de imágenes que se quiere descargar (de entre las posibles que ofrece COCO) y el número de imágenes que se desea. Es necessario importar las librerías que se indican en el propio script.      

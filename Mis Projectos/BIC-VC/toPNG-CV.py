#JESUS CHAVEZ ARIAS
#MAY, 12 2023
import cv2, os, time
import numpy as np
#--------------------------------------------------FUNCION CAMBIAR DE NOMBRE A LOS ARCHIVOS EN LA CARPETA--------------
def cambiarName():
    imagesPNG = np.array([file for file in os.listdir() if file.endswith('.png')])
    imagesJPG = np.array([file for file in os.listdir() if file.endswith('.jpg')])
    cont = 1
    
    imagesJPG.sort()
    imagesPNG.sort()
    anw = input("Nuevo nombre de los archivos: ")
    for imgJ in imagesJPG:
        if imgJ.endswith('.jpeg'):
            os.rename(imgJ, anw+" ("+str(cont)+").jpeg")
        cont = cont + 1
    for imgP in imagesPNG:
        if imgP.endswith('.png'):
            os.rename(imgP, anw+" ("+str(cont)+").png")
        cont = cont + 1

#--------------------------------------------------------------------------------------------------------------------
def tamanio(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_log = int(np.log(size_bytes)/np.log(2))
    size_unit = ["B", "KB", "MB", "GB", "TB", "PB", "EB"][size_log//10]
    size_name = "{:.2f} {}".format(size_bytes / 1024 ** (size_log//10), size_unit)
    return size_name
#Borrar arch. viejos -----------------------------------------------------------------------------------------------
def borradoArch():    
    imagesPNG = np.array([file for file in os.listdir() if file.endswith('.png')])
    imagesJPG = np.array([file for file in os.listdir() if file.endswith('.jpg')])
    size_1 = 0
    size_2 = 0
    for x in imagesPNG:
        size_1 = size_1 + os.stat(x).st_size
    for y in imagesJPG :
        size_2 = size_2 + os.stat(y).st_size


    print("Tamaño total de los PNG: "+tamanio(size_1))
    print("Tamaño total de los JPG: "+tamanio(size_2))
    
    anw = input("Quieres eliminar: \n 1.- Imagenes origen (Source) \n 2.- Imagenes Nuevas \n 3.- Ninguna Opcion \n R: ")
    
    if anw == '1':
        for x in imagesJPG:
            os.remove(x)
    elif anw == '2':
        for y in imagesPNG:
            os.remove(y)
    else:
        pass
#----------------------------------------------------------------------------------------------------------------------
#Main del Programa ----------------------------------------------------------------------------------------------------
def main():
    #Variables y listas necesarias para poder trabajar
    images_JPG = np.array([file for file in os.listdir() if file.endswith('.jpg')])

    print("Archivos a modificar! :")
    print(images_JPG)

    qlt = int(input("Ingresa la calidad del 0-9: "))
    params=[cv2.IMWRITE_PNG_COMPRESSION, qlt]


    while len(images_JPG) != 0: #PNG
        dirr = str(images_JPG[0])
        images_JPG = np.delete(images_JPG , 0)
        image_name = dirr.split('.')[0]
        print(f"This is the image name: {image_name}")
        # Leer la imagen desde el disco utilizando OpenCV
        imageCV = cv2.imread(dirr, -1)
        
        cv2.imwrite(f'{image_name}.png', imageCV, params)

if __name__ == "__main__":
    inicio = time.time()
    main()
    final = time.time()
    borradoArch()
    anw = input("Quieres cambiar de nombre? : \n 1.- Si \n 2.- No \n R: ")
    if anw == '1':
        cambiarName()
    
    # Tiempo transcurrido
    print("Tiempo transcurrido:", round(final - inicio, 3))


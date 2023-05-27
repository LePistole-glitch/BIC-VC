from PIL import Image
import os, io, math
import numpy as np

#Calculo de Bytes para comprobar dif de tamaño de archivos!
"""
def tamanio(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_nombre = np.array(["B", "KB", "MB", "GB", "TB"])
    i = int(np.floor(math.log(size_bytes, 1024)))
    p = np.power(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_nombre[i])
"""
def tamanio(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_log = int(np.log(size_bytes)/np.log(2))
    size_unit = ["B", "KB", "MB", "GB", "TB", "PB", "EB"][size_log//10]
    size_name = "{:.2f} {}".format(size_bytes / 1024 ** (size_log//10), size_unit)
    return size_name

def main():
    images = np.array([])
    qlt = int(input("Calidad 1-100: "))
    #Crea el array con las img dentro
    for file in os.listdir():
        if file.endswith('jpg') or file.endswith('jpeg'): 
            images = np.append(images, file)

    while len(images) != 0:
        dirr = str(images[0])
        images = np.delete(images, 0)
        if dirr.endswith('.jpg') or file.endswith('jpeg'):
            img = Image.open(dirr)
            buffer = io.BytesIO()          #Creo una img en el buffer
            img.save(buffer, format='PNG')
            buffer.seek(0)

            img = Image.open(buffer)
            img = img.convert('RGB')
            nombre_img = dirr.split('.')[0]
            print(f"Se esta conviertirendo -> {nombre_img}")
            img.save(f"{nombre_img}.png", 'png', compress_level = qlt)

            #borramos el buffer
            buffer.seek(0)
            buffer.truncate(0)
     
#Borrar arch. viejos -----------------------------------------------------------------------------------------------
def borradoArch():    
    imagesPNG = np.array([])
    imagesJPG = np.array([])
    size_1 = 0
    size_2 = 0
    for file in os.listdir():
        if file.endswith('jpeg') or file.endswith('jpg'):
            imagesJPG = np.append(imagesJPG, file)
        elif file.endswith('png'):
            imagesPNG = np.append(imagesPNG, file)
   
    for x in imagesPNG:
        size_1 = size_1 + os.stat(x).st_size
    for y in imagesJPG :
        size_2 = size_2 + os.stat(y).st_size


    print("Tamaño total de los PNG: "+tamanio(size_1))
    print("Tamaño total de los JPG: "+tamanio(size_2))
    
    anw = input("Quieres eliminar: \n 1.- Imagenes origen (Source) \n 2.- Imagenes Nuevas \n 3.- Ninguna Opcion \n R: ")
    
    if anw == '1':
        for x in imagesPNG:
            os.remove(x)
    elif anw == '2':
        for y in imagesJPG:
            os.remove(y)
    else:
        pass
#----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------FUNCION CAMBIAR DE NOMBRE A LOS ARCHIVOS EN LA CARPETA--------------
def cambiarName():
    images = np.array([])
    cont = 1
    for file in os.listdir():
        if file.endswith('png') or file.endswith('jpg'):
            images = np.append(images, file)
    images.sort()
    anw = input("Nuevo nombre de los archivos: ")
    for img in images:
        if img.endswith('.png'):
            os.rename(img, anw+" ("+str(cont)+").png")
        if img.endswith('.jpg'):
            os.rename(img, anw+" ("+str(cont)+").jpg")

#----------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
    borradoArch()
    anw = input("Quieres cambiar de nombre? : \n 1.- Si \n 2.- No \n R: ")
    if anw == '1':
        cambiarName()
    else:
        mn = input()

import os
import numpy as np

images = np.array([])
cont = 1

for file in os.listdir():
    if file.endswith('jpg') or file.endswith('png') or file.endswith('mp4'):
        images = np.append(images, file)

print("Archivos a modificar!:")
print(images)

newNombre = input("Ingresa el nuevo nombre que quieres ponerle: ")

while len(images) != 0:
    dirr = str(images[0])
    images = np.delete(images, 0)
    #print(dirr)

    if dirr.endswith('.png'):
        os.rename(dirr, newNombre+" ("+str(cont)+").png")
    elif dirr.endswith('.jpg'):
        os.rename(dirr, newNombre+" ("+str(cont)+").jpg")
    elif dirr.endswith('.mp4'):
        os.rename(dirr, newNombre+" ("+str(cont)+").mp4")
    cont += 1

print("Eso es todo!")
print = input()




    

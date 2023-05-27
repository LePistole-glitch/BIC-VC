from PIL import Image
import numpy as np
import os, io

images_JPG = np.array([])

for file in os.listdir():
    if file.endswith('.JPG') or file.endswith('.jpg') or file.endswith('.jpeg'):
        images_JPG = np.append(images_JPG, file)

while len(images_JPG) != 0:
    dirr = str(images_JPG[0])
    images_JPG = np.delete(images_JPG,0)
    img = Image.open(dirr)
    buffer = io.BytesIO()
    img.save(buffer, format = 'JPEG')
    img = Image.open(buffer)
    nombreImg = dirr.split('.')[0]
    print(f"Se esta optimizando ---> {nombreImg}")
    img.save(f"{nombreImg}_OP.jpeg", 'jpeg', optimize = True, quality = 100, progressive = True)

    buffer.seek(0)
    buffer.truncate(0)

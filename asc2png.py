from PIL import Image
import numpy as np
import csv
import io
import time

start = time.time()

dim = 1001
bytes = []
with open('../data/old/TM1_426_106.asc', 'r') as ascfile:
    csvreader = csv.reader(ascfile, delimiter=';')

    for x in range(dim):
        row = ()
        for y in range(dim):
            xyz = next(csvreader)
            z = xyz[2]

            z = int(float(z) * 100)

            bytes.append((z >> 16) & 255)
            bytes.append((z >> 8) & 255)
            bytes.append(z & 255)

pixels = np.reshape(bytes, (dim, dim, 3))
pixels = pixels.astype(np.uint8, copy=False)

im = Image.fromarray(pixels, mode='RGB')
im.save('../demo/heights00.png', 'PNG')

end = time.time()
print(end - start)

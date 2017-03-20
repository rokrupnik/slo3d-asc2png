from PIL import Image
import numpy as np
import csv
import io
import time

start = time.time()

dim = 1000
bytes = []
with open('../data/arso/TM1_425_105.asc', 'r') as ascfile:
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
pixels = np.rot90(pixels)
pixels = pixels.astype(np.uint8, copy=False)

for i in range(10, 0, -1):
    im = Image.fromarray(pixels, mode='RGB')
    im.save('../data/' + str(i) + '/425_105.png', 'PNG')

    print(pixels.shape)
    pixels = pixels[::2, ::2]

end = time.time()
print(end - start)

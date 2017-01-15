import csv
import io
import png
import time

start = time.time()

dim = 1001
rows = []
with open('../data/TM1_426_106.asc', 'r') as ascfile:
    csvreader = csv.reader(ascfile, delimiter=';')

    for x in range(dim):
        row = ()
        for y in range(dim):
            xyz = next(csvreader)
            z = xyz[2]
            
            z = int(float(z) * 100)

            row += ((z >> 16) & 255,)
            row += ((z >> 8) & 255,)
            row += (z & 255,)

        rows.append(row)

with open('../demo/heights.png', 'wb') as pngfile:
    w = png.Writer(dim, dim, alpha=False, bitdepth=8)
    w.write(pngfile, rows)

end = time.time()
print(end - start)
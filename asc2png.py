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
            #if (y % 2 == 0):
            #    z = 524287
            #else:
            #    z = 0

            row += ((z >> 14) & 127,)
            row += ((z >> 7) & 127,)
            row += (z & 127,)
        rows.append(row)

with open('test.png', 'wb') as pngfile:
    w = png.Writer(dim, dim, alpha=False, bitdepth=7)
    w.write(pngfile, rows)

end = time.time()
print(end - start)
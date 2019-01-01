"""
this module provides a method to generate a 'smiley face'
as a two-dimension data-set to show the difference after
k-means and dbscan works
"""
import random


def gen_smile():
    data = []

    a, b, d, c = 6, 8, 4, 0.15
    C = (c - a / (b**2))

    for i in range(2100):

        x = random.random() * 20 - 10   # (-10, 10]
        y = random.random() * 20 - 10   # (-10, 10]

        v1 = 81 < x**2 + y**2 < 100     # outline
        v2 = (x+4)**2 + (y-4)**2 < 1    # left eye
        v3 = (x-4)**2 + (y-4)**2 < 1    # right eye
        v4 = -b < x < b and c*x**2 - a < y < C*x**2 - d     # mouse

        if v1 or v2 or v3 or v4:
            data.append([round(x, 2), round(y, 2)])

    src_file = open("../src/smile.txt", "w")    # while the data-file stores
    src_file.write("float,float\n")

    for item in data:
        x, y = item
        block = "{0},{1}\n".format(x, y)
        src_file.write(block)

    src_file.close()


if __name__ == '__main__':
    gen_smile()

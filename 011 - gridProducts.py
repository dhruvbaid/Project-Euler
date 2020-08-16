"""
Largest Grid Product: What is the greatest product of four adjacent numbers in
the same direction (up, down, left, right, or diagonally) in the 20×20 grid?
"""

def products(w, h, matrix, size):
        # p will contain all the products
        p = []

        # vertical down/up
        for c in range(w):
                for r in range(h - size + 1):
                        prod = 1;
                        for x in range(size):
                                prod *= matrix[r + x][c];
                        p.append(prod);

        # horizontal left/right
        for r in range(h):
                for c in range(w - size + 1):
                        prod = 1;
                        for x in range(size):
                                prod *= matrix[r][c + x];
                        p.append(prod);

        # diagonal down right/up left
        for c in range(w - size + 1):
                for r in range(h - size + 1):
                        prod = 1;
                        for x in range(size):
                                prod *= matrix[r + x][c + x];
                        p.append(prod);

        # diagonal down left/up right
        for c in range(size - 1, w):
                for r in range(h - size + 1):
                        prod = 1;
                        for x in range(size):
                                prod *= matrix[r + x][c - x];
                        p.append(prod);

        # return largest element in p
        p.sort()
        return p[-1]

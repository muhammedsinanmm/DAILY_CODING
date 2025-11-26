def bruce(li):
    # 1. square the numbers
    squares = [x*x for x in li]

    # 2. compute popcount (number of 1s in binary)
    pairs = []
    for v in squares:
        c = bin(v).count("1")
        pairs.append((v, c))

    # 3. find X: max set bits, tie → smaller value
    # sort by (-setbits, value) so highest count comes first
    X = sorted(pairs, key=lambda t: (-t[1], t[0]))[0][0]

    # 4. find Y: min set bits, tie → smaller value
    Y = sorted(pairs, key=lambda t: (t[1], t[0]))[0][0]

    # 5. product
    P = X * Y

    # 6. nearest power of two ≥ P
    if P <= 1:
        return 1
    if (P & (P - 1)) == 0:   # already power of 2
        return P
    return 1 << (P.bit_length())   # next power of 2
    # here 1<< (p.bit_length()) works similar to 2**(p.bit_length()) !!


li = [2,3,4]
print(bruce(li))
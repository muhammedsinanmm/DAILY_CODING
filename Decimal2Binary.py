def inbuildConverter(number):
    return bin(number)[2:]

def manualConverter(num):
    s= ""
    while num > 0:
        s+= str(num & 1)
        num = num>>1
    return s[::-1]


n = int(input("Enter any number to convert to its binary: "))
binary = inbuildConverter(n)
print(f"The binary representaion of {n} is {binary}")
print()
binary2 = manualConverter(n)
print(f"The binary representaion of {n} is {binary2}")
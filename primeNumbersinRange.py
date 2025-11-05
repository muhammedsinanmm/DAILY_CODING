def prime(number):
    if(number==1):
        return False
    i = 2
    while i*i <= number:
        if number%i == 0:
            return False
        i+=1
    return True
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
total = 0
for i in range(start,end+1):
    if prime(i):
        total+=i
print(f"The sum of prime numbers from {start} to {end} is {total}")

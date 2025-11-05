def prime(number):
    i = 2
    while i<=number//2:
        if number%i == 0:
            return False
        i+=1
    return True
start = int(input("Enter the starting value: "))
end = int(input("Enter the ending value: "))
sum = 0
for i in range(start,end+1):
    if prime(i):
        sum+=i
print(f"The sum of prime numbers from {start} to {end} is {sum}")

string = input("Enter any string you need to compress: ")

preCh = string[0]
li = [string[0]]
count = 0
for ch in string:
    if ch == preCh:
        count += 1
    else:
        preCh = ch
        li.append(str(count))
        li.append(ch)
        count = 1
        
li.append(str(count))

print("".join(li))
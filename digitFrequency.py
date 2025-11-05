dic = {}
for i in range(10):
    ch = str(i)
    dic[ch] = 0
#input
s = input("Enter a string to compute: ")
for ch in s:
    if ch.isdigit():
        dic[ch] += 1
        
for ch in dic:
    print (ch,":",dic[ch])
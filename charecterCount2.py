string = input("Enter a string to find the number of repeating charecters:")
dic = {}
for ch in string:
    if ch != " ":
        dic[ch] = dic.get(ch, 0)+1
maxVal = 0
for ch,count in dic.items():
    if count > maxVal:
        freqCh = ch
        maxVal = count
print(f" The most frequent charecter is {freqCh}")
    
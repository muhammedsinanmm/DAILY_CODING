string = input("Enter a string to find the number of repeating charecters:").upper()
dic = {}
for ch in string:
    if ch != " ":
        dic[ch] = dic.get(ch, 0)+1

for ch in dic:
    if dic[ch]>1 :
        print(f"{ch}  is used {dic[ch]} times in the string")
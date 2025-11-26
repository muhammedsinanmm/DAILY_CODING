def bruse(li):
    sq = square(li) #list
    bitDic = setbit(sq) #hashmap/dictionary
    maxNum = maxNum(bitDic)
    minNum = minNum(bitDic)
    product = maxNum * minNum
    res = sqrt(product) #ceil the root to the next number
    return res**2
    
def square(li):
    for i in range(len(li)):
        li[i] = li[i]**2
    return li

def setbit(sq):
    bitDic = {}
    for num in sq:
        bitDic[num] = bin(num)[:2]
    return bitDic

def maxNum(bitDic):
    sortedDic = sorted(bitDic, reverse = True, key = lambda x: bitDic[x])    
    for num, val in bitDic.items():
        maxx = num
        #i dont get the balance logic for here, help !
        
def minNUm(bitDic):
    #the same logic like maxNUm but im stuck in max num right, so stuck here too, no need to teach this only max num logic is enough for me to understand and apply the same logic here,
    
def sqrt(product):
    #how to find the square root, any manual coding technique other than inbuild function, if any teach me that too along with the manual way



li = [2,3,4]
print(bruse(li))
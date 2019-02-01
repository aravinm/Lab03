def letterieCu(str):return varrr(str)

def doublerieCu(str1, str2): return varrr(str1, str2)
def varrr(*str):
    length =  "".join(str)
    # print length
    dd = dict.fromkeys(length, 0)

    for i in length:
        dd[i] +=1
    return dd
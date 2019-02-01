
def addit(x,y):
    return x + y

def subtra(x,y):
    return x - y

def evenNo(x):

    count = 0
    for i in x:
        if int (i)% 2 == 0:
            count+=1
    return count

def maxxx(x):

   return max(x)


def minn(x):
    return min(x)

def absolute(x):
    return abs(x)


def sumT(x):

    count = 0
    for i in x:
        count = i + count
    return count


def clear(x):
    if minn(x) < 5:
        for index, p in enumerate(x):
            x[index]=0
        return x
    else:
        return x


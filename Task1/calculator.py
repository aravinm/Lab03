import sys
from myMath import *

a = " "

try:
    a = str(sys.argv[1])

except:
    print("Your input is incorrect!")

Listie = a.split(",")
newListie = []
# print newListie


for i in Listie:
    newListie.append(int(i))

print "The difference is:" + str(subtra(maxxx(newListie), minn(newListie))) + " The summation is:" + str(
    addit(maxxx(newListie), minn(newListie))) + " The summation of all input is:" + str(
    sumT(newListie)) + " The number of even numbers is:" + str(evenNo(newListie)) + " The values in the list are:" + str(clear(newListie))

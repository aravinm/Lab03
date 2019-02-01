import sys
import letterCount


sortieT = letterCount.varrr(*sys.argv[1].split(","))

# print sortieT
for key, val in sorted(sortieT.items(), reverse=True):
    print("{}:{}".format(key,val)),
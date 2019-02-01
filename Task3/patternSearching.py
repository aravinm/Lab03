import sys


inputA = ""
inputB = ""


try:

    inputA = str(sys.argv[1])
    # getting user input for the first argument
    inputB = str(sys.argv[2])

    #getting user input for the second argument

except:

    print "Your input is invalid!"

count123 = 0

for indexatt in range (len(inputA)):
    if str(inputB) in str(inputA[indexatt:(indexatt) + len(inputB)]):
        count123 = count123 + 1
print "Pattern appears " + str(count123) + " time!"


# loop through the the input which are being givem, firstly get input A, then use input A to compare with
# input b if it matches then count and and hence that will tell how many time that particular pattern appears


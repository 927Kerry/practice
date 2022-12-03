import random

listA = []
listB = []

def makeList():    
    indexNumber = random.randint(4, 12)
    i = 0
    while i < indexNumber:
        floatNum = random.uniform(1, 1.5)
        roundedNum = round((floatNum),2)
        if roundedNum not in listA:
            listA.append(roundedNum)
            i += 1


    print(f"The generated list: \n{listA}")
    listB = sorted(listA)
    print(f"The sorted generated list: \n{listB}")
    # totalSum = round(sum(listB),4)
    # print(f"The sum of all values in the list is: \n{totalSum}")
    

    sumoflist = 0
    #y = listB[0]
    for x in listB:
        sumoflist += x
    print(sumoflist)




makeList()
# floatingNumber = random.uniform(1, 5)
# print(f"a: {floatingNumber}")

# x = round((floatingNumber), 2)


# print(floatingNumber)
# print(x)
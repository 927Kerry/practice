# #function that takes an integer as an input and returns a list of the multiples of 2 that returns up to the integer


# list = []

# def num(n):
#     for i in range(1, n):
#         #print(i)
#         i *= 2
#         list.append(i)
#     print(list)
    

# num(10)




# list = []   

# def num(n):
#     for i in range(n):
#         if i % 2 == 0:
#             # print(i)
#             list.append(i)
#     print(list)

# num(100)
# 
import random


def main():
    
    #listA = [2, 4, 6, 8, 10, 13, 15, 17, 19]
    randomList = []


    # def runThrice():
    #     for _ in range(3):
    #         randList()


    #create list of random numbers 
    # def randList():
    #     listLenEnd = 16
    #     i = 0
    #     n = random.randint(6, listLenEnd)

    #     while i < n:
    #         r = random.randint(1, 20)
    #         randomList.append(r)
    #         i+=1

    #         ##for a list with no duplicate elements
    #         # while r not in randomList:            
    #         #     randomList.append(r)
    #         #     i+=1
    #         # else:
    #         #     r = random.randint(1, 20)
            
    #     print(f"Our randomly generated list is: \n{randomList}")
    #     sortedList = sorted(randomList)
    #     #print(f"Our randomly generated sorted list is: \n{sortedList}")


    def smallRandList():
        listlenEnd = 8
        i = 0
        n = 4 #random.randint(4, listlenEnd)

        while i < n:
            r = random.randint(0, 2)
            randomList.append(r)
            i+=1

            #for a list with no duplicate elements 
            # while r not in randomList:            
            #     randomList.append(r)
            #     i+=1
            # else:
            #     r = random.randint(1, 20)
            
        print(f"Randomly generated small list is: \n{randomList}")
        sortedSmallList = sorted(randomList)
        #print(f"Our randomly generated sorted list is: \n{sortedList}")
    

    #function that checks for palindrome, even odd divided by 2
    def palindrome():
        listPalA = []
        listPalB = []
        #check if length of the list is odd or even 
        if len(randomList) % 2 == 0: #for even lengthed list
            listLength = len(randomList)
            halfListLength = listLength // 2
            #print(f"List Length is: {listLength}")
            #print(f"Half of the list length is: {halfListLength}")

            listPalA = randomList[:halfListLength]
            listPalB = randomList[halfListLength:]
            
            if listPalA == listPalB.reverse():
                #print(f"{randomList} is palindrome")
                return True
            else: 
                #print(f"{randomList} is not palindrome")
                return False


            # x = 0
            # for x in randomList:
            #     # if x < halfListLength:
            #     #     listPalA.append(x)
            #     #     x += 1
                
            #     # else:
            #     #     listPalB.append(x)
            #     #     x += 1

            #print(listPalA)
            #print(listPalB)
            
            
        #else:
            #print("lol")

        #if listPalA == listPalB


    def cycle():
        a = 0
        while palindrome == True:
            smallRandList()
            palindrome()
            a += 1

        print(f"{a} lists have been generated for palindrome to occur")



    #return elements on odd positions/index's of the list 

    #write a function that checks whether an element occurs in the list



    def checkForElement():
        elementA = random.randint(1,20)
        if elementA in randomList:
            print(f"Our randomly generated number {elementA} is in the list.")
        else:
            print(f"The randomly generated number {elementA} is not in the list")
            #dont print this if it random element was found in the list
    

    def listInfo():
        listLength = len(randomList)
        listSum = sum(randomList)
        listHighest = max(randomList)
        listLowest = min(randomList)
        print(f"This list is {listLength} digits long, total sum of {listSum} and its highest value of {listHighest} and lowest value of {listLowest}")        


    def biggestNumber():
        largestNumber = randomList[0]
        for number in randomList:
            print(f"{number} and {largestNumber}")
            if number >= largestNumber:
                number = largestNumber
        print(f"largest number is {largestNumber}")


    def smallestNumber():
        smallestNumber = randomList[0]
        for number in randomList:
            #print(number)
            if smallestNumber > number:
                smallestNumber = number
        print(f"smallest number is {number}")


    def evenOdd():
        evenList = []
        oddList = []
        for i in randomList:
            if i % 2 == 0: 
                evenList.append(i)
            else:
                oddList.append(i)
        print(f"Our list split into odd and even \nEven: {evenList} \nOdd: {oddList}")
        print(sorted(evenList))
        print(sorted(oddList))
    




    smallRandList()
    cycle()
    #palindrome()
    #randList()
    #checkForElement()
    # listInfo()
    # evenOdd()
    #biggestNumber()
    #smallestNumber()

if __name__ == "__main__":
    main()
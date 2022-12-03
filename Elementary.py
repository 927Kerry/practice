#Program that asks for input number n and prints up to n 


# def counting():
#     number = int(input("Give number for n: "))
#     emptyList = []
#     for i in range(1, number+1):
#         #print(i)
#         if i % 3 == 0:
#             emptyList.append(i)

#     print(emptyList)
#     print(sum(emptyList))


# counting()


# Write a program that prints a multiplication table for numbers up to 12
# def timesTables():
#     i = float(input("Which multiplation would you like to know:"))
#     x = 1
#     while x < 12:
#         answer = round((i*x))
#         print(f"{i} multiplied by {x} is {answer}")
#         x += 1


# timesTables()

#Write a program that prints all prime numbers, 
#Prime numbers can only be divided by 1 and itself 

# def is_prime():
#     for i in range(1000):
#         if ()

#Write a program that prints the next 20 leap years
nextLeapYears = []

def leapYear():
    year = 2022
    while len(nextLeapYears) < 20:
        #print("hello")
        if year % 4 == 0:
            #print("hello")
            nextLeapYears.append(year)
            year += 1
        else:
            year += 1
            # listlen = len(leap)
            # print(listlen)
    print(f"These are leap years: \n{nextLeapYears}")

leapYear()





# Question:1 Calculate the factorial of a number

'''def fact(x):
    if x == 0:
        return 1
    elif x > 0:
        return x * fact(x - 1)


x = int(input("Enter Number:"))
print(fact(x))'''


# Question:2 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

'''def func():
    upper = 0
    lower = 0
    x = input("Enter:")
    for i in x:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print(upper)
    print(lower)


func()'''

#Question:3 Write a Python function to print the even numbers from a given list.

'''def func():
    L=[1,3,4,5,6,7,8,9,0]
    for i in L:
        if i%2==0:
            print(i,end=" ")

func()'''

#Question:4 Write a Python function that checks whether a passed string is palindrome or not.

'''def Pali(string):
    left = 0
    right = len(string) - 1

    while right >= left:
        if not string[left] == string[right]:
            return False
        left += 1
        right -= 1
    return True

string=input("Enter:")
print(Pali(string))'''

#Question:5 Write a Python function that takes a number as a parameter and check the number is prime or not.

'''def prime():
    x=int(input("Enter Num:"))
    if x==1:
        print(x,"is not prime")
    if x==2:
        print(x,"is prime")
    for i in range(2, x):
        if x % i == 0:
            print(x,"is not prime")
            break
        else:
            print(x,"is prime")

prime()'''

#Question: 6 Suppose a customer is shopping in a market and you need to print all the items which user bought from market.
#Write a function which accepts the multiple arguments of user shopping list and print all the items which user bought from market.

'''def func():
    L=[]
    x=int(input("Enter No of items:"))
    for items in range(0,x):
        items=input("Enter Items:")
        L.append(items)
    print(L)
func()'''



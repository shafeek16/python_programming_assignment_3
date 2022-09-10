#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?


number = float(input("Enter a number: "))

if number >= 0:
    if number == 0:
        print("Given number is 'ZERO'")
    else:
        print("Given number is 'POSITIVE'")
else:
    print("Given number is 'NEGATIVE'")


#2. Write a Python Program to Check if a Number is Odd or Even?

number = float(input("Enter a number: "))

if  (number % 2) == 0:
    print('%0.2f is even number'%(number))
else:
    print('%0.2f is odd number' %(number))


#3. Write a Python Program to Check Leap Year?

year = int(input("Enter the year: "))

if  (year % 4) == 0:
    print('%0.f is a leap year'%(year))
else:
    print('%0.f is not a leap year' %(year))

#4. Write a Python Program to Check Prime Number?

number = int(input("Enter a number: "))

if number > 1:
   for i in range(2,number):
       if (number % i) == 0:
           print(number,"is not a prime number")
           break
   else:
       print(number,"is a prime number")
else:
   print(number,"is not a prime number")


#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

print("Prime numbers between 1 to 10000 are:")

for number in range(1, 10000 + 1):
    if number > 1:
       for i in range(2, number):
           if (number % i) == 0:
               break
       else:
           print(number)
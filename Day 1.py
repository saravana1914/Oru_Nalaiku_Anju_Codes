#Check wheather a number is Positive or Negative number 
num = int(input())
if num > 0:
    print(num, "is a positive number")
if num < 0:
    print(num, "is a negative number")
else:
    print("Zero da athu")


#check wheather a number is even or odd
num = int(input())
if num%2 == 0:
    print(num, "is a even number")
else:
    print(num, "is a even number")

#Sum of N natural numbers
num = int(input())
Tot = 0
for i in range (num+1):
    Tot += i
print(Tot)

#Sum of natural numbers in given range
start, end = map(int,input().split())
Tot = 0
for i in range (start,end+1):
    Tot += i
print(Tot)

#Greatest of two numbers
num1, num2 = map(int,input().split())
if num1 > num2:
    print(num1, "is greater")
if num2 > num1:
    print(num2, "is greater")
else:
    print("Rendumey equal nga")

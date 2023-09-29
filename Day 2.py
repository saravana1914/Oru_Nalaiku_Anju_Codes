# largest of three numbers
num1, num2, num3 = map(int, input().split())
temp = 0
if num1 >= num2 and num1 >= num3:
    print(num1, "is the largest number")
elif num2 >= num1 and num2 >= num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest")

#Leap year finder
year = int(input())
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#Prime number indicator
n = int(input("Enter the number: "))
for i in range (2,n):
       if n%i == 0:
              print("Not a prime number")
              break
       else:
              print(n, "is a prime number")
              break

#print prime numbers within a range
s,e = map(int, input().split())
pri_numb =[]
for i in range (s,e+1):
       f =0 
       if i == 2:
              pri_numb.append(2)
              continue
       for j in range (2, i):
              if i%j== 0:
                     f = 1
                     break
              if f == 0:
                    pri_numb.append(i)
                    break
print(pri_numb)

#sum of digits of a number
num = input()
sum= 0
def findSum(num, sum):
    if num == 0:
        return sum

    digit = int(num % 10)
    sum += digit
    return findSum(num / 10, sum)
print(findSum(num, sum))
    

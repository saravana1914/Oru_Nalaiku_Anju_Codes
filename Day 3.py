#To reverse a number 
Number= int(input())
reverse =0
while Number >0:
    rem = Number%10
    reverse =(reverse*10)+rem
    Number= Number//10
print(reverse)



#Palindrom finder
Number = int(input())
N= Number
reverse =0
while N >0:
    rem = N%10
    reverse =(reverse*10)+rem
    N= N//10
print("Reversed Number = ",reverse)
if Number == reverse:
    print("The Number", Number, "is a Palindrom!!")
else:
    print(Number, "Not a Palindrom")
    
    
    
#Amstrong number finder
def amstrong(Number):
    N = Number
    s = str(N)
    AmsN = 0
    while N >0:
        rem = N%10
        AmsN += rem**int(s(len(s)))
        N = N//10
    if Number==AmsN:
        print("The given number",Number,"is an Amstrong Number")
    else:
        print("This is not an Amstrong number")
amstrong(371)



#Amstrong number finder in a given range
def amstrong(Number):
    N = Number
    s = str(N)
    AmsN = 0
    while N >0:
        rem = N%10
        AmsN += rem**int(len(s))
        N = N//10
    if Number==AmsN:
        return 1
    else:
        return 0

AmsN_list = []
start, end = map(int,input().split())
for i in range (start, end+1):
    if amstrong(i) == 1:
        AmsN_list.append(i)
print(AmsN_list)



#Fiboncci Series upto nth term
n = int(input())
temp = 0
n1 = 0
n2 = 1
print(n1,n2, end=" ")
for i in range (2,n):
    temp = n1+n2
    n1 = n2
    n2 = temp
    
    print(temp,end=" ")
    
    
    
    
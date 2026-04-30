#print numbers from 1 to n
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    print(i,end=" ")'''

#Print Numbers from m to n
'''m=int(input("enter the value of m:"))
n=int(input("enetr the value if n:"))
for i in range(m,n+1):
    print(i,end=" ")'''


#Print Numbers from n to 1 in Reverse
'''n=int(input("enter the value of n:"))
for i in range(n,0,-1):
    print(i,end=" ")'''


#Print Numbers from n to m in Reverse
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
for i in range(n,m-1,-1):
    print(i,end=" ")'''

#Sum of n Natural Numbers
'''n=int(input("enter n values:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("sum of n numbers:",sum)'''


#Factorial of a Number
'''num=int(input("enter value of num:"))
fact=1
for i in range(num,0,-1):
    fact*=i
print("Factorial of number is:",fact)'''


#Sum of m to n Numbers
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
sum=0
for i in range(m,n+1):
    sum+=i
print("sum of numbers from m to n is:",sum)'''


#Product of m to n Numbers
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
prod=1
for i in range(m,n+1):
    prod*=i
print("product of numbers from m to n is:",prod)'''


#Print Factors of a Number
'''n=int(input("enter a value of n:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)'''

#Count of Factors
'''n=int(input("enter a value of n:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
print(count)'''



#prime Number Check
'''num=int(input("enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
if count==2:
    print("prime number")
else:
    print("not a prime number")'''


#Even Numbers from m to n
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
count=0
for i in range(m,n+1):
    if i%2==0:
        count+=1
        print(i)
print("total even numbers between m and n:",count)'''


#Odd Numbers from m to n
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
count=0
for i in range(m,n+1):
    if i%2!=0:
        count+=1
        print(i)
print("total odd numbers between m and n:",count)'''


#Count of Even and Odd Numbers
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
even=0
odd=0
for i in range(m,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even numbers:",even )
print("odd numbers:",odd)'''


#Reverse a string
'''str=input("enter a string:")
print(str[::-1])'''

#Check for Palindrome String
'''str=input("enter a string:")
reverse=str[::-1]
if str==reverse:
    print("palindrome")
else:
    print("not palindrome")'''


#Sum of Digits
'''num=int(input("enter a nuumber:"))
sum=0
while num>0:
    digits=num%10
    sum+=digits
    num=num//10
print(sum)'''


#Product of Digits
'''num=int(input("enter a nuumber:"))
prod=1
while num>0:
    digits=num%10
    prod*=digits
    num=num//10
print(prod)'''


#19. Armstrong Number Check
'''num=int(input("enter the value of n:"))
sum=0
for i in str(num):
    sum+=int(i)**len(str(num))
if sum==num:
    print("It is Armstrongg number")
else:
    print("It is not a armstrong number")'''


#20. Reverse a Number with loops and modulus
'''num=int(input("enter a number:"))
reverse=str()
while num>0:
    digits=num%10
    reverse+=str(digits)
    num=num//10
print(reverse)'''


#21. Palindrome Number Check
'''num=int(input("enter a number:"))
original=num
reverse=0
while num>0:
    digits=num%10
    reverse=reverse*10 + digits
    num=num//10
if reverse==original:
    print("It is palindrome number")
else:
    print("Not a palindrome number")'''


#22. Count Vowels in String
'''string=input("enter a string:")
vowels=["a","e","i","o","u"]
count=0
for i in string:
    if i in vowels:
        count+=1
print(count)'''


#23.Count Consonants in String
'''string=input("enter a string:")
vowels=["a","e","i","o","u"]
count=0
for i in string:
    if i  not in vowels:
        count+=1
print(count)'''


#24. Count Vowels and Consonants
'''string=input("enter a string:")
v=["a","e","i","o","u"]
vowels=0
consonants=0
for i in string:
    if i in v:
        vowels+=1
    else:
        consonants+=1
print("vowels count:",vowels)
print("consonants count:",consonants)'''


#25. Perfect Number Check
'''num=int(input("enter a number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("perfect number")
else:
    print("not perfect number")'''


#26. Neon Number Check
'''num=int(input("enter a number:"))
square=num*num
sum=0
while square>0:
    digits=square%10
    sum+=digits
    square=square//10
if sum==num:
    print("neon number")
else:
    print("not a neon number")'''


#27. Strong Number Check
'''num = int(input("Enter a number: "))
temp = num
sum_fact = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    
    sum_fact += fact
    temp //= 10

if sum_fact == num:
    print("Strong Number")
else:
    print("Not a Strong Number")'''


#28. Harshad Number Check
'''num=int(input("enter a number:"))
temp=num
sum=0
while temp>0:
    digits=temp%10
    sum+=digits
    temp //= 10
if num%sum==0:
    print("harshad number")
else:
    print("not harshad number")'''


#29. Fibonacci Series
n = int(input("Enter number of terms: "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1



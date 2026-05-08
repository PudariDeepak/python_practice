#1.Print All Prime Numbers from m to n
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
for num  in range(m,n+1):
    if num>1:
        for i in range(2,int(num*0.5)+1):
           if  num%i==0:
            break
        else:
           print(num,end=" ")'''
        


#2.Count of All Prime Numbers from m to n
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
count=0
for num in range(m,n+1):
    if num>1:
        for i in range(2,int(num*0.5)+1):
            if num % i==0:
                break
        else:
            count+=1
print(count)'''


#3.Print All Armstrong Numbers in a Range
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))

for num in range(m,n+1):
    prod=0
    for i in str(num):
        prod+=int(i)**len(str(num))
    if prod==num:
        print(num,end=" ")'''



#4.First Prime Number from m to n
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
for num in range(m,n+1):
    if num>1:
        for i in range(2,int(num*0.5)+1):
            if num % i ==0:
                break
        else:
            print(num)
            break'''


#5.Last Prime Number from m to n
'''m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
for num in range(n,m,-1):
    if num>1:
        for i in range(2,int(num*0.5)+1):
            if num % i==0:
                break
        else:
            print(num)
            break'''


#6.. First Vowel in a Name
'''name=input("enter the name:")
vowels="aeiouAEIOU"
for i in name:
    if i in vowels:
        print(i)
        break'''


#7.Last Vowel in a Name
'''name=input("enter the name:")
vowels="aeiouAEIOU"
for i in name[::-1]:
    if i in vowels:
        print(i)
        break'''


#8.Print All Even Numbers Using Continue
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    if i%2!=0:
        continue
    print(i,end=" ")'''

#9.Print All Odd Numbers Using Continue
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    if i%2==0:
        continue
    print(i,end=" ")'''



#10.Count of Prime and Composite Numbers from m to n
m=int(input("enter the value of m:"))
n=int(input("enter the value of n:"))
prime_count=0
composite_count=0
for num in range(m,n+1):
    if num>1:
        for i in range(2,int(num*0.5)+1):
            if num%i==0:
                composite_count+=1
                break
        else:
            prime_count+=1
print(prime_count)
print(composite_count)
 


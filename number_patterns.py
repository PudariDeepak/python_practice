#1.Increasing Number Triangle
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    patt=""
    for j in range(1,i+1):
        patt+=str(j)+" "
    print(patt)'''

#2.Repeating Row Number Triangle
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    pat=""
    for j in range(1,i+1):
        pat+=str(i)+" "
    print(pat)'''




#3.Continuous Number Triangle
'''n=int(input("enter the value of n:"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()'''

#4.Reverse Row Number Triangle
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    patt=""
    for j in range(1,i+1):
        patt+=str(i-j+1)+" "
    print(patt)'''

#5.Inverted Number Triangle
n=int(input("enter the value of n:"))
for i in range(n,0,-1):
    patt=""
    for j in range(1,i+1):
        patt+=str(i-j+1)+" "
    print(patt)


#6.Right-Aligned Number Triangle
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    star=""
    for k in range(1,i+1):
        star+=str(k)+" "
    print(space+star)'''

#7.Pyramid Number Pattern
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    star=""
    for k in range(1,i+1):
        star+=str(k)+" "
    for m in range(1,i):
        star+=str(i-m)+" "
    print(space+star)'''


#8.Even Number Triangle
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,i+1):
        star+=str(j*2)+" "
    print(star)'''


#9.Odd Number Triangle     
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,i+1):
        star+=str(j*2-1)+" "
    print(star)'''
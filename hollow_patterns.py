#1.Hollow Square Pattern
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,n+1):
        if i==1 or i==n:
            star+="* "
        elif j==1 or j==n:
            star+="* "
        else:
            star+="  "
    print(star)'''


#2.Hollow Rectangle Pattern
'''m=int(input("enetr the value of m:"))
n=int(input("enter the value of n:"))
for i in range(1,m+1):
    star=""
    for j in range(1,n+1):
        if i==1 or i==m:
            star+="* "
        elif j==1 or j==n:
            star+="* "
        else:
            star+="  "
    print(star)'''


#3.Hollow Right-Angled Triangle (Left-Aligned)
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,i+1):
        if i==1 or i==n:
            star+="* "
        elif j==1 or j==i:
            star+="* "
        else:
            star+="  "

    print(star)'''


#4.Hollow Right-Angled Triangle (Right-Aligned)
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    star=""
    for k in range(1,i+1):
        if i==1 or i==n:
            star+="* "
        elif k==1 or k==i:
            star+="* "
        else:
            star+="  "
    print(space+star)'''


#5.Hollow Inverted Triangle (Left-Aligned)
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,n-i+2):
        if i==1 or i==n:
            star+="* "
        elif j==1 or j==n-i+1:
            star+="* "
        else:
            star+="  "
    print(star)'''


#6.Hollow Inverted Triangle (Right-Aligned)
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,i):
        space+="  "
    star=""
    for k in range(1,n-i+2):
        if i==1 or i==n:
            star+="* "
        elif k==1 or k==n-i+1:
            star+="* "
        else:
            star+="  "
    print(space+star)'''


#7.Hollow Pyramid Pattern
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    star=""
    for k in range(1,i*2):
        if i==1 or i==n:
            star+="* "
        elif k==1 or k==i*2-1:
            star+="* "
        else:
            star+="  "
    print(space+star)'''


#8.Hollow Diamond Pattern
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    star=""
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            star+="* "
        else:
            star+="  "
    print(space+star)
for i in range(n-1,0,-1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    star=""
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            star+="* "
        else:
            star+="  "
    print(space+star)'''


#9.Hollow Butterfly Pattern
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    for j in range(1,2*n+1):
        if j==1 or j==i or j==2*n or j==2*n-i+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,2*n+1):
        if j==1 or j==i or j==2*n or j==2*n-i+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''


#10.Hollow Hourglass Pattern
n=int(input("enter the value of n:"))
for i in range(1,n):
    star=""
    for j in range(1,n+1):
        print()
    print(star)
      

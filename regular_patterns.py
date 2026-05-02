#1.Solid Square Pattern
'''n=int(input("enter a value of n:"))
for i in range(1,n+1):
    stars=""
    for j in range(1,n+1):
        stars+="* "
    print(stars)'''

#2.	Solid Rectangle Pattern
'''m=int(input("enter a value of m:"))
n=int(input("enter a value of n:"))
for m in range(1,m+1):
    stars=""
    for n in range(1,n+1):
        stars+="* "
    print(stars)'''


#3.	Right-Angled Triangle (Left-Aligned)
'''n=int(input("enter a value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,i+1):
        star+="* "
    print(star)'''


#4.	Right-Angled Triangle (Right-Aligned)
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    stars=""
    for k in range(1,i+1):
        stars+="* "
    print(space+stars)'''

#5.	Inverted Triangle (Left-Aligned)
'''n=int(input("enter a value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,n-i+2):
        star+="* "
    print(star)'''

#6.	Inverted Triangle (Right-Aligned)
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,i):
        space+="  "
    stars=""
    for k in range(1,n-i+2):
        stars+="* "
    print(space+stars)'''


#7.	Centered Pyramid Pattern
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    star=""
    for k in range(1,i*2):
        star+="* "
    print(space+star)'''


#8.	Diamond Pattern
'''n=int(input("enter a value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    stars=""
    for k in range(1,i*2):
        stars+="* "
    print(space+stars)
for i in range(n-1,0,-1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    stars=""
    for k in range(1,i*2):
        stars+="* "
    print(space+stars)'''


#9.	Butterfly Pattern  
'''n = 4
# Upper half
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(1, 2 * (n - i)+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print()
# Lower half
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(1, 2 * (n - i) + 1):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()'''


#10.Left-Aligned Half Diamond
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    star=""
    for  j in range(1,i+1):
        star+="* "
    print(star)
for i in range(n-1,0,-1):
    star=""
    for  j in range(1,i+1):
        star+="* "
    print(star)'''


#11.Right-Aligned Half Diamond
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    stars=""
    for j in range(1,i+1):
        stars+="* "
    print(space+stars)
for i in range(n-1,0,-1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    stars=""
    for j in range(1,i+1):
        stars+="* "
    print(space+stars)'''


#12.Sandglass Pattern
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,i):
        space+="  "
    star=""
    for j in range(1,n-i+2):
        star+="* "
    print(space+star)
for i in range(n-1,0,-1):
    space=""
    for j in range(1,i):
        space+="  "
    star=""
    for j in range(1,n-i+2):
        star+="* "
    print(space+star)'''


#13.Increasing Width Triangle
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,i+1):
        star+="* "
    print(star)'''


#14.Decreasing Width Triangle
'''n=int(input("enter the value of n:"))
for i in range(1,n+1):
    star=""
    for j in range(1,n-i+2):
        star+="* "
    print(star)'''


#15.Right-Aligned Hill Pattern
n=int(input("enter the value of n:"))
for i in range(1,n+1):
    space=""
    for j in range(1,n-i+1):
        space+="  "
    star=""
    for j in range(1,i+1):
        star+="* "
    print(space+star)
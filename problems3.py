#checking the number is even or odd
'''num=int(input("enter a number:"))
if num%2==0:
    print("even number")
else:
    print("odd number")'''

#divisible ny 5 but not by 10
'''num=int(input("enter a number:"))
if num%5==0 and num%10!=0:
    print("satisfy")
else:
    print("unsatisfy")'''


#biggest among two numbers
'''num1=int(input("enter a number1:"))
num2=int(input("enter a number2:"))
if num1>num2:
    print("num1 is biggest")
else:
    print("num2 is biggest")'''


#smallest among two numbers
'''num1=int(input("enter a number1:"))
num2=int(input("enter a number2:"))
if num1<num2:
    print("num1 is smallest")
else:
    print("num2 is smallest")'''

#divisible by 2,3 and 6
'''num=int(input("enter a number:"))
if num%2==0 and num%3==0 and num%6==0:
    print("satisfy")
else:
    print("unsatisfy")'''

#voting eligibility
'''age=int(input("enter the age of person:"))
if age>=18:
    print("he is eligible for vote")
else:
    print("not eligible for vote")'''

#student pass or fail Based on All Subjects >= 35
'''maths=int(input("enter the maths marks:"))
physics=int(input("enetr the physics marks:"))
chemistry=int(input("enter the chemistry marks:"))
if maths>=35 and physics>=35 and chemistry>=35:
    print("the student is pass")
else:
    print("the student is fail")'''
    

#Student Pass if Passed Any One Subject (>= 35)
'''maths=int(input("enter the maths marks:"))
physics=int(input("enetr the physics marks:"))
chemistry=int(input("enter the chemistry marks:"))
if maths>=35 or physics>=35 or chemistry>=35:
    print("the student is pass")
else:
    print("the student is fail")'''
            
#Student Pass if Passed Any Two Subjects
'''maths=int(input("enter the maths marks:"))
physics=int(input("enetr the physics marks:"))
chemistry=int(input("enter the chemistry marks:"))
count=0
if maths>=35:
    count+=1
if physics>=35:
    count+=1
if chemistry>=35:
    count+=1

if count>=2:
    print("student passed witth two subjects")
else:
    print("fail")'''


#Biggest Among Three Numbers
'''num1=int(input("enter a num1:"))
num2=int(input("enter a num2:"))
num3=int(input("enter a num3:"))
if num1>num2 and num1>num3:
    print("num1 is biggest")
elif num2>num1 and num2>num3:
    print("num2 is biggest")
else:
    print("num3 is biggest")'''

#Smallest Among Three Numbers
'''num1=int(input("enter a num1:"))
num2=int(input("enter a num2:"))
num3=int(input("enter a num3:"))
if num1<num2 and num1<num3:
    print("num1 is smallest")
elif num2<num1 and num2<num3:
    print("num2 is smallest")
else:
    print("num3 is smallest")'''


#Perfect Square or Not
'''num = int(input("Enter a number: "))

i = 1
while i * i <= num:
    if i * i == num:
        print("Perfect Square")
        break
    i += 1
else:
    print("Not a Perfect Square")'''


#Cars Required for Members (Max 5 per car)
'''people=int(input("enter the no.of members:"))
cars=people//5
if people%5 !=0:
    cars+=1
print(cars)'''


#Second Biggest Among Three Numbers
'''num1=int(input("enter a num1:"))
num2=int(input("enter a num2:"))
num3=int(input("enter a num3:"))
if (num1>=num2 and num1<=num3) or (num1<=num2 and num1>=num3):
    print("num1 is second largest")
elif (num2>=num1 and num2<=num3) or (num2<=num1 and num2>=num3):
    print("num2 is second largest")
else:
    print("num3 is second largest")'''


#Leap Year or Not
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
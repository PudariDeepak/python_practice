#Create a Python function greet(name) that takes a name as input and prints out a personalized greeting message.
'''def greet(name):
    return 'Happy to welcome you boss',name

print(greet("Deepak"))'''


#Write a function add_numbers(a, b) that adds two numbers and returns the result.
'''def add_numbers(a,b):
    return a+b
result=add_numbers(10,3)
print(result)'''


#Develop a function calculate_area(length, width) that calculates the area of a rectangle given its length and width.
'''def cal_area(length,width):
    return length*width
result=cal_area(4,8)
print(result)'''


#Create a function is_even(number) that checks if a given number is even and returns True if it is, False otherwise.
def is_even(num):
    if num%2==0:
        return "True"
    else:
        return "False"
print(is_even(10))


#Create a function is_even(number) that checks if a given number is even and returns True if it is, False otherwise.
def get_max(numbers):
    maximum=numbers[0]
    for num in numbers:
        if num>maximum:
            maximum=num
    return maximum

numbers=[30,20,50,90,10,25]
print("Maximum value is:",max(numbers))

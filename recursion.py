#1.Implement a recursive function in Python to calculate the factorial of a given integer
'''def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
print(fact(5))'''

#2.Write a recursive function to determine if a string is a palindrome.
'''def palindrome(name):
    if len(name)<=1:
        return True
    
    if name[0] != name[-1]:
        return False
    
    return palindrome(name[1:-1])
name=input("enetr a string:")
if palindrome(name):
    print("Palindrome")
else:
    print("Not a palindrome")'''


#3.Create a recursive function to calculate the sum of all numbers in a list
'''def sum_of_nums(numbers):
   if len(numbers)==0:
      return 0
   return numbers[0]+sum_of_nums(numbers[1:])

numbers=[2,4,6,8,10]
print(sum_of_nums(numbers))'''


#4.Implement a recursive binary search algorithm to find an element in a sorted list.
'''def binary_search(numbers,low,high,target):

    if low > high:
        return -1
    mid=(low+high)//2

    if numbers[mid]==target:
        return mid
    elif target<numbers[mid]:
        return binary_search(numbers,low,mid-1,target)
    else:
        return binary_search(numbers,mid+1,high,target)
    
numbers=[1,3,5,7,9,13,15]
target=3

result=binary_search(numbers,0,len(numbers)-1,target)

if result != -1:
    print("elemenet found at index:",result)
else:
    print("element not found")'''


#Write a recursive function to generate the Fibonacci sequence up to the nth term.
'''def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the no.of terms:"))
for i in range(n):
    print(fibonacci(i),end=" ")'''



#Use recursion to solve the Tower of Hanoi problem, where you need to move disks from one peg to another subject to certain constraints
def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)


n = 3

tower_of_hanoi(n, 'A', 'B', 'C')
#1.Implement a recursive function in Python to calculate the factorial of a given integer.
'''def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
print(fact(4))'''

#2.Write a recursive function to determine if a given string is a palindrome.
'''def is_palindrome(name):
    if len(name)<=1:
        return True
    if name[0]!=name[-1]:
        return False
    return is_palindrome(name[1:-1])
name=input("enter a string:")
if is_palindrome(name):
    print("the given string is palindrome")
else:
    print("the given string is not a palindrome")'''


#3.Create a recursive function to find the sum of all elements in a list.
'''def sum_of_list(nums):
    if len(nums)==0:
        return 0
    return nums[0]+sum_of_list(nums[1:])
nums=[1,3,5,7,9]
print(sum_of_list(nums))'''

#4.Develop a recursive function to perform a binary search in a sorted list.
'''def binary_search(nums,low,high,target):
    if low > high:
        return -1
    mid=(low+high)//2

    if nums[mid]==target:
        return mid
    
    elif target<nums[mid]:
        return binary_search(nums,low,mid-1,target)
    else:
        return binary_search(nums,mid+1,high,target)
    
nums=[2,4,6,9,11,17]
target=11
result=binary_search(nums,0,len(nums)-1,target)
if result != -1:
    print("element found at index",result)
else:
    print("element not found")'''


#5.Implement a recursive function to calculate the nth Fibonacci number
'''def fibo(num):
    if num==0:
        return 0
    if num==1:
        return 1
    return fibo(num-1)+fibo(num-2)
num=int(input("enter the number:"))
print(fibo(num))'''


#6.Use recursion to solve the Tower of Hanoi problem for n disks, providing a step-by-step solution.
'''def tower_of_hanoi(n, source, auxiliary, destination):

    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)

    print("Move disk", n, "from", source, "to", destination)

    tower_of_hanoi(n - 1, auxiliary, source, destination)

n = 2
tower_of_hanoi(n, 'A', 'B', 'C')'''


#7.Compare the time and space complexity of an iterative solution versus a recursive solution for one of the problems above, 
#discussing the trade-offs and scenarios where one approach might be preferred over the other.
#1.Iterative process
def factorial_iterative(n):
    result = 1

    for i in range(1, n+1):
        result*= i

    return result

print(factorial_iterative(4))
#2.Recurvisve process
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n*factorial_recursive(n-1)
print(factorial_recursive(4))


'''time complexity for both iterative and recusive are same o(n)
but space complexity for iterative is o(1) where recursive is o(n)

---When to Prefer Iteration
Use iterative approach when:
1)performance matters
2)memory efficiency is important
3)problem is simple looping
4)input size is very large
Best for:
*factorial
*summation
*counting problems

--When to Prefer Recursion
Use recursion when:
1)problem is naturally recursive
2)code readability is important
3)working with trees or graphs
4)divide-and-conquer algorithms
Best for:
*Tower of Hanoi
*Tree traversal
*Merge Sort
*Quick Sort
*DFS
*Backtracking
---Iteration saves memory, recursion improves simplicity.'''
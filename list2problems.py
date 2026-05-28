#1. Count Occurrence of an Element
'''def count_occurence(nums,value):
    count=0
    for i in nums:
        if i==value:
            count+=1
    return count
nums=[1,2,2,3,2]
value=2
res=count_occurence(nums,value)
print(res)'''

'''def count_occurences(nums,value):
    count=nums.count(value)
    return count
nums=[1,2,2,3,2]
value=2
res=count_occurences(nums,value)
print(res)'''


#2. Reverse a List    
'''def reverse_list(nums):
    nums.reverse()
    return nums 
nums=[1,2,3,4,5]
print(reverse_list(nums))

def reverse_lists(nums):
    return nums[::-1]
nums=[2,3,4,5,6,7]
print(reverse_lists(nums))'''

#3. Sort a List
'''def sort_list(nums):
    nums.sort()
    return nums
nums=[6,4,5,2,9,1]
print(sort_list(nums))

def sort_lists(nums):
    nums=sorted(nums)
    return nums
nums=[9,3,8,4,6,1,2]
print(sort_lists(nums))'''


#4. Remove Duplicates from a List
'''def remove_duplicates(nums):
    duplicates=[]
    for i in nums:
        if i not in duplicates:
            duplicates.append(i)
    return duplicates
nums=[5,4,5,7,3,2,3,1]
print(remove_duplicates(nums))

def remove_duplicate(nums):
    num=list(set(nums))
    return num
nums=[4,3,3,5,2,1,2]
print(remove_duplicate(nums))'''

#5. Merge Two Lists
'''def merge_lists(l1,l2):
    return l1+l2
l1=[1,2,3]
l2=[4,5,6]
print(merge_lists(l1,l2))

def merge_lists(l1,l2):
    l1.extend(l2)
    return l1
l1=[4,5,6]
l2=[1,2,3]
print(merge_lists(l1,l2))'''

#6. Find Common Elements in Two Lists
'''def common_elements(l1,l2):
    common=[]
    for i in l1:
        if i in l2:
            common.append(i)
    return common
l1=[1,2,3]
l2=[2,3,4]
print(common_elements(l1,l2))

def common_element(l1,l2):
    common=list(set(l1) & set(l2))
    return common
l1=[4,5,6,7]
l2=[9,8,6,7]
print(common_element(l1,l2))'''

#7. Print Even Numbers in a List
'''def even_numbers(nums):
    numbers=[]
    for i in nums:
        if i%2==0:
            numbers.append(i)
    return numbers
nums=[2,3,4,5,6,7]
print(even_numbers(nums))'''


#8.print odd numbers in a list
'''def even_numbers(nums):
    numbers=[]
    for i in nums:
        if i%2!=0:
            numbers.append(i)
    return numbers
nums=[2,3,4,5,6,7]
print(even_numbers(nums))'''


#9. Check if List is Palindrome
'''def is_palindrome(nums):
    rev=nums.copy()
    rev.reverse()
   
    if nums==rev:
        return "palindrome"
    else:
        return "not a palindrome"
nums=[1,2,3,4,5,4,3,2,1]
print(is_palindrome(nums))

def palindrome(nums):
    if nums==nums[::-1]:
        return "palindrome"
    else:
        return "not a palindrome"
nums=[1,2,3,4,2,1]
print(palindrome(nums))'''


#10. Count Positive, Negative, Zero
def count_numbers(nums):
    positive=0
    negative=0
    zero=0
    for i in nums:
        if i>0:
            positive+=1
        elif i < 0:
            negative+=1
        else:
            zero+=1
    return positive,negative,zero
nums=[0,-1,2,-3,4]
p,n,z=count_numbers(nums)
print("positive:",p)
print("negative:",n)
print("zero:",z)
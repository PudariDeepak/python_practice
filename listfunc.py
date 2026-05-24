#1. Find the Sum of Elements
'''def sum_list(nums):
    return sum(nums)
nums=[2,5,9,1,7]
print(sum_list(nums))'''

#2. Find Maximum Element
'''def list_max(nums):
    return max(nums)
nums=[7,3,9,3,1]
print(list_max(nums))'''

#3. Find Minimum Element
'''def list_min(nums):
    return min(nums)
nums=[7,3,9,3,1]
print(list_min(nums))'''

#4. Count Even Numbers
'''def list_even_count(nums):
    count=0
    for i in nums:
        if i%2==0:
            count+=1
    return count
nums=[3,4,2,6,7,8,9]
print(list_even_count(nums))'''


#5. Count Odd Numbers
'''def list_odd_count(nums):
    count=0
    for i in nums:
        if i%2!=0:
            count+=1
    return count
nums=[3,4,2,6,7,8,9]
print(list_odd_count(nums))'''

#6. Reverse a List
'''def reverse_list(nums):
    return nums[::-1]
nums=[3,5,7,9,1,2,4]
print(reverse_list(nums))'''


#7. Find Duplicate Elements
'''def list_duplicates(nums):
    duplicates=[]
    for i in nums:
        if nums.count(i)> 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates
nums=[2,3,5,6,2,3,7,9,5]
print(list_duplicates(nums))'''

#8. Remove Duplicates
'''def remove_duplicates(nums):
    return list(set(nums))
nums=[2,3,5,6,2,3,7,9,5]
print(remove_duplicates(nums))'''

#9. Find Second Largest Number
'''def second_largest(nums):
    nums=list(set(nums))
    nums.sort()
    return nums[-2]
nums=[10,20,5,8,20]
print(second_largest(nums))'''

#11. Find Average of List
'''def avg_list(nums):
    return sum(nums)/len(nums)
nums=[2,7,4,9,3,8,10]
print(avg_list(nums))'''


#12. Sort a List
'''def sort_list(nums):
   nums.sort()
   return nums
nums=[8,2,9,3,7,5]
print(sort_list(nums))'''

#15. Find Length of List Without len()
def len_list(nums):
    count=0
    for i in nums:
        count+=1
    return count
nums=[2,9,4,8,3,6,1]
print(len_list(nums))
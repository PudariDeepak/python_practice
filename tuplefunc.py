#1. Find Length of Tuple
'''def tuple_len(t):
    return len(t)
t=(1,3,5,7,9,2,4,6)
print(tuple_len(t))'''

#2. Find Maximum Element
'''def max_element(t):
    return max(t)
t=(3,9,2,8,4,6,1)
print(max_element(t))'''

#3. Find Minimum Element
'''def min_element(t):
    return min(t)
t=(3,9,2,8,4,6,1)
print(min_element(t))'''

#4. Find Sum of Elements
'''def sum_elements(t):
    return sum(t)
t=(4,2,8,9,1,3,5)
print(sum_elements(t))'''

#5. Count Occurrences of an Element
'''def count(t,key):
    count=0
    for i in t:
        if i==key:
            count+=1
    return count
print(count((2,3,4,3,5,3,6,7),3))'''

#6. Find Index of an Element
'''def index_element(t,key):
    return t.index(key)
t=(4,3,7,8,2,9,1)
print(index_element(t,8))'''

#7. Convert List to Tuple
'''def conversion(nums):
    return tuple(nums)
nums=[4,6,8,3,9]
print(conversion(nums))'''


#9. Convert Tuple to List
'''def conversions(t):
    return list(t)
t=(4,3,5,7,9,2)
print(conversions(t))'''

#10. Reverse a Tuple
'''def tup_reverse(t):
    return t[::-1]
t=(2,3,4,5,6,7)
print(tup_reverse(t))'''


#11. Find Duplicate Elements
'''def duplicate_elements(t):
    duplicates=[]
    for i in t:
        if t.count(i)>1 and i not in duplicates:
            duplicates.append(i)
    return duplicates
t=(3,4,3,5,3,6,4,5,9,7)
print(duplicate_elements(t))'''

#12. Count Even Numbers
'''def even_count(t):
    count=0
    for i in t:
        if i%2==0:
            count+=1
    return count
t=(3,2,5,4,7,6,8)
print(even_count(t))'''

#13. Find Average of Tuple Elements
'''def avg_elements(t):
    return sum(t)/len(t)
t=(5,3,7,9,2,6)
print(avg_elements(t))'''

#14.Find second largest element in a tuple.
def second_largest_element(t):
    unique=list(set(t))
    unique.sort()
    return unique[-2]
t=(3,5,7,2,8,3)
print(second_largest_element(t))




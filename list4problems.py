#1.Find Frequency of All Elements
'''def frequency(nums):
    list={}
    for i in nums:
        if i  in list:
            list[i]+=1
        else:
            list[i]=1
    return list
nums=[1,2,3,2,4,1,2,5]
print(frequency(nums))'''


#2.Flatten a Nested List
'''def nested_list(nums):
    new_list=[]
    for i in nums:
        for j in i:
            new_list.append(j)
    return new_list
nums=[[1,2],[3,4],[5,6]]
print(nested_list(nums))'''


#3.Split a List into Even and Odd Lists
'''def even_odd_elements(nums):
    even_nums=[]
    odd_nums=[]
    for i in nums:
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    return even_nums,odd_nums 
nums=[2,3,4,5,6,7,8]
even_nums,odd_nums=even_odd_elements(nums)
print("even list:",even_nums)
print("odd list:",odd_nums)'''

#4.Find Pair of Elements with Given Sum
'''def pair_sums(nums,sum):
    pairs=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==sum:
                pairs.append([nums[i],nums[j]])
    return pairs
nums=[1,2,3,4]
sum=5
print(pair_sums(nums,sum))'''

#5.Remove All Odd Numbers
'''def removing_odds(nums):
    new_nums=[]
    for i in nums:
        if i%2 ==0:
            new_nums.append(i)
    return new_nums
nums=[1,2,3,4,5]
print(removing_odds(nums))'''

#6.Remove All Even Numbers
'''def removing_even(nums):
    new_nums=[]
    for i in nums:
        if i%2 !=0:
            new_nums.append(i)
    return new_nums
nums=[1,2,3,4,5]
print(removing_even(nums))'''

#7.Multiply All Elements by a Number
'''def multipy_element(nums):
    result=[]
    for i in nums:
        result.append(i*2)
    return result
nums=[1,2,3,5,6]
print(multipy_element(nums))'''

#8.Find Difference Between Max and Min
'''def difference(nums):
    nums.sort()
    return nums[-1]-nums[0]
nums=[4,2,7,1]
print(difference(nums))'''

#9.Check if a List is Empty
'''def check_list(nums):
    if len(nums)==0:
        return True
    else:
        return False
nums=[]
print(check_list(nums))'''

#10.Insert Element at Specific Index
'''def insert_element(nums):
    nums.insert(2,3)
    return nums
nums=[1,2,4]
print(insert_element(nums))'''

#11.Remove All Instances of a Value
'''def remove_elements(nums,value):
    new_list=[]
    for i in nums:
        if i != value:
            new_list.append(i)
    return new_list
nums=[1,2,2,3]
value=2
print(remove_elements(nums,value))'''

#12.Get Index of an Element
'''def get_index(nums):
    index=nums.index(30)
    return index
nums=[10,20,30]
print(get_index(nums))

def get_indexs(num,element):
    for i in range(len(num)):
        if num[i]==element:
            return i
num=[10,20,30,40,50]
element=40
print(get_indexs(num,element))'''

#13.Square All Elements in a List
'''def square_elements(nums):
    new_list=[]
    for i in nums:
        new_list.append(i**2)
    return new_list
nums=[1,2,3]
print(square_elements(nums))'''

#14.Filter Out Negative Numbers
'''def filter_numbers(nums):
    new_nums=[]
    for i in nums:
        if i > 0:
            new_nums.append(i)
    return new_nums
nums=[-1,2,-3,4]
print(filter_numbers(nums))'''

#15.Get Elements Greater Than a Value
'''def greater_elements(nums,element):
    new_list=[]
    for i in nums:
        if i > element:
            new_list.append(i)
    return new_list
nums=[1,11,5,8,3,9]
element=5
print(greater_elements(nums,element))'''

#16.Find Duplicates in List
'''def find_duplicates(nums):
    duplicates=[]
    for i in nums:
        if nums.count(i)>1 and i not in duplicates:
            duplicates.append(i)
    return duplicates
nums=[1,2,2,3,3,4]
print(find_duplicates(nums))'''

#17.Rotate List Elements Right
'''def rotate_list(nums,k):
    return nums[-k:]+nums[:-k]
nums=[1,2,3,4,5,6]
k=3
print(rotate_list(nums,k))'''

#18.Check If List Contains a Value
'''def check_list(nums,value):
    for i in nums:
        if i == value:
            return True
    return False
nums=[1,2,3]
value=5
print(check_list(nums,value))'''

#19.Chunk List into Smaller Lists
def chunk_list(nums,size):
    chunk=[]
    for i in range(0,len(nums),size):
        chunk.append(nums[i:i+size])
    return chunk
nums=[1,2,3,4,5,6]
print(chunk_list(nums,2))
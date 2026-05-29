#1.Find Second Largest Number in List
'''def second_largest(nums):
    nums.sort()
    for i in range(len(nums)-1,0,-1):
        if nums[i]!=nums[i-1]:
            return nums[i-1]
nums=[4,6,8,1,3,9]
print(second_largest(nums))'''

#2. Find Second Smallest Number in List
'''def second_smallest(nums):
    nums.sort()
    for i in range(0,len(nums)-1):
        if nums[i]!= nums[i+1]:
            return nums[i+1]
nums=[4,6,8,1,3,9]
print(second_smallest(nums))'''

#3. Copy List to Another List
'''def copy_list(nums):
    new_nums=nums.copy()
    return new_nums
nums=[1,2,3,4,5]
print(copy_list(nums))

def copy_lists(nums):
    new_list=nums[0:len(nums)]
    return new_list
nums=[5,6,7,8]
print(copy_lists(nums))'''

#4. Print All Prime Numbers in List
'''def prime_elements(nums):
    primes=[]
    for num in nums:
        if num>1:
            is_prime=True

            for i in range(2,num):
                if num%i==0:
                    is_prime=False
                    break
            if is_prime:
                primes.append(num)
    return primes
nums=[1,2,3,4,5]
print(prime_elements(nums))'''

#5. Replace All Zeroes with a Given Number
'''def replace_values(nums):
        for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=-1
                    pass
        return nums
nums=[0,2,0,4]
print(replace_values(nums))'''

#6. Check if All Elements Are Same
def all_same(nums):
    new_nums=nums[0]
    for i in nums:
        if i != new_nums:
            return False
        
    return True
nums=[5,5,4,5]
print(all_same(nums))








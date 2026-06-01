#1. Add Element to a Set
'''def add_element(nums):
    nums.add(4)
    return nums
nums={1,2,3}
print(add_element(nums))'''

#2. Remove Element from Set
'''def remove_element(nums):
    nums.remove(5)
    return nums
nums={1,2,3,4,5}
print(remove_element(nums))

def remove_elements(nums):
    nums.discard(4)
    return nums
nums={1,2,3,4,5}
print(remove_elements(nums))'''

#3. Union of Two Sets
'''def union_element(nums1,nums2):
    return nums1|nums2
nums1={1,2,3,4}
nums2={3,4,5,6}
print(union_element(nums1,nums2))

def union_element(nums1,nums2):
    unionnums=nums1.union(nums2)
    return unionnums
nums1={1,2,3,4,9,8}
nums2={3,4,5,6}
print(union_element(nums1,nums2))'''

#4. Intersection of Sets
'''def common_elements(nums1,nums2):
    return nums1&nums2
nums1={1,2,3,4,5}
nums2={3,4,5,6,7}
print(common_elements(nums1,nums2))

def common_elements(nums1,nums2):
    common=nums1.intersection(nums2)
    return common
nums1={1,2,3,4,5,6}
nums2={3,4,5,6,7}
print(common_elements(nums1,nums2))'''

#5. Difference of Sets
'''def set_difference(nums1,nums2):
    return nums1-nums2
nums1={1,2,3,4}
nums2={3,4,5,6}
print(set_difference(nums1,nums2))

def set_differences(nums1,nums2):
    diff=nums1.difference(nums2)
    return diff
nums1={1,2,3,4}
nums2={4,5,6}
print(set_differences(nums1,nums2))'''

#6. Check Subset
'''def check_set(nums1,nums2):
    return nums2.issubset(nums1)
nums1={1,2,3}
nums2={1}
print(check_set(nums1,nums2))'''

#7. Set Length
'''def set_length(nums):
    return len(nums)
nums={1,2,3,4,5}
print(set_length(nums))'''

#8. Clear a Set
'''def set_clear(nums):
    return nums.clear()
nums={6,5,4,3,2}
print(set_clear(nums))'''

#9. Symmetric Difference
'''def symmetric_diff(nums1,nums2):
    return nums1^nums2
nums1={1,2,3,4}
nums2={2,3,4,5,6}
print(symmetric_diff(nums1,nums2))

def symmetric_diff(nums1,nums2):
    diff=nums1.symmetric_difference(nums2)
    return diff
nums1={1,2,3}
nums2={2,3,4,5,6}
print(symmetric_diff(nums1,nums2))'''


#10. Convert List to Set
def conversion(nums):
    new=set(nums)
    return new
nums=[1,2,2,3,3,4,5]
print(conversion(nums))
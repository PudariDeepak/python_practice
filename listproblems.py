#Add an Element to a List
'''def add_element(lst,i):
    lst.append(i)
    return lst
lst=[3,6,9,4,6]
print(add_element(lst,2))'''

#2. Remove an Element from a List
'''def remove_element(lst):
    #lst.remove(5)
    lst.pop(3)
    return lst
lst=[2,3,5,7,9,1]
print(remove_element(lst))'''

#3. Find Maximum in List
'''def max_element(lst):
    maximum=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>maximum:
            maximum=lst[i]
    return maximum
lst=[2,3,5,7,9,1] 
print(max_element(lst))'''

#4. Find Minimum in List
'''def min_element(lst):
    min=lst[0]
    for i in range(1,len(lst)):
        if lst[i]<min:
            min=lst[i]
    return min
lst=[2,3,5,7,9,1] 
print(min_element(lst))'''

#5. Sum of All Elements in List
def sum_elements(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum
lst=[2,3,4,5,6]
print(sum_elements(lst))
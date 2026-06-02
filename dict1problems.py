#1. Create a Dictionary from Two Lists
'''def dictionary(a,b):
    return dict(zip(a,b))
a=["a","b","c","d"]
b=[1,2,3,4]
print(dictionary(a,b))'''

#2. Update Dictionary Value
'''def dict_update(dict,key,value):
    dict[key]=value
    return dict
dict={"a":1,"b":2,"c":3}
key="b"
value=9
print(dict_update(dict,key,value))

def dict_update(dict):
    dict["c"]=10
    return dict
dict={"a":1,"b":2,"c":3}
print(dict_update(dict))'''

#3. Remove Key from Dictionary
'''def remove_key(dict):
    #dict.pop("b")
    dict.pop("c")
    return dict
dict={"a":1,"b":2,"c":3,"d":4}
print(remove_key(dict))'''

#4. Check Key Existence
'''def check_key(dict):
    if "d"in dict:
        return True
    return -1
dict={"a":1,"b":2,"c":3}
print(check_key(dict))'''

#5. Iterate Over Dictionary
'''def allkeys(d):
    for key,value in d.items():
        print(key,value)
d={"a":1,"b":2,"c":3,"d":4}
allkeys(d)'''


#6. Dictionary Length
'''def d_length(d):
    return len(d)
d={"a":1,"b":2,"c":3,"d":4}
print(d_length(d))'''


#7.Merge Two Dictionaries
'''def merge_dict(d1,d2):
    new=d1.update(d2)
    return d1
d1={"a":1,"b":2}
d2={"c":3,"d":4}
print(merge_dict(d1,d2))

def merge_dict_unpacking(d1,d2):
    return {**d1,**d2}
d1={"a":1,"b":2,"e":5}
d2={"c":3,"d":4}
print(merge_dict(d1,d2))'''


#8.Get Value with Default
'''def get_value(d):
    return d.get("d","not found")
d={"a":1,"b":2,"c":3}
print(get_value(d))'''

#9. Count Frequency of Elements
'''def count_frequency(d):
    res={}
    for i in d:
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    return res
d=[1,2,2,3]
print(count_frequency(d))'''

#10. Invert a Dictionary
def invert(d):
    inverted={}
    for key,value in d.items():
            inverted[value]=key
    return inverted
d={"a":1,"b":2,"c":3}
print(invert(d))


            



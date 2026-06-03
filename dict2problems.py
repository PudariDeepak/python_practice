#1. Find Key with Maximum Value
'''def max_key(d):
    max_v=None
    max_k=None
    for key,value in d.items():
        if max_v is None or value > max_v:
            max_v=value
            max_k=key
    return max_k
d={"a":1,"b":10,"c":3,"d":4}
print(max_key(d))

def max_keys(d):
    return max(d,key=d.get)
d={"a":10,"b":20,"c":30,"d":40}
print(max_keys(d))'''

#2.Sort Dictionary by Values
'''def get_value(d):
    return d[1]
def sort_dict(d):
    return  dict(sorted(d.items(), key=get_value))
d={"a":3,"b":1,"c":2}
print(sort_dict(d))'''

#3.Create Dictionary of Squares
'''def dict_creation():
    d1={}
    for i in range(1,5):
        d1[i]=i**2
    return d1
print(dict_creation())'''

#4.Filter Dictionary by Value Condition
'''def filter_dict(d):
    result={}
    for key,value in d.items():
        if value > 10:
            result[key]=value
    return result
d={"a":10,"b":5,"c":15}
print(filter_dict(d))'''
        

#5.Combine Values of Duplicate Keys
'''def combine_values(d1,d2):
    res={}
    for key,value in d1.items():
        res[key]=value
    for key,value in d2.items():
        if key in res:
            res[key]+=value
        else:
            res[key]=value

    return res
d1={"a":1,"b":2}
d2={"a":3,"c":4}
print(combine_values(d1,d2))'''


#6. Count Word Frequency in Sentence
'''def word_frequency(data):
    res={}
    for i in data.split():
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    return res
data="apple banana apple"
print(word_frequency(data))'''

#7.Remove Duplicate Values from Dictionary
'''def remove_duplicate(d):
    res={}
    seen_values=[]
    for key,value in d.items():
        if value  not in seen_values:
            res[key]=value
            seen_values.append(value)
    return res
d={"a":1,"b":2,"c":1}
print(remove_duplicate(d))'''


#8.Find Common Keys in Two Dictionaries
'''def common_keys(d1,d2):
    for key in d1.keys():
        for key in d2.keys():
            if key in d1 and key in d2:
                return key
    return -1
d1={"a":1,"b":2}
d2={"b":3,"c":4}
print(common_keys(d1,d2))

def common_key(d1,d2):
    res=[]
    for key in d1:
        if key in d2:
            res.append(key)
    return res
d1={"b":2,"d":3}
d2={"d":4,"e":5}
print(common_key(d1,d2))'''

#9. Swap Keys and Values Safely
'''def swap(d):
    res={}
    for key,value in d.items():
        res[value]=key
    return res
d={"x":1,"y":2}
print(swap(d))'''

#10. Delete Items by Value
def remove_value(d,delete_value):
    res={}
    for key,value in d.items():
        if value != delete_value:
            res[key]=value
    return res
d={"a":1,"b":2,"c":1}
print(remove_value(d,1))






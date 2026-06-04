#1.Remove Spaces from Given Text
'''def remove_spaces(text):
    return text.replace(" ","")
text="he llo wor ld"
print(remove_spaces(text))

def remove_space(s):
    res=""
    for ch in s:
        if ch != " ":
            res+=ch
    return res
s="  de  ep  a  k"
print(remove_space(s))'''

#2.Reverse a String
'''def reverse_string(s):
    return s[::-1]
s="deepak"
print(reverse_string(s))


def reverse_strings(s):
    res=""
    for ch in s:
        res=ch+res
    return res
s="hello"
print(reverse_strings(s))'''

#3.Reverse a String After Removing Spaces
'''def reverse_space(s):
    stm=s.replace(" ","")
    return stm
s=" he ll o wor ld"
print(reverse_space(s))

def reverse_space(sentc):
    res=""
    for ch in sentc:
        if ch != " ":
            res=ch+res
    return res
sentc=" de e p  ak"
print(reverse_space(sentc))'''

#4.Convert Snake Case to Camel Case
'''def snake_to_camel(text):
    words= text.split('_')
    res=words[0]
    for i in range(1,len(words)):
        res+=words[i].capitalize()
    return res
text="my_variable_name"
print(snake_to_camel(text))'''


#5.Convert Snake Case to Pascal Case
'''def snake_to_pascal(text):
    words=text.split("_")
    res=""
    for i in range(0,len(words)):
        res+=words[i].capitalize()
    return res
text="my_variable_name"
print(snake_to_pascal(text))'''

#6. Convert Camel Case to Snake Case
'''def camel_to_snake(text):
    res=""
    for ch in text:
        if ch.isupper():
            res+="_"+ ch.lower()
        else:
            res+=ch
    return res
text="myVariableName"
print(camel_to_snake(text))'''

#7.Convert Camel Case to Pascal Case
'''def camel_to_pascal(text):
    res=""
    for i in range(0,len(text)):
        if i==0:
            res+=text[i].upper()
        else:
            res+=text[i]
    return res
text="myVariable"
print(camel_to_pascal(text))

def cameltopascal(text):
    return text[0].upper()+text[1:]
text="myVariable"
print(cameltopascal(text))'''


#8.Convert Pascal Case to Camel Case
'''def pascal_to_camel(text):
    return text[0].lower()+text[1:]
text="MyVariable"
print(pascal_to_camel(text))


def pascaltocamel(text):
    res=""
    for i in range(len(text)):
        if i==0:
            res+=text[i].lower()
        else:
            res+=text[i]
    return res
text="MyVariableName"
print(pascaltocamel(text))'''

#9.Convert Pascal Case to Snake Case
'''def pascal_to_snake(text):
    res=""
    for i in range(len(text)):
        if text[i].isupper():
            if i != 0:
                res+="_"
            res+=text[i].lower()
        else:
            res+=text[i]
    return res
text="MyVariableName"
print(pascal_to_snake(text))'''

#10.Convert Text to Camel Case
def text_to_camel(text):
    t=text.split(" ")
    res=""
    for i in range(0,len(t)):
        if i==0:
            res+=t[i]
        else:
            res+=t[i].capitalize()
    return res
text="hello world example"
print(text_to_camel(text))


        
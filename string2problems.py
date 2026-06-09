#1.Convert Text to Snake Case
'''def text_to_snake(text):
    return text.replace(" ","_")
text="hello world example"
print(text_to_snake(text))

def texttosnake(text):
    res=""
    for ch in text:
        if ch==" ":
            res+="_"
        else:
            res+=ch
    return res
text="my name is deepak"
print(texttosnake(text))'''

#2.Convert Text to Pascal Case
'''def text_to_pascal(text):
    t=text.split(" ")
    res=""
    for i in range(0,len(t)):
        res+=t[i].capitalize()
    return res
text="hello world example"
print(text_to_pascal(text))'''

#3. Swap Upper and Lower Case
'''def swap_cases(text):
    res=""
    for ch in text:
        if ch.isupper():
            res+=ch.lower()
        else:
            res+=ch.upper()
    return res
text="DeEpAk"
print(swap_cases(text))'''

#4.Separate Digits from Text
'''def seperate_digits(input):
    res=""
    for ch in input:
        if ch.isdigit():
            res+=ch
    return res
input="abc12d34h7"
print(seperate_digits(input))'''

#5.Print Uppercase, Lowercase, Digits, and Special Characters Separately
'''def seperate(text):
    Uppercase=""
    Lowercase=""
    Digits=""
    Special_characters=""

    for ch in text:
        if ch.isupper():
            Uppercase+=ch+" "
        elif ch.islower():
            Lowercase+=ch+" "
        elif ch.isdigit():
            Digits+=ch+" "
        else:
            Special_characters+=ch+" "
    print("Uppercase:",Uppercase)
    print("Lowercase:",Lowercase)
    print("Digits:",Digits)
    print("Special_cheracter:",Special_characters)
text="Abc123!@#"
seperate(text)'''

#6.Count of Uppercase, Lowercase, Digits, and Special Characters
'''def seperatecount(text):
    Uppercount=0
    Lowercount=0
    Digitscount=0
    Specialcount=0

    for ch in text:
        if ch.isupper():
            Uppercount+=1
        elif ch.islower():
            Lowercount+=1
        elif ch.isdigit():
            Digitscount+=1
        else:
            Specialcount+=1
    print("Uppercase:",Uppercount)
    print("Lowercase:",Lowercount)
    print("Digits:",Digitscount)
    print("Special_cheracter:",Specialcount)
text="Abc123!@#"
seperatecount(text)'''

#7.Check Password Strength
'''def check_password(password):
    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if upper and lower and digit and special:
        return "Strong Password"
    else:
        return "Weak Password"

print(check_password("Pass123"))'''

#8.Remove Duplicates in a Given Input
'''def remove_duplicates(text):
    res=""
    for ch in text:
        if ch not in res:
            res+=ch
    return res
text="aabbcdd"
print(remove_duplicates(text))'''

#9.Print Duplicates in a Given String
'''def find_duplicates(text):
    seen=""
    res=""
    for ch in text:
        if ch not in seen:
            seen+=ch
        elif ch not in res:
            res+=ch + " "
    return res
text="aabbcdde"
print(find_duplicates(text))

def duplicates(text):
    duplicates=""
    for ch in text:
        if text.count(ch) > 1 and ch  not in duplicates:
            duplicates+=ch+" "
    return duplicates
text="xxyzzwwv"
print(duplicates(text))'''

#10. Print Next Characters in a Given String
def next_character(text):
    res=""
    for ch in text:
        res+=chr(ord(ch)+1)
    return res
text="abc"
print(next_character(text))


#1.Reverse Each Word In A String
'''def reverse_string_word(s):
    result = ""
    word = ""
    for ch in s:
        if ch != " ":
            word = ch + word
        else:
            result += word + " "
            word = ""

    result += word
    return result
s="one two  three"
print(reverse_string_word(s))'''

#2.Reverse Words in a String
'''def reverse_words(input):
    new=input.split()
    res=""
    for i in range(len(new)):
        res=new[i]+" "+res
    return res
input="the sky is blue"
print(reverse_words(input))'''

#3.Longest Substring Without Repeating Characters
'''def longest_substring(input):
    res=""
    for ch in input:
        if ch not in res:
            res+=ch
    return len(res)
input="abcdabdabcde"
print(longest_substring(input))'''


#4.Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""
    return prefix
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))




























 

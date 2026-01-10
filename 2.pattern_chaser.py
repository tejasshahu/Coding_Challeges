"""
Problem Statement
"aabecaa" contains the pattern aa, on the other hand "abbbaac" doesn't contain any pattern.
So if str were "aabejiabkfabed" the output should be yes abe.

the output should return no null. The string may either contain all characters (a through z only),
integers, or both.
But the parameter will always be a string type. The maximum length for the string
being passed in will be 20 characters.
If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa".
You must always return the longest pattern possible.

If str were "123224" the output should return no null.
The string may either contain all characters (a through z only), integers, or both.
But the parameter will always be a string type.
The maximum length for the string being passed in will be 20 characters.
If a string for example is "aa2bbbaacbbb" the pattern is "bbb" and not "aa".
You must always return the longest pattern possible.
"""

def pattern_chaser(input_str):
    detected_pattern = ""
    l = len(input_str)
    if(l > 20):
        print("Please enter input <20 char.")
    for i in range(0, l-1):
        for j in range(i+1, l-1):
            pattern = input_str[i:j]
            if input_str.count(pattern) > 1:
                if len(pattern) > len(detected_pattern):
                    detected_pattern = pattern
    return detected_pattern if detected_pattern else None


input1 = "aabecaa"
input2 = "aabejiabkfabed"
input3 = "aa2bbbaacbbb"
input4 = "aa2bbbaacbbb"
print(pattern_chaser(input4))
print(pattern_chaser(input3))
print(pattern_chaser(input2))
print(pattern_chaser(input1))


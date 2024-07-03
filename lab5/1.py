# re is imported to use regular expressions in PY
import re

def a(string):
    b = r'ab*'#The variable b is assigned the raw string r'ab*'
    if re.fullmatch(b, string):#checks if the entire string matches the parten b
        return True
    else:
        return False
    
test = ["a", "ab", "abb", "abbb", "ac","abc", "aab"]
for test in test:
    if a(test):
        print(test)    
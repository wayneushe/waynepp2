# containingone character after ab
import re

def a(string):
    b = r'ab.?'#.? matches zero or one occurrence of any character (except a newline).
    if re.fullmatch(b, string):
        return True
    else:
        return False
    
test= ["a", "ab", "abb", "abbb", "ac", "abc", "aab", "acb","abcd" ] 
for test in test:
    if a(test):
        print(test)   
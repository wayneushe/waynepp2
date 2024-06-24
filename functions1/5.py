from itertools import permutations 
def all_permutations(string):
    return[''.join(p) for p in permutations(string)]

string="abc"
print(f"All permutations of'{string}':{all_permutations(string)}")

    
    
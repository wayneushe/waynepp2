#3
def count_rabbits_and_chickens(num_heads,num_legs):
    chickens = num_heads * 2
    rabbits = num_legs / 4
    return(chickens,rabbits)

#example
num_heads = 35
num_legs = 94
rabbits , chickens = count_rabbits_and_chickens(num_heads,num_legs)
print(chickens, rabbits)
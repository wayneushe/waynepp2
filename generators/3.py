#which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
n = int(input())
for i in range(n+1):
    if(i%3==0 and i%4==0 and i!=0):
        print(i, end=" ")
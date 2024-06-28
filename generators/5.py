# a generator that returns all numbers from (n) down to 0.
n = int(input())
x = [i for i in range(n)]
x.reverse()
print(x)
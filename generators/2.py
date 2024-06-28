# the even numbers between 0 and n in comma separated form where n is input from console.
n = int(input())
for i in range(n+1):
    if(i%2==0 and i!=0):
        print(i, end=",")
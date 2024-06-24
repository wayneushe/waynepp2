def histogram(numbers):
    for num in numbers:
        print("*" * num)

numbers = list(map(int,input("Enter numbers seperating them with space: ").split()))        
histogram(numbers)
def has_33(numbers):
    for i in range(len(numbers)- 1):
        if numbers[i]==3 and numbers[i + 1]==3:
            return True
    return False
         

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))
print(has_33([5, 2, 2]))   


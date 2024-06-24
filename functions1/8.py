def spy_game(numbers):
    code = [0, 0, 7, 'x']
    for num in numbers:
        if num == code[0]:
            code.pop(0)
    return len(code)==1
        
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  
      
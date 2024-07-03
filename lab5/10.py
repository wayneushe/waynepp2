import  re
def camel_to_snake(camel_case_string):
    snake_case_string= re.sub(r'(?<!^)(?=[A-Z])','_',camel_case_string)
    #coverts the entire string to lowercase
    return snake_case_string.lower()

input_string= input()
snake_case_string = camel_to_snake(input_string)
print(snake_case_string)
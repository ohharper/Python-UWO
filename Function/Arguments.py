#POSITIONAL-These arguments are passed to the function in the order they appear in the function definition.
def welcome(student, grade):
    print(f"Hello, {student} - Welcome to grade {grade}!")
 
welcome("Sam", 10)

#KEYWORD-Arguments can be passed using their corresponding parameter names, regardless of their order.
def welcome1(student, grade):
    print(f"Hello, {student} - Welcome to grade {grade}!")
 
welcome1(grade = 10, student = "Sam")

#DEFAULT- If a value is not provided during the function call, the default value will be used.
def describe_pet(pet_name, species = "cat"):
    print(f"I have a {species} named {pet_name}.")
 
describe_pet("Lucky")
describe_pet("Lucy", "rabbit")

#VARIABLE LENGTH
def multiply_numbers(*args):
    total = 1
    for num in args:
        total *= num
    return total
 
result = multiply_numbers(1, 2, 3)
print(result)
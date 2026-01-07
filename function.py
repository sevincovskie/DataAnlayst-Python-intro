# funksiya-  
# def funksiya_adi(parametr):
    # kodlar
    # return netice
    
# def salam():
#     print("salam necesen")

# salam()

# set ile funksiya

# def vowels(string):
#     return {char for char in string if char in "aeiou"}

# print(vowels("python"))

# def say_hi():
#  return "Hi"
# say_hi()
# print(say_hi())


# def my_add(a,b) :
#     return a+b
# # print(my_add(1,2))

# sum=my_add(1,2)
# print(sum)

# def solution(first,second):
#     return first+second
# sum=solution(1,2)
# print(sum)  

# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#     return total


# print(sum_odd_numbers([1, 2, 3, 4, 5]))


# def odd_numbers(numbers):
#         if numbers % 2 != 0:
#          return True
#         else:
#          return False

# print(odd_numbers(3))
# print(odd_numbers(4))


# def odd_numbers(numbers):
#         if numbers % 2 != 0:
#          return True
#         return False

# print(odd_numbers(3))
# print(odd_numbers(4))

# def odd_numbers(numbers):
#        return  numbers % 2 != 0

# print(odd_numbers(3))
# print(odd_numbers(4))


# def full_name(first_name, last_name):
#     return f"{first_name} {last_name}"
# my_full_name = full_name("John", "Doe")
# print(my_full_name)


# def num (a,b=3):
#     return a+b
# print(num(1))

# def info (first_name= "Sevinc", instructor= False):
#     if first_name == "Sevinc" and instructor:
#         return "Instructor Sevinc"
#     elif first_name == "Sevinc":
#         return "Student Sevinc"
#     return f"Hi {first_name}"
# print(info("Sevinc", False))

# def my_add(a,b):
#     return a+b
# def my_sub(a,b):
#     return a-b

# def my_mul(a,b):
#     return a*b

# def my_math(a,b,func=my_add):
#     return func(a,b)

# num1=10
# num2=20
# print(my_math(num1,num2))
# print(my_math(num1,num2,my_sub))
# print(my_math(num1,num2,my_mul))


# instructor = "Sevinc"
# def say_hi ():
#     return f"Hi {instructor}"
# print(say_hi())


# def say_hi():
#     instructor = "Sevinc"
#     return f"Hi {instructor}"
# print(say_hi())

# def say_hi():
#   return f"Hi {instructor}"
# instructor = "Sevinc"
# print(say_hi())



# closure- Bir funksiya öz xarici scope-undan olan dəyişəni yadda saxlayır
# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count += 1
#         return count
#     return inner

# counter = outer()
# print(counter())

# def full_name(first_name, last_name):
#     return f"{first_name} {last_name}"
# fullName = full_name("John", "Doe")
# print(fullName)

# fullName = full_name(first_name="John", last_name="Doe")
# print(fullName)

# fullName = full_name(last_name="Doe", first_name="John")
# print(fullName)


# DOCSTRING-  Docstring is a string literal used to describe what a function does. It can be accessed using the doc attribute.
def say_hello():
   """ Hello """
print("Hello")

# say_hello.__doc__
print(say_hello.__doc__)

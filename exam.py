# number = 987654321
# while number > 9:
#     number = sum(int(d) for d in str(number))
# print(number)

#   Task 20 – Rəqəmlərin cəmini tək rəqəm olana qədər topla
# number = 987654321
# while number > 9:
#     sum_of_digits = 0
#     temp_number = number  
#     while temp_number > 0:
#         digit = temp_number % 10
#         sum_of_digits += digit
#         temp_number //= 10
#     number = sum_of_digits

# print(f"Son tək rəqəm: {number}")


# number = 98765432199999999999
# s = 0

# while number > 0 or s > 9:
#     if number == 0:
#         number = s
#         s = 0
    
#     s += number % 10
#     number //= 10

# print(f"Nəticə: {s}")

n = 0
while 3**n <= 1_000_000:
    n += 1
print(n+1)

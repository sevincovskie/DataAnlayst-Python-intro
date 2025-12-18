# Task 1
#  Print all numbers from 1 to 200 that are divisible by both 4 and 6, using a for loop.
# – For ilə 1-dən 200-ə qədər 4 və 6-ya tam bölünənləri çap et

# for num in range (1,201):
#     if num % 4 == 0 and num % 6 == 0:
        
# #  if num % 12 == 0:
#         print(num)
        

# Task 2
#  Using a while loop, print numbers from 100 down to 1, but skip numbers divisible by 7.
# – While ilə 100-dən 1-ə qədər geriyə say, amma 7-yə bölünənləri KEÇ

# for num in range(100, 0):
#     if num % 7 !== 0:
#         print(num)
    
# Task 3
#  Using a for loop, calculate the sum of all odd numbers between 1 and 999.
# – For ilə 1–999 arası bütün TƏK ədədlərin cəmini tap

# total = 0
# for num in range(1, 1000):
#     if num % 2 != 0:
#         total += num
# print(total)


# Task 4
#  Using a while loop, multiply numbers from 1 to 20 and stop early if the product exceeds 50,000. Print the final product.
# -While ilə 1-dən 20-yə qədər ədədləri bir-bir vur, hasil 50,000-dən böyük olanda DAYAN

# product = 1
# num = 1
# while num <= 20:
#     product *= num
#     if product > 50000:
#         break
#     num += 1
# print(product)

# Task 5
#  Given a list: nums = [4, 10, 3, 20, 9, 33, 7, 1], use a for loop to print only numbers greater than 10.
# – Verilən list-də yalnız 10-dan böyük ədədləri çap et
# numbers = [4, 10, 3, 20, 9, 33, 7, 1]
# for num in numbers:
#     if num > 10:
#         print(num)

# Task 6
#  Using a while loop, repeatedly subtract 3 from number = 500 until it becomes negative. Count how many subtractions happened.
# – While ilə 500-dən başlayaraq 3-ü təkrar-təkrar çıx, nəticə mənfi olanda DAYAN. Neçə çıxma əməliyyatı olduğunu say
# number = 500
# count = 0
# while number > 0:
#     number -= 3
#     count += 1   
#     # print(number)
# print(count)  
  
  
# Task 7
#  Using a for loop, print the multiplication table (1 to 10) for number = 8.
# – For ilə 8-in vurma cədvəlini çap et (1-dən 10-a qədər)
# number = 8
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")
    
    
# Task 8
#  Using a while loop, start with x = 2. Repeatedly square x until x becomes larger than 1,000,000. Print the number of iterations.
# – While ilə x=2-dən başla, hər dəfə kvadrat al (x = x*x), 1,000,000-dan böyük olanadək. Neçə iterasiya olduğunu çap et.

# x = 2
# count = 0
# while x <= 1000000:
#     x = x * x
#     count += 1
# print(count)

# Task 9
#  Using a for loop, count how many numbers from 1 to 200 contain the digit “5”.
# – For ilə 1-dən 200-ə qədər ədədlərdən “5” rəqəmini ehtiva edənləri say
# count = 0
# for num in range(1, 201):
#     if "5" in str(num):
#         print(num)
#         count += 1
# print("Total numbers containing digit '5':", count)




# Task 10
#  Using a while loop, reverse a string: text = "PYTHON LOOPS". Print the reversed result.
# – While ilə text = "PYTHON LOOPS" string-inin tərsini yazdır

# text = "PYTHON LOOPS"
# reversed_text = ""
# index = len(text) - 1

# while index >= 0:
#     reversed_text += text[index]
#     index -= 1

# print(reversed_text)




# Task 11
#  Using a for loop, print all prime numbers from 2 to 200.
# – For ilə 2–200 arası sadə ədədləri çap et
# for num in range(2, 201):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)


# Task 12
#  Given: nums = [12, 14, 17, 20, 25, 30, 33]
#  Using a while loop, print each number until you reach the first number greater than 25.
# Task 13
#  Using a for loop, print a right-angled triangle of stars with height = 10.
# Task 14
#  Using a while loop, print the first 20 numbers of the Fibonacci sequence.
# Task 15
#  Using a for loop, calculate how many numbers from 1 to 500 are perfect squares.
# Task 16
#  Using a while loop, repeatedly divide n = 1_000_000 by 5 until it becomes less than 10. Print the final value and number of divisions.
# Task 17
#  Using a for loop, count how many characters in the string text = "AABBBCCCCDDDDDE" occur more than once.
# Task 18
#  Using a while loop, find the smallest number n such that 3ⁿ > 1,000,000.
# Task 19
#  Using a for loop, check how many numbers between 100 and 999 have all distinct digits.
# Task 20
#  Using a while loop, sum digits of number = 987654321 until the number becomes a single digit.
# Task 21
#  Using a for loop, print every pair (i, j) such that 1 ≤ i, j ≤ 10 AND (i + j) is even.
# Task 22
#  Using a while loop, find the first number divisible by both 13 and 17 starting from 1.
# Task 23
#  Using a for loop, compute factorial of 12.
# Task 24
#  Using a while loop, simulate bank growth: start=1000, increase by 7% every loop until money exceeds 5000. Count loops.
# Task 25
#  Using a for loop, print all palindromic numbers from 1 to 500.
# Task 26
#  Using a while loop, remove vowels from string text = "COMPUTER SCIENCE" and print result.
# Task 27
#  Using a for loop, sum up numbers between 1 and 2000 that are NOT divisible by 4, 5, or 6.
# Task 28
#  Using a while loop, find how many digits the number 9 ** 30 has.
# Task 29
#  Using a for loop, count how many numbers between 1 and 300 have a digit sum equal to 9.
# Task 30
#  Using a while loop, create a string that repeats pattern “AB” exactly 50 times.
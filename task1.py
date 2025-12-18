# Task 1 – 1-dən 200-ə qədər ədədlər, həm 4-ə, həm 6-ya bölünənlər
# for loop
for i in range(1, 201):
    if i % 4 == 0 and i % 6 == 0: # if i % 12 == 0:
        print(i)

# while loop variantı
i = 1
while i <= 200:
    if i % 12 == 0:  # 4 və 6-nın KOK-u
        print(i)
    i += 1

# Task 2 – 100-dən 1-ə, 7-yə bölünənləri atla
# while loop
i = 100
while i >= 1:
    if i % 7 != 0:
        print(i)
    i -= 1

# Task 3 – 1-dən 999-a qədər tək ədədlərin cəmi
# for loop
total = 0
for i in range(1, 1000, 2):  # tək ədədlər
    total += i
print(total)

# Task 4 – 1-dən 20-yə qədər ədədləri vur, hasil 50,000-dən çox olsa dayandır
# while loop
product = 1
i = 1
while i <= 20:
    product *= i
    if product > 50000:
        break
    i += 1
print(product)

# Task 5 – nums siyahısından 10-dan böyük ədədlər
nums = [4, 10, 3, 20, 9, 33, 7, 1]
for n in nums:
    if n > 10:
        print(n)

# Task 6 – 500-dən 3-ü çıx, neçə dəfə çıxıldı
number = 500
count = 0
while number >= 0:
    number -= 3
    count += 1
print(count)

# Task 7 – 8 üçün vurma cədvəli
number = 8
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Task 8 – x=2-ni kvadratla 1,000,000-dan böyük olana qədər
x = 2
iterations = 0
while x <= 1000000:
    x = x ** 2
    iterations += 1
print(iterations)

# Task 9 – 1-dən 200-ə qədər “5” rəqəmi olan ədədlər
count = 0
for i in range(1, 201):
    if '5' in str(i):
        count += 1
print(count)

# Task 10 – PYTHON LOOPS-u tərs çevir
text = "PYTHON LOOPS"
reversed_text = ""
i = len(text) - 1
while i >= 0:
    reversed_text += text[i]
    i -= 1
print(reversed_text)

# Task 11 – 2-dən 200-ə qədər sadə ədədlər
for num in range(2, 201):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)

# Task 12 – nums-da 25-dən böyük ilk ədədə qədər çap et
nums = [12, 14, 17, 20, 25, 30, 33]
i = 0
while i < len(nums) and nums[i] <= 25:
    print(nums[i])
    i += 1

# Task 13 – 10 səviyyəli ulduz üçbucağı
for i in range(1, 11):
    print('*' * i)

# Task 14 – Fibonacci, ilk 20 ədəd
a, b = 0, 1
count = 0
while count < 20:
    print(a)
    a, b = b, a + b
    count += 1

# Task 15 – 1-dən 500-ə qədər tam kvadrat sayı
import math
count = 0
for i in range(1, 501):
    if int(math.sqrt(i)) ** 2 == i:
        count += 1
print(count)

# Task 16 – n=1_000_000-i 5-ə böl, <10 olana qədər
n = 1_000_000
divisions = 0
while n >= 10:
    n /= 5
    divisions += 1
print(n, divisions)

# Task 17 – text-də bir neçə dəfə olan simvollar
text = "AABBBCCCCDDDDDE"
count = 0
for char in set(text):
    if text.count(char) > 1:
        count += 1
print(count)

# Task 18 – Kiçik n tap ki, 3**n > 1_000_000
n = 0
while 3**n <= 1_000_000:
    n += 1
print(n)

# Task 19 – 100-999 arası fərqli rəqəmli ədədlər
count = 0
for i in range(100, 1000):
    s = str(i)
    if len(set(s)) == 3:
        count += 1
print(count)

# Task 20 – Rəqəmlərin cəmini tək rəqəm olana qədər topla
number = 987654321
while number > 9:
    number = sum(int(d) for d in str(number))
print(number)

# Task 21 – 1 ≤ i,j ≤10, (i+j) cütdür
for i in range(1, 11):
    for j in range(1, 11):
        if (i + j) % 2 == 0:
            print(i, j)

# Task 22 – İlk ədədi 13 və 17-ə bölünən tap
n = 1
while True:
    if n % 13 == 0 and n % 17 == 0:
        print(n)
        break
    n += 1

# Task 23 – 12! faktorial
fact = 1
for i in range(1, 13):
    fact *= i
print(fact)

# Task 24 – Bank artımı, 1000-dən 5000-ə 7%
money = 1000
count = 0
while money <= 5000:
    money *= 1.07
    count += 1
print(money, count)

# Task 25 – 1-500 arası palindrom ədədlər
for i in range(1, 501):
    if str(i) == str(i)[::-1]:
        print(i)

# Task 26 – COMPUTER SCIENCE-dən saitləri çıxar
text = "COMPUTER SCIENCE"
vowels = "AEIOU"
result = ""
i = 0
while i < len(text):
    if text[i] not in vowels:
        result += text[i]
    i += 1
print(result)

# Task 27 – 1-2000 4,5,6-ya bölünməyən ədədlərin cəmi
total = 0
for i in range(1, 2001):
    if i % 4 != 0 and i % 5 != 0 and i % 6 != 0:
        total += i
print(total)

# Task 28 – 9**30-un rəqəm sayı
n = 9 ** 30
count = 0
while n > 0:
    n //= 10
    count += 1
print(count)

# Task 29 – 1-300 arası rəqəm cəmi 9 olan ədədlər
count = 0
for i in range(1, 301):
    if sum(int(d) for d in str(i)) == 9:
        count += 1
print(count)

# Task 30 – AB-i 50 dəfə təkrar et
s = ""
i = 0
while i < 50:
    s += "AB"
    i += 1
print(s)
# Task 1 Given:Create a dictionary where each number is a key and its value is how many times it appears
# Hər ədədin açar (key) olduğu və dəyərinin (value) onun neçə dəfə təkrarlandığı bir dictionary yarat.
numbers = [2, 4, 2, 5, 4, 2]

count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print(count_dict)

# Task 2 Given:Create a dictionary with names as keys and occurrence counts as values.
# Adlar key-lər olacaq və dəyərlər onların neçə dəfə təkrarlandığı value-lər olacaq.

names = ["Ali", "Veli", "Ali", "Aysel", "Veli", "Ali"]

name_count = {}

for name in names:
    if name in name_count:
        name_count[name] += 1
    else:
        name_count[name] = 1

print(name_count)

# metod 2
names = ["Ali", "Veli", "Ali", "Aysel", "Veli", "Ali"]
name_count = {}
for name in names:
    name_count[name] = name_count.get(name, 0) + 1
print(name_count)


# Task 3 Given:Create a list containing only the product names whose price is greater than 5.
# Qiyməti 5-dən böyük olan məhsul adlarını ehtiva edən bir siyahı yaradın.

prices = {"pen": 2, "book": 10, "bag": 25}
expensive_products = [product for product, price in prices.items() if price > 5]
print(expensive_products)

# metod 2
prices = {"pen": 2, "book": 10, "bag": 25}
expensive_products = []
for product, price in prices.items():
    if price > 5:
        expensive_products.append(product)
print(expensive_products)


# Task 4 Given:Create a list of students who passed, where passing score is >= 60.
# bali 60-dan boyuk olan telebenin listini yaradın

scores = {"Ali": 55, "Veli": 72, "Aysel": 91}
passed_students = [student for student, score in scores.items() if score >= 60]
print(passed_students)

# metod 2
scores = {"Ali": 55, "Veli": 72, "Aysel": 91}
passed_students = []
for student, score in scores.items():
    if score >= 60:
        passed_students.append(student)
print(passed_students)

# Task 5 Given:Create a dictionary counting how many times each character appears.
# Her hərfin neçə dəfə təkrarlandığını saymaq üçün bir dictionary yaratın.

text = "success"

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

# metod 2
text = "success"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(char_count)

# Task 6 Given:Create a dictionary where each number is a key and its value is "even" or "odd".

numbers = [1, 2, 3, 4, 5]

number_dict = {}

for num in numbers:
    if num % 2 == 0:
        number_dict[num] = "even"
    else:
        number_dict[num] = "odd"

print(number_dict)


# Task 7 Given:Create a dictionary with student names as keys and average score as values.

students = {
"Ali": [70, 80, 90],
"Veli": [60, 65, 70],
"Aysel": [90, 95, 100]
}

student_scores = {}

for student, scores in students.items():
    average_score = sum(scores) / len(scores)
    student_scores[student] = average_score

print(student_scores)


# Task 8 Given:Create a dictionary grouping words by their length.

   
words = ["apple", "bat", "banana", "car"]

word_lengths = {}

for word in words:
    length = len(word)
    if length in word_lengths:
        word_lengths[length].append(word)
    else:
        word_lengths[length] = [word]

print(word_lengths)




# Task 9 Given:Create a list of product names that are out of stock.

inventory = {"pen": 0, "book": 3, "eraser": 0, "bag": 5}

out_of_stock = [product for product, quantity in inventory.items() if quantity == 0]
print(out_of_stock)



# Task 10 Given:Create a dictionary counting how many times each word appears.-Cümlədə sözlərin sayı

sentence = "this is a test this is a test"
count_dict = {}

for word in sentence.split():
    count_dict[word] = count_dict.get(word, 0) + 1

print(count_dict)
 

# Task 11 Given:Create a dictionary where keys and values are swapped.Key ↔ Value yerini dəyiş

data = {"a": 1, "b": 2, "c": 3}

swapped_dict = {}

for key, value in data.items():
    swapped_dict[value] = key

print(swapped_dict)

# Task 13 Given:Create a list of names of people who are 18 or older.

ages = {"Ali": 17, "Veli": 22, "Aysel": 18}

adult_names = [name for name, age in ages.items() if age >= 18]
print(adult_names)

# Task 14 Given:Create a dictionary where keys are numbers and values are numbers multiplied by 3.

numbers = [3, 6, 9, 12, 15]

multiplied_dict = {}

for num in numbers:
    multiplied_dict[num] = num * 3

print(multiplied_dict)

# Task 15 Given:Create a dictionary counting each item.

items = ["pen", "book", "pen", "pen", "book"]

item_count = {}

for item in items:
    if item in item_count:
        item_count[item] += 1
    else:
        item_count[item] = 1

print(item_count)




# Task 16 Given:Create a dictionary grouping student names by grade.

students = [
{"name": "Ali", "grade": "A"},
{"name": "Veli", "grade": "B"},
{"name": "Aysel", "grade": "A"}
]

grade_dict = {}

for student in students:
    grade = student["grade"]
    if grade in grade_dict:
        grade_dict[grade].append(student["name"])
    else:
        grade_dict[grade] = [student["name"]]

print(grade_dict)


# Task 17 Given:Create a list of numbers that are divisible by 10.
numbers = [10, 15, 20, 25, 30]

divisible_by_ten = [num for num in numbers if num % 10 == 0]
print(divisible_by_ten)

divisible_by_ten =[]

for num in numbers:
    if num % 10 == 0:
        divisible_by_ten.append(num)

print(divisible_by_ten)


# Task 18 Given:Create a new dictionary that keeps only students with marks >= 50.

marks = {"Ali": 45, "Veli": 75, "Aysel": 30}

passed_students = {}

for student, mark in marks.items():
    if mark >= 50:
        passed_students[student] = mark

print(passed_students)


# Task 19 Given:Create a dictionary where keys are letters and values are lists of indexes where they appear.
letters = ["a", "b", "a", "c", "b", "a"]
result = {}
for index in range(len(letters)):
    letter= letters[index]
    if letter not in result:
        result[letter] = [index]
    else:
        result[letter].append(index)

print(f"task19: {result} ")



# Task 20 Given:Create a new dictionary representing remaining stock after selling.
products = {"pen": 2, "book": 5}
sold = {"pen": 1, "book": 2}
result = {}

for p in products :
    result[p] = products[p] - sold[p]

print(result)


# Task 21 Given:Find the key with the maximum value.

data = {"x": 10, "y": 5, "z": 20}
max_key = None
max_value = -1

for key, value in data.items():
    if value > max_value:
        max_key = key
        max_value = value

print(f"task21: {max_key}: {max_value} ")


# Task 22 Given:Create a dictionary where indexes are keys and colors are values.
colors = ["red", "green", "blue"]
result = {}

for i in range(len(colors)):
    result[i] = colors[i]

print(result)


# Task 23 Given:Create a new dictionary by summing values of common keys and keeping unique keys.

d1 = {"a": 2, "b": 3}
d2 = {"b": 4, "c": 5}

merged={}
for key in d1:
    merged[key] = d1[key]
for key in d2:
    if key not in merged:
        merged[key] = d2[key] 
# merged[key] = merged.get(key, 0) + d2[key]
    else:
        merged[key] += d2[key]
        

print(f"task23: {merged} ")



# Task 24 Given:Create a dictionary counting only vowels (a e i o u).
text = "education"
vowels = "aeiou"
result = {}
for char in text:
     if char in vowels:
        result[char] = result.get(char, 0) + 1

print( f"task24: {result} " )

text = "education"
vowels = "aeiou"
result = {}

for char in text:
    if char in vowels:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

print(f"task24: {result} " )


# Task 25 Given:Create a dictionary where keys are numbers and values are their squares, but only for even numbers.
numbers = [1, 2, 3, 4, 5, 6]
result = {}

for num in numbers:
    if num % 2 == 0:
        result[num] = num ** 2  

print(result)


# Task 26 Given:Create a dictionary where values are keys and keys are lists of original keys.
data = {"a": 1, "b": 2, "c": 1}

result = {}
for key,value in data.items():
    if value not in result:
        result[value]=[]

    result[value].append(key)

print(result) 


# Task 27 Given:Create a list of keys that appear in both dictionaries, preserving order from dict1.

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}
result = []
for k in dict1:
    if k in dict2:
         result.append(k)

print(result)

# Task 28 Given:Create a dictionary mapping each word to its length.
words = ["hi", "hello", "hey", "welcome"]
result = {}

for word in words:
    result[word] = len(word)

print(result)



# Task 29 Given:Create a new dictionary removing all keys with value 0.
values = {"a": 0, "b": 5, "c": 0, "d": 3}
new_dict = {}
for key,value in values.items():
    if value != 0:
        new_dict[key] = value

print(new_dict)



# Task 30 Given:Create a list of names who have the highest score.
scores = {"Ali": 90, "Veli": 90, "Aysel": 85}
max_score = 0
for score in scores.values():
    if score > max_score:
        max_score = score
        print(max_score)

students_high_score = []
for name,score in scores.items():
    if score == max_score:
        students_high_score.append(name)

for name in students_high_score:
    print(name,":",scores[name])


# muellimskiy solutions

# Task 1
# result = {}
# for n in numbers:
# result[n] = result.get(n, 0) + 1
# Task 2
# counts = {}
# for name in names:
# counts[name] = counts.get(name, 0) + 1
# Task 3
# expensive = []
# for item, price in prices.items():
# if price > 5:
# expensive.append(item)
# Task 4
# passed = []
# for name, score in scores.items():
# if score >= 60:
# passed.append(name)
# Task 5
# char_count = {}
# for ch in text:
# char_count[ch] = char_count.get(ch, 0) + 1
# Task 6
# parity = {}
# for n in numbers:
# if n % 2 == 0:
#     parity[n] = "even"
# else:
# parity[n] = "odd"
# Task 7
# averages = {}
# for name, marks in students.items():
# averages[name] = sum(marks) / len(marks)
# Task 8
# grouped = {}
# for word in words:
# length = len(word)
# if length not in grouped:
# grouped[length] = []
# grouped[length].append(word)
# Task 9
# out_of_stock = []
# for item, qty in inventory.items():
# if qty == 0:
# out_of_stock.append(item)
# Task 10
# word_count = {}
# for word in sentence.split():
# word_count[word] = word_count.get(word, 0) + 1
# Task 11
# swapped = {}
# for key, value in data.items():
# swapped[value] = key
# Task 12
# domains = {}
# for email in emails:
# domain = email.split("@")[1]
# domains[domain] = domains.get(domain, 0) + 1
# Task 13
# adults = []
# for name, age in ages.items():
# if age >= 18:
# adults.append(name)
# Task 14
# multiplied = {}
# for n in numbers:
# multiplied[n] = n * 3
# Task 15
# item_count = {}
# for item in items:
# item_count[item] = item_count.get(item, 0) + 1
# Task 16
# by_grade = {}
# for student in students:
# grade = student["grade"]
# if grade not in by_grade:
# by_grade[grade] = []
# by_grade[grade].append(student["name"])
# Task 17
# div_by_10 = []
# for n in numbers:
# if n % 10 == 0:
# div_by_10.append(n)
# Task 18
# filtered = {}
# for name, mark in marks.items():
# if mark >= 50:
# filtered[name] = mark
# Task 19
# positions = {}
# for index in range(len(letters)):
# letter = letters[index]
# if letter not in positions:
# positions[letter] = []
# positions[letter].append(index)
# Task 20
# remaining = {}
# for item in products:
# remaining[item] = products[item] - sold.get(item, 0)
# Task 21
# max_key = None
# max_value = -1
# for key, value in data.items():
# if value > max_value:
# max_value = value
# max_key = key
# Task 22
# indexed = {}
# for i in range(len(colors)):
# indexed[i] = colors[i]
# Task 23
# merged = {}
# for key in d1:
# merged[key] = d1[key]
# for key in d2:
# merged[key] = merged.get(key, 0) + d2[key]
# Task 24
# vowels = {}
# for ch in text:
# if ch in "aeiou":
# vowels[ch] = vowels.get(ch, 0) + 1
# Task 25
# squares = {}
# for n in numbers:
# if n % 2 == 0:
# squares[n] = n * n
# Task 26
# inverted = {}
# for key, value in data.items():
# if value not in inverted:
# inverted[value] = []
# inverted[value].append(key)
# Task 27
# common = []
# for key in dict1:
# if key in dict2:
# common.append(key)
# Task 28
# lengths = {}
# for word in words:
# lengths[word] = len(word)
# Task 29
# cleaned = {}
# for key, value in values.items():
# if value != 0:
# cleaned[key] = value
# Task 30
# max_score = max(scores.values())
# top_students = []
# for name, score in scores.items():
# if score == max_score:
# top_students.append(name)
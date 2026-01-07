# Lambdas funksiyasi:P
# lambda argument: expression

# map = dəyişdir.Listin hər elementini götürüb dəyişir

# Sintaksis:map(function, iterable)

# numbers = [1, 2, 3]

# result = map(lambda x: x * 2, numbers)
# print(list(result))  # [2, 4, 6]


# filter = seç.Şərtə uyğun olanları saxlayır

# Sintaksis:filter(function, iterable)

# numbers = [1, 2, 3, 4, 5]

# result = filter(lambda x: x % 2 == 0, numbers)
# print(list(result))  # [2, 4]


# 10-dan böyük ədədlərin kvadratı
# numbers = [5, 10, 15, 20]

# result = map(
#     lambda x: x * x,
#     filter(lambda x: x > 10, numbers)
# )

# print(list(result))  # [225, 400]

# map / filter olmadan (for loop ilə)
# map yerinə
# result = []
# for x in numbers:
#     result.append(x * 2)

# # filter yerinə
# result = []
# for x in numbers:
#     if x % 2 == 0:
#         result.append(x)


# 📌 for loop = əsas,map/filter = qısa yazılış

# map(lambda dəyiş,
#     filter(lambda şərt, data))




# TASK
# Task 1 Given numbers = [1, 2, 3, 4, 5, 6], keep even numbers and double them.

numbers = [1, 2, 3, 4, 5, 6]
result = map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers))
print(list(result))

# Task 2 Given numbers = [-3, -1, 0, 2, 4], keep positive numbers and convert them to strings.

numbers = [-3, -1, 0, 2, 4]
result = map(str, filter(lambda x: x > 0, numbers))
print(list(result))

# Task 3 Given words = ["hi", "hello", "python", "go"], keep words longer than 3 characters and convert them to uppercase.

words = ["hi", "hello", "python", "go"]
result = map(str.upper, filter(lambda x: len(x) > 3, words))
print(list(result))


# Task 4 Given numbers = [10, 15, 20, 25], keep numbers divisible by 5 and subtract 1.

numbers = [10, 15, 20, 25]
result = map(lambda x: x - 1, filter(lambda x: x % 5 == 0, numbers))
print(list(result))

# Task 5 Given names = ["ali", "Bob", "eve", "John"], keep lowercase names and capitalize them.

names = ["ali", "Bob", "eve", "John"]
result = list(map(lambda x: x.capitalize(), filter(lambda x: x.islower(), names)))
print(list(result))

# Task 6 Given numbers = [1, 2, 3, 4, 5], keep odd numbers and label them as "odd:<number>".

numbers = [1, 2, 3, 4, 5]
result = map(lambda x: f"odd:{x}", filter(lambda x: x % 2 != 0, numbers))
print(list(result))


# Task 7 Given words = ["level", "code", "madam", "python"], keep palindromes and return their lengths.

words = ["level", "code", "madam", "python"]
result = map(len, filter(lambda x: x == x[::-1], words))
print(list(result))

# Task 8 Given prices = [50, 120, 200, 80], keep prices above 100 and apply a 20% discount.

prices = [50, 120, 200, 80]
result = map(lambda x: x * 0.8, filter(lambda x: x > 100, prices))
print(list(result))

# Task 9 Given numbers = [-10, -5, 0, 5, 10], keep non-zero numbers and return absolute values.

numbers = [-10, -5, 0, 5, 10]
result = map(abs, filter(lambda x: x != 0, numbers))
print(list(result))

# Task 10 Given scores = [30, 45, 60, 75, 90], keep passing scores (≥50) and divide by 10.

scores = [30, 45, 60, 75, 90]
result = map(lambda x: x / 10, filter(lambda x: x >= 50, scores))
print(list(result))

# Task 11 Given data = {"a": 10, "b": 3, "c": 8}, keep values greater than 5 and square them.

data = {"a": 10, "b": 3, "c": 8}
result = map(lambda x: x * x, filter(lambda x: x > 5, data.values()))
print(list(result))

# Task 12 Given data = {"apple": 5, "banana": 2, "cherry": 7}, keep fruits with quantity ≥5 and return their names.

data= {"apple": 5, "banana": 2, "cherry": 7}
result = map(lambda x: x, filter(lambda x: x[1] >= 5, data.items()))
print(list(result))

# Task 13 Given data = {"Ali": 80, "Bob": 45, "Eve": 90}, keep passing students and return "Name:Score".

data = {"Ali": 80, "Bob": 45, "Eve": 90}
result = map(lambda x: f"{x[0]}:{x[1]}", filter(lambda x: x[1] >= 50, data.items()))
print(list(result))

# Task 14 Given data = {"x": -3, "y": 0, "z": 4}, keep non-zero values and return absolute values.
data = {"x": -3, "y": 0, "z": 4}
result = map(abs, filter(lambda x: x != 0, data.values()))
print(list(result))

# result = dict(
#     map(lambda item: (item[0], abs(item[1])),
#         filter(lambda item: item[1] != 0, data.items()))
# )

# print(result)
# Task 15 Given data = {"A": 100, "B": 200, "C": 50}, keep values ≥100 and apply 10% tax.

data = {"A": 100, "B": 200, "C": 50}
result = map(lambda x: x * 1.1, filter(lambda x: x >= 100, data.values()))
print(list(result))

# Task 16 Given data = {"dog": 3, "cat": 4, "elephant": 8}, keep words longer than 3 letters and return their lengths.
data = {"dog": 3, "cat": 4, "elephant": 8}
result = map(len, filter(lambda x: len(x) > 3, data.keys()))
print(list(result))


# Task 17 Given data = {"p1": 10, "p2": 25, "p3": 30}, keep values ≥20 and subtract 5.

data = {"p1": 10, "p2": 25, "p3": 30}
result = map(lambda x: x - 5, filter(lambda x: x >= 20, data.values()))
print(list(result))


# Task 18 Given data = {"Anna": 22, "Bob": 17, "Chris": 30}, keep adults (≥18) and return uppercase names.

data = {"Anna": 22, "Bob": 17, "Chris": 30}
result = map(lambda x: x[0].upper(), filter(lambda x: x[1] >= 18, data.items()))
print(list(result))

# Task 19 Given data = {"x": 2, "y": 3, "z": 4}, keep even values and cube them.

data = {"x": 2, "y": 3, "z": 4}
result = map(lambda x: x * x * x, filter(lambda x: x % 2 == 0, data.values()))
print(list(result))

# Task 20 Given data = {"a": "hi", "b": "hello", "c": "hey"}, keep strings longer than 3 and uppercase them.

data = {"a": "hi", "b": "hello", "c": "hey"}
result = map(lambda x: x.upper(), filter(lambda x: len(x) > 3, data.values()))
print(list(result))


# Task 21 Given records = [("Ali", 80), ("Bob", 40), ("Eve", 90)], keep passing scores and return names.

records = [("Ali", 80), ("Bob", 40), ("Eve", 90)]
result = map(lambda x: x[0], filter(lambda x: x[1] >= 50, records))
print(list(result))

# Task 22 Given records = [("apple", 5), ("banana", 2), ("cherry", 8)], keep quantities ≥5 and double them.
records = [("apple", 5), ("banana", 2), ("cherry", 8)]
result = map(lambda x: x[1] * 2, filter(lambda x: x[1] >= 5, records))
print(list(result)) 

# Task 23 Given records = [("x", -2), ("y", 0), ("z", 3)], keep non-zero values and return absolute values.

records = [("x", -2), ("y", 0), ("z", 3)]
result = map(lambda x: abs(x[1]), filter(lambda x: x[1] != 0, records))
print(list(result))

# Task 24 Given records = [("John", 25), ("Anna", 17), ("Mike", 30)], keep adults and return names in lowercase.

records = [("John", 25), ("Anna", 17), ("Mike", 30)]
result = map(lambda x: x[0].lower(), filter(lambda x: x[1] >= 18, records)) 
print(list(result))

# Task 25 Given records = [("A", 100), ("B", 200), ("C", 50)], keep values ≥100 and divide by 10.

records = [("A", 100), ("B", 200), ("C", 50)]
result = map(lambda x: x[1] / 10, filter(lambda x: x[1] >= 100, records))
print(list(result))

# Task 26 Given records = [("cat", 3), ("elephant", 8), ("dog", 3)], keep animals with name length >3 and return name lengths.

records = [("cat", 3), ("elephant", 8), ("dog", 3)]
result = map(lambda x: len(x[0]), filter(lambda x: len(x[0]) > 3, records))
print(list(result))

# Task 27 Given records = [("p1", 10), ("p2", 20), ("p3", 30)], keep values ≥20 and label as "id:value".

records = [("p1", 10), ("p2", 20), ("p3", 30)]
result = map(lambda x: f"id:{x[0]} value:{x[1]}", filter(lambda x: x[1] >= 20, records))
print(list(result))

# Task 28 Given records = [("x", 2), ("y", 3), ("z", 4)], keep even values and return booleans.

records = [("x", 2), ("y", 3), ("z", 4)]
result = map(lambda x: x[1] % 2 == 0, filter(lambda x: x[1] % 2 == 0, records))
print(list(result))

# Task 29 Given records = [("Ali", 80), ("Bob", 45), ("Eve", 90)], keep failing students and return names.

records = [("Ali", 80), ("Bob", 45), ("Eve", 90)]
result = map(lambda x: x[0], filter(lambda x: x[1] < 50, records))
print(list(result))

# Task 30 Given records = [("a", "level"), ("b", "code"), ("c", "madam")], keep palindromes and uppercase them.

records = [("a", "level"), ("b", "code"), ("c", "madam")]
result = map(lambda x: x[1].upper(), filter(lambda x: x[1] == x[1][::-1], records))
print(list(result))

# muellimskiy task solution
# Task 1
# result = list(map(lambda x: x*2, filter(lambda x: x % 2 == 0, numbers)))
# Task 2
# result = list(map(lambda x: str(x), filter(lambda x: x > 0, numbers)))
# Task 3
# result = list(map(lambda w: w.upper(), filter(lambda w: len(w) > 3, words)))
# Task 4
# result = list(map(lambda x: x-1, filter(lambda x: x % 5 == 0, numbers)))
# Task 5
# result = list(map(lambda n: n.capitalize(), filter(lambda n: n.islower(), names)))
# Task 6
# result = list(map(lambda x: f"odd:{x}", filter(lambda x: x % 2 != 0, numbers)))
# Task 7
# result = list(map(lambda w: len(w), filter(lambda w: w == w[::-1], words)))
# Task 8
# result = list(map(lambda p: p*0.8, filter(lambda p: p > 100, prices)))
# Task 9
# result = list(map(lambda x: abs(x), filter(lambda x: x != 0, numbers)))
# Task 10
# result = list(map(lambda s: s/10, filter(lambda s: s >= 50, scores)))
# Task 11
# result = list(map(lambda v: v*v, filter(lambda v: v > 5, data.values())))
# Task 12
# result = list(map(lambda i: i[0], filter(lambda i: i[1] >= 5, data.items())))
# Task 13
# result = list(map(lambda i: f"{i[0]}:{i[1]}", filter(lambda i: i[1] >= 50, data.items())))
# Task 14
# result = list(map(lambda i: abs(i[1]), filter(lambda i: i[1] != 0, data.items())))
# Task 15
# result = list(map(lambda v: v*1.1, filter(lambda v: v >= 100, data.values())))
# Task 16
# result = list(map(lambda i: len(i[0]), filter(lambda i: len(i[0]) > 3, data.items())))
# Task 17
# result = list(map(lambda v: v-5, filter(lambda v: v >= 20, data.values())))
# Task 18
# result = list(map(lambda i: i[0].upper(), filter(lambda i: i[1] >= 18, data.items())))
# Task 19
# result = list(map(lambda v: v**3, filter(lambda v: v % 2 == 0, data.values())))
# Task 20
# result = list(map(lambda v: v.upper(), filter(lambda v: len(v) > 3, data.values())))
# Task 21
# result = list(map(lambda r: r[0], filter(lambda r: r[1] >= 50, records)))
# Task 22
# result = list(map(lambda r: r[1]*2, filter(lambda r: r[1] >= 5, records)))
# Task 23
# result = list(map(lambda r: abs(r[1]), filter(lambda r: r[1] != 0, records)))
# Task 24
# result = list(map(lambda r: r[0].lower(), filter(lambda r: r[1] >= 18, records)))
# Task 25
# result = list(map(lambda r: r[1]/10, filter(lambda r: r[1] >= 100, records)))
# Task 26
# result = list(map(lambda r: len(r[0]), filter(lambda r: len(r[0]) > 3, records)))
# Task 27
# result = list(map(lambda r: f"{r[0]}:{r[1]}", filter(lambda r: r[1] >= 20, records)))
# Task 28
# result = list(map(lambda r: r[1] % 2 == 0, filter(lambda r: r[1] % 2 == 0, records)))
# Task 29
# result = list(map(lambda r: r[0], filter(lambda r: r[1] < 50, records)))
# Task 30
# result = list(map(lambda r: r[1].upper(), filter(lambda r: r[1] == r[1][::-1], records)))

# TASK2

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = list(
#     map(lambda row:
#         list(map(lambda x: DƏYİŞİM, row)),
#         matrix)
# )


# Task 1 Given matrix = [[1, 2], [3, 4], [5, 6]], square every number using nested map.
matrix= [[1, 2], [3, 4], [5, 6]]
result=list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
print(result)


# Task 2 Given matrix = [[-1, 2], [-3, 4]], convert all numbers to their absolute values.

matrix = [[-1, 2], [-3, 4]]
result = list(map(lambda row: list(map(abs, row)), matrix))
print(result)

# Task 3 Given data = [[1, 2, 3], [4, 5], [6]], multiply every number by 10.

data = [[1, 2, 3], [4, 5], [6]]
result = list(map(lambda row: list(map(lambda x: x * 10, row)), data))
print(result)

# Task 4 Given words = [["hi", "hello"], ["python", "go"]], convert all words to uppercase.

words = [["hi", "hello"], ["python", "go"]]
result = list(map(lambda row: list(map(lambda x: x.upper(), row)), words))
print(result)

# Task 5 Given records = [[("Ali", 80), ("Bob", 40)], [("Eve", 90)]], extract only the names.

records = [[("Ali", 80), ("Bob", 40)], [("Eve", 90)]]
result = list(map(lambda row: list(map(lambda x: x[0], row)), records))
print(result)

# Task 6 Given matrix = [[1, 2, 3], [4, 5, 6]], replace each number with "even" or "odd".

matrix = [[1, 2, 3], [4, 5, 6]]
result = list(map(lambda row: list(map(lambda x: "even" if x % 2 == 0 else "odd", row)), matrix))
print(result)


# Task 7 Given data = [[10, 20], [30, 40]], subtract 5 from each element.

data = [[10, 20], [30, 40]]
result = list(map(lambda row: list(map(lambda x: x - 5, row)), data))
print(result)

# Task 8 Given words = [["level", "code"], ["madam", "python"]], convert each word to True if palindrome else False.

words = [["level", "code"], ["madam", "python"]]
result = list(map(lambda row: list(map(lambda x: x == x[::-1], row)), words))
print(result)

# Task 9 Given records = [[("a", 1), ("b", 2)], [("c", 3)]], extract only the values.

records = [[("a", 1), ("b", 2)], [("c", 3)]]
result = list(map(lambda row: list(map(lambda x: x[1], row)), records))
print(result)

# Task 10 Given matrix = [[1, -2], [-3, 4]], convert each number to its sign (-1, 0, 1).
matrix = [[1, -2], [-3, 4]]
result = list(map(lambda row: list(map(lambda x: -1 if x < 0 else 1 if x > 0 else 0, row)), matrix))
print(result)

# Task 11 Given data = [{"a": 1, "b": 2}, {"c": 3}], extract all dictionary values and double them.

data = [{"a": 1, "b": 2}, {"c": 3}]
result = list(map(lambda row: list(map(lambda x: x * 2, row.values())), data))
print(result)

# Task 12 Given scores = [[45, 78], [90, 32]], convert scores to "pass" or "fail" (≥50).

scores = [[45, 78], [90, 32]]
result = list(map(lambda row: list(map(lambda x: "pass" if x >= 50 else "fail", row)), scores))
print(result)

# Task 13 Given words = [["hi", "world"], ["python"]], replace each word with its length.

words = [["hi", "world"], ["python"]]
result = list(map(lambda row: list(map(len, row)), words))
print(result)

# Task 14 Given data = [[("x", 10), ("y", 20)], [("z", 30)]], extract keys and uppercase them.

data = [[("x", 10), ("y", 20)], [("z", 30)]]
result = list(map(lambda row: list(map(lambda x: x[0].upper(), row)), data))
print(result)

# Task 15 Given matrix = [[1, 4], [9, 16]], convert numbers to square roots.
matrix = [[1, 4], [9, 16]]
result = list(map(lambda row: list(map(lambda x: x ** 0.5, row)), matrix))
print(result)

# Task 16 Given prices = [[100, 200], [50]], apply 10% discount to all prices.

prices = [[100, 200], [50]]
result = list(map(lambda row: list(map(lambda x: x * 0.9, row)), prices))
print(result)

# Task 17 Given data = [[("Ali", 80)], [("Bob", 45), ("Eve", 90)]], extract scores only.

data = [[("Ali", 80)], [("Bob", 45), ("Eve", 90)]]
result = list(map(lambda row: list(map(lambda x: x[1], row)), data))
print(result)

# Task 18 Given matrix = [[1, 2], [3, 4]], replace each number with its multiplication by its row index (0-based).

matrix = [[1, 2], [3, 4]]
result = list(map(lambda row: list(map(lambda x: x * row.index(x), row)), matrix))
print(result)

# Task 19 Given words = [["sun", "moon"], ["star"]], append "!" to every word.

words = [["sun", "moon"], ["star"]]
result = list(map(lambda row: list(map(lambda x: x + "!", row)), words))
print(result)

# Task 20 Given data = [[("a", "level")], [("b", "code"), ("c", "madam")]], extract values and uppercase palindromes only (non-palindromes still included but unchanged).

data = [[("a", "level")], [("b", "code"), ("c", "madam")]]
result = list(map(lambda row: list(map(lambda x: x[1].upper() if x[1] == x[1][::-1] else x[1], row)), data))
print(result)

# muellimskiy task solution
# Task 1
# result = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
# Task 2
# result = list(map(lambda row: list(map(lambda x: abs(x), row)), matrix))
# Task 3
# result = list(map(lambda row: list(map(lambda x: x*10, row)), data))
# Task 4
# result = list(map(lambda row: list(map(lambda w: w.upper(), row)), words))
# Task 5
# result = list(map(lambda row: list(map(lambda r: r[0], row)), records))
# Task 6
# result = list(map(lambda row: list(map(lambda x: "even" if x % 2 == 0 else "odd", row)), matrix))
# Task 7
# result = list(map(lambda row: list(map(lambda x: x-5, row)), data))
# Task 8
# result = list(map(lambda row: list(map(lambda w: w == w[::-1], row)), words))
# Task 9
# result = list(map(lambda row: list(map(lambda r: r[1], row)), records))
# Task 10
# result = list(map(lambda row: list(map(lambda x: -1 if x < 0 else (1 if x > 0 else 0), row)), matrix))
# Task 11
# result = list(map(lambda d: list(map(lambda v: v*2, d.values())), data))
# Task 12
# result = list(map(lambda row: list(map(lambda s: "pass" if s >= 50 else "fail", row)), scores))
# Task 13
# result = list(map(lambda row: list(map(lambda w: len(w), row)), words))
# Task 14
# result = list(map(lambda row: list(map(lambda r: r[0].upper(), row)), data))
# Task 15
# result = list(map(lambda row: list(map(lambda x: x**0.5, row)), matrix))
# Task 16
# result = list(map(lambda row: list(map(lambda p: p*0.9, row)), prices))
# Task 17
# result = list(map(lambda row: list(map(lambda r: r[1], row)), data))
# Task 18
# result = list(map(lambda i: list(map(lambda x: x*i[0], i[1])), enumerate(matrix)))
# Task 19
# result = list(map(lambda row: list(map(lambda w: w + "!", row)), words))
# Task 20
# result = list(map(lambda row: list(map(lambda r: r[1].upper() if r[1] == r[1][::-1] else r[1], row)), data))

# TASK3

# Task 1 Given matrix = [[1, 2, 3], [4, 5, 6]], keep even numbers in each row and square them.

matrix = [[1, 2, 3], [4, 5, 6]]
result = list(map(lambda row: list(map(lambda x: x ** 2 if x % 2 == 0 else x, row)), matrix))
print(result)

# Task 2 Given matrix = [[-3, -2, 1], [0, 4, 5]], remove non-positive numbers and double the rest.

matrix = [[-3, -2, 1], [0, 4, 5]]
result = list(map(lambda row: list(map(lambda x: x * 2 if x > 0 else x, row)), matrix))
print(result)

# Task 3 Given words = [["hi", "hello"], ["python", "go"]], keep words longer than 3 letters and uppercase them.

words = [["hi", "hello"], ["python", "go"]]
result = list(map(lambda row: list(map(lambda x: x.upper() if len(x) > 3 else x, row)), words))
print(result)

# Task 4 Given records = [[("Ali", 80), ("Bob", 40)], [("Eve", 90)]], keep passing students and return their names.

records = [[("Ali", 80), ("Bob", 40)], [("Eve", 90)]]
result = list(map(lambda row: list(map(lambda x: x[0] if x[1] >= 50 else None, row)), records))
print(result)

# Task 5 Given matrix = [[1, 2], [3, 4]], keep odd numbers and label them "odd:<number>".

matrix = [[1, 2], [3, 4]]
result = list(map(lambda row: list(map(lambda x: f"odd:{x}" if x % 2 != 0 else x, row)), matrix))
print(result)

# Task 6 Given data = [[10, 15], [20, 25]], keep numbers divisible by 5 and subtract 2.

data = [[10, 15], [20, 25]] 
result = list(map(lambda row: list(map(lambda x: x - 2 if x % 5 == 0 else x, row)), data))
print(result)

# Task 7 Given words = [["level", "code"], ["madam", "python"]], keep palindromes and return their lengths.

words = [["level", "code"], ["madam", "python"]]
result = list(map(lambda row: list(map(lambda x: len(x) if x == x[::-1] else x, row)), words))
print(result)

# Task 8 Given records = [[("a", 1), ("b", 2)], [("c", 3)]], keep values greater than 1 and cube them.
records = [[("a", 1), ("b", 2)], [("c", 3)]]
result = list(map(lambda row: list(map(lambda x: x[1] ** 3 if x[1] > 1 else x[1], row)), records))  
print(result)

# Task 9 Given matrix = [[-1, 2], [-3, 4]], keep positive numbers and return booleans indicating evenness.

matrix = [[-1, 2], [-3, 4]]
result = list(map(lambda row: list(map(lambda x: x % 2 == 0, row)), matrix))
print(result)

# Task 10 Given prices = [[50, 120], [200, 80]], keep prices above 100 and apply 15% discount.

prices = [[50, 120], [200, 80]]
result = list(map(lambda row: list(map(lambda x: x * 0.85 if x > 100 else x, row)), prices))
print(result)

# Task 11 Given data = [{"a": 1, "b": 2}, {"c": 3, "d": 0}], keep values >1 and multiply by 10.

data = [{"a": 1, "b": 2}, {"c": 3, "d": 0}]
result = list(map(lambda x: {k: v * 10 for k, v in x.items() if v > 1}, data))
print(result)

# Task 12 Given scores = [[45, 78], [90, 32]], keep passing scores and divide by 3.

scores = [[45, 78], [90, 32]]
result = list(map(lambda row: list(map(lambda x: x / 3 if x >= 50 else x, row)), scores))
print(result)

# Task 13 Given words = [["hi", "world"], ["python", "go"]], keep words containing "o" and uppercase them.

words = [["hi", "world"], ["python", "go"]]
result = list(map(lambda row: list(map(lambda x: x.upper() if "o" in x else x, row)), words))
print(result)

# Task 14 Given records = [[("x", 10), ("y", 20)], [("z", 5)]], keep values ≥10 and return "key:value".

records = [[("x", 10), ("y", 20)], [("z", 5)]]
result = list(map(lambda row: list(map(lambda x: f"{x[0]}:{x[1]}", row)), records))
print(result)

# Task 15 Given matrix = [[1, 4], [9, 16]], keep numbers >5 and compute square roots.

matrix = [[1, 4], [9, 16]]
result = list(map(lambda row: list(map(lambda x: x ** 0.5 if x > 5 else x, row)), matrix))
print(result)

# Task 16 Given data = [[("Ali", 80)], [("Bob", 45), ("Eve", 90)]], keep scores ≥50 and return lowercase names.
data = [[("Ali", 80)], [("Bob", 45), ("Eve", 90)]]
result = list(map(lambda row: list(map(lambda x: x[0].lower() if x[1] >= 50 else x[0], row)), data))
print(result)

# Task 17 Given words = [["sun", "moon"], ["star"]], keep words with length >3 and append "!".

words = [["sun", "moon"], ["star"]]
result = list(map(lambda row: list(map(lambda x: x + "!" if len(x) > 3 else x, row)), words))
print(result)

# Task 18 Given matrix = [[1, 2], [3, 4]], keep numbers whose row index is even and multiply by 10.

matrix = [[1, 2], [3, 4]]
result = list(map(lambda row: list(map(lambda x: x * 10 if row.index(x) % 2 == 0 else x, row)), matrix))
print(result)

# Task 19 Given records = [[("a", -1), ("b", 2)], [("c", -3)]], keep positive values and return absolute values.

records = [[("a", -1), ("b", 2)], [("c", -3)]]
result = list(map(lambda row: list(map(lambda x: abs(x[1]) if x[1] > 0 else x[1], row)), records))
print(result)   
# Task 20 Given data = [[("x", "level")],[("y", "code"), ("z", "madam")]], keep palindromes and uppercase them.

data = [[("x", "level")],[("y", "code"), ("z", "madam")]]
result = list(map(lambda row: list(map(lambda x: x[1].upper() if x[1] == x[1][::-1] else x[1], row)), data))
print(result)


# muellimskiy task solution

# Task 1
# result = list(map(lambda r: list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, r))), matrix))
# Task 2
# result = list(map(lambda r: list(map(lambda x: x*2, filter(lambda x: x > 0, r))), matrix))
# Task 3
# result = list(map(lambda r: list(map(lambda w: w.upper(), filter(lambda w: len(w) > 3, r))), words))
# Task 4
# result = list(map(lambda r: list(map(lambda s: s[0], filter(lambda s: s[1] >= 50, r))), records))
# Task 5
# result = list(map(lambda r: list(map(lambda x: f"odd:{x}", filter(lambda x: x % 2 != 0, r))), matrix))
# Task 6
# result = list(map(lambda r: list(map(lambda x: x-2, filter(lambda x: x % 5 == 0, r))), data))
# Task 7
# result = list(map(lambda r: list(map(lambda w: len(w), filter(lambda w: w == w[::-1], r))), words))
# Task 8
# result = list(map(lambda r: list(map(lambda v: v**3, filter(lambda v: v > 1, map(lambda x: x[1], r)))), records))
# Task 9
# result = list(map(lambda r: list(map(lambda x: x % 2 == 0, filter(lambda x: x > 0, r))), matrix))
# Task 10
# result = list(map(lambda r: list(map(lambda p: p*0.85, filter(lambda p: p > 100, r))), prices))
# Task 11
# result = list(map(lambda d: list(map(lambda v: v*10, filter(lambda v: v > 1, d.values()))), data))
# Task 12
# result = list(map(lambda r: list(map(lambda s: s/3, filter(lambda s: s >= 50, r))), scores))
# Task 13
# result = list(map(lambda r: list(map(lambda w: w.upper(), filter(lambda w: "o" in w, r))), words))
# Task 14
# result = list(map(lambda r: list(map(lambda i: f"{i[0]}:{i[1]}", filter(lambda i: i[1] >= 10, r))), records))
# Task 15
# result = list(map(lambda r: list(map(lambda x: x**0.5, filter(lambda x: x > 5, r))), matrix))
# Task 16
# result = list(map(lambda r: list(map(lambda s: s[0].lower(), filter(lambda s: s[1] >= 50, r))), data))
# Task 17
# result = list(map(lambda r: list(map(lambda w: w+"!", filter(lambda w: len(w) > 3, r))), words))
# Task 18
# result = list(map(lambda i: list(map(lambda x: x*10, filter(lambda _: i[0] % 2 == 0, i[1]))), enumerate(matrix)))
# Task 19
# result = list(map(lambda r: list(map(lambda v: abs(v), filter(lambda v: v > 0, map(lambda x: x[1], r)))), records))
# Task 20
# result = list(map(lambda r: list(map(lambda i: i[1].upper(), filter(lambda i: i[1] == i[1][::-1], r))), data))

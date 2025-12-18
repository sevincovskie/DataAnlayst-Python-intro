# Task 1
# Given the list: [5, 2, 5, 7, 2, 9, 5, 2] Remove elements from the right side until the list contains no duplicates.
from asyncio import Task


list1 = [5, 2, 5, 7, 2, 9, 5, 2]
seen = set()
unique_list = []
for item in reversed(list1):
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
unique_list.reverse()
print(unique_list)


# 2ci variant
data = [5, 2, 5, 7, 2, 9, 5, 2]

while True:
    ok = True
    for x in data:
        if data.count(x) > 1:
            ok = False
    if ok:
        break
    data.pop()

print(data)


# Task 2
# Given the list: [3, 1, 3, 2, 3, 1] Create a new list where each element is repeated as many times as it appears in the original list.
list2 = [3, 1, 3, 2, 3, 1]
result = []
for item in list2:
    count = list2.count(item)
for _ in range(count):
        result.append(item)
print(result)

# Task 3
# Given the list: [10, 20, 30, 40, 50] Reverse the list using only pop and append (no slicing).
list3 = [10, 20, 30, 40, 50]
reversed_list = []
while list3:
    reversed_list.append(list3.pop())
print(reversed_list)    

# Task 4
# Given the list: [4,4,7,4,7,7,4,7] Remove every second occurrence of each number. Example: keep 1st, remove 2nd, keep 3rd, remove 4th…
     

data = [4,4,7,4,7,7,4,7]
result = []
counted = []

for x in data:
    if x not in counted:
        counted.append(x)
    c = result.count(x)
    if c % 2 == 0:
        result.append(x)

print(result)

# Task 5
# Interleave these two lists: [1, 3, 5, 7] [2, 4, 6] Result alternates: 1,2,3,4,5,6,7.
list5_a = [1, 3, 5, 7]
list5_b = [2, 4, 6]
result = []         
max_length = max(len(list5_a), len(list5_b))
for i in range(max_length):
    if i < len(list5_a):
        result.append(list5_a[i])
    if i < len(list5_b):
        result.append(list5_b[i])                    
print(result)

# Task 6
# Given the list: [9, 4, 9, 1, 4, 1, 1] Count how many times the smallest number appears. (do NOT use min())
list6 = [9, 4, 9, 1, 4, 1, 1]
smallest = list6[0]
count = 0
for num in list6:
    if num < smallest:
        smallest = num    
for num in list6:
    if num == smallest:
        count += 1         
print(count)

# Task 7
# Given the list: [1, 2, 3, 4, 5] Rotate it right by 3 steps using only pop + append.
list7 = [1, 2, 3, 4, 5]
steps = 3
for _ in range(steps):
    list7.insert(0, list7.pop())        
print(list7)

# Task 8
# Given the list: [2,2,2,3,3,4,4,4,4,5] Remove all numbers that appear more than 3 times.
list8 = [2,2,2,3,3,4,4,4,4,5]
result = []
seen = {}       
for num in list8:
    if num in seen:
        seen[num] += 1
    else:
        seen[num] = 1
for num in list8:
    if seen[num] <= 3:
        result.append(num)
print(result)


# Task 9
# Flatten this nested list using only loops + extend: [[1,2],[3,4,5],[6],[7,8,9]]
list9= [[1,2],[3,4,5],[6],[7,8,9]]
flattened = []
for sublist in list9:
 for item in sublist:
        flattened.append(item)
print(flattened)    

# Task 10
# Given the list: [2, 4, 6, 1] Build the cumulative-sum list: → [2, 6, 12, 13]

list10 = [2, 4, 6, 1]
cumulative_sum = [] 
current_sum = 0
for num in list10:
    current_sum += num
    cumulative_sum.append(current_sum)

print(cumulative_sum)
# Task 11
# Given the list: [5, 5, 3, 2, 8] Remove elements from the left until the sum of remaining elements is even.
list11 = [5, 5, 3, 2, 8]
while sum(list11) % 2 != 0:
    list11.pop(0)           
print(list11)

# Task 12
# Given the list: [7,7,7,2,2,3,3,3,3,1] Find the longest consecutive streak of equal numbers.
list12 = [7,7,7,2,2,3,3,3,3,1]
max_streak = 1
current_streak = 1
for i in range(1, len(list12)):
    if list12[i] == list12[i - 1]:
        current_streak += 1
        if current_streak > max_streak:
            max_streak = current_streak
    else:
        current_streak = 1  
print(max_streak)

# Task 13
# Given the list of words: ["car", "window", "to", "pan", "glass", "hi"] Remove all words shorter than: (length of longest word) − 1
list13 = ["car", "window", "to", "pan", "glass", "hi"]
longest_length = 0
for word in list13:
    if len(word) > longest_length:
        longest_length = len(word)
for word in list13:
    if len(word) < longest_length - 1:
        list13.remove(word)
print(list13)   


# Task 14
# Given the list: [8, 12, 3, 29, 17, 29, 4] Find the two largest numbers (no max()).
list14 = [8, 12, 3, 29, 17, 29, 4]
first_largest = second_largest = float('-inf')  
for num in list14:                  
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest and num != first_largest:
        second_largest = num    
print(first_largest, second_largest)


# Task 15
# Given the list: [9, 8, 7, 6, 5, 4, 3] Create a new list of elements whose index is divisible by 3.
list15 = [9, 8, 7, 6, 5, 4, 3]
result = []
for i in range(len(list15)):
    if i % 3 == 0:
        result.append(list15[i])                
print(result)

# Task 16
# Given the list: [9, 4, 3, 7, 6, 2] Repeatedly pop from the right until the sum is below 20.
list16 = [9, 4, 3, 7, 6, 2]
while sum(list16) >= 20:
    list16.pop()
print(list16)       

# Task 17
# Given the list: [4, -2, -7, 5, -7, 3] Replace all negative numbers with the absolute value of the smallest negative number.
list17 = [4, -2, -7, 5, -7, 3]
smallest_negative = 0
for num in list17:
    if num < smallest_negative:
        smallest_negative = num     
print(list17)   
for i in range(len(list17)):
    if list17[i] < 0:
        list17[i] = abs(smallest_negative)      
print(list17)

# Task 18
# Given the list: [6,6,1,2,6,3,2,1] Create a list of all indexes where the most frequent element appears.
list18 = [6,6,1,2,6,3,2,1]
frequency = {}      
for num in list18:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
max_frequency = max(frequency.values())         
most_frequent = [num for num, freq in frequency.items() if freq == max_frequency]
indexes = []
for i in range(len(list18)):
    if list18[i] in most_frequent:
        indexes.append(i)    
print(indexes)

# Task 19
# Given the list: [9, 1, 8, 2, 7, 3] Sort it in ascending order using loops + pop + append (implement your own simple bubble-sort-style process).
list19 = [9, 1, 8, 2, 7, 3]
n = len(list19)
for i in range(n):  
    for j in range(0, n-i-1):
        if list19[j] > list19[j+1]:
            list19[j], list19[j+1] = list19[j+1], list19[j]
print(list19)


# Task 20
# Given the list: [1,2,3,1,2,3,1,2,3] Remove the first and last identical blocks so result becomes [1,2,3].
list20 = [1,2,3,1,2,3,1,2,3]
block_size = 0
for i in range(1, len(list20)//2 + 1):
    if list20[:i] == list20[-i:]:
        block_size = i
if block_size > 0:
    list20 = list20[block_size:-block_size]
print(list20)
# Task 21
# Given the list: [1,2,3,4,5,6,7,8,9] Split the list into chunks of size 4.
list21 = [1,2,3,4,5,6,7,8,9]
chunk_size = 4      
chunks = []
for i in range(0, len(list21), chunk_size):
    chunk = []
    for j in range(i, min(i + chunk_size, len(list21))):
        chunk.append(list21[j])
    chunks.append(chunk)        
print(chunks)


# Task 22
# Given the list: [5, 1, 9, 3] Find the element whose total distance to all other elements is minimal.
list22 = [5, 1, 9, 3]
min_distance = float('inf')
for i in range(len(list22)):
    total_distance = 0
    for j in range(len(list22)):
        if i != j:
            total_distance += abs(list22[i] - list22[j])
    if total_distance < min_distance:
        min_distance = total_distance
        element = list22[i]
print(element)  

# Example: distance(5)=|5-1|+|5-9|+|5-3|        


# Task 23
# Given the list: [2,3,2,4,5,3,6,6,6] Remove all elements that appear exactly twice.
list23 = [2,3,2,4,5,3,6,6,6]
frequency = {}  
for num in list23:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1      
result = []
for num in list23:
    if frequency[num] != 2:
        result.append(num)
print(result)

# Task 24
# Simulate queue operations on an empty list: Operations: ["push 5", "push 7", "pop", "push 9", "push 1", "pop"] Return the final list.

queue = []
operations = ["push 5", "push 7", "pop", "push 9", "push 1", "pop"]

for op in operations:
    if op.startswith("push"):
        value = int(op.split()[1])
        queue.append(value)
    elif op == "pop":
        if queue:
            queue.pop(0)

print(queue)

# Task 25
# Given the list: [3,3,1,2,1,3] Create a list of lists, where each sublist contains all occurrences of one value.
# Example structure: [[3,3,3],[1,1],[2]]

list25 = [3,3,1,2,1,3]
frequency = {}
for num in list25:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1          
result = []
for num, freq in frequency.items():
    sublist = []
    for _ in range(freq):
        sublist.append(num)
    result.append(sublist)
print(result)


# Task 26
# Given the list: [9,2,7,4,6,3,8] Move all even numbers first, then odd, while keeping original order.
list26 = [9,2,7,4,6,3,8]
evens = []
odds = []
for num in list26:
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)
result = evens + odds
print(result)




# Task 27
# Given the list: [1,3,2,5,4] Count how many pops from the right are needed until the list becomes strictly increasing.
list27 = [1,3,2,5,4]
pops = 0

while len(list27) > 1:
    is_increasing = True
    for i in range(len(list27) - 1):
        if list27[i] >= list27[i + 1]:
            is_increasing = False
            break
    if is_increasing:
        break
    list27.pop()
    pops += 1

print(pops)

# Task 28
# Given the list: [4,4,4,7,7,1,1,1,1,9] Collapse consecutive duplicates into a list of unique runs: → [4,7,1,9]

list28 = [4,4,4,7,7,1,1,1,1,9]
result = []     
previous = None
for num in list28:
    if num != previous:
        result.append(num)
        previous = num
print(result)

# Task 29
# Given the list: [3,1,2,5,4,6] Remove items from the right until the last 3 elements form a strictly increasing sequence.
list29 = [3,1,2,5,4,6]
while len(list29) >= 3:
    if list29[-3] < list29[-2] < list29[-1]:
        break
    list29.pop()    
print(list29)

# Task 30
# Given the list: [10, 40, 20, 50, 30] Find the index of the second-largest element (no max()).

list30 = [10, 40, 20, 50, 30]
first_largest = second_largest = float('-inf')
for num in list30:
    if num > first_largest:
        second_largest = first_largest
        first_largest = num
    elif num > second_largest and num != first_largest:
        second_largest = num        
index = list30.index(second_largest)
print(index)    

# 2ci variant
list30 = [10, 40, 20, 50, 30]
first_largest = second_largest = float('-inf')
for num in list30:
   if num > first_largest:
         second_largest = first_largest
         first_largest = num
   elif num > second_largest and num != first_largest:
         second_largest = num
index = -1
for i in range(len(list30)):
    if list30[i] == second_largest:
        index = i
        break
print(index)


# muellimskiy cavab:
# Task 1
# data = [5, 2, 5, 7, 2, 9, 5, 2]

# while True:
#     ok = True
#     for x in data:
#         if data.count(x) > 1:
#             ok = False
#     if ok:
#         break
#     data.pop()

# print(data)


# Task 2
# data = [3, 1, 3, 2, 3, 1]
# result = []

# for x in data:
#     c = data.count(x)
#     for _ in range(c):
#         result.append(x)

# print(result)


# Task 3
# data = [10, 20, 30, 40, 50]
# rev = []

# while data:
#     x = data.pop()
#     rev.append(x)

# print(rev)


# Task 4
# data = [4,4,7,4,7,7,4,7]
# result = []
# counted = []

# for x in data:
#     if x not in counted:
#         counted.append(x)
#     c = result.count(x)
#     if c % 2 == 0:
#         result.append(x)

# print(result)


# Task 5
# a = [1, 3, 5, 7]
# b = [2, 4, 6]
# c = []

# i = 0
# j = 0
# while i < len(a) or j < len(b):
#     if i < len(a):
#         c.append(a[i])
#         i += 1
#     if j < len(b):
#         c.append(b[j])
#         j += 1

# print(c)


# Task 6
data = [9, 4, 9, 1, 4, 1, 1]

small = data[0]
for x in data:
    if x < small:
        small = x

cnt = data.count(small)
print(cnt)


# Task 7
data = [1, 2, 3, 4, 5]
steps = 3

for _ in range(steps):
    x = data.pop()
    data.insert(0, x)

print(data)


# Task 8
data = [2,2,2,3,3,4,4,4,4,5]
result = []

for x in data:
    if data.count(x) <= 3:
        result.append(x)

print(result)


# Task 9
data = [[1,2],[3,4,5],[6],[7,8,9]]
flat = []

for sub in data:
    for x in sub:
        flat.append(x)

print(flat)


# Task 10
data = [2, 4, 6, 1]
result = []

s = 0
for x in data:
    s += x
    result.append(s)

print(result)


# Task 11
data = [5, 5, 3, 2, 8]

while True:
    s = 0
    for x in data:
        s += x
    if s % 2 == 0:
        break
    data.pop(0)

print(data)


# Task 12
data = [7,7,7,2,2,3,3,3,3,1]

best = 1
curr = 1

for i in range(1, len(data)):
    if data[i] == data[i-1]:
        curr += 1
    else:
        if curr > best:
            best = curr
        curr = 1

if curr > best:
    best = curr

print(best)


# Task 13
words = ["car", "window", "to", "pan", "glass", "hi"]

longest = 0
for w in words:
    if len(w) > longest:
        longest = len(w)

limit = longest - 1

result = []
for w in words:
    if len(w) >= limit:
        result.append(w)

print(result)


# Task 14
data = [8, 12, 3, 29, 17, 29, 4]

first = data[0]
second = data[0]

for x in data:
    if x > first:
        first = x

for x in data:
    if x != first and x > second:
        second = x

print(first, second)


# Task 15
data = [9, 8, 7, 6, 5, 4, 3]
result = []

for i in range(len(data)):
    if i % 3 == 0:
        result.append(data[i])

print(result)


# Task 16
data = [9, 4, 3, 7, 6, 2]

while True:
    s = 0
    for x in data:
        s += x
    if s < 20:
        break
    data.pop()

print(data)


# Task 17
data = [4, -2, -7, 5, -7, 3]

mn = None
for x in data:
    if x < 0:
        if mn is None or x < mn:
            mn = x

mn = abs(mn)

result = []
for x in data:
    if x < 0:
        result.append(mn)
    else:
        result.append(x)

print(result)


# Task 18
data = [6,6,1,2,6,3,2,1]

best = 0
freq = None

for x in data:
    c = data.count(x)
    if c > best:
        best = c
        freq = x

indexes = []
for i in range(len(data)):
    if data[i] == freq:
        indexes.append(i)

print(indexes)


# Task 19
data = [9, 1, 8, 2, 7, 3]

n = len(data)
for _ in range(n):
    for i in range(n-1):
        if data[i] > data[i+1]:
            tmp = data[i]
            data[i] = data[i+1]
            data[i+1] = tmp

print(data)


# Task 20
data = [1,2,3,1,2,3,1,2,3]

block = data[:3]

data = data[3:]
data = data[:-3]

print(data)


# Task 21
data = [1,2,3,4,5,6,7,8,9]
size = 4
result = []

i = 0
while i < len(data):
    chunk = []
    j = i
    end = i + size
    while j < end and j < len(data):
        chunk.append(data[j])
        j += 1
    result.append(chunk)
    i += size

print(result)


# Task 22
data = [5, 1, 9, 3]

best_val = None
best_dist = None

for x in data:
    total = 0
    for y in data:
        total += abs(x - y)
    if best_dist is None or total < best_dist:
        best_dist = total
        best_val = x

print(best_val)


# Task 23
data = [2,3,2,4,5,3,6,6,6]
result = []

for x in data:
    if data.count(x) != 2:
        result.append(x)

print(result)


# Task 24
ops = ["push 5", "push 7", "pop", "push 9", "push 1", "pop"]
q = []

for op in ops:
    parts = op.split()
    if parts[0] == "push":
        q.append(int(parts[1]))
    else:
        if q:
            q.pop(0)

print(q)


# Task 25
data = [3,3,1,2,1,3]
result = []
used = []

for x in data:
    if x not in used:
        used.append(x)
        group = []
        for y in data:
            if y == x:
                group.append(y)
        result.append(group)

print(result)


# Task 26
data = [9,2,7,4,6,3,8]

evens = []
odds = []

for x in data:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)

result = []
for x in evens:
    result.append(x)
for x in odds:
    result.append(x)

print(result)


# Task 27
data = [1,3,2,5,4]
cnt = 0

while True:
    ok = True
    for i in range(len(data)-1):
        if data[i] >= data[i+1]:
            ok = False
    if ok:
        break
    data.pop()
    cnt += 1

print(cnt)


# Task 28
data = [4,4,4,7,7,1,1,1,1,9]
result = []

for x in data:
    if not result or x != result[-1]:
        result.append(x)

print(result)


# Task 29
data = [3,1,2,5,4,6]

while len(data) >= 3:
    a = data[-3]
    b = data[-2]
    c = data[-1]
    if a < b and b < c:
        break
    data.pop()

print(data)


# Task 30
data = [10, 40, 20, 50, 30]

mx = data[0]
for x in data:
    if x > mx:
        mx = x

second = None
for x in data:
    if x != mx:
        if second is None or x > second:
            second = x

idx = 0
for i in range(len(data)):
    if data[i] == second:
        idx = i

print(idx)
# Task 1 Write a function that takes a list of numbers and returns their sum.

def sum_list(numbers):
    total=0
    for num in numbers:
        total+=num
    return total

print(sum_list([1,2,3,4,5]))


# Task 2 Write a function that takes a list of numbers and returns the maximum value.

def max_list(numbers):
    max_num=numbers[0]
    for num in numbers:
        if num > max_num:
            max_num=num
    return max_num

print(max_list([1,2,3,4,5]))


# Task 3 Write a function that takes a list of strings and returns a new list with all strings in uppercase.

def uppercase_list(strings):
    uppercase_list =[]
    for str in strings:
        uppercase_list.append(str.upper())
    return uppercase_list
print(uppercase_list(["sevinc","sebr","ele"]))


# Task 4 Write a function that takes a list and returns it reversed (without using .reverse() or slicing [::-1]).

def reverse_list(list):
    reversed_list=[]
    i= len(list)-1
    while i>=0:  
     reversed_list.append(list[i])
     i-=1
    return reversed_list

print(reverse_list([1,2,3,4,5]))

# 2ci metod

def reverse_list(lst):
    reversed_list = []      

    while lst:             
        element = lst.pop() 
        reversed_list.append(element)  

    return reversed_list




# Task 5 Write a function that takes a list of numbers and returns only the even numbers.

def even_list(numbers):
    even_list=[]
    for num in numbers:
        if num%2==0:
            even_list.append(num)
    return even_list

print(even_list([1,2,3,4,5,6,7,8,9,10]))

# Task 6 Write a function that takes two lists and returns their intersection (common elements).

def intersection(list1, list2):
    intersection = []
    for item in list1:
        if item in list2:
            intersection.append(item)
    return intersection

print(intersection([1,2,3,4,5], [4,5,6,7,8]))

# Task 7 Write a function that takes a tuple of numbers and returns the average.

def average_tuple(tuple):
    total = sum(tuple)
    length = len(tuple)
    average = total / length
    return average

print(average_tuple((1,2,3,4,5)))

# Task 8 Write a function that takes a tuple and returns the first and last elements as a new tuple.

def first_last_tuple(tuple):
    return tuple[0], tuple[-1]

print(first_last_tuple((1,2,3,4,5)))

# Task 9 Write a function that counts how many times each element appears in a tuple and returns a dictionary.

def count_tuple(tuple):
    count_dict = {}
    for item in tuple:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

print(count_tuple((1,2,3,4,5)))

# Task 10 Write a function that checks if a given element exists in a tuple.

def element_exists(element, tuple):
    return element in tuple 

print(element_exists(3, (1,2,3,4,5)))


# Task 11 Write a function that takes a dictionary and returns the sum of its values.

def sum_dict(dictionary):
    total = 0
    for value in dictionary.values():
        total += value
    return total

print(sum_dict({"a": 1, "b": 2, "c": 3}))

# Task 12 Write a function that inverts a dictionary (keys become values, values become keys).

def invert_dict(dictionary):
    inverted_dict = {}
    for key in dictionary:
        value = dictionary[key]
        inverted_dict[value] = key
    return inverted_dict

print(invert_dict({"a": 1, "b": 2, "c": 3}))

# Task 13 Write a function that merges two dictionaries.

def merge_dict(a,b):
    merged=a.copy()
    merged.update(b)
    return merged

print(merge_dict({"a": 1, "b": 2}, {"c": 3, "d": 4}))

# Task 14 Write a function that takes a dictionary and returns the key with the maximum value.

def max_key(d):
  max_value = 0
  max_key = None
  for key, value in d.items():
    if value > max_value:
      max_value = value
      max_key = key
  return max_key

print(max_key({"a": 1, "b": 2, "c": 3}))

# Task 15 Write a function that removes all keys with duplicate values from a dictionary.

def remove_duplicates(d):
    unique_values = set()
    for value in d.values():
        unique_values.add(value)
    return {key: value for key, value in d.items() if value in unique_values}

print(remove_duplicates({"a": 1, "b": 2, "c": 1, "d": 3}))


# 2ci metod

def remove_duplicates(d):
    unique_values = set()
    result = {}

    for key, value in d.items():
        if value not in unique_values:
            unique_values.add(value)
            result[key] = value

    return result

print(remove_duplicates({"a": 1, "b": 2, "c": 1, "d": 3}))

# Task 16 Write a function that takes a set and a number, and returns True if the number is in the set.

def is_in_set(s, num):
    return num in s

print(is_in_set({1, 2, 3}, 2))


# Task 17 Write a function that returns the union of two sets.

def union_set(a,b):
    return a.union(b)

print(union_set({1,2,3},{4,5,6}))
    
   
# Task 18 Write a function that returns the difference between two sets.

def difference_set(a,b):
    # return a.difference(b)
    return a-b


print(difference_set({1,2,3},{4,5,6}))

# Task 19 Write a function that returns the symmetric difference of two sets.

def symmetric_difference_set(a,b):
    return a.symmetric_difference(b)

print(symmetric_difference_set({1,2,3},{4,5,6}))
# Task 20 Write a function that removes duplicates from a list using a set.
def remove_duplicates_list(l):
    return list(set(l))

print(remove_duplicates_list([1,2,3,4,5,1,2,3,4,5]))

# Task 21 Write a function that takes a list of words and returns a dictionary with word lengths.
 
def word_lengths(words):
    return {word: len(word) for word in words}

print(word_lengths(["apple", "banana", "cherry"]))

# Task 22 Write a function that takes a dictionary of student names and grades, and returns the average grade.

def average_grades(grades):
    total = 0
    count = 0
    for grade in grades.values():
        total += grade
        count += 1
    return total / count

print(average_grades({"Alice": 85, "Bob": 92, "Charlie": 78}))

# Task 23 Write a function that takes a list of tuples (name, age) and returns the name of the oldest person.

def oldest_person(people):
    oldest_name = people[0][0]
    oldest_age = people[0][1]
    for name, age in people:
        if age > oldest_age:
            oldest_name = name
            oldest_age = age
    return oldest_name

print(oldest_person([("Alice", 25), ("Bob", 30), ("Charlie", 20)]))
    

# Task 24 Write a function that takes a dictionary and returns a sorted list of its keys.
def sorted_keys(d):
    keys = []
    for key in d:
        keys.append(key)
    keys.sort()
    return keys

print(sorted_keys({'b': 1, 'a': 2}))  # Output: ['a', 'b']


# Task 25 Write a function that flattens a list of tuples into a single list. Example: [(1,2), (3,4)] → [1,2,3,4].
def flatten_list_of_tuples(lst):
    result = []
    for t in lst:
        result.extend(t)
    return result

print(flatten_list_of_tuples([(1,2), (3,4)]))  # Output: [1,2,3,4]


# Task 26 Write a function that takes a list of numbers and returns a tuple of (min, max).
def min_max_tuple(l):
    return (min(l), max(l))

print(min_max_tuple([1,2,3,4,5]))

# Task 27 Write a function that takes a list of strings and returns the one with the most characters.
def longest_string(l):
    longest = ""
    for s in l:
        if len(s) > len(longest):
            longest = s
    return longest

print(longest_string(["apple", "banana"]))
# Task 28 Write a function that takes a list of numbers and returns a set of unique numbers greater than 10.
def greater_than_10(l):
    return {num for num in l if num > 10}

print(greater_than_10([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
# Task 29 Write a function that takes a dictionary and returns a list of (key, value) tuples.
def dict_to_list(d):
    return list(d.items())

print(dict_to_list({"a": 1, "b": 2, "c": 3}))

# Task 30 Write a function that takes two dictionaries and returns a set of keys they have in common.
def common_keys(a,b):
     result= set()
     for key in a:
         if key in b:
             result.add(key)
     return result

print(common_keys({"a": 1, "b": 2, "c": 3}, {"b": 4, "c": 5, "d": 6}))
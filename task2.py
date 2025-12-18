# Task 1
#  Given [1, 2, 3, 4], append the number 9 four times.

# list1 = [1, 2, 3, 4]
# for _ in range(4):
#     list1.append(9) 
# print(list1)

# Task 2
#  Given [3, 1, 4, 1, 5], count how many times 1 appears.

# list2 = [3, 1, 4, 1, 5]
# count_ones= list2.count(1)
# print(count_ones)



# Task 3
#  Given [10, 20, 30, 40], remove the element at index 2.

# list3 = [10, 20, 30, 40]
# list3.pop(2) 
# # del list3[2]
# print(list3)

# Task 4
#  Given [8, 6, 7, 5, 3, 0, 9], append all even numbers into a new list.
# list4 = [8, 6, 7, 5, 3, 0, 9]
# even_numbers = []
# for num in list4:
#     if num %2 ==0:
#         even_numbers.append(num)
# print(even_numbers)

# Task 5
#  Given [2, 4, 6, 8] and [1, 3, 5], extend the first list with the second.

# list5 = [2, 4, 6, 8]
# list55 = [1, 3, 5]
# list5.extend(list55)
# print(list55)


# Task 6
#  Given [7, 7, 2, 9, 2, 2], remove the first occurrence of 2.

# list6 = [7, 7, 2, 9, 2, 2]
# list6.remove(2)
# print(list6)

# Task 7
#  Given [5, 1, 5, 1, 5], build a list of indexes where 5 appears.

# list7 = [5, 1, 5, 1, 5]
# indexes_of_5 = []
# for i in range(len(list7)):
#     if list7[i] == 5:
#         indexes_of_5.append(i)
# print(indexes_of_5)


# Task 8
#  Given [4, 3, 2, 1], print items using a while loop.

# list8 = [4, 3, 2, 1]
# index = 0
# while index < len(list8):
#     print(list8[index])
#     index += 1
    
# Task 9
#  Given [9, 8, 7, 6], pop all elements one by one and store them in a new list.

# list9= [9, 8, 7, 6]
# popped_elements = []
# while list9:
#     popped_elements.append(list9.pop())
# print(popped_elements)

# Task 10
#  Given [1, 2, 3, 4, 5], create a list of squares.
# list10 = [1, 2, 3, 4, 5]
# squares = []
# for num in list10:
#     squares.append(num ** 2)
# print(squares)

# Task 11
#  Given [3, 6, 9, 12], check if 9 is in the list using a loop.
# list11 = [3, 6, 9, 12]
# found_9 = False
# for num in list11:
#     if num == 9:
#         found_9 = True
#         break
# print(found_9)

# Task 12
#  Given [4, 4, 1, 2, 1], create a list of elements that appear only once.
# list12 = [4, 4, 1, 2, 1]
# unique_elements = []
# for num in list12:
#     if list12.count(num) == 1:
#         unique_elements.append(num)
# print(unique_elements) 

# # 2ci variant
# list12 = [4, 4, 1, 2, 1] 
# unique_elements = set(list12)
# single_occurrence = []
# for element in unique_elements:
#     if list12.count(element) == 1:
#         single_occurrence.append(element)
# print(single_occurrence)    


# Task 13
#  Given [1, 2, 3, 4, 5], remove all odd numbers.
# list13 = [1, 2, 3, 4, 5]
# index = 0
# while index < len(list13):
#     if list13[index] % 2 != 0:
#         list13.pop(index)
#     else:
#         index += 1
# print(list13)

# # 2ci variant=
# list13 = [1, 2, 3, 4, 5]
# odd_num = []
# for num in list13:
#     if num % 2 == 0:
#         odd_num.append(num)
# print(f"Odd numbers: {odd_num}")

# Task 14
#  Given [5, 4, 3, 2, 1], reverse it using a while + pop.
# list14 = [5, 4, 3, 2, 1]
# reversed_list = []
# while list14:
#    reversed_list.append(list14.pop())
# print(reversed_list)

# # 2ci metod
# list14 = [5, 4, 3, 2, 1]
# reversed_list = []
# while len(list14) > 0:
#     num=list14.pop()
#     reversed_list.append (num)
# print(reversed_list)

# Task 15
#  Given [10, 3, 8, 1], find the smallest number using a loop.

# list15 = [10, 3, 8, 1]
# smallest = list15[0]
# for num in list15:
#     if num < smallest:
#         smallest = num
# print(smallest)


# Task 16
#  Given [2, 2, 2, 3, 3, 4], build a frequency list where each element appears count(x) times.

# list16 = [2, 2, 2, 3, 3, 4]
# frequency_list = []
# for num in list16:
#     for _ in range(list16.count(num)):
#         frequency_list.append(num)
# print(frequency_list)

# Task 17
#  Given [1, 3, 5, 7], insert the number 9 at the beginning manually (no insert).
# list17 = [1, 3, 5, 7]
# list17 = [9] + list17
# print(list17)

# # # 2ci variant
# list17 = [1, 3, 5, 7]
# new_element = 9
# list17 = [new_element] + list17
# print(list17)

# # 3cu variant
# list17 = [1, 3, 5, 7]
# list17[0:0] = [9]
# print(list17)
# Task 18
#  Given [1, 4, 1, 4, 1, 4], count how many pairs of 1 and 4 exist next to each other.
# list18 = [1, 4, 1, 4, 1, 4]
# pair_count = 0
# for i in range(len(list18) - 1):
#     if (list18[i] == 1 and list18[i + 1] == 4) or (list18[i] == 4 and list18[i + 1] == 1):
#         pair_count += 1
# print(pair_count)



# Task 19
#  Given [3, 1, 4, 1, 5], find the index of the largest value (no max()).
# list19 = [3, 1, 4, 1, 5]
# largest_index = 0
# for i in range(1, len(list19)):
#     if list19[i] > list19[largest_index]:
#         largest_index = i    
# print(largest_index)


# Task 20
#  Given [2, 4, 6, 8, 10], build cumulative products.

list20 = [2, 4, 6, 8, 10]
cumulative_products = []
current_product = 1
for num in list20:
    current_product *= num
    cumulative_products.append(current_product)
print(cumulative_products)

# Task 21
# #  Given [9, 3, 9, 3, 9], remove all occurrences of 3.
# list21 = [9, 3, 9, 3, 9]
# list21 = [num for num in list21 if num != 3]
# print(list21)

# # 2ci variant
# list21 = [9, 3, 9, 3, 9]
# while 3 in list21:
#     list21.remove(3)
# print(list21)

# Task 22
#  Given [1, 2, 3, 4], create a new list where each number appears twice.
# list22 = [1, 2, 3, 4]
# doubled_list = []
# for num in list22:
#     doubled_list.append(num)
#     doubled_list.append(num)
# print(doubled_list)

# # 2ci variant
# list22 = [1, 2, 3, 4]
# doubled_list = []
# for num in list22:
#     doubled_list.extend([num, num])
# print(doubled_list)   


# # Task 23
#  Given [8, 2, 7, 3, 6], create a list of numbers at even indexes.

# list23 = [8, 2, 7, 3, 6]
# even_indexed = []
# for i in range(0, len(list23), 2):
#     even_indexed.append(list23[i])
# print(even_indexed)


# # # 2ci variant
# list23 = [8, 2, 7, 3, 6]
# even_indexed = [list23[i] for i in range(len(list23)) if i % 2 == 0]
# print(even_indexed)


# Task 24
#  Given [5, 4, 3, 2, 1], find the first number larger than 3.

# list24 = [5, 4, 3, 2, 1]
# first_larger_than_3 = None
# for num in list24:
#     if num > 3:
#         first_larger_than_3 = num
#         break
# print(first_larger_than_3)


# Task 25
#  Given [3, 3, 3, 2, 2, 1], compress consecutive duplicates into [3,2,1].
# list25 = [3, 3, 3, 2, 2, 1]
# compressed_list = []
# if list25:
#     compressed_list.append(list25[0])
#     for i in range(1, len(list25)):
#         if list25[i] != list25[i - 1]:
#             compressed_list.append(list25[i])
# print(compressed_list)


# Task 26
#  Given [9, 1, 8, 2], swap first and last manually.
# list26 = [9, 1, 8, 2]
# temp = list26[0]
# list26[0] = list26[-1]
# list26[-1] = temp
# print(list26)

# # # 2ci variant
# list26 = [9, 1, 8, 2]
# list26[0], list26[-1] = list26[-1], list26[0]
# print(list26)


# Task 27
#  Given [7, 2, 5, 2, 7], check if the list is symmetrical.

# list27 = [7, 2, 5, 2, 7]
# is_symmetrical = True
# for i in range(len(list27) // 2):
#     if list27[i] != list27[-(i + 1)]:
#         is_symmetrical = False
#         break   
# print(is_symmetrical)


# 2ci variant
# list27 = [7, 2, 5, 2, 7]
# is_symmetrical = list27 == list27[::-1]  
# print(is_symmetrical)       


# Task 28
#  Given [1, 1, 2, 2, 3, 3], count how many distinct elements exist.
# list28 = [1, 1, 2, 2, 3, 3]
# distinct_elements = set(list28)
# print(len(distinct_elements))   
# # # 2ci variant
# list28 = [1, 1, 2, 2, 3, 3]
# distinct_count = 0
# for num in list28:
#     if list28.index(num) == list28.index(num):
#         distinct_count += 1
# print(distinct_count)
# Task 29
#  Given [4, 1, 4, 2, 4, 3], remove every second 4.
# list29 = [4, 1, 4, 2, 4, 3]
# count_4 = 0
# index = 0
# while index < len(list29):
#     if list29[index] == 4:
#         count_4 += 1
#         if count_4 % 2 == 0:
#             list29.pop(index)
#             index -= 1
#     index += 1
# print(list29)


# # Task 30
#  Given [10, 20, 10, 30], remove all duplicates, keeping only first occurrences.
# list30 = [10, 20, 10, 30]
# seen = set()
# unique_list = []
# for num in list30:
#     if num not in seen:
#         seen.add(num)
#         unique_list.append(num)
# print(unique_list)
# # # 2ci variant
# list30 = [10, 20, 10, 30]
# unique_list = []    
# for num in list30:
#     if num not in unique_list:
#         unique_list.append(num)
# print(unique_list)


# Task 31
#  Given [1, 2, 3, 4, 5], shift all elements left by 1.
# list31 = [1, 2, 3, 4, 5]
# first_element = list31.pop(0)
# list31.append(first_element)
# print(list31)
# # # 2ci variant
# list31 = [1, 2, 3, 4, 5]
# list31.insert(0, list31.pop())
# print(list31) 


# # Task 32
#  Given [2, 5, 2, 5, 2], count how many times the pair 2,5 appears.
# list32 = [2, 5, 2, 5, 2]
# pair_count = 0      
# for i in range(len(list32) - 1):
#     if list32[i] == 2 and list32[i + 1] == 5:
#         pair_count += 1
# print(pair_count)
# # # 2ci variant
# list32 = [2, 5, 2, 5, 2]
# pair = (2, 5) 
# pair_count = 0
# for i in range(len(list32) - 1):  
#     if (list32[i], list32[i + 1]) == pair:
#         pair_count += 1   
# print(pair_count)


# Task 33
#  Given [8, 6, 7, 5, 3], find the difference between max and min (no max/min functions).
# list33 = [8, 6, 7, 5, 3]
# max_value = list33[0]
# min_value = list33[0]
# for num in list33:
#     if num > max_value:
#         max_value = num
#     if num < min_value:
#         min_value = num
# difference = max_value - min_value
# print(difference)

# Task 34
#  Given [1, 2, 3, 4], create partial sums: [1, 3, 6, 10].
# list34 = [1, 2, 3, 4]
# partial_sums = []
# current_sum = 0
# for num in list34:
#     current_sum += num
#     partial_sums.append(current_sum)
# print(partial_sums)

# Task 35
#  Given [5, 10, 15, 20], create a list of elements divided by 5.
# list35 = [5, 10, 15, 20]
# divided_by_5 = []
# for num in list35:
#     divided_by_5.append(num / 5)        
# print(divided_by_5)

# Task 36
#  Given [1, 2, 1, 2, 1, 2], check if it alternates 1,2,... correctly.
# list36 = [1, 2, 1, 2, 1, 2]
# is_alternating = True
# for i in range(len(list36)):
#     if i % 2 == 0:
#         if list36[i] != 1:
#             is_alternating = False
#             break
#     else:
#         if list36[i] != 2:
#             is_alternating = False
#             break
# print(is_alternating)


# Task 37
#  Given [4, 3, 2, 1], remove elements until the list becomes sorted ascending.

# list37 = [4, 3, 2, 1]
# while list37 != sorted(list37):
#     if len(list37) > 1:
#         list37.pop(0)
#     else:
#         break    
# print(list37)

# Task 38
#  Given [2, 3, 4, 5], create a new list of cumulative maximums.

# list38 = [2, 3, 4, 5]
# cumulative_max = []
# current_max = None
# for num in list38:
#     if current_max is None or num > current_max:
#         current_max = num
#     cumulative_max.append(current_max)
# print(cumulative_max)

# Task 39
#  Given [3, 6, 9, 12, 15], count elements divisible by 3.
# list39 = [3, 6, 9, 12, 15]
# count_divisible_by_3 = len([x for x in list39 if x % 3 == 0])
# print(count_divisible_by_3)

# Task 40
#  Given [5, 1, 5, 1, 5, 1], remove the last three elements using pop.
# list40 = [5, 1, 5, 1, 5, 1]
# for _ in range(3):
#     list40.pop()
# print(list40)


# Task 41
#  Given [1, 4, 9, 16], double each element and store in a new list.
# list41 = [1, 4, 9, 16]
# doubled_list = [x * 2 for x in list41]
# print(doubled_list)

# Task 42
#  Given [9, 8, 7, 6, 5], check if the list is strictly decreasing.
# list42 = [9, 8, 7, 6, 5]
# decreasing = True
# for i in range(len(list42) - 1):
#     if list42[i] <= list42[i + 1]:
#         decreasing = False
#         break
# print(decreasing)



# Task 43
#  Given [3, 3, 2, 1, 2, 3, 3], find the longest consecutive sequence.

list43 = [3, 3, 2, 1, 2, 3, 3]

if not list43 :
    longest_sequence = []
else:
    max_length =1
    current_length =1
    max_sequence = [list43[0]]
for i in range(1, len(list43)):
    if list43[i] == list43[i -1]:
        current_length += 1
    else:
        current_length = 1
        if current_length > max_length:
            max_length = current_length
            max_sequence = [list43[i -1]] * max_length
print(max_sequence)


# Task 44
#  Given [4, 7, 1, 9], append elements until the sum exceeds 30.

# list44= [4, 7, 1, 9]
# target_sum = 30
# element_append = 1
# current_sum = sum(list44)
# while current_sum <= target_sum:
#     list44.append(element_append)
#     current_sum += element_append  
# print(list44)



# Task 45
#  Given [1, 3, 5, 7], insert 0 at index 2 manually.

# list45 = [1, 3, 5, 7]
# list45 [2:2] = [0]
# print(list45)

# # 2ci variant

# list45 = [1, 3, 5, 7]
# element = 0
# index= 2
# list45 = list45[:index] + [element] + list45[index:]
# print(list45)


# Task 46
#  Given [6, 5, 4, 3, 2, 1], create a list of running minimums.
# list46 = [6, 5, 4, 3, 2, 1]
# running_mins = []
# current_min = list46[0]
# for num in list46:
#     if num < current_min :
#         current_min = num
#     running_mins.append(current_min)
# print(running_mins)


# Task 47
#  Given [2, 4, 6, 8, 10], sum elements using a while loop.

# list47 = [2, 4, 6, 8, 10]
# index = 0
# total_sum = 0
# while index < len(list47):
#     total_sum += list47[index]
#     index += 1
# print(total_sum)

# Task 48
#  Given [1, 1, 1, 2, 2, 3], create a list of (value, count) pairs.

# list48= [1, 1, 1, 2, 2, 3]
# value_pairs = []
# unique_values = sorted(set(list48))
# for value in unique_values :
#     count = list48.count(value)
#     value_pairs.append((value, count))
# print(value_pairs)


# Task 49
#  Given [7, 1, 5, 1, 7], check if first and last elements appear the same number of times.

# list49 = [7, 1, 5, 1, 7]
# first_element = list49[0]
# last_element = list49[-1]
# if not list49:
#     equal = True
# elif first_element == last_element:
#     equal= True
# else:
#     count_first = list49.count(first_element)
#     count_last = list49.count(last_element)
#     equal = (count_first == count_last)
# print(equal)

# 2ci variant
# list49 = [7, 1, 5, 1, 7]
# first_element = list49[0]
# last_element = list49[-1]
# count_first = list49.count(first_element)
# count_last = list49.count(last_element)
# equal  = count_first == count_last
# print(f"equal: {equal}")
    
# Task 50
#  Given [3, 1, 4, 1, 5, 9], remove all elements after the first 4.

# list50 = [3, 1, 4, 1, 5, 9]
# new_list = []
# for item in list50:
#     new_list.append(item)
#     if item == 4:
#         break
# # print(new_list)
# list50 = new_list
# print(list50)



# # 2ci variant
# list50 = [3, 1, 4, 1, 5, 9]
# index_of_4 = list50.index(4)
# del list50[index_of_4 + 1 :]
# print(list50)

# Muellimskiy solutions:

# Task 1
# data = [1, 2, 3, 4]
# for _ in range(4):
# data.append(9)
# print(data)
# Task 2
# data = [3, 1, 4, 1, 5]
# c = data.count(1)
# print(c)
# Task 3
# data = [10, 20, 30, 40]
# data.pop(2)
# print(data)
# Task 4
# data = [8, 6, 7, 5, 3, 0, 9]
# ev = []
# for x in data:
# if x % 2 == 0:
# ev.append(x)
# print(ev)
# Task 5
# a = [2, 4, 6, 8]
# b = [1, 3, 5]
# a.extend(b)
# print(a)
# Task 6
# data = [7, 7, 2, 9, 2, 2]
# data.remove(2)
# print(data)
# Task 7
# data = [5, 1, 5, 1, 5]
# res = []
# for i in range(len(data)):
# if data[i] == 5:
# res.append(i)
# print(res)
# Task 8
# data = [4, 3, 2, 1]
# i = 0
# while i < len(data):
# print(data[i])
# i += 1
# Task 9
# data = [9, 8, 7, 6]
# rev = []
# while data:
# rev.append(data.pop())
# print(rev)
# Task
# data = [1, 2, 3, 4, 5]
# sq = []
# for x in data:
# sq.append(x*x)
# print(sq)
# Task 11
# data = [3, 6, 9, 12]
# f = False
# for x in data:
# if x == 9:
# f = True
# print(f)
# Task 12
# data = [4, 4, 1, 2, 1]
# res = []
# for x in data:
# if data.count(x) == 1:
# res.append(x)
# print(res)
# Task 13
# data = [1, 2, 3, 4, 5]
# res = []
# for x in data:
# if x % 2 == 0:
# res.append(x)
# print(res)
# Task 14
# data = [5, 4, 3, 2, 1]
# rev = []
# while data:
# rev.append(data.pop())
# print(rev)
# Task 15
# data = [10, 3, 8, 1]
# mn = data[0]
# for x in data:
# if x < mn:
# mn = x
# print(mn)
# Task 16
# data = [2, 2, 2, 3, 3, 4]
# res = []
# for x in data:
# for _ in range(data.count(x)):
# res.append(x)
# print(res)
# Task 17
# data = [1, 3, 5, 7]
# data = [9] + data
# print(data)
# Task 18
# data = [1, 4, 1, 4, 1, 4]
# cnt = 0
# for i in range(len(data)-1):
# if data[i] == 1 and data[i+1] == 4:
# cnt += 1
# print(cnt)
# Task 19
# data = [3, 1, 4, 1, 5]
# mx = data[0]
# idx = 0
# for i in range(len(data)):
# if data[i] > mx:
# mx = data[i]
# idx = i
# print(idx)
# Task 20
# data = [2, 4, 6, 8, 10]
# res = []
# p = 1
# for x in data:
# p = p * x
# res.append(p)
# print(res)
# Task 21
# data = [9, 3, 9, 3, 9]
# res = []
# for x in data:
# if x != 3:
# res.append(x)
# print(res)
# Task 22
# data = [1, 2, 3, 4]
# res = []
# for x in data:
# res.append(x)
# res.append(x)
# print(res)
# Task 23
# data = [8, 2, 7, 3, 6]
# res = []
# for i in range(len(data)):
# if i % 2 == 0:
# res.append(data[i])
# print(res)
# Task 24
# data = [5, 4, 3, 2, 1]
# ans = None
# for x in data:
# if x > 3:
# ans = x
# break
# print(ans)
# Task 25
# data = [3, 3, 3, 2, 2, 1]
# res = []
# for x in data:
# if not res or x != res[-1]:
# res.append(x)
# print(res)
# Task 26
# data = [9, 1, 8, 2]
# tmp = data[0]
# data[0] = data[-1]
# data[-1] = tmp
# print(data)
# Task 27
# data = [7, 2, 5, 2, 7]
# sym = True
# for i in range(len(data)//2):
# if data[i] != data[-1-i]:
# sym = False
# print(sym)
# Task 28
# data = [1, 1, 2, 2, 3, 3]
# u = []
# for x in data:
# if x not in u:
# u.append(x)
# print(len(u))
# Task 29
# data = [4, 1, 4, 2, 4, 3]
# cnt = 0
# res = []
# for x in data:
# if x == 4:
# cnt += 1
# if cnt % 2 == 1:
# res.append(x)
# else:
# res.append(x)
# print(res)
# Task 30
# data = [10, 20, 10, 30]
# res = []
# for x in data:
# if x not in res:
# res.append(x)
# print(res)
# Task 31
# data = [1, 2, 3, 4, 5]
# first = data[0]
# for i in range(len(data)-1):
# data[i] = data[i+1]
# data[-1] = first
# print(data)
# Task 32
# data = [2, 5, 2, 5, 2]
# cnt = 0
# for i in range(len(data)-1):
# if data[i] == 2 and data[i+1] == 5:
# cnt += 1
# print(cnt)
# Task 33
# data = [8, 6, 7, 5, 3]
# mx = data[0]
# mn = data[0]
# for x in data:
# if x > mx:
# mx = x
# if x < mn:
# mn = x
# print(mx - mn)
# Task 34
# data = [1, 2, 3, 4]
# res = []
# s = 0
# for x in data:
# s += x
# res.append(s)
# print(res)
# Task 35
# data = [5, 10, 15, 20]
# res = []
# for x in data:
# res.append(x/5)
# print(res)
# Task 36
# data = [1, 2, 1, 2, 1, 2]
# alt = True
# for i in range(len(data)):
# if i % 2 == 0 and data[i] != 1:
#     alt = False
# if i % 2 == 1 and data[i] != 2:
# alt = False
# print(alt)
# Task 37
# data = [4, 3, 2, 1]
# while True:
# ok = True
# for i in range(len(data)-1):
# if data[i] > data[i+1]:
# ok = False
# if ok:
# break
# data.pop()
# print(data)
# Task 38
# data = [2, 3, 4, 5]
# res = []
# mx = data[0]
# for x in data:
# if x > mx:
# mx = x
# res.append(mx)
# print(res)
# Task 39
# data = [3, 6, 9, 12, 15]
# cnt = 0
# for x in data:
# if x % 3 == 0:
#     cnt += 1
# print(cnt)
# Task 40
# data = [5, 1, 5, 1, 5, 1]
# data.pop()
# data.pop()
# data.pop()
# print(data)
# Task 41
# data = [1, 4, 9, 16]
# res = []
# for x in data:
# res.append(x*2)
# print(res)
# Task 42
# data = [9, 8, 7, 6, 5]
# ok = True
# for i in range(len(data)-1):
# if data[i] <= data[i+1]:
# ok = False
# print(ok)
# Task 43
# data = [3, 3, 2, 1, 2, 3, 3]
# best = 1
# cur = 1
# for i in range(1, len(data)):
#     if data[i] == data[i-1]:
# cur += 1
# else:
# if cur > best:
# best = cur
# cur = 1
# if cur > best:
# best = cur
# print(best)
# Task 44
# data = [4, 7, 1, 9]
# s = 0
# res = []
# for x in data:
# res.append(x)
# s += x
# if s > 30:
# break
# print(res)
# Task 45
# data = [1, 3, 5, 7]
# res = []
# for i in range(len(data)):
# if i == 2:
# res.append(0)
# res.append(data[i])
# print(res)
# Task 46
# data = [6, 5, 4, 3, 2, 1]
# res = []
# mn = data[0]
# for x in data:
# if x < mn:
# mn = x
# res.append(mn)
# print(res)
# Task 47
# data = [2, 4, 6, 8, 10]
# i = 0
# s = 0
# while i < len(data):
# s += data[i]
# i += 1
# print(s)
# Task 48
# data = [1, 1, 1, 2, 2, 3]
# res = []
# used = []
# for x in data:
# if x not in used:
# used.append(x)
# res.append((x, data.count(x)))
# print(res)
# Task 49
# data = [7, 1, 5, 1, 7]
# f = data[0]
# l = data[-1]
# c1 = data.count(f)
# c2 = data.count(l)
# print(c1 == c2)
# Task 50
# data = [3, 1, 4, 1, 5, 9]
# i = 0
# while i < len(data):
# if data[i] == 4:
# data = data[:i+1]
# break
# i += 1
# print(data)
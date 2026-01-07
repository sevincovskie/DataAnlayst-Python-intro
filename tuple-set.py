# tuple-Python-da birdən çox dəyəri ardıcıl şəkildə saxlayan,amma dəyişdirilə BİLMƏYƏN (immutable) məlumat tipidir.
# numbers =(1,2,3,4)
# type(numbers)
# print(numbers[1])
# print(type(numbers))
 
# first_tuple =(1,2,3,4)
# second_tuple = tuple([1,2,3,4])

# print(first_tuple)
# print(second_tuple)

# names= ('Colt', 'Rusty', 'Kurt')
# for name in names:
#     print(name)
    
# for ind,name in enumerate(names):
#     print(ind,name)

# t=(5)
# print(type(t))

# t=(5,)
# print(type(t))

# t=(1,2,3,3,3)
# print(t.index(1))


# set-təkrarlanan elementləri saxlamayan, sırasız (unordered) bir data strukturudur.

my_set={1,2,3,4,5}
print(my_set)

my_set= set([1,2,3,4,5])
print(my_set)
# print(my_set[0]) index yoxdur

# deyisendir
my_set= {1,2,3,4,5}
my_set.add(6)
print(my_set)

my_set= {1,2,3,4,5}
my_set.remove(3)
print(my_set)


# discard-elementi silir
my_set= {1,2,3,4,5}
my_set.discard(3)
print(my_set)

# pop-elementi silir
my_set= {1,2,3,4,5}
my_set.pop()
print(my_set)

# clear-elementi silir
my_set= {1,2,3,4,5}
my_set.clear()
print(my_set)

# union-birlesdir
set1= {1,2,3,4,5}
set2= {4,5,6,7,8}
set3= set1.union(set2)
print(set3)

# intersection-ortaq
set1= {1,2,3,4,5}
set2= {4,5,6,7,8}
set3= set1.intersection(set2)
print(set3)

print(set1.symmetric_difference(set2))

# difference-fark
set1= {1,2,3,4,5}
set2= {4,5,6,7,8}
set3= set1.difference(set2)
print(set3)





# Set-i list-ə extend etmək , SƏHV OLAN YOL: append()
my_set = {1, 2, 3}
my_list = [10, 20]

my_list.extend(my_set)
print(my_list)

my_list.extend(sorted(my_set))
print(my_list)


# copy

my_set = set([1, 2, 3])  
my_set2 = my_set.copy()
print(my_set2)


# Set Comprehension

set1= {1,2,3,4,5}
set2= {4,5,6,7,8}
set3= {i for i in set1 if i in set2}
print(set3)

nums= [1,2,3,4,5]
s = {num for num in nums if num % 2 == 0}
print(s)

s = {i for i in range(1, 11) if i % 2 == 1}
print(s)



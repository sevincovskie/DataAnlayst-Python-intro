# Create a list of squares of numbers from 1 to 5.

list_of_squares = [num**2 for num in range(1, 6)]
print(list_of_squares)


# Create a list of even numbers from 0 to 10.
even_numbers = [num for num in range(11) if num % 2 == 0]
print(even_numbers)


# Create a list of all characters in the string "hello".
char_list = [char for char in "hello"]
print(char_list)
 

# Create a list of the first letter of each word in ["apple", "banana", "cherry"].
first_letters = [word[0] for word in ["apple", "banana", "cherry"]]
print(first_letters)


# Create a list of numbers from 1 to 10 that are divisible by 3.
divisible_by_three = [num for num in range(1, 11) if num % 3 == 0]
print(divisible_by_three)

# Create a list of numbers from 1 to 5 multiplied by 10.
multiplied_by_ten = [num * 10 for num in range(1, 6)]
print(multiplied_by_ten)


# Create a list of uppercase versions of ["cat", "dog", "fox"].
uppercase_versions = [animal.upper() for animal in ["cat", "dog", "fox"]]
print(uppercase_versions)  

         
# Create a list of lengths of each word in ["tree", "mountain", "river"].

lengths = [len(word) for word in ["tree", "mountain", "river"]]
print(lengths)


# Create a list of odd numbers from 1 to 15.
odd_numbers = [num for num in range(1, 16) if num % 2 != 0]
print(odd_numbers)


# Create a list of cubes of numbers from 1 to 4.
cubes = [num**3 for num in range(1, 5)]
print(cubes)
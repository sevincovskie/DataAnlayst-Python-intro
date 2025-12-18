# player1 = input('Player 1, make your move: ')
# player2 = input('Player 2, make your move: ')

# if player1 == 'rock' and player2 == 'scissors':
#     print('Player 1 wins!')
# elif player1 == 'rock' and player2 == 'paper':
#     print('Player 2 wins!')
# elif player1 == 'paper' and player2 == 'rock':
#     print('Player 1 wins!')
# elif player1 == 'paper' and player2 == 'scissors':
#     print('Player 2 wins!')
# elif player1 == 'scissors' and player2 == 'paper':
#     print('Player 1 wins!')
# elif player1 == 'scissors' and player2 == 'rock':
#     print('Player 2 wins!')
# else:
#     print('Draw!')

# user_response = None
# while user_response != "please" :
#  user_response = input("AH AH AH , you don't say the magic word : ")

# user = input("Salam necesen?: ")
# while user != "stop" :
#     user= input(f'{user} ')

# for num in range (1,11) :
#     if (num ==4):
#         break
#     print(num)




# play = "y"
# while play == "y":
#     secret_number = int(input("Enter a secret number: "))
    
#     while True:
#         print('I am starting to guess the number!')
#         guess = int(input("Enter your guess: "))
        
#         if guess < secret_number:
#             print("Too low, try again!")
#         elif guess > secret_number:
#             print("Too high, try again!")
#         else:
#             print("You guessed it! You won!")
#             break

#     play = input("Do you want to keep playing? (y/n) ")

# print("Goodbye!")


# task1 = 'install python'
# task2 = 'learn python'
# task3 = 'apply for a job'

# tasks = ['install python', 'learn python', 'apply for a job']
# tasks[0]
# tasks[1]
# tasks[2]

# friends = ["sona", "matt", "sevinc"]
# friends[0] 

# "Sevinc" in friends

# for friend in friends :
#   print(friend)

# ind = 0
# while ind < len(friends):
#     print(friends[ind])
#     ind += 1

# append-> sona elave etmek
# first_list = [1,2,3,4]
# first_list.append(5)
# print(first_list)

# first_list = [1,2,3,4]
# first_list.append([5,6,7])

# print(first_list[-1][1])

# insert-> istediyimiz yere elave etmek

# first_list = [1,2,3,4]
# first_list.insert(2, "sevinc")
# print(first_list)

# # clear-> butun elementleri silir
# first_list.clear()
# first_list = []
# print(first_list)

# # remove-> deyeri silir
# first_list = [1,2,3,4]
# first_list.remove(3)
# print(first_list)

# first_list = [5,2,8,1,4,41,4,4]
# first_list.remove(4)  # ilk gorduyunu silir
# print(first_list)

# # pop-> indexe gore silir
# first_list = [1,2,3,5,7,84]
# first_list.pop(2)   
# print(first_list)

# first_list = [1,2,3,5,7,84]
# first_list.pop()   #sonuncunu silir
# print(first_list)



# first_list = [5,2,8,1,4]
# del first_list[2]
# print(first_list)



# index-> deyerin sirasini verir
# number =[1,2,3,4,5]
# print(number.index(3))  #3-un indexini verir number. 

# number =[1,2,34,67,4,5,31,3]
# print(number.index(4,3.))  

# count-> deyerin siyahida nece defe ishtirak etdiyini gosterir
# number =[1,2,34,67,4,5,31,3,4,4,4]
# print(number.count(4))

# nums =[1,2,3,4,4,4,4,4,4,4,4,4,4]
# remove_fours = nums.count(4)
# for n in range(remove_fours):
#         print(nums.remove(4))
        
        

# # # reverse-> tersi duzur
# first_list = [1,2,3,4,5]
# first_list.reverse ()
# print(first_list)

# # # sort-> kicikden boyuye duzur

# first_list = [5,2,8,1,4]
# first_list.sort()
# print(first_list)

# another_list = [1,2,3]
# another_list.sort(reverse=True)
# print(another_list)

# words = ["Sevinc" , "sebr ele."]
# myMotto = " ".join(words)
# print(myMotto)


# qosa noqte : slice gosterir, slice

# list=[1,2,3,4]
# print(list[1:3])
# print(list)
# print(list[0])




# list = [1,2,3,4,5,6,7,8,9,10]
# print(list[1::2])  
# print(list[::2])  #butun ededleri 2-2 artirir
# print(list[::3])  #butun ededleri 3-3 artirir
# print(list[:1:-1])  #tersine duzur , indekse gore end goturulmur
# print(list[-1::1])
# print(list[-1::-1])  #butunu tersine duzur

# number =[1,2,3,4,5]
# doubled_num = []
# for num in number :
#         doubled_num.append (num *2)
# print(f"number: {number} , doubled_num: {doubled_num}")      

# list comprehension

# number = [1,2,3,4,5]
# doubled_num = [num * 2 for num in number]
# print(f"number: {number} , doubled_num: {doubled_num}")

# name = "sevinc"
# upper_name = [char.upper() for char in name]
# print(f"name: {name} , upper_name: {upper_name} " )



# friends = ["sona", "matt", "sevinc", "anna"]
# upper_friends = [friend[0].upper() for friend in friends  ]
# print(f"friends: {friends} , upper_friends: {upper_friends} ")
# upper_friends = [friend[0].upper() + friend[1:] for friend in friends ]
# print(f" upper_friends: {upper_friends} ")

# print([num*10 for num in range(1,11)])

# print(bool(val) for val in [0,[],''])

# numbers = [1,2,3,4,5,6,7,8,9,10]
# string_list = [str(num) for num in numbers]
# print(string_list)

# evens =[num for num in numbers if num % 2 ==0 ]
# odds = [num for num in numbers if num % 2 !=0 ]
# print(f"evens: {evens} , odds: {odds} ")

# result = [num *2 if num %2 ==0 else num /2 for num in numbers ]
# print(result)

# saitleri silmek
# vowels = " This is Spartaaaaaaa!"
# print(''.join(char for char in vowels if char not in 'aeiouAEIOU'))


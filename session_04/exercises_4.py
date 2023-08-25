# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
list= ["Apples", "Cheeries", "Pears", "Pineapple", "Peaches", "Mango"]
print (list)


# 2. Add "Grapes" to the list and print the list.
list.append("Grapes")
print(list)

# 3. Change "Pears" to "Strawberries" and print the list.
list[2] = "Strawberries"
print(list)


# 4. Remove "Apples" from the list and print the list.
del(list[0])
print(list)


# 5. Print out the current length of the list.
print(len(list))


# 6. Order the list alphabetically.
list.sort()
print(list)

# 7. Print out the list again.
print(list)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
lists = ["Apples", "Cheeries", "Pears", "Pineapple", "Peaches", "Mango"]
for list in lists:
  print(list)


# 2. Print the numbers 1 to 100 (including the number 100).
for number in range (1, 101): 
  print(number)
# go up to 101 but not include 101


# 3. Print all odd numbers from 1 to 100. # check the condition - If, how to interprete odd number - %
 
for number in range (1, 101):
  if number % 2:
    print(number)
  

# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020). # every 4 years
not_held = [1916, 1940, 1944, 2020]
for olympics_years in range(1896,2024,4):
  if olympics_years  not in not_held:
    print(olympics_years)

# how to skip the year has not been held:

# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
# a_list = ["1", "4", "6", "11", "3", "12", "67", "45", "55", "88"] count(if a_number % 2 in a_list)
# correct answer
numbers = [1, 10, 13 , 15, 765, 32, 65, 23, 56, 101]
even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        # This is short hand for the line above
        odd_count += 1

print("This list has " + str(even_count) + " even numbers and " + str(odd_count) + " odd numbers.")


# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
fname = ["lily", "eris", "bob", "tim", "jerry"]
print("Hello, " + str(fname[0]))
print("Hello, " + str(fname[1]))
print("Hello, " + str(fname[2]))
print("Hello, " + str(fname[3]))
print("Hello, " + str(fname[4]))

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
# correct answer
word = "supercalifragilisticexpialidocious"

for i in word:
    print(i)

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
# wrong: fnumber = ["1", "4", "6", "11", "3"] - dont need to put "" for number 
# fnumber.append(list[0]**2) #fnumber.append(list[1]**2)
#fnumber.append(list[2]**2)
#fnumber.append(list[3]**2)
#fnumber.append(list[4]**2)
#print(fnumber)

# correct answer: Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list

numbers = [2, 5, 8, 9, 10]
sqr_numbers = []

for i in numbers:
    sqr_numbers.append(i ** 2)

print(sqr_numbers)

# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
names = ["Saf", "Graham", "Jake", "Sanj", "Fis"]
drs = []
for name in names:
    drs.append("Dr. " + name)
print(drs)



# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)
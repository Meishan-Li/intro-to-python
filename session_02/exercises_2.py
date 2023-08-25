# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
x = 10
y = 20
area = x * y
print(str(area))
print("Retangle of width " + str(x) +"and height " + str(y) + "has an area of " + str(area))


# 2. Write code that prints the length of the string, 'python'.
name="python"
name_length = len(name)


# 3. Print out the first and third letter of the word 'python'.
name="python"
print(name[0:3:2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
name=input("What's your name?")
print("Hello " + name)



# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
age = int(input("How old are you?"))
age_in_15_years = age + 15
print("In 15 years you will be" + str(age_in_15_years))


# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
print("Hello," + str(name) + "you are curretnly " + str(age) + " years old. " + "In 15 years you will be " + str(age_in_15_years))


# 7. Ask the user to enter their hometown, print it out in uppercase letters.
hometown = input("Where is your hometown?")
print(hometown.lower())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
fcolour = input("What is your favorite colour?")
fcolour_length = len(fcolour)


# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
w = str(input("What is the weather?"))
m = str(input("What is the month?"))
print("It is " + m + " and it is " + w +" today")

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
t1 = float(input("What is the temperature in day 1?"))
t2 = float(input("What is the temperature in day 2?"))
t3 = float(input("What is the temperature in day 3?"))
t4 = float(input("What is the temperature in day 4?"))
t5 = float(input("What is the temperature in day 5?"))
m1 = input("What is the month?")
t = str((t1 + t2 + t3 +t4 + t5)/5)
print("It is " + str(m1) + " and the average temperature is " + t +" degree celsius")



# 11. Print out the above sentence but make the month upper case.
print("It is " + str(m1).upper() + " and the average temperature is " + t +" degree celsius")



# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
fanimals = "My favourite animals:\n\tCats,\n\tDogs,\n\tPigs"
print(fanimals)


# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
name = input("What is your name?\n")
number = int(input("Pick a number:\n"))
print(name[number].upper())
# Answer: print the number as the index for the name and use .upper()


# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
string = "WelcometoPython"
print(len(string))
print(string[1:14:2])

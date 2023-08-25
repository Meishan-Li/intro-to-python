# Session 5 Exercises

## Section A
# 1. Print 10 random numbers. - randin = random integer
import random
# wrong: number = random.randint(1,11)
# print(number)

# the loop will print a random number 10 times.
for number in range(10):
    print(random.random())


# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".

# wrong: guess = int(input("what's you number?"))
# while guess == int(7):
#print("Wow hucky number 7")
guess = None
while guess != 7:
    guess = int(input("Guess the computer's number:\n"))
  print("Wow! Lucky number 7!")


#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
# wrong: s_guess = int(input("what's you number?"))
#while s_guess == int(7):
  #print("pick another number")
#while s_guess != int(7):
 # print(str(s_guess))
import random 
computer_choice = random.randint(1, 10)
user_choice = None
while computer_choice != user_choice:
    user_choice = int(input("Guess the computer's number:\n"))
print("Well done! You guess the computer's number!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.
import math
width = int(input("What is the width of your rectangle:\n"))
height = int(input("What is the height of your rectangle:\n"))
# area_in_cm, is th width multiplied by height.
# area_in_m2 is first divided by 10000 to get from cm to m2 and math.ceil will round it up.
area_in_cm = width * height
area_in_m2 = math.ceil(area_in_cm/10000)
print("Your rectangle is " + str(area_in_m2) + ' metres squared.')

#or
width = int(input("What is the width of your rectangle:\n"))
height = int(input("What is the height of your rectangle:\n"))
area = width * height 
print(str(width) + "cm X " + str(height) + "com = " + str(area) + "cm2 = " + str(round(area / 10000) + "cm2"))

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
password = input("What's the password?")
correct_pw = "qwerty123"
times = 0
# wrong while password == correct_pw:
while times < 2:
  if password == correct_pw:
    print("You have successfully logged in")
    break
  else:
    print("PASSWORD FAILURE\n")
    password = input("What's the password?")
    times +=1

if times == 2:
  print("PASSWORD FAILURE\n")
  print("System Failure - You have entered 3 incorrect passwords.")

# 5. Add up all the numbers from 1 to 500 and print the answer.
# for i in range(1,501):
 # sum = sum(i)
 # print (str(sum))
  
total = 0

for x in range(1, 501):
    total += x

print(total)

# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
list_to_add = []
for x in range(10):
  list_to_add.append(int(input("Type a number to add: ")))
print(list_to_add.index(99))
  
  



# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
# wrong: multiplication = range(1,16)
#print(str(multiplication) + "x" + "18")
i=0
while i < 15:
  print(i*18)
  i += 1

#or
for x in range(1,16):
  print(str(x) + " x 18 = " + str(x*18))

# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
i=1
while i >= 1 and i<= 100:
  print (i)
  i += 1

#or answer
i=0
while i < 101:
    print(i)
    i += 1
  
# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.

lesson = None

while lesson < 3:
    lesson = input("Input your lesson:\n")
    mark = int(input("Input your mark:\n"))
    if mark > 80:
        print(lesson + " - A grade")
    elif mark <= 80 and mark > 60:
        print(lesson + " - B grade")
    elif mark <= 60 and mark > 50:
        print(lesson + " - C grade")
    elif mark <= 50 and mark> 45:
        print(lesson + " - D grade")
    elif mark <= 45 and mark > 25:
        print(lesson + " - E grade")
    elif mark < 25:
        print(lesson + " - F grade")
    else:
        print("Go to see your teacher")


# 10. IDK - Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
import random
prize_draw_list = []
user_input = None

# while the user does not enter a blank space, keep asking for names to be added to the draw
while user_input != "":
    user_input = input("Please input your name to be added to the prize draw:\n")
    # only if the user enters a name and not an empty string will it be added to the prize draw list
    if user_input != "":
        prize_draw_list.append(user_input)

# getting a random item out of the list and printing it as the winner 
print("Congratulations! " + random.choice(prize_draw_list) + " you are the winner of the prize draw!")


# 11. IDK - Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
import random

print("Welcome to Rock, Paper, Scissors")

user_score = 0
computer_score = 0
turns = 0

while turns < 3:
  user_choice = input("What is your move? (rock, paper, scissors) ")
  computer_choice = random.choice(["rock", "paper", "scissors"])
  print("You picked " + user_choice)
  print("The computer picked " + computer_choice)
  turns += 1
  print("This is turn: " + str(turns))
  if user_choice == "rock":
      if computer_choice == "scissors":
          print("You Win")
          user_score += 1
      elif computer_choice == "paper":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")
  elif user_choice == "paper":
      if computer_choice == "rock":
          print("You Win")
          user_score += 1
      elif computer_choice == "scissors":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")
  else:
      if computer_choice == "paper":
          print("You Win")
          user_score += 1
      elif computer_choice == "rock":
          print("You Lose")
          computer_score += 1
      else:
          print("It's a draw")

print("Game Over! Final Score: User Score: " + str(user_score) + "\n Computer Score: " + str(computer_score)) 

  
  
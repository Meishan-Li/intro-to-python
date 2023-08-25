# Session 8 Exercises


# All of these questions will use a set of pre-made files with data in. The files are in the text_files directory.
# In order to access the text files from this file, make sure you get into the text_files directory when using read/write.
# Ex: f = open("text_files/austen.txt", "r") OR f = open("text_files/register.txt", "w")


## Section A
# 1. Read the file 'jabberwocky.txt' and print its content to the screen.
# need to specify the ful path to the file, "r" = open in the read mod
f = open("text_files/jabberwocky.txt", "r")
print(f.read())


# 2. Read the file 'austen.txt' and print the amount of lines in the file.
total = 0
f = open("text_files/austen.txt", "r")
for line in f:
  total +=1

print(total)


# 3. Each line of the file 'numbers.txt' contains a number, write a script to add up all the values in the file.
f = open("text_files/number.txt", "r")
sum = 0
for x in f:
  # x would be string at this point. need to change it into integer
  x = int(x)
  sum += x

print(sum)


# <---------------------------------------------------------------------------------------------->

## Section B 
# "r"= read "a" = append "w" = write (will overwrite if things esist) "x" = create 
# 1. Ask the user to enter their name and append this to a file called 'register.txt'.
f = open("register.txt", "a")

  name = input("Enter a name: ")
  f.write(name)




# 2. Create a new file called 'even.txt' that contains only the even numbers from the file 'numbers.txt'.
f = open("even.txt", "w")

for x in open("numbers.txt"):
    x = int(x)
    if x % 2 == 0:
        f.write(str(x) + "\n")

f.close()
  


# 3. 'secret.txt' contains a secret message. Each number represents the letter of the alphabet where 1 = A, 2 = B ... Z = 26.  - tip: need to create a dictionary
#    Work out what the secret message says.
# start with secrete is empty string
alphabet = {
    0: "!",
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z"
}

word = ""
for x in open("secret.txt", "r"):
    x = int(x)
    word = word + alphabet[x]
print(word)


# 4. Benford’s law states that the leading digits in a collection of data are probably going to be small. 
#   For example, most numbers in a set (about 30%) will have a leading digit of 1, when the expected probability is 11.1% (i.e. one out of nine digits). 
#   Fake data is usually evenly distributed, where as real data isn't. The files 'accounts_1.txt', 'accounts_2.txt' and 'accounts_3.txt' contain financial transaction data. 
#   Work out which of the files contains fake data.
# STAGE 1 - this code allows us to check the values of one of the account files.
f = open("accounts_1.txt", "r")

count = {
  "0":0,
  "1":0,
  "2":0,
  "3":0,
  "4":0,
  "5":0,
  "6":0,
  "7":0,
  "8":0,
  "9":0
}

for x in f:
  if x:
    count[x[0]] += 1

for y in range(1,10):
  print(str(y) + " = " + str(count[str(y)]/100) + "%")

# STAGE 2 - Adding a for loop so we are able to loop through all accounts.
for x in range(1,4):
  f = open("accounts_" + str(x) + ".txt", "r")

  count = {
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
  }

  for num in f:
    if num:
      count[num[0]] += 1
  print(x)
  for y in range(1,10):
    print(str(y) + " = " + str(count[str(y)]/100) + "%")

#STAGE 3 - Changing count so instead of us manually having to input count, it will create itself
for x in range(1,4):
  f = open("accounts_" + str(x) + ".txt", "r")

  count = {}
  for i in range(1,10):
    count[str(i)] = 0

  for num in f:
    if num:
      count[num[0]] += 1
  print(x)
  for y in range(1,10):
    print(str(y) + " = " + str(count[str(y)]/100) + "%")

# STAGE 4 - Putting our code into a function - call 3 times

def benford_calc(file_name):
  f = open(file_name, "r")

  count = {}
  for i in range(1,10):
    count[str(i)] = 0

  for num in f:
    if num:
      count[num[0]] += 1
  print("Results for:" + file_name)
  for y in range(1,10):
    print(str(y) + " = " + str(count[str(y)]/100) + "%")

benford_calc("accounts_1.txt")
benford_calc("accounts_2.txt")
benford_calc("accounts_3.txt")

# STAGE 5 - Looping through file names, so we don't need to call the function 3 times, as per stage 4
def benford_calc(file_name):
  f = open(file_name, "r")

  count = {}
  for i in range(1,10):
    count[str(i)] = 0

  for num in f:
    if num:
      count[num[0]] += 1
  print("Results for:" + file_name)
  for y in range(1,10):
    print(str(y) + " = " + str(count[str(y)]/100) + "%")

for x in range (1,4):
  file_name = "accounts_" + str(x) + ".txt"
  benford_calc(file_name)

# STAGE 6 - Separating file function from data function 

def benford_calc_file(file_name):
  f = open(file_name, "r")
  return benford_calc(f)

def benford_calc(data):

  count = {}
  for x in range(1,10):
    count[str(x)] = 0

  for num in data:
      if num:
        count[str(num[0])] += 1
  
  return count 

for x in range (1,4):
  file_name = "accounts_" + str(x) + ".txt"
  data = benford_calc_file(file_name)

  print("Results for:" + file_name)

  for y in range(1,10):
      print(str(y) + " = " + str(data[str(y)]/100) + "%")

# STAGE 7 - Sending in a list of random numbers 

def benford_calc_file(file_name):
  f = open(file_name, "r")
  return benford_calc(f)

def benford_calc(data):

  count = {}
  for x in range(1,10):
    count[str(x)] = 0

  for num in data:
      if num:
        count[str(num[0])] += 1
  
  return count 

for x in range (1,4):
  file_name = "accounts_" + str(x) + ".txt"
  data = benford_calc_file(file_name)

  print("Results for:" + file_name)

  for y in range(1,10):
      print(str(y) + " = " + str(data[str(y)]/100) + "%")

random_nums = [str(random.randint(1,100)) for x in range(1,10001)]
data = benford_calc(random_nums)
print("Results for Random Nums")

for y in range(1,10):
      print(str(y) + " = " + str(data[str(y)]/100) + "%")
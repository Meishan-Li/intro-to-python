# Project Name: Ski Pass Cost Culculation
# Opening Readme file for this Project Description: 
f = open('Readme.md', 'r')
print(f.read(-1))

def ski_pass_cost (age, duration, is_student):
  base_price = 50
  week_price = 300
  season_price = 2000
  
  if duration == "day":
    total_cost = base_price
  elif duration == "week":
    total_cost = week_price
  elif duration == "season":
    total_cost = season_price
  else:
    print("Enter you pass duration again: ")

  
  if age < 7:
    total_cost = 0
  if age < 18 or is_student == "yes":
    total_cost *= 0.6
  else:
    total_cost = total_cost
    
  return total_cost


def main():
  print("Welcom to the Ski Pass Culculator!")
  age = int(input("Enter your age: "))
  duration = input("Enter pass duration (day/week/season): ").lower()
  is_student = input("Are you a student?(yes/no): ").lower()
  total_cost = ski_pass_cost(age, duration, is_student)
  print ("Your total ski pass cost is " + str(total_cost))

if __name__ == "__main__":
  main()

for age in range (60,200):
  print ("Please take good care of yourself!")
  break




    
  
    
    
    
   
  
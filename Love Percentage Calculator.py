print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1lower = name1.lower()
name2lower = name2.lower()
True_number = name1lower.count("t")+ name1lower.count("r")+ name1lower.count("u") + name1lower.count("e") + name2lower.count("t") + name2lower.count("r") + name2lower.count("u") + name2lower.count("e") 
Love_number = name1lower.count("l") + name1lower.count("o") + name1lower.count("v") + name1lower.count("e") + name2lower.count("l") + name2lower.count("o") + name2lower.count("v") + name2lower.count("e")
love_percent = str(True_number) + str(Love_number)
if int(love_percent) <10 or int(love_percent) > 90:
  print(f"Your love percentage is {love_percent}%. You mix up like coke and mentos.")
elif int(love_percent) > 40 or int(love_percent) <50:
  print(f"Your love percentage is {love_percent}%. You are fine together.")
else:
  print(f"Your love percentage is {love_percent}%.")
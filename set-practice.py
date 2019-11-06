#Prompt user to enter a string and then check if it has already entered
input_set = set()
str = input("Enter the input or -q to quit:  ")
while (str != "-q"):
  if str in input_set:
    print("You have already entered this string!")
  else:
    input_set.add(str)
    print("Thanks")

  str = input("Enter the input or -q to quit: ")

print ("Quit successfully!")



from datetime import datetime
# Question: Create a script that asks the user to enter their age, and the script
#  calculates the user's year of birth and prints it out in a string like in the expected output. 
# Please make sure you generate the current year dynamically.
dob = int(input("Enter your age: "))
today = datetime.now()
print(f"We think you were born in {today.year-dob}")
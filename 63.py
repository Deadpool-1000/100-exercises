# Question: Create a program that, once executed the programs prints Hello  instantly first, 
# then it prints it after 1 second, then after 2, 3, and 
# then the program prints out the message "End of the Loop" and stops.
import time
counter = 0
while counter <= 3:
    counter += 1
    print('hello')
    time.sleep(counter)

print("End of loop")
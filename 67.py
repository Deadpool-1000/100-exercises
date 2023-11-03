# Question: Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using 
# the following dictionary as a vocabulary source. 
# In addition, try to return the message, "We couldn't find that word!" 
# when the user enters a word that is not in the dictionary.
# Question: Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates it using the following dictionary as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 
word = input("Enter Word: ")
if word in d.keys():
    print(d.get(word))
else:
    print("We couldn't find that word!")
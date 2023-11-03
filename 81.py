
def is_ok_username(username):
    with open('users.txt', 'r') as f:
        users = f.readlines()
        print("Users: ", users)
    return False if username in users else True
while True:
    username = input("Enter Username: ")
    while not is_ok_username(username):
        print("Username Taken")
        username = input("Enter Username: ")
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)

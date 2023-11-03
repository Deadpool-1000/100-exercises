class PasswordGenerator:
    def __init__(self):
        self.path = r'users.txt'
        self.res = []
        with open(self.path, "r") as file:
            content = file.readlines()
            for line in content:
                self.res.append(line.strip())

    def username_checker(self, username):
        for name in self.res:
            if username == name.strip():
                print("Username already exists!!")
                return False
        print("Good Username")
        return True

    def password_validator(self, password):
        if (not any(num.isdigit() for num in password)) or (not any(num.isupper() for num in password)) or (len(password) < 5):
            print("Atleast one number should be in password.")
            return False
        else:
            return True
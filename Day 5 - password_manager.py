from cryptography.fernet import Fernet #this is a module that allows you to encrypt text

master_pswd = input("What is the master password? ")

#key + password + text to encrypt = random text
#random text + key + password = text to encrypt 

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: #this is going to create a file called key.key in wb (write in bytes) mode
        key_file.write(key)

write_key()

def view():
    with open('passwords.txt', 'r')as f:
        for line in f.readlines():
            data = (line.rstrip()) #rstrip takes away the carriage return after your username/password is displayed
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)
def add():
    name = input('Account Name: ')
    pswd = input("Password: ")

    with open('passwords.txt', 'a')as f: #using the 'with' keyword automatically closes the file for you. 'a' means append, 'w' means write to new (anything already in that file will be deleted when opened). 'r' means read only
        f.write(name + "|" + pswd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones? (view, add) Press q to quit: ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue 

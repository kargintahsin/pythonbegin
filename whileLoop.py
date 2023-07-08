# # Username and Password Checker with While + if else

defUsername = "MessiTaso"
defPassword = "Kargintino"


while (True):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if(username == defUsername) and (password == defPassword):
        print("Logged In")
        break
    else:
        print("Username or Password incorrect")
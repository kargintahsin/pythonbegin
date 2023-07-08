playerName = input("Enter the name: ")
playerSurname = input("Enter the surname: ")
playerTeam = input("Enter the team: ")

# print("Saving....")
# playerInfo = [playerName, playerSurname, playerTeam]
# print("Player Name: {}\nPlayer Surname: {}\nPlayer Team: {}".format(playerInfo[0], playerInfo[1], playerInfo[2]))
if playerTeam in ("Barcelona", "Barça"):
    print("Visca Barça")
elif playerTeam in ("Real Madrid", "Madritista"):
    print("Hala Madrid!!")
else:
    print("Player isn't playing Real Madrid or Barcelona")

# Username and Password Checker with if-else

defUsername = "MessiTaso"
defPassword = "Kargintino"

username = input("Enter your username: ")
password = input("Enter your password: ")

if (username == defUsername) and (password == defPassword):
    print("Logged In")
else:
    print("Username or Password incorrect")

computer = -1
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youstr]
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
print(f"You chose {reverseDict[you]}\nComputer chose:{reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you == 1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 1 and you == 0):
        print("you win")
    elif(computer == 1 and you == -1):
        print("you lose!")
    elif(computer == 0 and you == -1):
        print("you win")
    elif(computer == 0 and you == 1):
        print("you lose!")
    else:
        print("Something went wrong!")
import random
rules = ["rock", "paper", "scissor"]
user = "";
userScore = 0;
computerScore = 0;
def determineWin(user,computer):
    if (
        ( user == "rock" and computer == "paper" ) or
        ( user == "paper" and computer == "scissor" ) or
        ( user == "scissor" and computer == "rock" )
    ):
        return False
    return True
while(True):
    user = input("Type in your move (\"quit\" to end the game): ")
    computer = random.choice(rules)
    if (user == "quit"):
        break;
    elif (user == computer):
        print(f"Computer's move: {computer}")
        print("It's a tie")
    elif (determineWin(user,computer) == False):
        print(f"Computer's move: {computer}")
        print("Computer wins")
        computerScore +=1
    else:
        print(f"Computer's move: {computer}")
        print("User wins")
        userScore += 1
print(f"Final score \nUser {userScore} : {computerScore} Computer")
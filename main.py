import random 

def game_win(user , computer):
    if user == computer:
        return None
    
    #Snake v/s Water 
    if (user == "s" and computer == "w"):
        return True
    elif(user == "w" and computer == "s"):
        return False

    #water v/s gun
    if (user == "w" and computer == "g"):
        return True
    elif(user == "g" and computer == "w"):
        return False

    #Gun v/s Snake
    if (user == "g" and computer == "s"):
        return True
    elif(user == "s" and computer == "g"):
        return False

    return False

computer = random.choice(["s" , "w" , "g"])

player_score = 0
computer_score = 0


print("\n===== SNAKE - WATER - GUN =====")
print("Instructions:")
print("Snake (s), Water (w), Gun (g)")
print("Press 'q' anytime to quit the game.")
print("Let's start playing!\n")

while True:


    user = input("your turn (s/w/g) or 'q' to quit : ").strip().lower()
    if user == 'q':
        
        break
    if user not in ("s" , "w" , "g"):
        print("Invalid choice! Please enter 's' , 'w' , 'g' ")
        continue

    computer = random.choice(["s" , "w" , "g"])

    result = game_win(user ,computer) #Return True if you win, false for lose , None for draw
    
    choices = {"s": "Snake", "w": "Water", "g": "Gun"}

    print(f"\nYou chose: {choices[user]}")
    print(f"Computer chose: {choices[computer]}")


    if result is None:
        print("It's a draw")

    elif result:
        print("You Win")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1 

    print(f"Score -> you: {player_score} | computer: {computer_score}")




print("\n===== FINAL SCORE =====")
print(f"Your score: {player_score}")
print(f"Computer score: {computer_score}")

if player_score > computer_score:
    print("Congratulations! You won the game.")
elif computer_score > player_score:
    print("Computer won the game. Better luck next time!")
else:
    print("The game ended in a draw.")

print("Thanks for playing!")





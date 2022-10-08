import random
import time


def main():

    # Set base score values:
    user_score = 0
    computer_score = 0
    
    # Retrieve score from game and update base values:
    score = [0, "play"]
    while score[1] == "play":
        score = play(user_score, computer_score)
        if score[0] == 1:
            user_score += 1
        elif score[0] == 2:
            computer_score += 1


def play(p1, p2):

    # Set options to play with:
    options = ["rock", "paper", "scissors"]

    # Get user's input within available options:
    user = get_user(options)

    # Get a random choice to play as computer:
    computer = random.choice(options)

    # Print out how the game played out:
    print(f"You've chosen {user.upper()}, I've chosen {computer.upper()}")
    
    # Wait half a second before continue:
    time.sleep(0.5)

    # Check results:
    winner = check_result(user, computer, options)
    score = 0
    if winner == user:
        print("Congrats! You've WON :D")
        
        # Update score value:
        score = 1
        p1 += 1
    elif winner == "tie":
        print("Well well well, we have a TIE match! :|")
    else:
        print("Aw, it seems that you've LOST :(")
        
        # Update score value:
        score = 2
        p2 += 1
    
    # Ask to play again:
    while True:
        try:
            again = play_again(p1, p2)
            if again == "yes":
                print()
                return score, "play"
            elif again == "no":
                return score, print("Ok, See you next time!")
            else:
                print("Sorry, I don't know what you mean.")
                raise ValueError
        except ValueError:
            pass
        

def get_user(op):
    
    # Set counter:
    i = 0

    # Define 10 tries:
    while i < 10:
        try:
            
            # Retrieve user's input and check that's a valid option:
            user = input(f"{op[0]}, {op[1]} or {op[2]}? \n").lower()
            if user == op[0] or user == op[1] or user == op[2]:
                return user

            # If not valid, increase counter and raise Value Error:
            else:
                i += 1
                raise ValueError
        except ValueError:
            pass


def check_result(p1, p2, op):

    # If both player choose the same, declare a tie:
    if p1 == p2:
        return "tie"
    
    # If player 1 crushes player 2, declare player 1 as the winner:
    # (op[0] = rock, op[1] = paper, op[2] = scissors)
    elif (p1 == op[0] and p2 == op[2]) or (p1 == op[2] and p2 == op[1]) or (p1 == op[1] and p2 == op[0]):
        return p1
    
    # Else declare player 2 as the winner:
    else:
        return p2


def play_again(p1, p2):

    # Wait half a second before continue:
    time.sleep(0.5)

    # Print out current score:
    print(f"SCORE: You: {p1} - Me: {p2}")
    print()

    # Wait half a second before continue:
    time.sleep(0.5)

    # Ask to play again:
    return input(f"Do you want to play again? (yes or no) \n").lower()


if __name__ == "__main__":
    main()
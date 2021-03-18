import random

def play():
    print("Lets play Rock, Paper, Scissors")
    user = input("Enter 'r' for rock, 'p' for paper or 's' for scissor\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "It's a Tie..."

    if is_win(user, computer):
        return "Yay!! You Won..."
    
    return "Oh You Lost"
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
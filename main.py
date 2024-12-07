from random import randint as r

user = input("Rock Paper or Scissors: ").capitalize()
comp = r(1, 3)

def convert_comp_select(comp: int)-> str:
    if comp == 1:
        return "Rock"
    elif comp == 2:
        return "Paper"
    elif comp == 3:
        return "Scissors"
    
comp_choice = convert_comp_select(comp)
    
print(f"Comp: {comp_choice}")

while True:
    def game(user: str, comp: str)-> str:
        if user == "Rock" and comp == "Rock":
            return "Draw"
        elif user == "Paper" and comp == "Paper":
            return "Draw"
        elif user == "Scissors" and comp == "Scissors":
            return "Draw"
        elif user == "Rock" and comp == "Paper":
            return "Lose"
        elif user == "Rock" and comp == "Scissors":
            return "Win"
        elif user == "Paper" and comp == "Rock":
            return "Win"
        elif user == "Paper" and comp == "Scissors":
            return "Lose"
        elif user == "Scissors" and comp == "Rock":
            return "Lose"
        elif user == "Scissors" and comp == "Paper":
            return "Win"
        return 
    break
        
game_result = game(user, comp_choice)

print(game_result)
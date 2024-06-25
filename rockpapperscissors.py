
# Educational implementation without functions.
# Feel free to use, modify, and comment on the code.

# Python 3.10 - Rock, Paper, Scissors Game
# Olamigoke Philip 11-06-2024

import random

menu_message = "\n\n\tMenu Options \n1. Enter 'End' to Close Game.\n:"
END_KEYWORD = "end"
name_entry_message = "Enter Player Name: "
game_entry_message = "Enter [Rock, Paper, or Scissors] to play: "
game_entry_error_message = "Invalid Input. Enter [Rock, Paper, or Scissors] to play: "
game_points = {
    "paper": { "rock": 0, "scissors": 3, "paper": 1},
    "scissors": {"rock": 3, "paper": 0, "scissors": 1},
    "rock": {"rock": 1, "paper": 3, "scissors": 0},
}


results = {}

# PLAYER REGISTRATION
player_name = input(name_entry_message)
while len(player_name) < 3:
    print("Error!: Player name cannot be less than 3 characters")
    player_name = input(f"{name_entry_message} {menu_message}")

if player_name.lower() == END_KEYWORD:
    exit()

game_entry = input(f"{game_entry_message}").lower()
while game_entry:
    if game_entry != END_KEYWORD:
        if game_entry not in game_points.keys():
            game_entry = input(f"{game_entry_error_message} {menu_message}").lower()
        else:
            # DETERMIN COMPUTER ENTRY
            computer_entry = list(game_points.keys())[
                random.randrange(0, len(game_points.keys()))
            ]

            # Formula  => Game_points["oponnent_choice"]["player_choice"]
            player_score = game_points[computer_entry][game_entry]
            computer_score = game_points[game_entry][computer_entry]
            results["player_score"] = results.get("player_score", 0) + player_score
            results["computer_score"] = (
                results.get("computer_score", 0) + computer_score
            )
            print(f"You chose: {game_entry} and Computer chose: {computer_entry}")
            if player_score == computer_score:
                print("Oh! It's a draw")
            elif player_score > computer_score:
                print("You WON!!!")
            else:
                print("Computer Won!")

            game_entry = input(f"{game_entry_message} {menu_message}").lower()
    else:
        player_score = results.get("player_score", 0)
        computer_score = results.get("computer_score", 0)
        if player_score > 0 or computer_score > 0:
            print("Your Score", player_score)
            print("Computer Score", computer_score)
            if player_score == computer_score:
                print("You had a DRAW")
            elif player_score > computer_score:
                print("You WON the round.")
            else:
                print("Computer Won the round")
        exit()
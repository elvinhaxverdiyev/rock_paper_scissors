Rock, Paper, Scissors Game
This Python program implements the classic "Rock, Paper, Scissors" game. It allows the user to play against the computer, which makes a random choice. The game determines the result (Win, Lose, or Draw) based on the rules of Rock, Paper, Scissors.

How It Works
User Input:

The user is prompted to input their choice: "Rock", "Paper", or "Scissors".
The input is case-insensitive and automatically converted to a capitalized format (e.g., rock becomes Rock).
Computer's Random Choice:

The computer makes a random choice (1, 2, or 3) using the randint function.
This number is then converted into one of the following:
1 -> "Rock"
2 -> "Paper"
3 -> "Scissors"
Game Logic:

The program compares the user's choice with the computer's choice using a function called game().
The rules are:
Rock beats Scissors.
Scissors beat Paper.
Paper beats Rock.
Identical choices result in a draw.
Output:

The computer's choice and the result of the game (Win, Lose, or Draw) are displayed.

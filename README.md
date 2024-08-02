# TCP -- Terminal Chess with Powers

## What
A simple chess game with powers played in the command line by two players. I don't know how to play chess, but it is a profound game. Designed to be minimal and clean.

## Usage
Download all files and run the program using main.py. Follow the directions printed to the terminal. Ensure all dependencies are installed.\
\
You can run the program from the terminal in the src folder using:\
`python3 main.py`\
\
This will be updated when a binary is created.

## Questions
You can contact me at andy1233567890@gmail.com

## Issues by priority (tentative)
- account for special moves
    - castle (done, testing)
    - pawn promotion (done [only promotes to queen for now], testing)
    - en passant (done, testing)
- must devise way to look for check states before allowing a move to be made
    - putting a player into check
    - must not be able to put self into check, make these moves invalid
- check for checkmate
    - analyze all possible moves
    - if no move is possible (to exit check), player is checkmated
- power system
    - on random turns, pick a random empty tile to spawn a power
    - moving to that tile will give the piece the power
    - if player chooses to use a power, forfeit the move
- display for scores and captured pieces




## Dependencies
- colorama, for printing colored output
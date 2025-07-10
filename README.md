# memory-game
## Overview

This is a simple two-player memory matching game implemented in Python. The game uses numbers and hidden characters where players take turns to find matching pairs.

How to Play
The game starts with a list of numbers from 1 to 20.

Each number hides a secret character behind it.

Two players take turns to pick two numbers by entering their positions.

If the characters behind the numbers match, the player scores a point, and the numbers are replaced with *.

If they don't match, the numbers return to their original state.

The player with the highest score when all matches are found wins.

## Rules
Choose two different valid numbers from the list.

Numbers must not have been matched before (i.e., not replaced by *).

If you find a matching pair, you get a point and another chance.

If no match is found, the turn switches to the other player.

## How to Run
Make sure you have Python installed on your machine.

Download or clone this repository.

Run the script: python memory_game.py

## Features
Two-player turn-based game.

Real-time score tracking.

Input validation to avoid invalid or repeated selections.

Automatic detection of game end and winner announcement.



# Dice game

## General requirements

The idea is the following

* 2 players start with counters at 10.
    - One player is a computer the other human.
* Players role 1 dice each per round, the greatest number wins.
    - The one who wins the round will decrease their counter by one.
    - The one who lose the round will increase their counter by one.
* The first one to get their counter to zero wins the game.

## Specific requirements

### Interactivity

* Player should be prompted to roll the dice by presing any key.

### Rolling the dice

* The dice is six-sided and should produce numbers accordingly.

### Messages

* Game should congratulate the human player if thay win 
* Game should wish the player luck if they lose
* Game should explain the rules

## Requirements by class

### Player class

* Counter attribute (int) starting at 10.
* Dice attribute (Dice) holding and instance of Dice.
* Is_computer (Boolean) to check if it is a computer or not.

### Dice class

* roll_dice method to roll the siz sided-dice. Assign the result to value attribute.
* The score should be updated each time the dice is rolled.

### Game

* A Game class that loops through the rounds until the one player wins.
* Attributes
    * Human player
    * Computer player
    * Winner
* Start_game
    * Starts the infinite loop and creates the instances of the other classes. Display rules and options to play or exit.
* play_round
    * Plays a round, determines winner of round and updates players' counter attributes
* winner
    * Checks if somebody won the game (counter == 0), if so it interrupts the game and shows the adequate message.
* The Game class should display
    * Introduction and rules of the game
    * Options to play or quit
    * Game over 


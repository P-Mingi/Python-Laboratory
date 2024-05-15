
# 1. Introduction:

#### a. Application Description:
The name of the game is “Tic Tac Toe”, and it’s an python adaptation of the famous game. 
You can play using a consol-based interface, where player can interact with game, using numbers inputs.

####  b. How to Run the Program:  b. How to Run the Program:
  To run the program, we have to execute the program “TicTacToe.py”, and then, the game will appear in the consol, 
 asking the first player to put hes first token. 

####   c. How to Use the Program:
  When the program is run, the game appears on the consol with a 3x3 grill, each box correspond to one number, going from one to nine. 
  The player needs to enter the number of the box where they want to place their symbol (X or O). At the end of the game, 
  the players are asked if they want to play again. The game can end on a Win from a player or in a tied game.

# 2. Body/Analysis
#### a. The functional Requirements Coverage:
 
**Abstraction:** The Board class is abstracting the concept of the Tic Tac Toe board, providing methods for displaying, updating, 
and also checking the winning conditions.

**Inheritance:** The ConcreteBoard class inherits from the abstract Board class, providing a concrete implementation of the game board.

**Inheritance: **The is_winner method in the Board class is an example of inheritance, as it is inherited by the ConcreteBoard class to 
determine winning conditions.

**Encapsulation:** The Player classes encapsulate the logic for player moves, abstracting away the details of how moves are made.
 
**Encapsulation: **The is_equal method in the Board class encapsulates the logic for checking if the game has ended in a tie.

**Factory Method Pattern:** The game loop utilizes the Factory Method pattern to create instances of XPlayer and OPlayer, 
encapsulating the creation logic and allowing for easy extension with new player types.

**File import/export:** The program implements functions to import and export game results using an SVG file format, 
as specified in Requirement 3.

# 3. Results and Summary:

####  a. Results:  a. Results:
  - The program’s result is exactly what i wanted to create, the functionality of the Tic Tac Toe game are perfectly implemented, the players can put their tokens anywhere in the nine possible positions, the game determine the winner, the ties, and also save the previous game results. 
  
- The challenges that I faced were when I had to implement a design pattern, because I needed to rethink my code structure, and as well finding an idea to how I could implement data importation and exportation.

####   b. Conclusions:
 -  Using the coursework, I’ve made an enjoyable game where the user can play several games to find put the winner.
 
 - I implemented the object-oriented programming principles, using some element like inheritance or encapsulation, to make the code and the game effective.

####   c. Possible Extensions:
  - In the future I could make a graphic interface to the maker the game even more enjoyable. 
  
-  I could maybe think of implementing a solo game mode, where the user could play with an IA.
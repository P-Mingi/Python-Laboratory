
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
 
**-- Abstraction --** 

**ConcreteBoard Class:** This class is a concrete implementation of the Board abstract base class. It implements the update_box method.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/abstract-1.png)

**XPlayer Class:** This class is a concrete implementation of the Player abstract base class for the "X" player. It implements the move method.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/abstract-2.png)

**-- Polymorphism --** 

In the play_game function, polymorphism is demonstrated when instances of XPlayer and OPlayer are created through their respective factory objects (XPlayerFactory and OPlayerFactory). Despite being different classes, both XPlayer and OPlayer instances can be treated uniformly as instances of the Player abstract base class.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/Polymorphidm.png)

**-- Inheritance --** 

**OPlayer Class:** is a subclass of the Player abstract base class. It also inherits methods and properties from Player and implements the move method.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/abstract-3.png)

**-- Encapsulation --** 

**Board class:** uses _box as a protected attribute. In Python, a single underscore "_" prefix indicates that the attribute is intended for internal use within the class and its subclasses, but not for direct access from outside these classes.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/encapsulation.png)

**-- Factory Method Pattern --** 

The factory method pattern is implemented through the PlayerFactory abstract base class and its concrete subclasses XPlayerFactory and OPlayerFactory. This pattern allows for the creation of XPlayer and OPlayer instances without specifying the exact class of the object being created, promoting flexibility and adherence to the Open/Closed Principle.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/Factory%20method.png)

**-- Decorator Pattern --** 

The Decorator pattern is utilized in this code to add additional behavior (printing a message) to the move method of player objects without modifying their original implementations. This pattern promotes code reusability, extensibility, and separation of concerns by allowing behavior to be added dynamically to objects at runtime.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/Decorator.png)


**-- File import/export --** 

The save_game_results function writes the current game results to a CSV file. This function uses the csv.DictWriter class to write the dictionary of results to the file.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/Csv-1.png)

The load_game_results function reads the game results from a CSV file and returns them as a dictionary. This function uses the csv.DictReader class to read the CSV file into a dictionary.

![Alt text](https://raw.githubusercontent.com/P-Mingi/Python-Laboratory/main/Images/Csv-2.png)


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

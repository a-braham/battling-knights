# Battling Knights
The Battling Knights project simulates a battle arena where knights can move, attack, acquire items, and fight each other. This README will guide you on how to use the code and determine the output based on an instruction file.

## Getting Started
To use the code and determine the output, follow the steps below:

1. Clone the repository: [Battling Knights](https://github.com/a-braham/battling-knights.git)
2. Make sure you have Python >3.7 installed on your system.

## Project Structure
The project consists of the following files:

- `knight.py`: Defines the `Knight` class, representing a knight with attributes such as ID, color, position, status, equipped item, attack, and defense.
- `fight.py`: Contains the `Fight` class with methods for attacking knights and handling knight deaths.
- `position.py`: Defines the `Position` class, representing a position on the game board.
- `arena.py`: Contains the `Arena` class, representing the battle arena, with methods for moving knights, resolving fights, and managing items.
- `item.py`: Defines the `Item` class, representing an item that knights can acquire.
- `serializer.py`: Provides serialization and deserialization functions for reading moves from a file and saving the final game state.
- `run.py`: Contains the main logic of setting up the game board, reading instructions, and rendering the game state.

## Instructions File
To determine the output of the game based on a set of instructions, create a file named `moves.txt` and populate it with the desired instructions. Each instruction should be in the format: `KnightID:Direction`.

For example, to move knight R north and knight Y east, the `moves.txt` file would look like this:
```
R:N
Y:E
```
Make sure to place the `moves.txt` file in the same directory as the Python files.

## Running the Game
To run the game and determine the output:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
```
python run.py
```
4. Run tests
```
python test.py
```

The game will execute the instructions from the `moves.txt` file, simulate the battles, and display the resulting game state.

## Output
The output of the game will be displayed in the terminal. It includes:

- The initial state of the arena with knights and items.
- Information about knight movements, fights, and acquisitions.
- The final state of the arena after executing all instructions.

## Saving the Final Game State
After the game finishes executing the instructions, it will save the final game state to a file named `final_state.json` in the project directory. This file contains the serialized representation of the knights and items in the game.

## Conclusion
You can use the provided code and the instructions file to simulate battles between knights, move them around the arena, and observe the outcomes. Have fun exploring different scenarios and strategies within the Battling Knights game!

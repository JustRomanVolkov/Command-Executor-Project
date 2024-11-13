# Command Executor Project 
This project is a Python-based command executor that recursively reads Python files in a given directory, extracts a list of commands defined in the variable CMDS, and executes them sequentially, ensuring each command runs only once.

## Features 
- Recursively scans the given directory to find Python files (.py). 
- Extracts commands from a variable named CMDS in each Python file. 
- Executes commands in alphabetical order based on file path. 
- Avoids repeated execution of the same command. 
- Provides informative output if a command has already been executed.

## Requirements 
The project does not require any third-party libraries. 

## Installation 
1. Clone the repository: 
``` 
 git clone https://github.com/JustRomanVolkov/Command-Executor-Project.git
```

## Usage 
Run the script by specifying the directory you want to scan. The directory should contain Python files with commands stored in a variable named CMDS.

```
python main.py <directory> 
```
For example: 
```
python main.py examples/ 
```

### Example Directory Structure 
The script expects Python files to have list called CMDS that defines commands to be executed. Here is an example:

``` 
 main.py 
 examples/ 
    a.py (contains CMDS = ['echo 1', 'echo 2']) 
    1/ b.py (contains CMDS = ['echo 3']) 
    2/ c.py (contains CMDS = ['echo 4', 'echo 5']) 
``` 
### Example Output 
If you run the script as follows, output will look like this: 
 ``` 
4
5
2
3
1
команда "echo 2" уже выполнялась
``` 

## Code Structure 
- CommandExecutor: Handles the execution of commands and keeps track of executed commands to avoid repetitions. 
- CommandLoader: Loads Python files and extracts the commands from the CMDS variable. 
- CommandRunner: Manages the flow by coordinating between CommandLoader and CommandExecutor.


## Testing 
Unit tests have been provided to verify the core functionality of the Command Executor. 
These tests ensure that: 
- Commands from the CMDS variable are executed in the correct order. 
- Commands are not repeated if they have already been executed. 
- The script properly handles various directory structures and file contents. 
 
To run the tests, use the following command: 
``` 
python -m unittest discover 
```
The tests utilize the unittest framework along with unittest.mock to validate the printed output.

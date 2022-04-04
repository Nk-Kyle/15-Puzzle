# 15-Puzzle
 Tugas Kecil 3 IF2211 Strategi Algoritma <br>
 IF2211 Algorithm Strategies Course Task.
# Author
> Ng Kyle (13520040)

## Table of Contents
* [General Info](#general-information)
* [Technologies Used and Requirements](#technologies-used-and-requirements)
* [Usage](#usage)
* [Setup](#setup)
* [Project Status](#project-status)


## General Information
- 15-Puzzle Solver using Branch and Bound Algorithm made using python language
- Implementation including: Console Application and GUI application
- Heuristic chosen to estimate cost is: The number of tiles doesn't match with target configuration


## Technologies Used and Requirements
- Python3 
- Required External Libraries (for main.py): <br>
   numpy, colorama <br>
   Installation (using pip) <br><br>
   ``` python
   pip install numpy, colorama
   ``` 


## Usage
To use console application:
- Go to src folder
- Open console.py
- Do the steps according the prompts

To use GUI application:
- Go to src folder and open program.py (or go to bin folder, run program.exe)
- To set grid:
  - Option 1: Manually set the grid values by changing the input boxes (4 x 4 boxes)
  - Option 2: Randomize by pressing the Random button
  - Option 3: Use configuration from file by pressing Open File Button and select wanted configuration file side effects of chosen heuristic.
- Press Solve Button to start solving.

### The program may buffer indefinitely for a complex configuration (32> steps) and take lots of memory in the runtime.

## Setup
You need to have python installed in your machine (or using venv in vscode)


## Project Status
Project is: _completed_

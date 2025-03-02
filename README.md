# Student Progression System

## Overview
This is a Python-based application that determines a student's progression status based on their module scores. The program follows predefined rules to categorize students into different progression outcomes: **Progress**, **Progress (module trailer)**, **Module retriever**, and **Exclude**.

## Features
- Accepts student marks as input.
- Validates inputs to ensure only integer values within the valid range are accepted.
- Determines and displays the correct progression outcome.
- Supports multiple test cases.
- Displays a histogram of student outcomes.

## Installation
1. Ensure you have **Python 3.x** installed.
2. Clone this repository or download the project files:
   ```bash
   git clone <repository_url>
   cd student-progression-system
   ```
3. Run the program:
   ```bash
   python main.py
   ```

## Usage
1. Enter the required pass, defer, and fail marks.
2. The program will validate the input and determine the progression outcome.
3. The program loops to accept multiple inputs until the user chooses to exit.
4. A histogram will be displayed showing the total counts for each category.

## Test Cases
The program has been tested with the following inputs:

| Pass | Defer | Fail | Expected Outcome |
|------|-------|------|-----------------|
| 120  | 0     | 0    | Progress |
| 100  | 20    | 0    | Progress (module trailer) |
| 80   | 20    | 20   | Module retriever |
| 40   | 0     | 80   | Exclude |

## Validation Rules
- Inputs must be integers.
- Total of Pass, Defer, and Fail marks must be **exactly 120**.
- Values must be in the range of **0, 20, 40, 60, 80, 100, or 120**.

## Histogram Representation
At the end of execution, a histogram is displayed, showing the total number of students in each category:

## Author
**Dhanushi Dewmindi Panamulla Arachchi**

## License
This project is licensed under the MIT License.


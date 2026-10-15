# Student Performance Analytics System

## Project Title
Student Performance Analytics System

## Objective
Build a Python-based system that reads student data and analyzes total marks, average marks, grades, pass/fail statistics, subject-wise performance, and top performers.

## Technologies Used
- Python
- NumPy
- Pandas

## Dataset
`students.csv` contains 20 student records with these columns:
- `Student_ID`
- `Name`
- `Department`
- `Computer_Marks`
- `Maths_Marks`
- `English_Marks`
- `Attendance_Percent`

## Grading and Pass/Fail Rules
The assignment requires clearly defined rules but does not prescribe specific thresholds. This project uses:
- Total: sum of the three subject marks.
- Average: total divided by 3.
- Grade A: average >= 90
- Grade B: average >= 75 and < 90
- Grade C: average >= 60 and < 75
- Grade D: average >= 35 and < 60
- Grade F: average < 35
- Pass: at least 35 marks in every subject; otherwise Fail.

## Project Files
- `main.py` — loads the CSV and runs the analysis.
- `students.csv` — student dataset.
- `functions.py` — reusable calculations and output functions.
- `Project_Documentation.md` — project documentation.
- `README.md`: this file.
- `screenshots/`: output screenshots.

## Requirements and Run Instructions
Python 3, NumPy, and Pandas are required.

Install the libraries if needed:
```bash
python -m pip install numpy pandas
```

Run the project from this folder:
```bash
python main.py
```

The program displays the dataset, student totals and averages, grades, pass/fail results, class summary, subject-wise averages, and top-performing student(s).


from pathlib import Path
import pandas as pd
from functions import calculate_student_results, display_analysis


def main():
    data_file = Path(__file__).with_name("students.csv")

    try:
        students = pd.read_csv(data_file)
    except FileNotFoundError:
        print("Error: students.csv was not found. Keep it in the same folder as main.py.")
        return
    except (pd.errors.EmptyDataError, pd.errors.ParserError):
        print("Error: students.csv is empty or badly formatted.")
        return

    required_columns = [
        "Student_ID", "Name", "Department", "Computer_Marks",
        "Maths_Marks", "English_Marks", "Attendance_Percent"
    ]
    missing_columns = [column for column in required_columns if column not in students.columns]
    if missing_columns:
        print("Error: Missing required columns:", ", ".join(missing_columns))
        return

    results = calculate_student_results(students)
    display_analysis(students, results)


if __name__ == "__main__":
    main()

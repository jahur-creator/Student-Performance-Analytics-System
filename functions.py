import numpy as np
import pandas as pd

SUBJECT_COLUMNS = ["Computer_Marks", "Maths_Marks", "English_Marks"]


def calculate_student_results(data):
    results = data.copy()
    results["Total_Marks"] = results[SUBJECT_COLUMNS].sum(axis=1)
    results["Average_Marks"] = np.round(results[SUBJECT_COLUMNS].mean(axis=1), 2)

    def assign_grade(average):
        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 35:
            return "D"
        return "F"

    results["Grade"] = results["Average_Marks"].apply(assign_grade)

    results["Result"] = results[SUBJECT_COLUMNS].ge(35).all(axis=1).map(
        {True: "Pass", False: "Fail"}
    )
    return results


def get_class_summary(results):
    subject_averages = results[SUBJECT_COLUMNS].mean().round(2)
    return {
        "student_count": int(len(results)),
        "class_average": round(float(results["Average_Marks"].mean()), 2),
        "highest_average": round(float(results["Average_Marks"].max()), 2),
        "lowest_average": round(float(results["Average_Marks"].min()), 2),
        "pass_count": int((results["Result"] == "Pass").sum()),
        "fail_count": int((results["Result"] == "Fail").sum()),
        "subject_averages": subject_averages,
        "lowest_students": results[
    results["Average_Marks"] == results["Average_Marks"].min()
][["Student_ID", "Name", "Average_Marks"]],
"best_subject": subject_averages.idxmax(),
        "top_performers": results[
            results["Average_Marks"] == results["Average_Marks"].max()
        ][["Student_ID", "Name", "Average_Marks", "Grade", "Result"]],
    }


def display_analysis(data, results):
    print("\nSTUDENT PERFORMANCE ANALYTICS SYSTEM")
    print("=" * 42)
    print("\nDATASET PREVIEW")
    print(data.to_string(index=False))
    print("\nDATASET INFORMATION")
    print(f"Number of records: {len(data)}")
    print(f"Columns: {', '.join(data.columns)}")
    print("\nSTUDENT RESULTS")
    display_columns = [
        "Student_ID", "Name", "Department", "Total_Marks",
        "Average_Marks", "Grade", "Result", "Attendance_Percent"
    ]
    print(results[display_columns].to_string(index=False))

    summary = get_class_summary(results)
    print("\nCLASS SUMMARY")
    print(f"Number of students: {summary['student_count']}")
    print(f"Class average marks: {summary['class_average']}")
    print(f"Highest student average: {summary['highest_average']}")
    print(f"Lowest student average: {summary['lowest_average']}")
    print(f"Students passed: {summary['pass_count']}")
    print(f"Students failed: {summary['fail_count']}")

    print("\nSUBJECT-WISE AVERAGE MARKS")
    for subject, average in summary["subject_averages"].items():
        print(f"{subject.replace('_Marks', '')}: {average}")

        best_subject = summary["best_subject"].replace("_Marks", "")
    print(f"\nBest subject: {best_subject} ({summary['subject_averages'].max()})")

    print("\nLOWEST-PERFORMING STUDENT(S)")
    print(summary["lowest_students"].to_string(index=False))

    print("\nTOP-PERFORMING STUDENT(S)")
    print(summary["top_performers"].to_string(index=False))

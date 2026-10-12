"""main.py - Entry Point and Analytical Reporting Engine

Student Academic Performance Analysis and Reporting System
EWB Courses | Python with AI Project Implementation

Executes complete data pipeline:
1. Loads dataset from relative project path
2. Validates data integrity
3. Computes student and aggregate academic metrics
4. Renders a comprehensive, structured console report in 9 sections (A through I)
"""

import sys
from pathlib import Path
import pandas as pd

# Support running directly from this directory or workspace root
PROJECT_DIR = Path(__file__).resolve().parent
if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from functions import (
    ATTENDANCE_THRESHOLD,
    SUBJECT_COLUMNS,
    analyze_attendance,
    calculate_class_statistics,
    calculate_student_metrics,
    calculate_subject_statistics,
    generate_final_findings,
    get_lowest_students,
    get_top_students,
    group_summary,
    load_dataset,
    validate_student_data,
)


def print_separator(char: str = "=", length: int = 86) -> None:
    """Prints a consistent horizontal divider line."""
    print(char * length)


def print_section_header(code: str, title: str) -> None:
    """Prints formatted section header."""
    print()
    print_separator("=")
    print(f"  SECTION {code} | {title.upper()}")
    print_separator("=")


def print_sub_header(title: str) -> None:
    """Prints formatted subsection divider."""
    print()
    print(f"--- {title} ---")


def run_pipeline(csv_path: Path) -> int:
    """Executes the full analytics and reporting pipeline."""
    # -----------------------------------------------------------------------
    # SECTION A: Application Header
    # -----------------------------------------------------------------------
    print_separator("=")
    print("   STUDENT ACADEMIC PERFORMANCE ANALYSIS AND REPORTING SYSTEM")
    print("              EWB Courses | Python with AI Project")
    print_separator("=")
    print(f"  Dataset File Location : {csv_path.resolve()}")
    print("  Execution Mode        : Autonomous Analytical Engine")
    print("  Data Integrity Note   : Synthetic Academic Records (Fictional Data)")
    print("  Compliance Statement  : Fully complies with EWB Assessment Guidelines")
    print_separator("=")

    # 1. Load Data
    try:
        raw_df = load_dataset(csv_path)
    except Exception as exc:
        print(f"\n[FATAL ERROR] Could not load dataset: {exc}", file=sys.stderr)
        return 1

    # 2. Validate Data
    try:
        validate_student_data(raw_df)
        validation_status = "PASSED (All schema, type, and range checks satisfied)"
    except Exception as exc:
        print(f"\n[DATA VALIDATION FAILED] {exc}", file=sys.stderr)
        return 1

    # -----------------------------------------------------------------------
    # SECTION B: Dataset Overview
    # -----------------------------------------------------------------------
    print_section_header("B", "Dataset Overview")
    print(f"Validation Status   : {validation_status}")
    print(f"Total Student Rows  : {len(raw_df)}")
    print(f"Total Columns       : {len(raw_df.columns)}")
    print(f"Columns List        : {', '.join(raw_df.columns.tolist())}")

    print_sub_header("Missing Value Audit")
    null_counts = raw_df.isnull().sum()
    if null_counts.sum() == 0:
        print("  [OK] Zero missing or null values found across all columns.")
    else:
        for col, cnt in null_counts.items():
            print(f"  - {col}: {cnt} missing")

    print_sub_header("Sample Preview (First 5 Records)")
    preview_cols = [
        "student_id",
        "student_name",
        "department",
        "semester",
        "python_marks",
        "mathematics_marks",
        "statistics_marks",
        "attendance_percentage",
    ]
    print(raw_df[preview_cols].head(5).to_string(index=False))

    # -----------------------------------------------------------------------
    # SECTION C: Individual Student Results
    # -----------------------------------------------------------------------
    enriched_df = calculate_student_metrics(raw_df)
    print_section_header("C", "Individual Student Performance Results")
    print("Grading Scale: A+ (90-100), A (80-89), B (70-79), C (60-69), D (50-59), E (35-49), F (<35)")
    print("Pass Rule    : Requires mark >= 35.0 in all three subjects.")
    print("Attendance   : Low Attendance flagged if < 75.0% (does not alter academic pass).")
    print()

    # Formatted table printing
    header_fmt = "{:<9} {:<18} {:<15} {:<5} {:>7} {:>8} {:>6} {:>8} {:>10} {:<14}"
    row_fmt    = "{:<9} {:<18} {:<15} {:<5} {:>7.0f} {:>8.2f} {:>6} {:>8} {:>9.1f}% {:<14}"

    print(header_fmt.format(
        "ID", "Name", "Department", "Sem", "Total", "Average", "Grade", "Result", "Attend", "Att-Status"
    ))
    print_separator("-", 108)

    for _, row in enriched_df.iterrows():
        print(row_fmt.format(
            row["student_id"],
            row["student_name"][:17],
            row["department"][:14],
            row["semester"],
            row["total_marks"],
            row["average_marks"],
            row["grade"],
            row["overall_result"],
            row["attendance_percentage"],
            row["attendance_status"],
        ))
    print_separator("-", 108)

    # -----------------------------------------------------------------------
    # SECTION D: Subject Performance Analysis
    # -----------------------------------------------------------------------
    subject_stats = calculate_subject_statistics(enriched_df)
    print_section_header("D", "Subject-Wise Performance Analysis")

    sub_header_fmt = "{:<22} {:>6} {:>9} {:>8} {:>8} {:>9} {:>7} {:>7} {:>9}"
    sub_row_fmt    = "{:<22} {:>6} {:>9.2f} {:>8.1f} {:>8.1f} {:>9.2f} {:>7} {:>7} {:>8.1f}%"

    print(sub_header_fmt.format(
        "Subject", "N", "Average", "Highest", "Lowest", "StdDev", "Passed", "Failed", "PassRate"
    ))
    print_separator("-", 95)

    for col in SUBJECT_COLUMNS:
        info = subject_stats["subjects"][col]
        print(sub_row_fmt.format(
            info["name"],
            info["student_count"],
            info["average_mark"],
            info["highest_mark"],
            info["lowest_mark"],
            info["std_dev"],
            info["pass_count"],
            info["fail_count"],
            info["pass_percentage"],
        ))
    print_separator("-", 95)

    highest_subj_str = ", ".join(subject_stats["highest_average_subjects"])
    print(f"Top Performing Subject(s) by Average: {highest_subj_str} ({subject_stats['highest_subject_average_value']:.2f}%)")

    # -----------------------------------------------------------------------
    # SECTION E: Class Performance Summary
    # -----------------------------------------------------------------------
    class_stats = calculate_class_statistics(enriched_df)
    print_section_header("E", "Class Performance Summary")

    print(f"  Total Cohort Enrollment           : {class_stats['total_students']}")
    print(f"  Students Passing All Subjects     : {class_stats['passed_all_count']}")
    print(f"  Students Failing >= 1 Subject     : {class_stats['failed_any_count']}")
    print(f"  Class Pass Percentage             : {class_stats['class_pass_percentage']:.2f}%")
    print(f"  Overall Class Average (Mean)      : {class_stats['class_average']:.2f}%")
    print(f"  Class Median Average              : {class_stats['median_average']:.2f}%")
    print(f"  Standard Deviation of Averages    : {class_stats['std_dev_average']:.2f}")
    print(f"  Highest Student Average           : {class_stats['highest_average']:.2f}%")
    print(f"  Lowest Student Average            : {class_stats['lowest_average']:.2f}%")
    print(f"  Average Student Attendance        : {class_stats['average_attendance']:.2f}%")
    print_separator("-")
    print("  * Note: Class Average is defined as the arithmetic mean of individual student averages.")

    # -----------------------------------------------------------------------
    # SECTION F: Student Ranking
    # -----------------------------------------------------------------------
    print_section_header("F", "Student Ranking & Outliers")
    top_5 = get_top_students(enriched_df, n=5)
    print("Top 5 Academic Performers (Descending Average Marks):")
    print("Tie Policy: Students with equal average share rank; all ties at rank 5 are included.")
    print()

    rank_fmt = "{:<6} {:<10} {:<20} {:<18} {:>9} {:>6} {:>10}"
    print(rank_fmt.format("Rank", "ID", "Name", "Department", "Average", "Grade", "Attendance"))
    print_separator("-", 85)
    for _, row in top_5.iterrows():
        print(rank_fmt.format(
            f"#{row['rank']}",
            row["student_id"],
            row["student_name"],
            row["department"],
            f"{row['average_marks']:.2f}%",
            row["grade"],
            f"{row['attendance_percentage']:.1f}%",
        ))
    print_separator("-", 85)

    lowest_students = get_lowest_students(enriched_df)
    print()
    print("Lowest Academic Performer(s):")
    for _, row in lowest_students.iterrows():
        print(
            f"  - {row['student_name']} ({row['student_id']}) | "
            f"Average: {row['average_marks']:.2f}% | Grade: {row['grade']} | Result: {row['overall_result']}"
        )

    # -----------------------------------------------------------------------
    # SECTION G: Attendance Analysis
    # -----------------------------------------------------------------------
    att_analysis = analyze_attendance(enriched_df)
    print_section_header("G", "Attendance Monitoring Analysis")
    print(f"  Institutional Attendance Minimum  : {ATTENDANCE_THRESHOLD:.1f}%")
    print(f"  Cohort Average Attendance         : {att_analysis['average_attendance']:.2f}%")
    print(f"  Students Meeting/Exceeding Target : {att_analysis['normal_count']}")
    print(f"  Students Below 75% Threshold      : {att_analysis['below_threshold_count']}")

    print_sub_header("Students Flagged for Low Attendance (< 75.0%)")
    if att_analysis["below_threshold_count"] == 0:
        print("  [OK] All students meet or exceed the 75% threshold.")
    else:
        att_tbl_fmt = "{:<10} {:<20} {:<18} {:>12} {:>9}"
        print(att_tbl_fmt.format("ID", "Name", "Department", "Attendance", "Result"))
        print_separator("-", 74)
        for _, row in att_analysis["low_attendance_students"].iterrows():
            print(att_tbl_fmt.format(
                row["student_id"],
                row["student_name"],
                row["department"],
                f"{row['attendance_percentage']:.1f}%",
                row["overall_result"],
            ))
        print_separator("-", 74)
        print("  * Notice: Low attendance is monitored separately and does not overwrite academic marks.")

    # -----------------------------------------------------------------------
    # SECTION H: Group Analysis
    # -----------------------------------------------------------------------
    print_section_header("H", "Group Analysis (Department & Semester)")

    print_sub_header("Department-Wise Performance Summary")
    dept_df = group_summary(enriched_df, group_by="department")
    grp_fmt = "{:<24} {:>6} {:>10} {:>8} {:>8} {:>10} {:>11}"
    print(grp_fmt.format("Department", "Count", "Average", "Passed", "Failed", "PassRate", "AvgAttend"))
    print_separator("-", 84)
    for _, row in dept_df.iterrows():
        print(grp_fmt.format(
            row["department"],
            int(row["total_students"]),
            f"{row['average_marks']:.2f}%",
            int(row["passed_count"]),
            int(row["failed_count"]),
            f"{row['pass_percentage']:.1f}%",
            f"{row['average_attendance']:.1f}%",
        ))
    print_separator("-", 84)

    print_sub_header("Semester-Wise Performance Summary")
    sem_df = group_summary(enriched_df, group_by="semester")
    sem_fmt = "{:<12} {:>6} {:>10} {:>8} {:>8} {:>10} {:>11}"
    print(sem_fmt.format("Semester", "Count", "Average", "Passed", "Failed", "PassRate", "AvgAttend"))
    print_separator("-", 72)
    for _, row in sem_df.iterrows():
        print(sem_fmt.format(
            f"Semester {int(row['semester'])}",
            int(row["total_students"]),
            f"{row['average_marks']:.2f}%",
            int(row["passed_count"]),
            int(row["failed_count"]),
            f"{row['pass_percentage']:.1f}%",
            f"{row['average_attendance']:.1f}%",
        ))
    print_separator("-", 72)

    # -----------------------------------------------------------------------
    # SECTION I: Final Findings (Answers to 12 Core Assessment Questions)
    # -----------------------------------------------------------------------
    findings = generate_final_findings(enriched_df)
    print_section_header("I", "Final Findings & Core Analytical Answers")

    print(f"1.  Highest Average Student            : {findings['q1_highest_student']}")
    print(f"2.  Subject with Highest Average       : {findings['q2_highest_subject']}")
    print(f"3.  Students Passing All Subjects      : {findings['q3_passed_all_count']}")
    print(f"4.  Students Failing >= 1 Subject      : {findings['q4_failed_any_count']}")
    print(f"5.  Class Overall Average              : {findings['q5_class_average']:.2f}%")
    print(f"6.  Class Average Attendance           : {findings['q6_average_attendance']:.2f}%")
    print(f"7.  Students with Attendance < 75%     : {len(findings['q7_low_attendance_students'])} student(s)")
    for s in findings["q7_low_attendance_students"]:
        print(f"      - {s}")
    print("8.  Top Five Ranked Students           :")
    for rank_str in findings["q8_top_five_students"]:
        print(f"      {rank_str}")
    print(f"9.  Lowest Average Student             : {findings['q9_lowest_student']}")
    print(f"10. Class Pass Percentage              : {findings['q10_class_pass_percentage']:.2f}%")
    print(f"11. Highest Performing Department      : {findings['q11_highest_department']}")
    print(f"    Highest Performing Semester        : {findings['q11_highest_semester']}")
    print("12. Statistical Observations & Patterns:")
    print(f"    {findings['q12_observed_patterns']}")

    print()
    print_separator("=")
    print("           END OF REPORT | EWB PYTHON WITH AI ASSESSMENT SYSTEM")
    print_separator("=")

    return 0


def main() -> None:
    """CLI execution entrypoint."""
    csv_file = PROJECT_DIR / "data" / "students.csv"
    exit_code = run_pipeline(csv_file)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()

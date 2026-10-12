"""functions.py - Reusable Analytical and Data Processing Functions

Student Academic Performance Analysis and Reporting System
EWB Courses | Python with AI Project Implementation

This module provides reusable, modular functions for:
- Dataset loading and thorough integrity validation
- Academic metrics calculation (totals, unrounded averages, grades, pass/fail)
- Subject-level and class-level statistical summaries (using NumPy & Pandas)
- Attendance threshold analysis
- Student ranking with deterministic tie-handling
- Department and semester aggregation
- Dynamic answering of core analytical queries
"""

from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
import numpy as np
import pandas as pd

# ---------------------------------------------------------------------------
# Constants and Academic Rules Configuration
# ---------------------------------------------------------------------------

REQUIRED_COLUMNS: List[str] = [
    "student_id",
    "student_name",
    "department",
    "semester",
    "python_marks",
    "mathematics_marks",
    "statistics_marks",
    "attendance_percentage",
]

SUBJECT_COLUMNS: List[str] = [
    "python_marks",
    "mathematics_marks",
    "statistics_marks",
]

SUBJECT_DISPLAY_NAMES: Dict[str, str] = {
    "python_marks": "Python Programming",
    "mathematics_marks": "Mathematics",
    "statistics_marks": "Statistics",
}

SUBJECT_PASS_MARK: float = 35.0
ATTENDANCE_THRESHOLD: float = 75.0


# ---------------------------------------------------------------------------
# Data Ingestion & Validation
# ---------------------------------------------------------------------------

def load_dataset(filepath: Union[str, Path]) -> pd.DataFrame:
    """Loads a student records dataset from a CSV file.

    Args:
        filepath: Path to the CSV file (str or Path object).

    Returns:
        pd.DataFrame: Loaded dataset.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        ValueError: If the file is empty or cannot be parsed as CSV.
    """
    path = Path(filepath)
    if not path.is_file():
        raise FileNotFoundError(f"Dataset file not found at: {path.resolve()}")

    if path.stat().st_size == 0:
        raise ValueError(f"Dataset file is completely empty (0 bytes): {path.resolve()}")

    try:
        df = pd.read_csv(path)
    except Exception as exc:
        raise ValueError(f"Failed to parse CSV file at {path}: {exc}") from exc

    if df.empty:
        raise ValueError(f"Dataset at {path} contains no data rows.")

    return df


def validate_student_data(df: pd.DataFrame) -> None:
    """Validates student dataset against strict data quality requirements.

    Checks performed:
    1. Input is a non-empty pandas DataFrame.
    2. All 8 required columns are present.
    3. No blank/null values in student_id, student_name, department, semester.
    4. Student IDs are strictly unique (no duplicates).
    5. Semester values are positive integers (1, 2, 3, ...).
    6. Numerical fields (marks, attendance) contain valid numbers.
    7. Marks for each subject are within [0, 100].
    8. Attendance percentages are within [0, 100].

    Args:
        df: pandas DataFrame containing student records.

    Raises:
        TypeError: If input is not a pandas DataFrame.
        ValueError: If any validation rule is violated, with actionable detail.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"Expected pandas DataFrame, received {type(df).__name__}")

    if df.empty:
        raise ValueError("Cannot validate an empty DataFrame.")

    # 1. Required column presence
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        raise ValueError(
            f"Dataset is missing required columns: {missing_cols}. "
            f"Expected all of: {REQUIRED_COLUMNS}"
        )

    # 2. Duplicate Student IDs
    duplicates = df[df.duplicated(subset=["student_id"], keep=False)]
    if not duplicates.empty:
        dup_ids = duplicates["student_id"].unique().tolist()
        raise ValueError(
            f"Duplicate student_id detected: {dup_ids}. "
            f"Student IDs must be unique across all records."
        )

    # 3. Blank or null student identifiers
    text_cols = ["student_id", "student_name", "department"]
    for col in text_cols:
        if df[col].isnull().any():
            bad_rows = df[df[col].isnull()].index.tolist()
            raise ValueError(f"Column '{col}' contains null/missing values at rows {bad_rows}.")
        # Also check for whitespace-only strings
        blank_mask = df[col].astype(str).str.strip() == ""
        if blank_mask.any():
            bad_rows = df[blank_mask].index.tolist()
            raise ValueError(f"Column '{col}' contains blank/whitespace values at rows {bad_rows}.")

    # 4. Semester validation (must be positive integer)
    try:
        sem_numeric = pd.to_numeric(df["semester"], errors="raise")
    except Exception as exc:
        raise ValueError(f"Column 'semester' must contain valid numeric integers: {exc}") from exc

    if not (sem_numeric == sem_numeric.round()).all():
        raise ValueError("Column 'semester' contains non-integer decimal values.")

    if (sem_numeric <= 0).any():
        bad_sems = df[sem_numeric <= 0]["semester"].tolist()
        raise ValueError(f"Column 'semester' contains non-positive values: {bad_sems}. Must be > 0.")

    # 5. Numerical validation for marks & attendance
    numeric_fields = SUBJECT_COLUMNS + ["attendance_percentage"]
    for col in numeric_fields:
        try:
            converted = pd.to_numeric(df[col], errors="raise")
        except Exception as exc:
            raise ValueError(f"Column '{col}' contains non-numeric values: {exc}") from exc

        # Range checks: [0, 100]
        out_of_bounds = converted[(converted < 0) | (converted > 100)]
        if not out_of_bounds.empty:
            raise ValueError(
                f"Column '{col}' contains values outside the allowable range [0, 100]: "
                f"{out_of_bounds.tolist()}"
            )


# ---------------------------------------------------------------------------
# Academic Evaluation Logic
# ---------------------------------------------------------------------------

def assign_grade(average: float) -> str:
    """Assigns an academic letter grade based on unrounded average mark.

    Grading Scale (project-defined):
        90.0 to 100.0 : A+
        80.0 to < 90.0: A
        70.0 to < 80.0: B
        60.0 to < 70.0: C
        50.0 to < 60.0: D
        35.0 to < 50.0: E
        < 35.0        : F

    Args:
        average: Unrounded floating-point average mark.

    Returns:
        str: Letter grade (A+, A, B, C, D, E, or F).

    Raises:
        ValueError: If average mark is outside [0, 100].
    """
    if not isinstance(average, (int, float, np.number)) or np.isnan(average):
        raise ValueError(f"Invalid average mark for grading: {average}")

    if average < 0.0 or average > 100.0:
        raise ValueError(f"Average mark {average} out of allowable range [0, 100].")

    if average >= 90.0:
        return "A+"
    elif average >= 80.0:
        return "A"
    elif average >= 70.0:
        return "B"
    elif average >= 60.0:
        return "C"
    elif average >= 50.0:
        return "D"
    elif average >= 35.0:
        return "E"
    else:
        return "F"


def check_subject_pass(mark: float) -> bool:
    """Determines if a single subject mark meets the pass threshold (>= 35)."""
    return bool(mark >= SUBJECT_PASS_MARK)


def check_overall_pass(python_mark: float, math_mark: float, stats_mark: float) -> bool:
    """Determines overall academic pass status.

    Rule: A student passes overall if and only if all three subject marks are >= 35.
    """
    return (
        check_subject_pass(python_mark)
        and check_subject_pass(math_mark)
        and check_subject_pass(stats_mark)
    )


def check_attendance_status(attendance: float, threshold: float = ATTENDANCE_THRESHOLD) -> str:
    """Evaluates attendance percentage against the institutional threshold (75%).

    Returns 'Normal' if attendance >= 75%, otherwise 'Low Attendance'.
    """
    return "Normal" if attendance >= threshold else "Low Attendance"


def calculate_student_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Computes academic metrics for each student and returns an enriched DataFrame.

    Calculations added:
    - total_marks: sum of python, mathematics, statistics marks
    - average_marks: arithmetic mean of the three subject marks (unrounded float)
    - grade: letter grade assigned from average_marks
    - overall_result: 'Pass' if all 3 subjects >= 35, else 'Fail'
    - attendance_status: 'Normal' if attendance >= 75%, else 'Low Attendance'
    - python_pass, math_pass, stats_pass: boolean pass indicators per subject

    Args:
        df: Validated student DataFrame.

    Returns:
        pd.DataFrame: New copy of DataFrame with calculated columns.
    """
    result = df.copy()

    # Numerical calculations using pandas vectorized arithmetic
    result["total_marks"] = (
        result["python_marks"] + result["mathematics_marks"] + result["statistics_marks"]
    )
    result["average_marks"] = result["total_marks"] / 3.0

    # Subject-wise pass flags
    result["python_pass"] = result["python_marks"] >= SUBJECT_PASS_MARK
    result["mathematics_pass"] = result["mathematics_marks"] >= SUBJECT_PASS_MARK
    result["statistics_pass"] = result["statistics_marks"] >= SUBJECT_PASS_MARK

    # Overall result: must pass all 3
    all_passed_mask = (
        result["python_pass"] & result["mathematics_pass"] & result["statistics_pass"]
    )
    result["overall_result"] = np.where(all_passed_mask, "Pass", "Fail")

    # Letter Grade assignment based on unrounded average
    result["grade"] = result["average_marks"].apply(assign_grade)

    # Attendance status
    result["attendance_status"] = np.where(
        result["attendance_percentage"] >= ATTENDANCE_THRESHOLD,
        "Normal",
        "Low Attendance",
    )

    return result


# ---------------------------------------------------------------------------
# Aggregate Analytics: Subject & Class
# ---------------------------------------------------------------------------

def calculate_subject_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """Calculates comprehensive subject-level performance metrics using NumPy & Pandas.

    Metrics computed for each subject:
    - student_count: total students evaluated
    - average_mark: arithmetic mean (float)
    - highest_mark: maximum mark obtained
    - lowest_mark: minimum mark obtained
    - std_dev: standard deviation (sample standard deviation, ddof=1)
    - pass_count: count of students scoring >= 35
    - fail_count: count of students scoring < 35
    - pass_percentage: (pass_count / student_count) * 100

    Also identifies the subject(s) with the highest average, handling ties cleanly.

    Args:
        df: Validated student DataFrame.

    Returns:
        dict: Detailed dictionary of per-subject metrics and best-performing subject(s).
    """
    stats: Dict[str, Any] = {"subjects": {}}

    highest_avg = -1.0
    best_subjects: List[str] = []

    for col in SUBJECT_COLUMNS:
        scores = df[col].to_numpy(dtype=float)
        count = len(scores)
        mean_val = float(np.mean(scores))
        max_val = float(np.max(scores))
        min_val = float(np.min(scores))
        std_val = float(np.std(scores, ddof=1)) if count > 1 else 0.0

        passes = int(np.sum(scores >= SUBJECT_PASS_MARK))
        fails = count - passes
        pass_pct = (passes / count * 100.0) if count > 0 else 0.0

        stats["subjects"][col] = {
            "name": SUBJECT_DISPLAY_NAMES[col],
            "student_count": count,
            "average_mark": mean_val,
            "highest_mark": max_val,
            "lowest_mark": min_val,
            "std_dev": std_val,
            "pass_count": passes,
            "fail_count": fails,
            "pass_percentage": pass_pct,
        }

        # Track highest average
        if np.isclose(mean_val, highest_avg, atol=1e-5):
            best_subjects.append(SUBJECT_DISPLAY_NAMES[col])
        elif mean_val > highest_avg:
            highest_avg = mean_val
            best_subjects = [SUBJECT_DISPLAY_NAMES[col]]

    stats["highest_average_subjects"] = best_subjects
    stats["highest_subject_average_value"] = highest_avg

    return stats


def calculate_class_statistics(df_metrics: pd.DataFrame) -> Dict[str, Any]:
    """Calculates overall class-level performance summary using NumPy & Pandas.

    The overall class average is explicitly defined as the arithmetic mean
    of the individual student averages.

    Metrics:
    - total_students: total number of enrolled records
    - passed_all_count: students passing all 3 subjects
    - failed_any_count: students failing at least 1 subject
    - class_average: arithmetic mean of individual student averages
    - median_average: median of individual student averages (via numpy.median)
    - std_dev_average: standard deviation of individual student averages (sample, ddof=1)
    - highest_average: highest student average score
    - lowest_average: lowest student average score
    - average_attendance: mean attendance across the class
    - class_pass_percentage: (passed_all_count / total_students) * 100

    Args:
        df_metrics: Enriched DataFrame produced by calculate_student_metrics().

    Returns:
        dict: Summary statistics dictionary.
    """
    total = len(df_metrics)
    if total == 0:
        raise ValueError("Cannot calculate class statistics for an empty DataFrame.")

    averages = df_metrics["average_marks"].to_numpy(dtype=float)
    attendances = df_metrics["attendance_percentage"].to_numpy(dtype=float)

    passed_all = int((df_metrics["overall_result"] == "Pass").sum())
    failed_any = total - passed_all

    class_avg = float(np.mean(averages))
    median_avg = float(np.median(averages))
    std_avg = float(np.std(averages, ddof=1)) if total > 1 else 0.0
    highest_avg = float(np.max(averages))
    lowest_avg = float(np.min(averages))
    avg_attendance = float(np.mean(attendances))
    pass_pct = (passed_all / total * 100.0)

    return {
        "total_students": total,
        "passed_all_count": passed_all,
        "failed_any_count": failed_any,
        "class_average": class_avg,
        "median_average": median_avg,
        "std_dev_average": std_avg,
        "highest_average": highest_avg,
        "lowest_average": lowest_avg,
        "average_attendance": avg_attendance,
        "class_pass_percentage": pass_pct,
    }


# ---------------------------------------------------------------------------
# Rankings & Extreme Performers
# ---------------------------------------------------------------------------

def get_top_students(df_metrics: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Returns the top n students ordered by average_marks descending.

    Tie-handling policy:
    Students are sorted primarily by `average_marks` descending, and secondarily
    by `attendance_percentage` descending and `student_id` ascending for deterministic order.
    Furthermore, if any students are tied with the nth student's average mark,
    all tied students are included to ensure fairness.

    Args:
        df_metrics: Enriched DataFrame with student metrics.
        n: Cutoff rank (default: 5).

    Returns:
        pd.DataFrame: Top students DataFrame.
    """
    if df_metrics.empty:
        return df_metrics.copy()

    # Sort descending by average marks, then attendance
    sorted_df = df_metrics.sort_values(
        by=["average_marks", "attendance_percentage", "student_id"],
        ascending=[False, False, True],
    ).reset_index(drop=True)

    if len(sorted_df) <= n:
        top_df = sorted_df.copy()
    else:
        cutoff_avg = sorted_df.iloc[n - 1]["average_marks"]
        # Include all students with score >= cutoff score
        top_df = sorted_df[sorted_df["average_marks"] >= cutoff_avg].copy()

    # Assign dense ranking for display
    top_df["rank"] = top_df["average_marks"].rank(ascending=False, method="min").astype(int)
    return top_df


def get_lowest_students(df_metrics: pd.DataFrame) -> pd.DataFrame:
    """Identifies the student(s) with the minimum average marks.

    Handles ties by returning all students sharing the lowest average score.

    Args:
        df_metrics: Enriched DataFrame with student metrics.

    Returns:
        pd.DataFrame: Records of lowest performer(s).
    """
    if df_metrics.empty:
        return df_metrics.copy()

    min_avg = df_metrics["average_marks"].min()
    lowest_mask = np.isclose(df_metrics["average_marks"], min_avg, atol=1e-5)
    return df_metrics[lowest_mask].copy().reset_index(drop=True)


def get_highest_students(df_metrics: pd.DataFrame) -> pd.DataFrame:
    """Identifies the student(s) with the maximum average marks.

    Handles ties by returning all students sharing the highest average score.
    """
    if df_metrics.empty:
        return df_metrics.copy()

    max_avg = df_metrics["average_marks"].max()
    highest_mask = np.isclose(df_metrics["average_marks"], max_avg, atol=1e-5)
    return df_metrics[highest_mask].copy().reset_index(drop=True)


# ---------------------------------------------------------------------------
# Attendance & Group Aggregations
# ---------------------------------------------------------------------------

def analyze_attendance(
    df_metrics: pd.DataFrame, threshold: float = ATTENDANCE_THRESHOLD
) -> Dict[str, Any]:
    """Analyzes attendance distribution across the cohort.

    Returns:
    - average_attendance: class-wide mean attendance
    - below_threshold_count: number of students with attendance < threshold
    - normal_count: number of students with attendance >= threshold
    - low_attendance_students: DataFrame slice of students below threshold
    - normal_attendance_students: DataFrame slice of students meeting threshold
    """
    attendances = df_metrics["attendance_percentage"].to_numpy(dtype=float)
    avg_att = float(np.mean(attendances))

    low_mask = df_metrics["attendance_percentage"] < threshold
    low_df = df_metrics[low_mask].copy().reset_index(drop=True)
    normal_df = df_metrics[~low_mask].copy().reset_index(drop=True)

    return {
        "average_attendance": avg_att,
        "below_threshold_count": len(low_df),
        "normal_count": len(normal_df),
        "low_attendance_students": low_df,
        "normal_attendance_students": normal_df,
    }


def group_summary(df_metrics: pd.DataFrame, group_by: str = "department") -> pd.DataFrame:
    """Generates an aggregated summary grouped by department or semester.

    Metrics calculated per group:
    - total_students: group size
    - average_marks: mean of individual student averages
    - passed_count: count of students who passed all subjects
    - failed_count: count of students who failed at least 1 subject
    - pass_percentage: (passed_count / total_students) * 100
    - average_attendance: mean attendance within the group

    Args:
        df_metrics: Enriched DataFrame.
        group_by: Column name ('department' or 'semester').

    Returns:
        pd.DataFrame: Sorted summary DataFrame.
    """
    if group_by not in df_metrics.columns:
        raise ValueError(f"Grouping column '{group_by}' not found in DataFrame.")

    grouped = df_metrics.groupby(group_by)

    summary_records = []
    for name, group in grouped:
        total = len(group)
        passes = int((group["overall_result"] == "Pass").sum())
        fails = total - passes
        avg_score = float(group["average_marks"].mean())
        pass_pct = (passes / total * 100.0) if total > 0 else 0.0
        avg_att = float(group["attendance_percentage"].mean())

        summary_records.append({
            group_by: name,
            "total_students": total,
            "average_marks": avg_score,
            "passed_count": passes,
            "failed_count": fails,
            "pass_percentage": pass_pct,
            "average_attendance": avg_att,
        })

    summary_df = pd.DataFrame(summary_records)
    # Sort descending by average marks
    return summary_df.sort_values(by="average_marks", ascending=False).reset_index(drop=True)


# ---------------------------------------------------------------------------
# Programmatic Synthesis of the 12 Analytical Questions
# ---------------------------------------------------------------------------

def generate_final_findings(df_metrics: pd.DataFrame) -> Dict[str, Any]:
    """Generates precise runtime answers for the 12 required analytical questions.

    Guarantees every answer is derived from data at runtime without hardcoding.
    """
    subject_stats = calculate_subject_statistics(df_metrics)
    class_stats = calculate_class_statistics(df_metrics)
    top_students_df = get_top_students(df_metrics, n=5)
    highest_students_df = get_highest_students(df_metrics)
    lowest_students_df = get_lowest_students(df_metrics)
    att_stats = analyze_attendance(df_metrics)

    dept_summary = group_summary(df_metrics, group_by="department")
    sem_summary = group_summary(df_metrics, group_by="semester")

    # Q1: Highest average student(s)
    q1_highest = [
        f"{row['student_name']} ({row['student_id']}) with {row['average_marks']:.2f}%"
        for _, row in highest_students_df.iterrows()
    ]

    # Q2: Subject with highest average
    q2_subjects = ", ".join(subject_stats["highest_average_subjects"])
    q2_avg_val = subject_stats["highest_subject_average_value"]

    # Q7: Low attendance students
    q7_low_att = [
        f"{row['student_name']} ({row['student_id']} - {row['attendance_percentage']:.1f}%)"
        for _, row in att_stats["low_attendance_students"].iterrows()
    ]

    # Q8: Top five students summary
    q8_top_five = [
        f"#{int(row['rank'])} {row['student_name']} ({row['student_id']}): {row['average_marks']:.2f}% [Grade: {row['grade']}]"
        for _, row in top_students_df.iterrows()
    ]

    # Q9: Lowest average student(s)
    q9_lowest = [
        f"{row['student_name']} ({row['student_id']}) with {row['average_marks']:.2f}%"
        for _, row in lowest_students_df.iterrows()
    ]

    # Q11: Top department and semester
    best_dept = dept_summary.iloc[0]
    best_sem = sem_summary.iloc[0]
    sem_val = int(best_sem['semester']) if pd.notnull(best_sem['semester']) else best_sem['semester']

    # Q12: Numerical patterns
    # Observe actual data correlations cleanly
    corr_att_score = float(df_metrics["attendance_percentage"].corr(df_metrics["average_marks"]))
    pattern_desc = (
        f"1. Overall cohort pass rate is {class_stats['class_pass_percentage']:.1f}%. "
        f"2. Pearson correlation between attendance and average marks is {corr_att_score:+.2f}, "
        f"reflecting a {'positive' if corr_att_score > 0 else 'neutral/negative'} association in the cohort. "
        f"3. While attendance issues were flagged for {att_stats['below_threshold_count']} students, "
        f"failures ({class_stats['failed_any_count']} students) were strictly driven by academic subject marks (< 35)."
    )

    return {
        "q1_highest_student": ", ".join(q1_highest),
        "q2_highest_subject": f"{q2_subjects} ({q2_avg_val:.2f}%)",
        "q3_passed_all_count": class_stats["passed_all_count"],
        "q4_failed_any_count": class_stats["failed_any_count"],
        "q5_class_average": class_stats["class_average"],
        "q6_average_attendance": class_stats["average_attendance"],
        "q7_low_attendance_students": q7_low_att,
        "q8_top_five_students": q8_top_five,
        "q9_lowest_student": ", ".join(q9_lowest),
        "q10_class_pass_percentage": class_stats["class_pass_percentage"],
        "q11_highest_department": f"{best_dept['department']} ({best_dept['average_marks']:.2f}%)",
        "q11_highest_semester": f"Semester {sem_val} ({best_sem['average_marks']:.2f}%)",
        "q12_observed_patterns": pattern_desc,
    }

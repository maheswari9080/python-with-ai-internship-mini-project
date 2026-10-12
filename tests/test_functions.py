"""test_functions.py - Comprehensive Unit Tests

Student Academic Performance Analysis and Reporting System
EWB Courses | Python with AI Project Implementation

Covers:
- Grade boundaries (A+, A, B, C, D, E, F) and extreme values
- Subject pass boundary (35 vs 34.9)
- Overall academic pass logic (requires passing all three subjects)
- Attendance threshold boundaries (75.0% vs 74.9%)
- Total marks and average calculations
- Subject and class statistics verification
- Top-five rankings and tie-handling behavior
- Data validation rules (duplicate IDs, blank fields, invalid ranges, bad semesters, missing columns)
- File ingestion error handling (missing files, empty files)
"""

import sys
import tempfile
import unittest
from pathlib import Path
import numpy as np
import pandas as pd

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from functions import (
    ATTENDANCE_THRESHOLD,
    SUBJECT_PASS_MARK,
    analyze_attendance,
    assign_grade,
    calculate_class_statistics,
    calculate_student_metrics,
    calculate_subject_statistics,
    check_attendance_status,
    check_overall_pass,
    check_subject_pass,
    generate_final_findings,
    get_lowest_students,
    get_top_students,
    group_summary,
    load_dataset,
    validate_student_data,
)


class TestGradingLogic(unittest.TestCase):
    """Unit tests for grade assignment boundaries."""

    def test_grade_boundaries_a_plus(self):
        self.assertEqual(assign_grade(100.0), "A+")
        self.assertEqual(assign_grade(95.5), "A+")
        self.assertEqual(assign_grade(90.0), "A+")

    def test_grade_boundaries_a(self):
        self.assertEqual(assign_grade(89.999), "A")
        self.assertEqual(assign_grade(85.0), "A")
        self.assertEqual(assign_grade(80.0), "A")

    def test_grade_boundaries_b(self):
        self.assertEqual(assign_grade(79.999), "B")
        self.assertEqual(assign_grade(75.0), "B")
        self.assertEqual(assign_grade(70.0), "B")

    def test_grade_boundaries_c(self):
        self.assertEqual(assign_grade(69.999), "C")
        self.assertEqual(assign_grade(65.0), "C")
        self.assertEqual(assign_grade(60.0), "C")

    def test_grade_boundaries_d(self):
        self.assertEqual(assign_grade(59.999), "D")
        self.assertEqual(assign_grade(55.0), "D")
        self.assertEqual(assign_grade(50.0), "D")

    def test_grade_boundaries_e(self):
        self.assertEqual(assign_grade(49.999), "E")
        self.assertEqual(assign_grade(40.0), "E")
        self.assertEqual(assign_grade(35.0), "E")

    def test_grade_boundaries_f(self):
        self.assertEqual(assign_grade(34.999), "F")
        self.assertEqual(assign_grade(20.0), "F")
        self.assertEqual(assign_grade(0.0), "F")

    def test_grade_out_of_bounds_errors(self):
        with self.assertRaises(ValueError):
            assign_grade(-1.0)
        with self.assertRaises(ValueError):
            assign_grade(100.1)
        with self.assertRaises(ValueError):
            assign_grade(float("nan"))


class TestPassFailRules(unittest.TestCase):
    """Unit tests for subject and overall pass/fail determination."""

    def test_subject_pass_threshold(self):
        self.assertTrue(check_subject_pass(35.0))
        self.assertTrue(check_subject_pass(35.1))
        self.assertTrue(check_subject_pass(100.0))
        self.assertFalse(check_subject_pass(34.999))
        self.assertFalse(check_subject_pass(0.0))

    def test_overall_pass_all_passed(self):
        # All three >= 35
        self.assertTrue(check_overall_pass(35.0, 35.0, 35.0))
        self.assertTrue(check_overall_pass(80.0, 90.0, 85.0))

    def test_overall_pass_single_subject_failure(self):
        # If any single subject is below 35, overall must be False
        self.assertFalse(check_overall_pass(34.9, 90.0, 90.0))
        self.assertFalse(check_overall_pass(90.0, 34.9, 90.0))
        self.assertFalse(check_overall_pass(90.0, 90.0, 34.9))

    def test_overall_pass_multiple_subject_failures(self):
        self.assertFalse(check_overall_pass(20.0, 20.0, 90.0))
        self.assertFalse(check_overall_pass(15.0, 15.0, 15.0))


class TestAttendanceStatus(unittest.TestCase):
    """Unit tests for attendance monitoring threshold."""

    def test_attendance_status_threshold(self):
        self.assertEqual(check_attendance_status(100.0), "Normal")
        self.assertEqual(check_attendance_status(75.0), "Normal")
        self.assertEqual(check_attendance_status(74.99), "Low Attendance")
        self.assertEqual(check_attendance_status(0.0), "Low Attendance")


class TestCalculationsAndAnalytics(unittest.TestCase):
    """Unit tests for student metrics and summary statistics."""

    def setUp(self):
        self.sample_df = pd.DataFrame([
            {
                "student_id": "S01",
                "student_name": "Alice",
                "department": "CS",
                "semester": 1,
                "python_marks": 90.0,
                "mathematics_marks": 90.0,
                "statistics_marks": 90.0,
                "attendance_percentage": 95.0,
            },
            {
                "student_id": "S02",
                "student_name": "Bob",
                "department": "CS",
                "semester": 1,
                "python_marks": 60.0,
                "mathematics_marks": 60.0,
                "statistics_marks": 60.0,
                "attendance_percentage": 70.0,
            },
            {
                "student_id": "S03",
                "student_name": "Charlie",
                "department": "IT",
                "semester": 2,
                "python_marks": 35.0,
                "mathematics_marks": 35.0,
                "statistics_marks": 35.0,
                "attendance_percentage": 75.0,
            },
            {
                "student_id": "S04",
                "student_name": "David",
                "department": "IT",
                "semester": 2,
                "python_marks": 80.0,
                "mathematics_marks": 30.0,  # Math fails!
                "statistics_marks": 80.0,
                "attendance_percentage": 85.0,
            },
        ])

    def test_calculate_student_metrics(self):
        enriched = calculate_student_metrics(self.sample_df)

        # Alice: 90, 90, 90 -> total 270, avg 90.0, Grade A+, Pass, Normal
        alice = enriched[enriched["student_id"] == "S01"].iloc[0]
        self.assertEqual(alice["total_marks"], 270.0)
        self.assertEqual(alice["average_marks"], 90.0)
        self.assertEqual(alice["grade"], "A+")
        self.assertEqual(alice["overall_result"], "Pass")
        self.assertEqual(alice["attendance_status"], "Normal")

        # Bob: 60, 60, 60 -> total 180, avg 60.0, Grade C, Pass, Low Attendance
        bob = enriched[enriched["student_id"] == "S02"].iloc[0]
        self.assertEqual(bob["total_marks"], 180.0)
        self.assertEqual(bob["average_marks"], 60.0)
        self.assertEqual(bob["grade"], "C")
        self.assertEqual(bob["overall_result"], "Pass")
        self.assertEqual(bob["attendance_status"], "Low Attendance")

        # Charlie: exactly 35 in all subjects -> Grade E, Pass, Normal (75.0%)
        charlie = enriched[enriched["student_id"] == "S03"].iloc[0]
        self.assertEqual(charlie["average_marks"], 35.0)
        self.assertEqual(charlie["grade"], "E")
        self.assertEqual(charlie["overall_result"], "Pass")
        self.assertEqual(charlie["attendance_status"], "Normal")

        # David: 80, 30, 80 -> avg 63.33, Grade C, Fail (due to Math 30)
        david = enriched[enriched["student_id"] == "S04"].iloc[0]
        self.assertAlmostEqual(david["average_marks"], 190.0 / 3.0)
        self.assertEqual(david["grade"], "C")
        self.assertEqual(david["overall_result"], "Fail")

    def test_class_statistics(self):
        enriched = calculate_student_metrics(self.sample_df)
        stats = calculate_class_statistics(enriched)

        self.assertEqual(stats["total_students"], 4)
        self.assertEqual(stats["passed_all_count"], 3)
        self.assertEqual(stats["failed_any_count"], 1)
        self.assertEqual(stats["class_pass_percentage"], 75.0)
        self.assertAlmostEqual(stats["highest_average"], 90.0)
        self.assertAlmostEqual(stats["lowest_average"], 35.0)
        # Expected class average: (90 + 60 + 35 + 63.3333) / 4 = 62.0833
        expected_class_avg = (90.0 + 60.0 + 35.0 + (190.0 / 3.0)) / 4.0
        self.assertAlmostEqual(stats["class_average"], expected_class_avg)

    def test_subject_statistics(self):
        enriched = calculate_student_metrics(self.sample_df)
        sub_stats = calculate_subject_statistics(enriched)

        # Check Python marks: 90, 60, 35, 80 -> mean = 66.25, max = 90, min = 35, pass = 4, fail = 0
        py_info = sub_stats["subjects"]["python_marks"]
        self.assertEqual(py_info["student_count"], 4)
        self.assertAlmostEqual(py_info["average_mark"], 66.25)
        self.assertEqual(py_info["highest_mark"], 90.0)
        self.assertEqual(py_info["lowest_mark"], 35.0)
        self.assertEqual(py_info["pass_count"], 4)
        self.assertEqual(py_info["fail_count"], 0)

        # Check Math marks: 90, 60, 35, 30 -> pass = 3, fail = 1
        math_info = sub_stats["subjects"]["mathematics_marks"]
        self.assertEqual(math_info["pass_count"], 3)
        self.assertEqual(math_info["fail_count"], 1)

    def test_top_students_and_ties(self):
        # Create dataset with tied 5th place
        records = [
            {"student_id": "S01", "student_name": "A", "department": "CS", "semester": 1,
             "python_marks": 95, "mathematics_marks": 95, "statistics_marks": 95, "attendance_percentage": 90},
            {"student_id": "S02", "student_name": "B", "department": "CS", "semester": 1,
             "python_marks": 90, "mathematics_marks": 90, "statistics_marks": 90, "attendance_percentage": 90},
            {"student_id": "S03", "student_name": "C", "department": "CS", "semester": 1,
             "python_marks": 85, "mathematics_marks": 85, "statistics_marks": 85, "attendance_percentage": 90},
            {"student_id": "S04", "student_name": "D", "department": "CS", "semester": 1,
             "python_marks": 80, "mathematics_marks": 80, "statistics_marks": 80, "attendance_percentage": 90},
            {"student_id": "S05", "student_name": "E", "department": "CS", "semester": 1,
             "python_marks": 75, "mathematics_marks": 75, "statistics_marks": 75, "attendance_percentage": 90},
            {"student_id": "S06", "student_name": "F", "department": "CS", "semester": 1,
             "python_marks": 75, "mathematics_marks": 75, "statistics_marks": 75, "attendance_percentage": 85}, # Tied with 5th!
            {"student_id": "S07", "student_name": "G", "department": "CS", "semester": 1,
             "python_marks": 50, "mathematics_marks": 50, "statistics_marks": 50, "attendance_percentage": 80},
        ]
        df = pd.DataFrame(records)
        enriched = calculate_student_metrics(df)
        top = get_top_students(enriched, n=5)

        # Both S05 and S06 should be included because of tie at cutoff score 75.0
        self.assertEqual(len(top), 6)
        ids = top["student_id"].tolist()
        self.assertIn("S05", ids)
        self.assertIn("S06", ids)
        self.assertNotIn("S07", ids)

    def test_lowest_students(self):
        enriched = calculate_student_metrics(self.sample_df)
        lowest = get_lowest_students(enriched)
        self.assertEqual(len(lowest), 1)
        self.assertEqual(lowest.iloc[0]["student_id"], "S03")
        self.assertEqual(lowest.iloc[0]["average_marks"], 35.0)

    def test_group_summary(self):
        enriched = calculate_student_metrics(self.sample_df)
        dept_sum = group_summary(enriched, group_by="department")
        self.assertEqual(len(dept_sum), 2)
        # Check that departments are CS and IT
        depts = dept_sum["department"].tolist()
        self.assertIn("CS", depts)
        self.assertIn("IT", depts)


class TestValidationAndDataQuality(unittest.TestCase):
    """Unit tests for data validation and error handling."""

    def setUp(self):
        self.valid_data = {
            "student_id": ["ST01", "ST02"],
            "student_name": ["John Doe", "Jane Smith"],
            "department": ["Computer Science", "Information Technology"],
            "semester": [1, 2],
            "python_marks": [80, 85],
            "mathematics_marks": [75, 90],
            "statistics_marks": [70, 80],
            "attendance_percentage": [85.5, 92.0],
        }

    def test_valid_data_passes(self):
        df = pd.DataFrame(self.valid_data)
        # Should not raise any exception
        validate_student_data(df)

    def test_empty_dataframe_raises(self):
        df = pd.DataFrame()
        with self.assertRaises(ValueError):
            validate_student_data(df)

    def test_non_dataframe_raises(self):
        with self.assertRaises(TypeError):
            validate_student_data({"key": "val"})  # type: ignore

    def test_missing_column_raises(self):
        data = self.valid_data.copy()
        del data["statistics_marks"]
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(df)
        self.assertIn("statistics_marks", str(ctx.exception))

    def test_duplicate_student_id_raises(self):
        data = self.valid_data.copy()
        data["student_id"] = ["ST01", "ST01"]
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(df)
        self.assertIn("Duplicate student_id", str(ctx.exception))

    def test_blank_or_null_student_name_raises(self):
        data = self.valid_data.copy()
        data["student_name"] = ["John Doe", "   "]  # whitespace only
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            validate_student_data(df)

        data2 = self.valid_data.copy()
        data2["student_name"] = ["John Doe", None]
        df2 = pd.DataFrame(data2)
        with self.assertRaises(ValueError):
            validate_student_data(df2)

    def test_invalid_marks_out_of_range_raises(self):
        # Marks > 100
        data = self.valid_data.copy()
        data["python_marks"] = [80, 105]
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError) as ctx:
            validate_student_data(df)
        self.assertIn("outside the allowable range", str(ctx.exception))

        # Marks < 0
        data2 = self.valid_data.copy()
        data2["mathematics_marks"] = [-5, 80]
        df2 = pd.DataFrame(data2)
        with self.assertRaises(ValueError):
            validate_student_data(df2)

    def test_invalid_attendance_raises(self):
        data = self.valid_data.copy()
        data["attendance_percentage"] = [80.0, 102.5]
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            validate_student_data(df)

    def test_invalid_semester_raises(self):
        # Negative semester
        data = self.valid_data.copy()
        data["semester"] = [-1, 2]
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            validate_student_data(df)

        # Zero semester
        data2 = self.valid_data.copy()
        data2["semester"] = [0, 2]
        df2 = pd.DataFrame(data2)
        with self.assertRaises(ValueError):
            validate_student_data(df2)

        # Non-integer semester
        data3 = self.valid_data.copy()
        data3["semester"] = [1.5, 2.0]
        df3 = pd.DataFrame(data3)
        with self.assertRaises(ValueError):
            validate_student_data(df3)

    def test_non_numeric_marks_raises(self):
        data = self.valid_data.copy()
        data["python_marks"] = ["eighty", 85]
        df = pd.DataFrame(data)
        with self.assertRaises(ValueError):
            validate_student_data(df)


class TestFileIngestion(unittest.TestCase):
    """Unit tests for dataset loading from disk."""

    def test_missing_file_raises_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_dataset("non_existent_file_path_12345.csv")

    def test_empty_file_raises_value_error(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tmp:
            tmp_path = Path(tmp.name)
        try:
            with self.assertRaises(ValueError):
                load_dataset(tmp_path)
        finally:
            if tmp_path.exists():
                tmp_path.unlink()

    def test_valid_file_loads_correctly(self):
        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv") as tmp:
            tmp.write(
                "student_id,student_name,department,semester,python_marks,mathematics_marks,statistics_marks,attendance_percentage\n"
                "S1,Alice,CS,1,80,85,90,95.0\n"
            )
            tmp_path = Path(tmp.name)
        try:
            df = load_dataset(tmp_path)
            self.assertEqual(len(df), 1)
            self.assertEqual(df.iloc[0]["student_id"], "S1")
        finally:
            if tmp_path.exists():
                tmp_path.unlink()


if __name__ == "__main__":
    unittest.main()

# Student Academic Performance Analysis and Reporting System

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Tests-Passed](https://img.shields.io/badge/tests-32%20passed-brightgreen.svg)](tests/)
[![Course](https://img.shields.io/badge/Course-EWB%20Python%20with%20AI-orange.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#)

A modular, automated command-line analytics and reporting system engineered in Python, Pandas, and NumPy for academic performance assessment. Developed in compliance with the **EWB Courses | Python with AI** project curriculum.

---

## 1. Project Title & Overview

The **Student Academic Performance Analysis and Reporting System** is a software solution designed to ingest, validate, analyze, and report cohort-level student performance data. It transforms raw academic records into actionable intelligence, producing individual student performance evaluations, subject-level distributions, statistical cohort indicators, and grouped performance breakdowns across academic departments and semesters.

---

## 2. Problem Statement & Objective

Educational institutions require reliable, automated methods to analyze student scores and attendance records without human error or manual calculations. 

### Core Objectives:
- Ingest and validate student records from CSV datasets with zero data corruption.
- Calculate unrounded average marks, assign project-defined letter grades (A+ to F), and determine multi-subject pass/fail outcomes.
- Track attendance deficiencies separately from academic competency.
- Compute descriptive statistics (mean, median, standard deviation, pass percentages) using NumPy and Pandas.
- Produce a structured, professional 9-section executive console report answering key analytical queries at runtime.

---

## 3. Implemented Features

- **Robust CSV Ingestion & Pre-Flight Validation**:
  - Enforces schema integrity, rejecting empty files, missing columns, duplicate IDs, non-positive semesters, and out-of-range marks ($0-100$) or attendance ($0-100\%$).
- **Precision Academic Calculations**:
  - Unrounded floating-point averages with display-only rounding.
  - Multi-subject pass determination: passing requires scoring $\ge 35.0$ in Python, Mathematics, and Statistics.
  - 7-tier letter grading scale: A+ ($90-100$), A ($80-89$), B ($70-79$), C ($60-69$), D ($50-59$), E ($35-49$), F ($<35$).
- **Administrative Attendance Monitoring**:
  - Flags students with attendance $< 75.0\%$ without overwriting academic marks.
- **Subject-Wise Analytics**:
  - Per-subject enrollment counts, means, min/max values, sample standard deviations, pass counts, fail counts, and top subject identification with tie resolution.
- **Class-Level Analytics**:
  - Cohort size, total passing/failing all subjects, overall class average (arithmetic mean of student averages), median, standard deviation, and class pass rate.
- **Rankings & Extreme Performers**:
  - Top-5 rankings with deterministic tie-handling (all tied 5th-place students included).
  - Identification of lowest-performing student(s).
- **Multi-Dimensional Group Aggregation**:
  - Department-wise and semester-wise grouping with size, average score, pass rates, and attendance means.
- **Dynamic Findings Engine**:
  - Generates runtime answers for 12 core academic questions without hardcoding.
- **32 Automated Unit Tests**:
  - Built-in `unittest` covering edge cases, grade boundaries, tie handling, and error handling.

---

## 4. Technologies Used

- **Language**: Python 3.11+
- **Data Analysis**: Pandas 2.0+ / 3.0+
- **Numerical Computation**: NumPy 1.24+ / 2.0+
- **Testing**: Python `unittest` framework
- **Filesystem & Paths**: Python `pathlib.Path` (Cross-platform portability)

---

## 5. Project Structure

```text
student-performance-analytics/
├── main.py                     # Application entry point & CLI reporting engine
├── functions.py                # Reusable pure functions for data validation & analytics
├── data/
│   └── students.csv            # 25 realistic, diverse synthetic student records
├── tests/
│   ├── __init__.py
│   └── test_functions.py       # 32 automated unit tests using unittest
├── screenshots/
│   └── README.md               # Visual proof guide & full CLI execution transcript
├── README.md                   # Complete system overview & execution manual
├── Project_Documentation.md    # 10-section EWB coursework submission document
├── requirements.txt            # Minimal dependencies (pandas, numpy)
└── .gitignore                  # Git ignore specification
```

---

## 6. Dataset Schema

The system analyzes `data/students.csv`, containing **25 synthetic student records**:

| Column Name | Type | Allowed Values / Constraints | Description |
|---|---|---|---|
| `student_id` | String | Unique, non-empty (e.g. `STD1001`) | Primary student identification number |
| `student_name` | String | Non-empty string | Full name of the student |
| `department` | String | Non-empty string | Department (Computer Science, Data Science, IT, AI) |
| `semester` | Integer | Positive integer ($1, 2, 3, 4$) | Current semester of enrollment |
| `python_marks` | Numeric | $0.0 \le \text{mark} \le 100.0$ | Marks in Python Programming |
| `mathematics_marks` | Numeric | $0.0 \le \text{mark} \le 100.0$ | Marks in Mathematics |
| `statistics_marks` | Numeric | $0.0 \le \text{mark} \le 100.0$ | Marks in Statistics |
| `attendance_percentage` | Numeric | $0.0 \le \text{attendance} \le 100.0$ | Overall semester attendance rate |

---

## 7. Grading and Attendance Policy

### Subject Pass Mark
- A mark of **35.0 or higher** is required to pass a subject.

### Overall Academic Result
- A student achieves an overall **Pass** if and only if all three subject marks are $\ge 35.0$. If any subject mark is $< 35.0$, the student receives an overall **Fail**.

### Attendance Monitoring
- Minimum institutional attendance threshold is **75.0%**. Attendance $< 75.0\%$ is flagged as **Low Attendance**.
- **Important**: Attendance status is monitored separately and does not automatically alter or fail a student's academic marks.

### Letter Grade Rubric (Unrounded Average)
Grades are computed from the continuous unrounded average of the three subjects:

| Average Mark Range | Grade | Description |
|---|---|---|
| 90.0 to 100.0 | **A+** | Outstanding Mastery |
| 80.0 to below 90.0 | **A** | Excellent Performance |
| 70.0 to below 80.0 | **B** | Good / Above Average |
| 60.0 to below 70.0 | **C** | Satisfactory / Average |
| 50.0 to below 60.0 | **D** | Needs Improvement |
| 35.0 to below 50.0 | **E** | Borderline Pass |
| Below 35.0 | **F** | Academic Failure |

---

## 8. Prerequisites

- **Operating System**: Windows 10/11, macOS, or Linux.
- **Python**: Version 3.11 or higher installed and added to `PATH`.
- **Git**: Installed for version control.

---

## 9. Windows Installation Instructions

1. Open PowerShell or Command Prompt.
2. Clone or navigate into the project directory:
   ```powershell
   cd "d:\current project\python with AI\mw\student-performance-analytics"
   ```

---

## 10. Virtual Environment Setup

Isolate your Python environment to avoid version conflicts:

```powershell
# Create a virtual environment named .venv
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate
```

---

## 11. Dependency Installation

Install the required external packages:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 12. Program Execution

Launch the analytical engine:

```powershell
python main.py
```

*Note: The program uses relative paths and can also be run from any parent directory:*
```powershell
python student-performance-analytics\main.py
```

---

## 13. Automated Testing

Run the full automated test suite using Python's built-in `unittest` runner:

```powershell
python -m unittest discover -s tests -v
```

### Verified Test Summary:
- **Total Tests**: 32 unit tests
- **Coverage**: Grade boundary tests, pass/fail thresholds, attendance limits, mathematical correctness, tie handling, error validation, corrupted data handling.
- **Status**: 100% Passed (`Ran 32 tests in ~0.15s - OK`).

---

## 14. Description of the Console Report

When `python main.py` runs, it prints a structured report divided into 9 sections:

- **Section A | Application Header**: Displays project metadata, file location, and synthetic data disclaimer.
- **Section B | Dataset Overview**: Displays row/column count, column headers, zero-null audit, and first 5 rows preview.
- **Section C | Individual Student Results**: Full tabular breakdown showing Student ID, Name, Department, Semester, Total Marks, Average, Grade, Overall Result, Attendance %, and Attendance Status.
- **Section D | Subject-Wise Performance Analysis**: Detailed table showing N, Mean, High, Low, StdDev, Pass Count, Fail Count, Pass Rate for each subject, plus top-performing subject identification.
- **Section E | Class Performance Summary**: Cohort pass rate, overall class mean, median, standard deviation, and class attendance mean.
- **Section F | Student Ranking & Outliers**: Top-5 ranked performers with tie-handling policy applied, plus identification of lowest performer(s).
- **Section G | Attendance Monitoring Analysis**: List of students flagged for attendance $< 75.0\%$.
- **Section H | Group Analysis**: Comparative breakdowns grouped by Department and by Semester.
- **Section I | Final Findings**: Direct runtime answers to all 12 core academic questions.

---

## 15. Documentation Link

For the comprehensive 10-section EWB coursework submission document, refer to:
[Project_Documentation.md](file:///d:/current%20project/python%20with%20AI/mw/student-performance-analytics/Project_Documentation.md)

---

## 16. Data Privacy Statement

This application operates exclusively on synthetic, fictional student data. No real personal student information, institutional identities, or private grades are contained within or processed by this repository.

---

## 17. Limitations

- **Dataset Scale**: Designed for small-to-medium classroom cohorts in CSV format; large multi-million row deployments would benefit from Parquet or SQL-backed databases.
- **Static Schema**: Assumes the three core subjects (`python_marks`, `mathematics_marks`, `statistics_marks`). Extending to elective curricula requires dynamic subject column discovery.
- **Console Interface**: Terminal-based CLI output; no web UI or graphical desktop dashboard is included.

---

## 18. GitHub Submission Checklist

Before submitting to EWB Courses:
- [x] Directory structure matches EWB specification.
- [x] Synthetic dataset contains $\ge 20$ valid records (25 records provided).
- [x] `requirements.txt` contains only required dependencies.
- [x] `.gitignore` prevents virtual environment and cache pollution.
- [x] All 32 automated unit tests execute and pass (`unittest`).
- [x] `main.py` runs without errors on Windows terminals (`cp1252` safe).
- [x] `Project_Documentation.md` contains all 10 required sections.
- [x] `README.md` is complete and verified against real project execution.
- [x] No sensitive files, credentials, or `.env` files committed.

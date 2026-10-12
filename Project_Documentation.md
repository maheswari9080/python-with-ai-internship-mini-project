# Project Documentation: Student Academic Performance Analysis and Reporting System

**Course**: EWB Courses | Python with AI  
**Assessment Milestone**: Complete Project Implementation  
**Submission Deadline**: 15 October 2026  

---

## 1. Project Title and Student Details

- **Project Title**: Student Academic Performance Analysis and Reporting System
- **Student Name**: [Student Name Placeholder]
- **Student ID / Roll Number**: [Student ID Placeholder]
- **Course Name**: Python with AI
- **Institution / Organization**: EWB Courses
- **Batch / Cohort**: 2026 Academic Session
- **Submission Date**: 12 October 2026

---

## 2. Objective

The primary objective of this project is to develop an automated, reproducible, command-line data analytics and reporting system written in Python. The system ingests structured student academic records, performs data quality audits, calculates individual scholastic indicators (totals, unrounded averages, project-defined letter grades, pass/fail status, and attendance monitoring flags), generates subject-level and class-wide descriptive statistics, ranks students with robust tie-handling, and provides aggregated group breakdowns across academic departments and semesters.

### Key Goals
1. **Automated Quality Assurance**: Eliminate faulty calculations by validating data schema, non-empty fields, positive integer semesters, unique student IDs, and score ranges ($0 \le \text{marks, attendance} \le 100$).
2. **Transparent Academic Grading**: Compute arithmetic means with floating-point precision and map them to a defined 7-tier grading rubric (A+ through F), ensuring display rounding occurs only during presentation.
3. **Multi-Factor Result Determination**: Enforce subject-level pass criteria ($\ge 35$ marks) alongside institutional attendance thresholds ($\ge 75\%$), keeping attendance flags separate from subject mastery results.
4. **Cohort Performance Insights**: Utilize NumPy and Pandas for statistical calculations (mean, median, standard deviation, pass percentage, correlation) and answer core analytical queries dynamically at runtime.

---

## 3. Technologies Used

| Technology | Version / Specification | Role in Architecture |
|---|---|---|
| **Python** | 3.11+ | Core programming language, providing object model, structured exception handling, and modular script execution. |
| **Pandas** | 2.0+ (Tested on 3.0.6) | High-performance DataFrame manipulation, data ingestion from CSV, columnar validation, filtering, sorting, and multi-dimensional grouping (`groupby`). |
| **NumPy** | 1.24+ (Tested on 2.4.6) | Fast numerical operations, vectorized conditions (`np.where`), array-based aggregation (`mean`, `median`, `std`, `min`, `max`), and floating-point comparisons (`np.isclose`). |
| **Unittest** | Built-in Python Standard Library | Test automation framework implementing boundary checks, assertion tests, and validation regression suites. |
| **Pathlib** | Built-in Python Standard Library | Cross-platform, object-oriented filesystem path resolution, guaranteeing reliable execution regardless of current working directory. |
| **Git & GitHub** | Distributed Version Control | Version management, code review, change history tracking, and repository sharing. |

---

## 4. Dataset Description

The application processes a synthetic academic dataset located at `data/students.csv`. The dataset contains exactly **25 records** representing fictional students across multiple engineering and technology disciplines. No personally identifiable real-world student data is used.

### Schema Specification

| Column Name | Data Type | Constraint / Allowed Range | Description |
|---|---|---|---|
| `student_id` | String | Unique, non-blank (e.g., `STD1001`) | Unique institutional student registration code. |
| `student_name` | String | Non-empty, non-whitespace string | Full name of the student. |
| `department` | String | Non-empty string | Academic department (Computer Science, Data Science, IT, AI). |
| `semester` | Integer | Positive integer ($1, 2, 3, 4$) | Current enrolled semester of the student. |
| `python_marks` | Float / Int | $0.0 \le \text{mark} \le 100.0$ | Marks scored in Python Programming (Pass mark: 35). |
| `mathematics_marks` | Float / Int | $0.0 \le \text{mark} \le 100.0$ | Marks scored in Mathematics (Pass mark: 35). |
| `statistics_marks` | Float / Int | $0.0 \le \text{mark} \le 100.0$ | Marks scored in Statistics (Pass mark: 35). |
| `attendance_percentage` | Float | $0.0 \le \text{attendance} \le 100.0$ | Overall attendance rate (Threshold: 75.0%). |

### Dataset Diversity
The synthetic dataset includes:
- Top-tier academic performers (e.g., `STD1018` with $96.33\%$ average mark).
- Consistent average performers ($50\% - 80\%$).
- Exact boundary students (e.g., `STD1021` with exactly $35$ marks in all subjects and exactly $75\%$ attendance).
- Single-subject failures (e.g., `STD1009` failing Mathematics with $30$, `STD1010` failing Python with $28$, `STD1011` failing Statistics with $32$).
- Multi-subject and complete failures (e.g., `STD1012` failing all three subjects, `STD1023` scoring $22.00\%$ average).
- Attendance edge cases (students with high marks but low attendance like `STD1004` at $72\%$, and low marks with high attendance).

---

## 5. Implementation

The system is engineered as a modular, pure-function analytical architecture separated into distinct modules:

```text
student-performance-analytics/
├── main.py                     # Entry point & structured console reporting engine
├── functions.py                # Reusable pure functions for data validation & analytics
├── data/
│   └── students.csv            # 25 realistic, diverse synthetic student records
├── tests/
│   ├── __init__.py
│   └── test_functions.py       # Comprehensive unittest suite (32 tests)
├── screenshots/
│   └── README.md               # Guide on screenshots & captured CLI output
├── README.md                   # Full professional README with Windows setup & instructions
├── Project_Documentation.md    # 10-section EWB coursework submission document
├── requirements.txt            # Minimal dependencies (pandas, numpy)
└── .gitignore                  # Clean standard Python gitignore
```

### Major Functions and Responsibilities

1. **`load_dataset(filepath)`**:
   - Resolves filesystem path using `Pathlib`.
   - Rejects missing files (`FileNotFoundError`) and empty 0-byte or header-only files (`ValueError`).
   - Ingests CSV into a Pandas `DataFrame`.

2. **`validate_student_data(df)`**:
   - Audits required column headers.
   - Detects duplicate `student_id` entries.
   - Verifies that names and departments are not blank or whitespace.
   - Ensures `semester` values are strictly positive integers.
   - Validates that numeric columns contain valid numbers within $[0, 100]$.
   - Rejects malformed records with descriptive exception messages.

3. **`calculate_student_metrics(df)`**:
   - Computes `total_marks` by summing Python, Math, and Statistics.
   - Computes unrounded `average_marks` ($\text{total} / 3.0$).
   - Determines subject pass flags (`mark >= 35.0`).
   - Evaluates overall result: a student receives `Pass` if and only if all three subjects are $\ge 35.0$, otherwise `Fail`.
   - Assigns letter grades using `assign_grade()`.
   - Flags attendance as `Normal` ($\ge 75.0\%$) or `Low Attendance` ($< 75.0\%$).

4. **`assign_grade(average)`**:
   - Maps continuous unrounded average marks into discrete grade brackets:
     - $90.0 \le \text{avg} \le 100.0 \rightarrow \mathbf{A+}$
     - $80.0 \le \text{avg} < 90.0 \rightarrow \mathbf{A}$
     - $70.0 \le \text{avg} < 80.0 \rightarrow \mathbf{B}$
     - $60.0 \le \text{avg} < 70.0 \rightarrow \mathbf{C}$
     - $50.0 \le \text{avg} < 60.0 \rightarrow \mathbf{D}$
     - $35.0 \le \text{avg} < 50.0 \rightarrow \mathbf{E}$
     - $\text{avg} < 35.0 \rightarrow \mathbf{F}$

5. **`calculate_subject_statistics(df)`**:
   - Computes subject count, arithmetic mean (`np.mean`), maximum (`np.max`), minimum (`np.min`), and sample standard deviation (`np.std(ddof=1)`).
   - Counts subject pass and fail frequencies.
   - Dynamically identifies the subject(s) with the highest average, handling ties cleanly.

6. **`calculate_class_statistics(df_metrics)`**:
   - Class average is defined as the arithmetic mean of individual student averages.
   - Uses NumPy to calculate median and sample standard deviation.
   - Calculates cohort pass percentage: $(\text{passed\_all} / \text{total\_students}) \times 100$.

7. **`get_top_students(df_metrics, n=5)` & `get_lowest_students(df_metrics)`**:
   - Performs deterministic ranking with explicit tie-handling: students sharing the 5th place cutoff average are all included in the top list.
   - Identifies lowest performer(s) by matching minimum average scores.

8. **`analyze_attendance(df_metrics, threshold=75.0)`**:
   - Segregates students meeting the $75\%$ threshold from those flagged for low attendance.
   - Emphasizes that low attendance is monitored separately and does not overwrite academic marks.

9. **`group_summary(df_metrics, group_by="department")`**:
   - Groups cohort by department or semester using Pandas `.groupby()`.
   - Aggregates cohort size, average marks, passed counts, failed counts, pass rate, and average attendance.

10. **`generate_final_findings(df_metrics)`**:
    - Synthesizes programmatic runtime answers for all 12 analytical questions without hardcoded values.

---

## 6. Key Features

- **Strict Data Validation & Zero-Data-Corruption Guarantee**: Invalid data files, out-of-range marks, negative semesters, or duplicate IDs are caught immediately before analytics execute.
- **Pure Vectorized Calculations**: Computations leverage Pandas and NumPy operations for speed and clarity.
- **Unrounded Precision**: All grade assignments and statistical metrics use full floating-point precision, rounding only at presentation time (2 decimal places).
- **Graceful Multi-Factor Policy Separation**: Attendance flags do not artificially fail students who achieved passing academic marks, maintaining distinct academic and administrative indicators.
- **Deterministic Ranking with Tie Resolution**: Handles multi-student ties at rank boundaries fairly.
- **Comprehensive Terminal User Interface**: Generates clean, formatted tables and summaries using plain ASCII characters, avoiding Unicode encoding errors on Windows `cp1252` terminals.
- **Cross-Directory Portability**: File paths resolve relative to source files, allowing execution from any working directory.

---

## 7. Output and Screenshots

### Verified Terminal Run Summary (25 Records)

```text
======================================================================================
   STUDENT ACADEMIC PERFORMANCE ANALYSIS AND REPORTING SYSTEM
              EWB Courses | Python with AI Project
======================================================================================
  Dataset File Location : D:\current project\python with AI\mw\student-performance-analytics\data\students.csv
  Execution Mode        : Autonomous Analytical Engine
  Data Integrity Note   : Synthetic Academic Records (Fictional Data)
  Compliance Statement  : Fully complies with EWB Assessment Guidelines
======================================================================================
```

#### Section Summary Highlights:
- **Total Records Validated**: 25 records, 8 columns, 0 nulls.
- **Subject Analysis**:
  - Python Programming: Average $65.24\%$, Highest $98.0$, Lowest $22.0$, Pass Rate $88.0\%$ (Top Subject).
  - Mathematics: Average $64.56\%$, Highest $96.0$, Lowest $19.0$, Pass Rate $88.0\%$.
  - Statistics: Average $64.56\%$, Highest $96.0$, Lowest $25.0$, Pass Rate $88.0\%$.
- **Class Performance**:
  - Total Enrolled: 25
  - Passed All Subjects: 20
  - Failed $\ge 1$ Subject: 5
  - Class Pass Percentage: $80.00\%$
  - Class Average (Mean of Student Averages): $64.79\%$
  - Class Median Average: $66.00\%$
  - Class Standard Deviation: $21.29$
  - Class Average Attendance: $80.76\%$
- **Top 5 Performers**:
  1. `#1` Riya Banerjee (`STD1018`) — $96.33\%$ (Grade: A+)
  2. `#2` Ananya Iyer (`STD1004`) — $93.67\%$ (Grade: A+)
  3. `#3` Aarav Sharma (`STD1001`) — $92.67\%$ (Grade: A+)
  4. `#4` Priya Nambiar (`STD1024`) — $91.00\%$ (Grade: A+)
  5. `#5` Diya Patel (`STD1002`) — $87.67\%$ (Grade: A)
- **Lowest Performer**: Yash Chopra (`STD1023`) — $22.00\%$ (Grade: F, Fail)
- **Attendance Findings**: 6 students below $75.0\%$ threshold; 19 students meeting or exceeding threshold.
- **Top Department**: Data Science ($73.44\%$ average, $83.3\%$ pass rate).
- **Top Semester**: Semester 1 ($72.00\%$ average, $100.0\%$ pass rate).

Full console transcripts are preserved in [screenshots/README.md](file:///d:/current%20project/python%20with%20AI/mw/student-performance-analytics/screenshots/README.md).

---

## 8. Final Outcome

The implemented system satisfies all EWB Python with AI project specifications:

| Requirement Area | Specification Target | Status | Implementation Evidence |
|---|---|---|---|
| Synthetic Dataset | $\ge 20$ records, 8 required columns | **Met** | 25 varied synthetic records in `data/students.csv`. |
| Data Quality Check | Rejection of bad data & duplicates | **Met** | Comprehensive validator in `functions.py` with custom error messages. |
| Subject Pass Mark | Mark $\ge 35$ required | **Met** | Implemented in `check_subject_pass()` & vectorized masks. |
| Overall Academic Result | Pass all 3 subjects to pass | **Met** | Implemented in `calculate_student_metrics()`. |
| Attendance Policy | $< 75\%$ flagged separately | **Met** | Implemented in `check_attendance_status()` & `analyze_attendance()`. |
| Grading Scale | A+, A, B, C, D, E, F boundaries | **Met** | Implemented in `assign_grade()` using unrounded averages. |
| Class Analytics | Mean, Median, StdDev, Pass % | **Met** | Implemented using NumPy and Pandas functions. |
| Reporting Sections | Sections A through I | **Met** | Fully formatted console presentation in `main.py`. |
| Core Questions | Dynamic answers to 12 questions | **Met** | Programmatically answered at runtime in Section I. |
| Automated Testing | `unittest` with boundary cases | **Met** | 32 tests passing in `tests/test_functions.py`. |

---

## 9. Challenges and Learning

### Technical Challenges Encountered
1. **Windows Console Character Encoding (`cp1252`)**:
   - *Challenge*: Initial console output using Unicode checkmark characters (`\u2713`) crashed on standard Windows PowerShell/CMD environments due to `UnicodeEncodeError`.
   - *Solution*: Replaced non-ASCII characters with clean, cross-platform ASCII tokens (`[OK]`, `[PASS]`, `*`) and configured standard output encoding to guarantee 100% portable CLI execution.
2. **Unrounded Average Mark Precision vs Display Rounding**:
   - *Challenge*: Premature rounding can cause incorrect letter grade assignment on edge cases (e.g., $89.98$ rounded to $90.0$ could incorrectly receive `A+` instead of `A`).
   - *Solution*: Kept raw calculations unrounded in DataFrame columns and passed raw floats to `assign_grade()`. Only applied formatting (`:.2f`) when printing terminal strings.
3. **Deterministic Tie Handling at Top-5 Cutoff**:
   - *Challenge*: Simple `.head(5)` slicing arbitrarily drops students who tie with the 5th position.
   - *Solution*: Implemented ranking logic that computes the score of the 5th student and includes all records matching or exceeding that cutoff score.
4. **Distinguishing Attendance Deficiencies from Academic Pass/Fail**:
   - *Challenge*: Preventing administrative attendance rules from corrupting purely academic competency metrics.
   - *Solution*: Decoupled `overall_result` (Pass/Fail based on marks $\ge 35$) from `attendance_status` (Normal/Low Attendance based on attendance $\ge 75\%$).

### Key Learnings
- Mastered vectorization using Pandas and NumPy, avoiding slow row iteration.
- Deepened understanding of test-driven development using Python's `unittest` framework to catch regression errors before deployment.
- Gained practical experience designing clean terminal user interfaces and cross-platform Python scripts.

---

## 10. GitHub Repository

- **Repository Name**: `student-performance-analytics`
- **Recommended Remote URL**: `https://github.com/[Your-Username]/student-performance-analytics.git`
- **Local Workspace Path**: `d:\current project\python with AI\mw\student-performance-analytics`
- **Branch**: `main`

### Publication Instructions
To publish this project to GitHub:
```powershell
# Navigate into project directory
cd "d:\current project\python with AI\mw\student-performance-analytics"

# Initialize git repository
git init -b main

# Stage all project files
git add .

# Create initial commit
git commit -m "feat: complete student academic performance analysis and reporting system"

# Link to your remote GitHub repository
git remote add origin https://github.com/[Your-Username]/student-performance-analytics.git

# Push to GitHub
git push -u origin main
```

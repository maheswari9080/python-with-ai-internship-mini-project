# Application Execution Screenshots & CLI Artifacts

This directory stores visual evidence and terminal captures of the **Student Academic Performance Analysis and Reporting System** in execution, adhering to EWB Courses assessment standards.

## How to Capture and Add Screenshots

1. **Run the Application in Terminal**:
   ```powershell
   python main.py
   ```
2. **Capture the Terminal Output**:
   - On Windows: Press `Win + Shift + S` or use the Snipping Tool to capture full terminal windows of:
     - Application Header & Dataset Validation (Sections A & B)
     - Individual Student Results table (Section C)
     - Subject & Class Analytical Summaries (Sections D & E)
     - Rankings & Attendance Analysis (Sections F, G, H)
     - Final Findings (Section I)
     - Unit Test Execution (`python -m unittest discover -s tests -v`)
3. **Save Files**:
   - Save your image files in this folder (e.g., `01_dataset_overview.png`, `02_individual_results.png`, `03_subject_class_analytics.png`, `04_rankings_attendance.png`, `05_final_findings.png`, `06_unittest_success.png`).

---

## Actual CLI Execution Log (Reference Transcript)

Below is the verified, runtime terminal transcript from the certified test run:

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

======================================================================================
  SECTION B | DATASET OVERVIEW
======================================================================================
Validation Status   : PASSED (All schema, type, and range checks satisfied)
Total Student Rows  : 25
Total Columns       : 8
Columns List        : student_id, student_name, department, semester, python_marks, mathematics_marks, statistics_marks, attendance_percentage

--- Missing Value Audit ---
  [OK] Zero missing or null values found across all columns.

--- Sample Preview (First 5 Records) ---
student_id  student_name             department  semester  python_marks  mathematics_marks  statistics_marks  attendance_percentage
   STD1001  Aarav Sharma       Computer Science         3            92                 95                91                   94.0
   STD1002    Diya Patel           Data Science         3            88                 85                90                   88.5
   STD1003   Rohan Verma Artificial Intelligence        4            76                 82                79                   81.0
   STD1004   Ananya Iyer Information Technology         2            94                 91                96                   72.0
   STD1005  Vikram Singh       Computer Science         3            62                 58                65                   85.0

======================================================================================
  SECTION C | INDIVIDUAL STUDENT PERFORMANCE RESULTS
======================================================================================
Grading Scale: A+ (90-100), A (80-89), B (70-79), C (60-69), D (50-59), E (35-49), F (<35)
Pass Rule    : Requires mark >= 35.0 in all three subjects.
Attendance   : Low Attendance flagged if < 75.0% (does not alter academic pass).

ID        Name               Department      Sem    Total  Average  Grade   Result     Attend Att-Status    
------------------------------------------------------------------------------------------------------------
STD1001   Aarav Sharma       Computer Scien  3        278    92.67     A+     Pass      94.0% Normal        
STD1002   Diya Patel         Data Science    3        263    87.67      A     Pass      88.5% Normal        
STD1003   Rohan Verma        Artificial Int  4        237    79.00      B     Pass      81.0% Normal        
STD1004   Ananya Iyer        Information Te  2        281    93.67     A+     Pass      72.0% Low Attendance
STD1005   Vikram Singh       Computer Scien  3        185    61.67      C     Pass      85.0% Normal        
STD1006   Sneha Kulkarni     Data Science    1        162    54.00      D     Pass      78.5% Normal        
STD1007   Rahul Nair         Artificial Int  4        127    42.33      E     Pass      80.0% Normal        
STD1008   Pooja Mehta        Information Te  2        109    36.33      E     Pass      76.0% Normal        
STD1009   Arjun Das          Computer Scien  3        170    56.67      D     Fail      82.5% Normal        
STD1010   Meera Reddy        Data Science    3        151    50.33      D     Fail      68.0% Low Attendance
STD1011   Karan Malhotra     Artificial Int  4        205    68.33      C     Fail      90.0% Normal        
STD1012   Tanvi Joshi        Information Te  2         94    31.33      F     Fail      62.0% Low Attendance
STD1013   Aditya Rao         Computer Scien  1        251    83.67      A     Pass      89.0% Normal        
STD1014   Ishita Sen         Data Science    2        217    72.33      B     Pass      91.5% Normal        
STD1015   Harsh Vardhan      Artificial Int  3        192    64.00      C     Pass      74.0% Low Attendance
STD1016   Kavya Pillai       Information Te  4        165    55.00      D     Pass      83.0% Normal        
STD1017   Nikhil Gupta       Computer Scien  2        144    48.00      E     Pass      79.0% Normal        
STD1018   Riya Banerjee      Data Science    1        289    96.33     A+     Pass      96.0% Normal        
STD1019   Siddharth Jain     Artificial Int  3        235    78.33      B     Pass      86.0% Normal        
STD1020   Neha Choudhury     Information Te  4        198    66.00      C     Pass      70.0% Low Attendance
STD1021   Devendra Prasad    Computer Scien  1        105    35.00      E     Pass      75.0% Normal        
STD1022   Simran Kaur        Data Science    2        240    80.00      A     Pass      84.0% Normal        
STD1023   Yash Chopra        Artificial Int  3         66    22.00      F     Fail      55.0% Low Attendance
STD1024   Priya Nambiar      Information Te  1        273    91.00     A+     Pass      92.0% Normal        
STD1025   Gaurav Saxena      Computer Scien  4        222    74.00      B     Pass      87.0% Normal        
------------------------------------------------------------------------------------------------------------

======================================================================================
  SECTION D | SUBJECT-WISE PERFORMANCE ANALYSIS
======================================================================================
Subject                     N   Average  Highest   Lowest    StdDev  Passed  Failed  PassRate
-----------------------------------------------------------------------------------------------
Python Programming         25     65.24     98.0     22.0     22.91      22       3     88.0%
Mathematics                25     64.56     96.0     19.0     23.03      22       3     88.0%
Statistics                 25     64.56     96.0     25.0     21.78      22       3     88.0%
-----------------------------------------------------------------------------------------------
Top Performing Subject(s) by Average: Python Programming (65.24%)

======================================================================================
  SECTION E | CLASS PERFORMANCE SUMMARY
======================================================================================
  Total Cohort Enrollment           : 25
  Students Passing All Subjects     : 20
  Students Failing >= 1 Subject     : 5
  Class Pass Percentage             : 80.00%
  Overall Class Average (Mean)      : 64.79%
  Class Median Average              : 66.00%
  Standard Deviation of Averages    : 21.29
  Highest Student Average           : 96.33%
  Lowest Student Average            : 22.00%
  Average Student Attendance        : 80.76%
--------------------------------------------------------------------------------------

======================================================================================
  SECTION F | STUDENT RANKING & OUTLIERS
======================================================================================
Top 5 Academic Performers (Descending Average Marks):
Tie Policy: Students with equal average share rank; all ties at rank 5 are included.

Rank   ID         Name                 Department           Average  Grade Attendance
-------------------------------------------------------------------------------------
#1     STD1018    Riya Banerjee        Data Science          96.33%     A+      96.0%
#2     STD1004    Ananya Iyer          Information Technology    93.67%     A+      72.0%
#3     STD1001    Aarav Sharma         Computer Science      92.67%     A+      94.0%
#4     STD1024    Priya Nambiar        Information Technology    91.00%     A+      92.0%
#5     STD1002    Diya Patel           Data Science          87.67%      A      88.5%
-------------------------------------------------------------------------------------

Lowest Academic Performer(s):
  - Yash Chopra (STD1023) | Average: 22.00% | Grade: F | Result: Fail

======================================================================================
  SECTION G | ATTENDANCE MONITORING ANALYSIS
======================================================================================
  Institutional Attendance Minimum  : 75.0%
  Cohort Average Attendance         : 80.76%
  Students Meeting/Exceeding Target : 19
  Students Below 75% Threshold      : 6

--- Students Flagged for Low Attendance (< 75.0%) ---
ID         Name                 Department           Attendance    Result
--------------------------------------------------------------------------
STD1004    Ananya Iyer          Information Technology        72.0%      Pass
STD1010    Meera Reddy          Data Science              68.0%      Fail
STD1012    Tanvi Joshi          Information Technology        62.0%      Fail
STD1015    Harsh Vardhan        Artificial Intelligence        74.0%      Pass
STD1020    Neha Choudhury       Information Technology        70.0%      Pass
STD1023    Yash Chopra          Artificial Intelligence        55.0%      Fail
--------------------------------------------------------------------------

======================================================================================
  SECTION H | GROUP ANALYSIS (DEPARTMENT & SEMESTER)
======================================================================================

--- Department-Wise Performance Summary ---
Department                Count    Average   Passed   Failed   PassRate   AvgAttend
------------------------------------------------------------------------------------
Data Science                  6     73.44%        5        1      83.3%       84.4%
Computer Science              7     64.52%        6        1      85.7%       84.5%
Information Technology        6     62.22%        5        1      83.3%       75.8%
Artificial Intelligence       6     59.00%        4        2      66.7%       77.7%
------------------------------------------------------------------------------------

--- Semester-Wise Performance Summary ---
Semester      Count    Average   Passed   Failed   PassRate   AvgAttend
------------------------------------------------------------------------
Semester 1        5     72.00%        5        0     100.0%       86.1%
Semester 3        8     64.17%        5        3      62.5%       79.1%
Semester 4        6     64.11%        5        1      83.3%       81.8%
Semester 2        6     60.28%        5        1      83.3%       77.4%
------------------------------------------------------------------------

======================================================================================
  SECTION I | FINAL FINDINGS & CORE ANALYTICAL ANSWERS
======================================================================================
1.  Highest Average Student            : Riya Banerjee (STD1018) with 96.33%
2.  Subject with Highest Average       : Python Programming (65.24%)
3.  Students Passing All Subjects      : 20
4.  Students Failing >= 1 Subject      : 5
5.  Class Overall Average              : 64.79%
6.  Class Average Attendance           : 80.76%
7.  Students with Attendance < 75%     : 6 student(s)
      - Ananya Iyer (STD1004 - 72.0%)
      - Meera Reddy (STD1010 - 68.0%)
      - Tanvi Joshi (STD1012 - 62.0%)
      - Harsh Vardhan (STD1015 - 74.0%)
      - Neha Choudhury (STD1020 - 70.0%)
      - Yash Chopra (STD1023 - 55.0%)
8.  Top Five Ranked Students           :
      #1 Riya Banerjee (STD1018): 96.33% [Grade: A+]
      #2 Ananya Iyer (STD1004): 93.67% [Grade: A+]
      #3 Aarav Sharma (STD1001): 92.67% [Grade: A+]
      #4 Priya Nambiar (STD1024): 91.00% [Grade: A+]
      #5 Diya Patel (STD1002): 87.67% [Grade: A]
9.  Lowest Average Student             : Yash Chopra (STD1023) with 22.00%
10. Class Pass Percentage              : 80.00%
11. Highest Performing Department      : Data Science (73.44%)
    Highest Performing Semester        : Semester 1 (72.00%)
12. Statistical Observations & Patterns:
    1. Overall cohort pass rate is 80.0%. 2. Pearson correlation between attendance and average marks is +0.73, reflecting a positive association in the cohort. 3. While attendance issues were flagged for 6 students, failures (5 students) were strictly driven by academic subject marks (< 35).
```

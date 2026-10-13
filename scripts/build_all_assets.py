import os
import textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import numpy as np

os.makedirs("assets", exist_ok=True)
os.makedirs("screenshots", exist_ok=True)

# -------------------------------------------------------------------------
# 1. LINKEDIN POST IMAGE: image.png (1400 x 1400)
# -------------------------------------------------------------------------
def generate_linkedin_image():
    fig = plt.figure(figsize=(14, 14), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1400)
    ax.set_ylim(0, 1400)
    ax.axis('off')

    # Clean light-themed background
    ax.add_patch(patches.Rectangle((0, 0), 1400, 1400, facecolor='#F8FAFC', edgecolor='none'))
    
    # Top indigo bar
    ax.add_patch(patches.Rectangle((0, 1386), 1400, 14, facecolor='#4F46E5', edgecolor='none'))

    # Soft ambient circles in corners
    ax.add_patch(patches.Circle((1320, 1320), radius=260, facecolor='#EEF2FF', edgecolor='none', alpha=0.7))
    ax.add_patch(patches.Circle((80, 80), radius=220, facecolor='#F0FDF4', edgecolor='none', alpha=0.7))
    ax.add_patch(patches.Circle((1350, 150), radius=200, facecolor='#F0F9FF', edgecolor='none', alpha=0.7))

    # Top Pill
    pill = patches.FancyBboxPatch((70, 1285), 460, 42, boxstyle="round,pad=0.2,rounding_size=20",
                                  facecolor='#EEF2FF', edgecolor='#C7D2FE', linewidth=1.5)
    ax.add_patch(pill)
    ax.text(300, 1306, "EWB COURSES  |  PYTHON WITH AI MINI-PROJECT", fontsize=11.5, fontweight='bold',
            color='#4338CA', ha='center', va='center', fontfamily='Segoe UI')

    # Main Project Title & Subtitle
    ax.text(70, 1225, "Student Academic Performance Analysis", fontsize=34, fontweight='bold',
            color='#0F172A', fontfamily='Segoe UI')
    ax.text(70, 1175, "& Reporting System", fontsize=34, fontweight='bold',
            color='#4F46E5', fontfamily='Segoe UI')

    sub1 = "An end-to-end automated analytics engine built in Python, Pandas & NumPy with strict QA validation,"
    sub2 = "7-tier letter grading, deterministic tie-aware ranking, and dynamic executive reporting."
    ax.text(70, 1130, sub1, fontsize=14.5, color='#475569', fontfamily='Segoe UI')
    ax.text(70, 1104, sub2, fontsize=14.5, color='#475569', fontfamily='Segoe UI')

    # Top KPI Banner (4 metrics)
    kpis = [
        ("25", "Synthetic Students", "#4F46E5", "#EEF2FF"),
        ("32 / 32", "Unit Tests Passed", "#059669", "#ECFDF5"),
        ("80.0%", "Class Pass Rate", "#0284C7", "#F0F9FF"),
        ("+0.73", "Attendance Corr.", "#D97706", "#FFFBEB")
    ]
    card_w = 285
    card_gap = 40
    start_x = 70
    kpi_y = 965

    for i, (val, label, color, bg) in enumerate(kpis):
        cx = start_x + i * (card_w + card_gap)
        box = patches.FancyBboxPatch((cx, kpi_y), card_w, 100, boxstyle="round,pad=0.2,rounding_size=16",
                                     facecolor=bg, edgecolor='#E2E8F0', linewidth=1.5)
        ax.add_patch(box)
        stripe = patches.FancyBboxPatch((cx, kpi_y), 8, 100, boxstyle="round,pad=0.0,rounding_size=4",
                                        facecolor=color, edgecolor='none')
        ax.add_patch(stripe)
        ax.text(cx + 25, kpi_y + 58, val, fontsize=27, fontweight='bold', color=color, fontfamily='Segoe UI')
        ax.text(cx + 25, kpi_y + 24, label, fontsize=12.5, fontweight='semibold', color='#334155', fontfamily='Segoe UI')

    # 4 Bento Cards
    bento_cards = [
        {
            "x": 70, "y": 575, "w": 610, "h": 360,
            "tag": "MODULE 01", "tag_bg": "#EFF6FF", "tag_fg": "#1D4ED8",
            "title": "Data Ingestion & Integrity Audit",
            "desc": "Validates incoming CSV against schema constraints before processing. Enforces non-empty names, positive semester ints, and strict ranges [0-100] for marks and attendance.",
            "bullets": [
                "Automated schema verification & column presence check",
                "Zero null, zero whitespace policy with explicit error handling",
                "Duplicate Student ID detection (e.g. STD1001 uniqueness)",
                "Rejects corrupted or truncated CSV files via Pathlib"
            ],
            "accent": "#2563EB"
        },
        {
            "x": 720, "y": 575, "w": 610, "h": 360,
            "tag": "MODULE 02", "tag_bg": "#F0FDF4", "tag_fg": "#15803D",
            "title": "Precision Grading & Multi-Subject Rules",
            "desc": "Calculates arithmetic means with unrounded float precision. Maps scores against a 7-tier rubric while strictly enforcing multi-subject passing criteria (>=35 in all subjects).",
            "bullets": [
                "7-Tier Scale: A+ (90-100), A (80-89), B, C, D, E, F (<35)",
                "Subject Pass Threshold: Minimum 35.0 required in each subject",
                "Administrative Attendance Flag (< 75%) decoupled from marks",
                "Display-only rounding prevents premature grade drift"
            ],
            "accent": "#16A34A"
        },
        {
            "x": 70, "y": 185, "w": 610, "h": 360,
            "tag": "MODULE 03", "tag_bg": "#FAF5FF", "tag_fg": "#7E22CE",
            "title": "Deterministic Top-5 Ranking & Outliers",
            "desc": "Computes class rankings with robust tie resolution. If multiple students tie at 5th place, all qualifying students are transparently recognized without arbitrary cutoff.",
            "bullets": [
                "#1 Riya Banerjee (96.33% Avg, Data Science)",
                "#2 Ananya Iyer (93.67% Avg, Information Tech)",
                "#3 Aarav Sharma (92.67% Avg, Computer Science)",
                "Identifies lowest performing outliers for academic intervention"
            ],
            "accent": "#9333EA"
        },
        {
            "x": 720, "y": 185, "w": 610, "h": 360,
            "tag": "MODULE 04", "tag_bg": "#FFF7ED", "tag_fg": "#C2410C",
            "title": "Group Analytics & 9-Section Reporting",
            "desc": "Generates multi-dimensional group aggregations across 4 departments and 4 semesters with mean, standard deviation, and pass rate calculations.",
            "bullets": [
                "Department Leader: Data Science leads cohort with 73.44% avg",
                "Semester Breakdown: Semester 1 achieved 100% pass rate",
                "Answers 12 dynamic academic research queries at runtime",
                "Complete console report with tabular ASCII formatting"
            ],
            "accent": "#EA580C"
        }
    ]

    for card in bento_cards:
        bg_card = patches.FancyBboxPatch((card["x"], card["y"]), card["w"], card["h"],
                                        boxstyle="round,pad=0.2,rounding_size=18",
                                        facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
        ax.add_patch(bg_card)

        top_line = patches.FancyBboxPatch((card["x"] + 20, card["y"] + card["h"] - 4), card["w"] - 40, 4,
                                          boxstyle="round,pad=0.0,rounding_size=2",
                                          facecolor=card["accent"], edgecolor='none')
        ax.add_patch(top_line)

        tag_box = patches.FancyBboxPatch((card["x"] + 25, card["y"] + card["h"] - 44), 105, 25,
                                         boxstyle="round,pad=0.2,rounding_size=10",
                                         facecolor=card["tag_bg"], edgecolor='none')
        ax.add_patch(tag_box)
        ax.text(card["x"] + 77, card["y"] + card["h"] - 32, card["tag"],
                fontsize=10.5, fontweight='bold', color=card["tag_fg"], ha='center', va='center', fontfamily='Segoe UI')

        ax.text(card["x"] + 25, card["y"] + card["h"] - 78, card["title"],
                fontsize=19.5, fontweight='bold', color='#0F172A', fontfamily='Segoe UI')

        wrapped = textwrap.wrap(card["desc"], width=62)
        desc_y = card["y"] + card["h"] - 110
        for line in wrapped:
            ax.text(card["x"] + 25, desc_y, line, fontsize=12.5, color='#475569', fontfamily='Segoe UI')
            desc_y -= 21

        bullet_y = card["y"] + 128
        for bullet in card["bullets"]:
            ax.add_patch(patches.Circle((card["x"] + 32, bullet_y + 4), radius=4,
                                        facecolor=card["accent"], edgecolor='none'))
            ax.text(card["x"] + 46, bullet_y, bullet, fontsize=12.2, fontweight='semibold',
                    color='#1E293B', fontfamily='Segoe UI')
            bullet_y -= 31

    # Bottom Tech Stack Badges & Attribution
    footer_box = patches.FancyBboxPatch((70, 50), 1260, 105, boxstyle="round,pad=0.2,rounding_size=16",
                                       facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5)
    ax.add_patch(footer_box)

    ax.text(95, 115, "TECH STACK & ARCHITECTURE", fontsize=10.5, fontweight='bold', color='#64748B', fontfamily='Segoe UI')
    
    techs = [
        ("Python 3.11+", "#3776AB", "#EFF6FF"),
        ("Pandas 2.0+", "#150458", "#F3E8FF"),
        ("NumPy 1.24+", "#013243", "#ECFEFF"),
        ("Unittest Suite", "#059669", "#ECFDF5"),
        ("Pure Functional", "#D97706", "#FFFBEB")
    ]
    chip_x = 95
    chip_y = 70
    for t_label, t_color, t_bg in techs:
        t_w = len(t_label) * 9.5 + 24
        t_patch = patches.FancyBboxPatch((chip_x, chip_y), t_w, 32, boxstyle="round,pad=0.2,rounding_size=12",
                                         facecolor=t_bg, edgecolor='#E2E8F0', linewidth=1)
        ax.add_patch(t_patch)
        ax.text(chip_x + t_w / 2, chip_y + 16, t_label, fontsize=11.5, fontweight='bold',
                color=t_color, ha='center', va='center', fontfamily='Segoe UI')
        chip_x += t_w + 12

    ax.text(1305, 115, "DEVELOPER & REPOSITORY", fontsize=10.5, fontweight='bold', color='#64748B', ha='right', fontfamily='Segoe UI')
    ax.text(1305, 87, "Vijay Mahes  |  maheswari9080", fontsize=14.5, fontweight='bold', color='#0F172A', ha='right', fontfamily='Segoe UI')
    ax.text(1305, 68, "python-with-ai-internship-mini-project", fontsize=11, color='#64748B', ha='right', fontfamily='Segoe UI')

    # Save to image.png and backup
    plt.savefig("image.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.savefig("assets/linkedin_showcase.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.savefig("screenshots/image.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.close()
    print("Created: image.png, assets/linkedin_showcase.png, screenshots/image.png")


# -------------------------------------------------------------------------
# 2. README HERO BANNER: assets/banner_light.png (1200 x 420)
# -------------------------------------------------------------------------
def generate_readme_banner():
    fig = plt.figure(figsize=(12, 4.2), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 420)
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0, 0), 1200, 420, facecolor='#F8FAFC', edgecolor='none'))
    
    ax.add_patch(patches.Circle((1100, 360), radius=160, facecolor='#EEF2FF', edgecolor='none', alpha=0.8))
    ax.add_patch(patches.Circle((100, 80), radius=140, facecolor='#ECFDF5', edgecolor='none', alpha=0.8))

    main_card = patches.FancyBboxPatch((25, 20), 1150, 380, boxstyle="round,pad=0.2,rounding_size=20",
                                       facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(main_card)
    
    top_strip = patches.FancyBboxPatch((25, 394), 1150, 6, boxstyle="round,pad=0.0,rounding_size=3",
                                       facecolor='#4F46E5', edgecolor='none')
    ax.add_patch(top_strip)

    # Top Tag pill - cleanly centered without overlapping dot
    pill = patches.FancyBboxPatch((60, 340), 380, 30, boxstyle="round,pad=0.2,rounding_size=15",
                                  facecolor='#EEF2FF', edgecolor='#C7D2FE', linewidth=1)
    ax.add_patch(pill)
    ax.text(250, 355, "EWB COURSES  |  PYTHON WITH AI INTERNSHIP", fontsize=10.5, fontweight='bold',
            color='#4338CA', ha='center', va='center', fontfamily='Segoe UI')

    # Title
    ax.text(60, 285, "Student Academic Performance Analysis", fontsize=28, fontweight='bold',
            color='#0F172A', fontfamily='Segoe UI')
    ax.text(60, 245, "& Reporting System", fontsize=28, fontweight='bold',
            color='#4F46E5', fontfamily='Segoe UI')

    # Subtitle
    ax.text(60, 208, "Automated data validation, descriptive statistical analytics, 7-tier grading rubric,",
            fontsize=13.5, color='#475569', fontfamily='Segoe UI')
    ax.text(60, 185, "and multi-dimensional cohort reporting powered by Python, Pandas & NumPy.",
            fontsize=13.5, color='#475569', fontfamily='Segoe UI')

    # Stat Chips
    stats = [
        ("Python 3.11+", "#1D4ED8", "#EFF6FF"),
        ("Pandas & NumPy", "#0369A1", "#F0F9FF"),
        ("32/32 Tests Passed", "#047857", "#ECFDF5"),
        ("80% Pass Rate", "#B45309", "#FFFBEB"),
        ("100% QA Validated", "#6D28D9", "#FAF5FF")
    ]
    sx = 60
    sy = 125
    for s_txt, s_fg, s_bg in stats:
        sw = len(s_txt) * 9 + 20
        sp = patches.FancyBboxPatch((sx, sy), sw, 32, boxstyle="round,pad=0.2,rounding_size=12",
                                    facecolor=s_bg, edgecolor='#CBD5E1', linewidth=1)
        ax.add_patch(sp)
        ax.text(sx + sw/2, sy + 16, s_txt, fontsize=11, fontweight='bold', color=s_fg,
                ha='center', va='center', fontfamily='Segoe UI')
        sx += sw + 12

    # Right side Mini Preview Card
    preview_box = patches.FancyBboxPatch((855, 50), 295, 315, boxstyle="round,pad=0.2,rounding_size=16",
                                        facecolor='#F8FAFC', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(preview_box)
    
    ax.text(875, 335, "COHORT OVERVIEW", fontsize=11, fontweight='bold', color='#64748B', fontfamily='Segoe UI')
    
    metrics = [
        ("Total Students", "25", "#0F172A"),
        ("Top Performer", "Riya B. (96.3%)", "#059669"),
        ("Top Subject", "Python (65.2%)", "#4F46E5"),
        ("Passed Students", "20 / 25 (80%)", "#0284C7"),
        ("Attendance Rate", "80.76% avg", "#D97706"),
        ("Flagged <75%", "6 students", "#DC2626")
    ]
    my = 295
    for m_label, m_val, m_c in metrics:
        ax.text(875, my, m_label, fontsize=11, color='#64748B', fontfamily='Segoe UI')
        ax.text(1125, my, m_val, fontsize=11.5, fontweight='bold', color=m_c, ha='right', fontfamily='Segoe UI')
        ax.plot([875, 1125], [my - 10, my - 10], color='#E2E8F0', lw=1)
        my -= 38

    plt.savefig("assets/banner_light.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.close()
    print("Created: assets/banner_light.png")


# -------------------------------------------------------------------------
# 3. ARCHITECTURE PIPELINE: assets/architecture_light.png (1200 x 500)
# -------------------------------------------------------------------------
def generate_architecture_diagram():
    fig = plt.figure(figsize=(12, 5.2), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1200)
    ax.set_ylim(0, 520)
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0, 0), 1200, 520, facecolor='#F8FAFC', edgecolor='none'))

    # Header
    ax.text(60, 480, "SYSTEM ARCHITECTURE & EXECUTION PIPELINE", fontsize=12, fontweight='bold',
            color='#4F46E5', fontfamily='Segoe UI')
    ax.text(60, 445, "Modular Pure-Function Data Pipeline", fontsize=24, fontweight='bold',
            color='#0F172A', fontfamily='Segoe UI')
    ax.text(60, 420, "Strict end-to-end separation between data validation, calculation, aggregation, and presentation layers.",
            fontsize=13, color='#64748B', fontfamily='Segoe UI')

    stages = [
        {
            "num": "01", "name": "Ingestion & QA", "sub": "Data Validation",
            "color": "#2563EB", "bg": "#EFF6FF",
            "items": ["Pathlib Path Verification", "Schema & Columns Audit", "Range Check [0-100]", "Unique Student IDs"]
        },
        {
            "num": "02", "name": "Calculations", "sub": "Analytical Engine",
            "color": "#059669", "bg": "#ECFDF5",
            "items": ["Unrounded Float Means", "7-Tier Rubric (A+ to F)", ">=35 Subject Pass Rule", "Attendance Flag (<75%)"]
        },
        {
            "num": "03", "name": "Aggregation", "sub": "Statistical Engine",
            "color": "#7C3AED", "bg": "#F5F3FF",
            "items": ["NumPy Descriptive Stats", "Department Breakdown", "Semester Performance", "Deterministic Ties Rank"]
        },
        {
            "num": "04", "name": "Reporting", "sub": "Console Presentation",
            "color": "#EA580C", "bg": "#FFF7ED",
            "items": ["9 Structured Sections", "12 Dynamic Q&A Answers", "Formatted ASCII Tables", "Zero Floating Drift"]
        }
    ]

    bw = 250
    gap = 40
    start_x = 60
    sy = 100

    for i, st in enumerate(stages):
        x = start_x + i * (bw + gap)
        cbox = patches.FancyBboxPatch((x, sy), bw, 280, boxstyle="round,pad=0.2,rounding_size=16",
                                     facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5)
        ax.add_patch(cbox)

        hbar = patches.FancyBboxPatch((x, sy + 225), bw, 55, boxstyle="round,pad=0.0,rounding_size=12",
                                     facecolor=st["bg"], edgecolor='none')
        ax.add_patch(hbar)

        ax.text(x + 20, sy + 252, f"STAGE {st['num']}", fontsize=11, fontweight='bold', color=st["color"], fontfamily='Segoe UI')
        ax.text(x + 20, sy + 200, st["name"], fontsize=18, fontweight='bold', color='#0F172A', fontfamily='Segoe UI')
        ax.text(x + 20, sy + 180, st["sub"], fontsize=12, fontweight='semibold', color='#64748B', fontfamily='Segoe UI')

        iy = sy + 140
        for item in st["items"]:
            ax.add_patch(patches.Circle((x + 26, iy + 4), radius=3.5, facecolor=st["color"], edgecolor='none'))
            ax.text(x + 38, iy, item, fontsize=11.5, color='#334155', fontfamily='Segoe UI')
            iy -= 32

        if i < len(stages) - 1:
            ax.annotate("", xy=(x + bw + gap - 8, sy + 140), xytext=(x + bw + 8, sy + 140),
                        arrowprops=dict(arrowstyle="->", color="#94A3B8", lw=2.5, mutation_scale=16))

    ax.text(600, 45, "Verified with 32 Automated Unit Tests (100% Pass Rate) | Unittest Framework",
            fontsize=12, fontweight='semibold', color='#64748B', ha='center', fontfamily='Segoe UI')

    plt.savefig("assets/architecture_light.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.close()
    print("Created: assets/architecture_light.png")


# -------------------------------------------------------------------------
# 4. REAL DATA CHARTS: assets/analytics_overview.png (1200 x 800)
# -------------------------------------------------------------------------
def generate_analytics_dashboard():
    df = pd.read_csv("data/students.csv")
    df['average'] = (df['python_marks'] + df['mathematics_marks'] + df['statistics_marks']) / 3.0
    df['passed'] = (df['python_marks'] >= 35) & (df['mathematics_marks'] >= 35) & (df['statistics_marks'] >= 35)

    fig, axs = plt.subplots(2, 2, figsize=(14, 10), facecolor='#F8FAFC')
    # generous margins so no label clipping
    fig.subplots_adjust(top=0.90, bottom=0.08, left=0.15, right=0.95, hspace=0.38, wspace=0.32)
    
    fig.suptitle("Student Academic Performance • Analytical Dashboard Overview",
                 fontsize=22, fontweight='bold', color='#0F172A', y=0.96, fontfamily='Segoe UI')

    # Chart 1: Subject Score Comparison
    ax1 = axs[0, 0]
    ax1.set_facecolor('#FFFFFF')
    subjects = ['Python Programming', 'Mathematics', 'Statistics']
    subj_means = [df['python_marks'].mean(), df['mathematics_marks'].mean(), df['statistics_marks'].mean()]
    colors = ['#4F46E5', '#0284C7', '#059669']
    
    bars = ax1.bar(subjects, subj_means, color=colors, width=0.55, edgecolor='#E2E8F0', linewidth=1.2)
    ax1.set_title("Subject Score Means (Cohort Average)", fontsize=14, fontweight='bold', color='#1E293B', pad=12, fontfamily='Segoe UI')
    ax1.set_ylim(0, 100)
    ax1.set_ylabel("Marks (0 - 100)", fontsize=11, color='#64748B')
    ax1.grid(axis='y', linestyle='--', alpha=0.5, color='#CBD5E1')
    ax1.set_axisbelow(True)
    ax1.tick_params(colors='#475569', labelsize=10.5)

    for bar, val in zip(bars, subj_means):
        ax1.text(bar.get_x() + bar.get_width()/2, val + 2.5, f"{val:.2f}%",
                 ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#0F172A', fontfamily='Segoe UI')

    # Chart 2: Department-wise Average Performance (Vertical bars for clean aesthetics)
    ax2 = axs[0, 1]
    ax2.set_facecolor('#FFFFFF')
    dept_order = ['Data Science', 'Computer Science', 'Information Tech', 'Artificial Intel']
    dept_vals = [
        df[df['department'] == 'Data Science']['average'].mean(),
        df[df['department'] == 'Computer Science']['average'].mean(),
        df[df['department'] == 'Information Technology']['average'].mean(),
        df[df['department'] == 'Artificial Intelligence']['average'].mean()
    ]
    dept_colors = ['#8B5CF6', '#3B82F6', '#10B981', '#F59E0B']
    
    bars2 = ax2.bar(dept_order, dept_vals, color=dept_colors, width=0.55, edgecolor='#E2E8F0', linewidth=1.2)
    ax2.set_title("Department Academic Performance (Mean %)", fontsize=14, fontweight='bold', color='#1E293B', pad=12, fontfamily='Segoe UI')
    ax2.set_ylim(0, 100)
    ax2.set_ylabel("Average Mark (%)", fontsize=11, color='#64748B')
    ax2.grid(axis='y', linestyle='--', alpha=0.5, color='#CBD5E1')
    ax2.set_axisbelow(True)
    ax2.tick_params(colors='#475569', labelsize=10.5)

    for bar, val in zip(bars2, dept_vals):
        ax2.text(bar.get_x() + bar.get_width()/2, val + 2.5, f"{val:.2f}%",
                 ha='center', va='bottom', fontsize=11.5, fontweight='bold', color='#0F172A', fontfamily='Segoe UI')

    # Chart 3: Pass vs Fail Ratio (Donut Chart)
    ax3 = axs[1, 0]
    ax3.set_facecolor('#FFFFFF')
    passed_count = df['passed'].sum()
    failed_count = len(df) - passed_count
    pie_labels = [f"Passed ({passed_count})", f"Failed ({failed_count})"]
    pie_colors = ['#10B981', '#EF4444']
    
    wedges, texts, autotexts = ax3.pie(
        [passed_count, failed_count],
        labels=pie_labels,
        autopct='%1.1f%%',
        pctdistance=0.72,
        colors=pie_colors,
        startangle=90,
        wedgeprops=dict(width=0.45, edgecolor='#FFFFFF', linewidth=3),
        textprops=dict(color='#1E293B', fontsize=12, fontweight='bold', fontfamily='Segoe UI')
    )
    for at in autotexts:
        at.set_color('#FFFFFF')
        at.set_fontsize(12)
        at.set_fontweight='bold'
    ax3.set_title(f"Class Result Distribution (Total: {len(df)})", fontsize=14, fontweight='bold', color='#1E293B', pad=12, fontfamily='Segoe UI')

    # Chart 4: Attendance vs Average Marks
    ax4 = axs[1, 1]
    ax4.set_facecolor('#FFFFFF')
    corr = np.corrcoef(df['attendance_percentage'], df['average'])[0, 1]
    
    colors_scatter = ['#10B981' if p else '#EF4444' for p in df['passed']]
    ax4.scatter(df['attendance_percentage'], df['average'], c=colors_scatter, s=70, alpha=0.85, edgecolors='#334155', linewidth=0.8)
    
    m, b = np.polyfit(df['attendance_percentage'], df['average'], 1)
    x_line = np.linspace(df['attendance_percentage'].min(), df['attendance_percentage'].max(), 50)
    ax4.plot(x_line, m*x_line + b, color='#4F46E5', linestyle='-', lw=2.2, label=f"Trend (r = +{corr:.2f})")
    ax4.axvline(75.0, color='#D97706', linestyle='--', lw=1.5, label="75% Attendance Min")

    ax4.set_title(f"Attendance vs. Academic Mark Correlation", fontsize=14, fontweight='bold', color='#1E293B', pad=12, fontfamily='Segoe UI')
    ax4.set_xlabel("Attendance Percentage (%)", fontsize=11, color='#64748B')
    ax4.set_ylabel("Average Mark (%)", fontsize=11, color='#64748B')
    ax4.set_xlim(50, 100)
    ax4.set_ylim(15, 105)
    ax4.grid(True, linestyle='--', alpha=0.5, color='#CBD5E1')
    ax4.tick_params(colors='#475569', labelsize=10.5)
    ax4.legend(loc='lower right', frameon=True, facecolor='#F8FAFC', edgecolor='#E2E8F0', fontsize=10)

    for ax in [ax1, ax2, ax3, ax4]:
        for spine in ['top', 'right']:
            ax.spines[spine].set_visible(False)
        for spine in ['left', 'bottom']:
            ax.spines[spine].set_color('#CBD5E1')

    plt.savefig("assets/analytics_overview.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.close()
    print("Created: assets/analytics_overview.png")


# -------------------------------------------------------------------------
# 5. GRADING RUBRIC CARD: assets/grading_rubric_light.png (1000 x 530)
# -------------------------------------------------------------------------
def generate_grading_rubric():
    fig = plt.figure(figsize=(10, 5.3), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 530)
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0, 0), 1000, 530, facecolor='#F8FAFC', edgecolor='none'))

    card = patches.FancyBboxPatch((30, 25), 940, 480, boxstyle="round,pad=0.2,rounding_size=18",
                                 facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(card)

    ax.text(60, 468, "ACADEMIC EVALUATION & GRADING BENCHMARK", fontsize=11, fontweight='bold',
            color='#4F46E5', fontfamily='Segoe UI')
    ax.text(60, 436, "7-Tier Project Grading Rubric & Decision Matrix", fontsize=21, fontweight='bold',
            color='#0F172A', fontfamily='Segoe UI')

    headers = ["Grade", "Score Range", "Qualitative Standing", "Pass / Fail Status"]
    hx = [60, 200, 420, 720]
    hy = 395

    ax.add_patch(patches.FancyBboxPatch((50, 380), 900, 32, boxstyle="round,pad=0.1,rounding_size=6",
                                        facecolor='#F1F5F9', edgecolor='none'))
    for h, x in zip(headers, hx):
        ax.text(x, hy, h, fontsize=12, fontweight='bold', color='#334155', fontfamily='Segoe UI')

    rows = [
        ("A+", "90.0% – 100.0%", "Outstanding Mastery", "Pass", "#059669", "#ECFDF5"),
        ("A",  "80.0% – 89.9%",  "Excellent Performance", "Pass", "#10B981", "#ECFDF5"),
        ("B",  "70.0% – 79.9%",  "Very Good Understanding", "Pass", "#0284C7", "#F0F9FF"),
        ("C",  "60.0% – 69.9%",  "Good / Above Average", "Pass", "#3B82F6", "#EFF6FF"),
        ("D",  "50.0% – 59.9%",  "Satisfactory Performance", "Pass", "#D97706", "#FFFBEB"),
        ("E",  "35.0% – 49.9%",  "Marginal Pass (Subject Min)", "Pass", "#EA580C", "#FFF7ED"),
        ("F",  "Below 35.0%",    "Unsatisfactory / Fail", "Fail", "#DC2626", "#FEF2F2")
    ]

    ry = 346
    for g, rng, desc, st, col, bg in rows:
        gb = patches.FancyBboxPatch((hx[0], ry - 8), 45, 26, boxstyle="round,pad=0.2,rounding_size=6",
                                    facecolor=bg, edgecolor=col, linewidth=1)
        ax.add_patch(gb)
        ax.text(hx[0] + 22.5, ry + 5, g, fontsize=12, fontweight='bold', color=col, ha='center', va='center', fontfamily='Segoe UI')

        ax.text(hx[1], ry + 5, rng, fontsize=12, color='#1E293B', va='center', fontfamily='Segoe UI')
        ax.text(hx[2], ry + 5, desc, fontsize=12, color='#475569', va='center', fontfamily='Segoe UI')
        
        st_col = '#059669' if st == 'Pass' else '#DC2626'
        ax.text(hx[3], ry + 5, st, fontsize=12, fontweight='bold', color=st_col, va='center', fontfamily='Segoe UI')

        ax.plot([50, 950], [ry - 13, ry - 13], color='#F1F5F9', lw=1)
        ry -= 38

    # Rules note comfortably separated at bottom
    note_box = patches.FancyBboxPatch((50, 42), 900, 36, boxstyle="round,pad=0.2,rounding_size=8",
                                      facecolor='#F8FAFC', edgecolor='#CBD5E1', linewidth=1)
    ax.add_patch(note_box)
    ax.text(500, 60, "Policy: Passing requires >= 35.0 in Python, Math & Stats. Attendance < 75.0% is flagged separately without mark alteration.",
            fontsize=10.5, color='#475569', ha='center', va='center', fontfamily='Segoe UI')

    plt.savefig("assets/grading_rubric_light.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.close()
    print("Created: assets/grading_rubric_light.png")


# -------------------------------------------------------------------------
# 6. TOP PERFORMERS LEADERBOARD: assets/top_performers_light.png (1000 x 450)
# -------------------------------------------------------------------------
def generate_top_performers():
    fig = plt.figure(figsize=(10, 4.5), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1000)
    ax.set_ylim(0, 450)
    ax.axis('off')

    ax.add_patch(patches.Rectangle((0, 0), 1000, 450, facecolor='#F8FAFC', edgecolor='none'))

    card = patches.FancyBboxPatch((30, 20), 940, 410, boxstyle="round,pad=0.2,rounding_size=18",
                                 facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
    ax.add_patch(card)

    ax.text(60, 395, "HONOR ROLL & LEADERBOARD", fontsize=11, fontweight='bold',
            color='#4F46E5', fontfamily='Segoe UI')
    ax.text(60, 365, "Top 5 Academic Performers (Cohort Ranking)", fontsize=21, fontweight='bold',
            color='#0F172A', fontfamily='Segoe UI')

    top_5 = [
        ("Rank #1", "STD1018", "Riya Banerjee", "Data Science", "96.33%", "A+", "96.0%", "#D97706", "#FFFBEB"),
        ("Rank #2", "STD1004", "Ananya Iyer", "Information Technology", "93.67%", "A+", "72.0%*", "#64748B", "#F1F5F9"),
        ("Rank #3", "STD1001", "Aarav Sharma", "Computer Science", "92.67%", "A+", "94.0%", "#B45309", "#FEF3C7"),
        ("Rank #4", "STD1024", "Priya Nambiar", "Information Technology", "91.00%", "A+", "92.0%", "#475569", "#F8FAFC"),
        ("Rank #5", "STD1002", "Diya Patel", "Data Science", "87.67%", "A", "88.5%", "#475569", "#F8FAFC")
    ]

    col_x = [60, 170, 270, 520, 720, 830]
    headers = ["Rank", "ID", "Student Name", "Department", "Average", "Grade"]
    
    ax.add_patch(patches.FancyBboxPatch((50, 315), 900, 30, boxstyle="round,pad=0.1,rounding_size=6",
                                        facecolor='#F8FAFC', edgecolor='none'))
    for h, x in zip(headers, col_x):
        ax.text(x, 325, h, fontsize=11.5, fontweight='bold', color='#475569', fontfamily='Segoe UI')

    ry = 275
    for rank, sid, name, dept, avg, grade, attend, col, bg in top_5:
        rp = patches.FancyBboxPatch((col_x[0], ry - 7), 80, 26, boxstyle="round,pad=0.2,rounding_size=8",
                                    facecolor=bg, edgecolor=col, linewidth=1)
        ax.add_patch(rp)
        ax.text(col_x[0] + 40, ry + 6, rank, fontsize=11, fontweight='bold', color=col, ha='center', va='center', fontfamily='Segoe UI')

        ax.text(col_x[1], ry + 6, sid, fontsize=11.5, color='#64748B', va='center', fontfamily='Segoe UI')
        ax.text(col_x[2], ry + 6, name, fontsize=12, fontweight='bold', color='#0F172A', va='center', fontfamily='Segoe UI')
        ax.text(col_x[3], ry + 6, dept, fontsize=11.5, color='#475569', va='center', fontfamily='Segoe UI')
        ax.text(col_x[4], ry + 6, avg, fontsize=13, fontweight='bold', color='#4F46E5', va='center', fontfamily='Segoe UI')
        
        gp = patches.FancyBboxPatch((col_x[5], ry - 7), 40, 26, boxstyle="round,pad=0.2,rounding_size=6",
                                    facecolor='#ECFDF5', edgecolor='#10B981', linewidth=1)
        ax.add_patch(gp)
        ax.text(col_x[5] + 20, ry + 6, grade, fontsize=11.5, fontweight='bold', color='#059669', ha='center', va='center', fontfamily='Segoe UI')

        ax.plot([50, 950], [ry - 14, ry - 14], color='#F1F5F9', lw=1)
        ry -= 44

    ax.text(500, 36, "* Note: Ties at 5th rank are deterministically preserved. Attendance marked with (*) reflects administrative flag (<75%).",
            fontsize=10.5, color='#64748B', ha='center', fontfamily='Segoe UI')

    plt.savefig("assets/top_performers_light.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.close()
    print("Created: assets/top_performers_light.png")


if __name__ == "__main__":
    generate_linkedin_image()
    generate_readme_banner()
    generate_architecture_diagram()
    generate_analytics_dashboard()
    generate_grading_rubric()
    generate_top_performers()
    print("All refreshed visual assets created successfully!")

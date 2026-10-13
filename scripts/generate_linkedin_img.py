import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Ensure assets directory exists
os.makedirs("assets", exist_ok=True)

def create_linkedin_image():
    # 1400x1400 high resolution LinkedIn showcase post image
    fig = plt.figure(figsize=(14, 14), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 1400)
    ax.set_ylim(0, 1400)
    ax.axis('off')

    # Background gradient simulation with light theme
    ax.add_patch(patches.Rectangle((0, 0), 1400, 1400, facecolor='#F8FAFC', edgecolor='none'))
    
    # Subtle top accent gradient bar
    ax.add_patch(patches.Rectangle((0, 1385), 1400, 15, facecolor='#4F46E5', edgecolor='none'))

    # Background soft decorative circles/blobs
    circle1 = patches.Circle((1300, 1300), radius=280, facecolor='#EEF2FF', edgecolor='none', alpha=0.6)
    circle2 = patches.Circle((100, 100), radius=250, facecolor='#F0FDF4', edgecolor='none', alpha=0.6)
    circle3 = patches.Circle((1350, 200), radius=220, facecolor='#F0F9FF', edgecolor='none', alpha=0.7)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(circle3)

    # Top Category Pill
    pill = patches.FancyBboxPatch((80, 1280), 450, 42, boxstyle="round,pad=0.2,rounding_size=20",
                                  facecolor='#EEF2FF', edgecolor='#C7D2FE', linewidth=1.5)
    ax.add_patch(pill)
    ax.text(305, 1301, "★  EWB COURSES  |  PYTHON WITH AI MINI-PROJECT", fontsize=12, fontweight='bold',
            color='#4338CA', ha='center', va='center', fontfamily='Segoe UI')

    # Main Project Title
    ax.text(80, 1220, "Student Academic Performance Analysis", fontsize=34, fontweight='bold',
            color='#0F172A', fontfamily='Segoe UI')
    ax.text(80, 1170, "& Reporting System", fontsize=34, fontweight='bold',
            color='#4F46E5', fontfamily='Segoe UI')

    # Subtitle
    ax.text(80, 1125, "An end-to-end automated analytics engine built in Python, Pandas & NumPy with strict QA validation,",
            fontsize=15, color='#475569', fontfamily='Segoe UI')
    ax.text(80, 1098, "7-tier letter grading, deterministic tie-aware ranking, and dynamic executive reporting.",
            fontsize=15, color='#475569', fontfamily='Segoe UI')

    # Top KPI / Metric Banner (4 stats)
    kpis = [
        ("25", "Synthetic Students", "#4F46E5", "#EEF2FF"),
        ("32/32", "Unit Tests Passed", "#059669", "#ECFDF5"),
        ("80.0%", "Class Pass Rate", "#0284C7", "#F0F9FF"),
        ("+0.73", "Attendance Corr.", "#D97706", "#FFFBEB")
    ]
    card_w = 280
    card_gap = 33
    start_x = 80
    kpi_y = 960

    for i, (val, label, color, bg) in enumerate(kpis):
        cx = start_x + i * (card_w + card_gap)
        box = patches.FancyBboxPatch((cx, kpi_y), card_w, 100, boxstyle="round,pad=0.2,rounding_size=15",
                                     facecolor=bg, edgecolor='#E2E8F0', linewidth=1.5)
        ax.add_patch(box)
        # Left accent stripe
        stripe = patches.FancyBboxPatch((cx, kpi_y), 8, 100, boxstyle="round,pad=0.0,rounding_size=4",
                                        facecolor=color, edgecolor='none')
        ax.add_patch(stripe)
        ax.text(cx + 25, kpi_y + 60, val, fontsize=28, fontweight='bold', color=color, fontfamily='Segoe UI')
        ax.text(cx + 25, kpi_y + 25, label, fontsize=13, fontweight='semibold', color='#334155', fontfamily='Segoe UI')

    # 4 Main Feature Bento Cards (2x2 grid)
    bento_cards = [
        {
            "x": 80, "y": 570, "w": 595, "h": 360,
            "tag": "MODULE 01", "tag_bg": "#EFF6FF", "tag_fg": "#1D4ED8",
            "title": "Data Ingestion & Integrity Audit",
            "icon": "🛡️",
            "desc": "Validates incoming CSV against schema constraints before processing. Enforces non-empty names, positive semester ints, and strict ranges [0-100] for marks and attendance.",
            "bullets": [
                "✓ Automated schema verification & column presence check",
                "✓ Zero null, zero empty string policy with explicit error handling",
                "✓ Duplicate Student ID detection (e.g. STD1001 unique checks)",
                "✓ Rejects corrupted/truncated CSV files via Pathlib"
            ],
            "accent": "#2563EB"
        },
        {
            "x": 725, "y": 570, "w": 595, "h": 360,
            "tag": "MODULE 02", "tag_bg": "#F0FDF4", "tag_fg": "#15803D",
            "title": "Precision Grading & Multi-Subject Rules",
            "icon": "📊",
            "desc": "Calculates arithmetic means with unrounded float precision. Maps scores against a 7-tier rubric while strictly enforcing multi-subject passing criteria (>=35 in all subjects).",
            "bullets": [
                "✓ 7-Tier Scale: A+ (90-100), A (80-89), B, C, D, E, F (<35)",
                "✓ Subject Pass Threshold: Minimum 35.0 required in each subject",
                "✓ Administrative Attendance Flag (< 75%) decoupled from marks",
                "✓ Display-only rounding prevents premature grade drift"
            ],
            "accent": "#16A34A"
        },
        {
            "x": 80, "y": 180, "w": 595, "h": 360,
            "tag": "MODULE 03", "tag_bg": "#FAF5FF", "tag_fg": "#7E22CE",
            "title": "Deterministic Top-5 Ranking & Outliers",
            "icon": "🏆",
            "desc": "Computes class rankings with robust tie resolution. If multiple students tie at 5th place, all qualifying students are transparently recognized without arbitrary cutoff.",
            "bullets": [
                "✓ #1 Riya Banerjee (96.33% Avg, Data Science)",
                "✓ #2 Ananya Iyer (93.67% Avg, Information Tech)",
                "✓ #3 Aarav Sharma (92.67% Avg, Computer Science)",
                "✓ Identifies lowest performing outliers for academic intervention"
            ],
            "accent": "#9333EA"
        },
        {
            "x": 725, "y": 180, "w": 595, "h": 360,
            "tag": "MODULE 04", "tag_bg": "#FFF7ED", "tag_fg": "#C2410C",
            "title": "Group Analytics & 9-Section Reporting",
            "icon": "📈",
            "desc": "Generates multi-dimensional group aggregations across 4 departments and 4 semesters with mean, standard deviation, and pass rate calculations.",
            "bullets": [
                "✓ Department Leader: Data Science leads cohort with 73.44% avg",
                "✓ Semester Breakdown: Semester 1 achieved 100% pass rate",
                "✓ Answers 12 dynamic academic research queries at runtime",
                "✓ Complete console report with tabular ASCII formatting"
            ],
            "accent": "#EA580C"
        }
    ]

    for card in bento_cards:
        # Card Background
        bg_card = patches.FancyBboxPatch((card["x"], card["y"]), card["w"], card["h"],
                                        boxstyle="round,pad=0.2,rounding_size=18",
                                        facecolor='#FFFFFF', edgecolor='#E2E8F0', linewidth=1.5)
        ax.add_patch(bg_card)

        # Card subtle top colored line
        top_line = patches.FancyBboxPatch((card["x"] + 20, card["y"] + card["h"] - 4), card["w"] - 40, 4,
                                          boxstyle="round,pad=0.0,rounding_size=2",
                                          facecolor=card["accent"], edgecolor='none')
        ax.add_patch(top_line)

        # Tag pill
        tag_box = patches.FancyBboxPatch((card["x"] + 25, card["y"] + card["h"] - 45), 110, 26,
                                         boxstyle="round,pad=0.2,rounding_size=10",
                                         facecolor=card["tag_bg"], edgecolor='none')
        ax.add_patch(tag_box)
        ax.text(card["x"] + 80, card["y"] + card["h"] - 32, card["tag"],
                fontsize=11, fontweight='bold', color=card["tag_fg"], ha='center', va='center', fontfamily='Segoe UI')

        # Card Title
        ax.text(card["x"] + 25, card["y"] + card["h"] - 80, card["title"],
                fontsize=20, fontweight='bold', color='#0F172A', fontfamily='Segoe UI')

        # Card Description
        desc_lines = [card["desc"][:75], card["desc"][75:150], card["desc"][150:]]
        desc_y = card["y"] + card["h"] - 115
        for line in desc_lines:
            if line.strip():
                ax.text(card["x"] + 25, desc_y, line.strip(), fontsize=13, color='#475569', fontfamily='Segoe UI')
                desc_y -= 22

        # Card Bullets
        bullet_y = card["y"] + 125
        for bullet in card["bullets"]:
            ax.text(card["x"] + 25, bullet_y, bullet, fontsize=12.5, fontweight='semibold',
                    color='#1E293B' if '✓' in bullet else '#334155', fontfamily='Segoe UI')
            bullet_y -= 30

    # Bottom Tech Stack Badges & Attribution
    footer_box = patches.FancyBboxPatch((80, 50), 1240, 100, boxstyle="round,pad=0.2,rounding_size=16",
                                       facecolor='#FFFFFF', edgecolor='#CBD5E1', linewidth=1.5)
    ax.add_patch(footer_box)

    ax.text(110, 112, "TECH STACK & ARCHITECTURE", fontsize=11, fontweight='bold', color='#64748B', fontfamily='Segoe UI')
    
    # Tech chips
    techs = [
        ("Python 3.11+", "#3776AB", "#EFF6FF"),
        ("Pandas 2.0+", "#150458", "#F3E8FF"),
        ("NumPy 1.24+", "#013243", "#ECFEFF"),
        ("Unittest Suite", "#059669", "#ECFDF5"),
        ("Pure Functional", "#D97706", "#FFFBEB"),
        ("100% Reproducible", "#4F46E5", "#EEF2FF")
    ]
    chip_x = 110
    chip_y = 68
    for t_label, t_color, t_bg in techs:
        t_w = len(t_label) * 9.5 + 24
        t_patch = patches.FancyBboxPatch((chip_x, chip_y), t_w, 32, boxstyle="round,pad=0.2,rounding_size=12",
                                         facecolor=t_bg, edgecolor='#E2E8F0', linewidth=1)
        ax.add_patch(t_patch)
        ax.text(chip_x + t_w / 2, chip_y + 16, t_label, fontsize=12, fontweight='bold',
                color=t_color, ha='center', va='center', fontfamily='Segoe UI')
        chip_x += t_w + 14

    # Student / Developer Signature
    ax.text(1290, 112, "AUTHOR & REPOSITORY", fontsize=11, fontweight='bold', color='#64748B', ha='right', fontfamily='Segoe UI')
    ax.text(1290, 80, "Vijay Mahes | maheswari9080", fontsize=14, fontweight='bold', color='#0F172A', ha='right', fontfamily='Segoe UI')
    ax.text(1290, 60, "python-with-ai-internship-mini-project", fontsize=11, color='#64748B', ha='right', fontfamily='Segoe UI')

    # Save to image.png in root and in assets/
    plt.savefig("image.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.savefig("assets/linkedin_showcase.png", dpi=100, bbox_inches='tight', pad_inches=0.1, facecolor='#F8FAFC')
    plt.close()
    print("Successfully generated image.png and assets/linkedin_showcase.png")

if __name__ == "__main__":
    create_linkedin_image()

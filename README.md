# Bacalla - Streamlit Portfolio

A minimalist personal autobiography and project portfolio built with Streamlit, developed by **Mc Cauley Bacalla**, a 3rd-year Computer Science student at Cebu Institute of Technology - University (PACUCOA Level IV accredited).

---

## Overview

This application serves as an interactive showcase of academic coursework, foundational computer science milestones, and practical software engineering capstones. The design strictly prioritizes high information density, clean typography (Inter font), responsive column layouts, and a zero-emoji minimalist aesthetic.

### Core Sections
- **About & Identity:** Student profile, educational standing, program, section, and contact links.
- **Autobiography & Journey:** Academic philosophy, hands-on laboratory experiences using CodeChum, comprehensive semester-by-semester coursework from First Year to Third Year, chronological milestones timeline, 14 verified technical & academic certificates, and side developer utilities.
- **Skills & Technical Coursework:** Concrete metric visualizations mapping completed projects and coursework units per technology stack (static Altair bar chart with fixed zoom).
- **Projects Showcase:** Interactive portfolio of 10 software projects spanning client web apps, automata theory verification, browser extensions, mobile engineering, enterprise inventory, and native desktop systems with direct GitHub repository buttons and keyword/role filtering.
- **Connect & Feedback:** Direct contact channels (Gmail, LinkedIn, CIT-U institutional email) and an interactive session-state inquiry form.

---

## Featured Projects

1. **I Will Pass Automata Theory** (Closed Source / Private Friends-Only)
   - Mathematical verification website for CS313 Automata Theory using exact formulas and algorithms, independent from AI.
   - *Tools:* TypeScript, JavaScript, Antigravity, Google Identity Services, Vercel Serverless.
2. **Labelscript**
   - Minimal browser extension for converting text to Unicode superscripts and inserting frequent snippets via right-click context menu.
   - *Tools:* JavaScript, HTML, CSS, Chrome Extension API.
3. **MyRoutine**
   - Kotlin Android habit tracking application featuring glanceable home-screen widgets and scheduled reminder notifications.
   - *Tools:* Kotlin, Android Studio, App Widgets, AlarmManager.
4. **Clinic Inventory System**
   - Pharmacy management platform with automated FEFO (First-Expired, First-Out) batch deduction and full audit logging.
   - *Tools:* PHP, CSS, MySQL, XAMPP.
5. **YouTube Audio Downloader**
   - Browser extension with a Python Flask backend for extracting and converting YouTube video audio into high-quality local MP3 files.
   - *Tools:* Python Flask, JavaScript, yt-dlp, ffmpeg.
6. **Pomodoro Timer**
   - Lightweight status-bar Pomodoro timer built with SwiftUI for macOS with zero dock footprint.
   - *Tools:* Swift, SwiftUI, Xcode, macOS MenuBarExtra.
7. **+inHealth**
   - Desktop health and ergonomics tracking suite monitoring meal consumption and physical activities, built for OOP 2.
   - *Tools:* Java, Java Swing, OOP Design Patterns, Multithreading, JDBC, MySQL (XAMPP).
8. **CodeChum++**
   - Zero-dependency offline code judging environment with a LeetCode-style split-pane interface, built for OOP 1.
   - *Tools:* Java, Java Swing, ProcessBuilder.
9. **WattWise**
   - Software-based smart energy monitoring system utilizing a simulated smart-breaker environment, created for ES038 Technopreneurship.
   - *Tools:* Python, JavaScript, Software Simulation.
10. **Pretty Nails by Atasha**
   - Ongoing client landing and booking website with automated Messenger notifications for a nail salon business owner.
   - *Tools:* Antigravity, TypeScript, JavaScript, Vercel Serverless, Google Identity Services API, Google Token Verification API.

### Additional Side Projects & Utilities (Under "More" Tab)
- **Anki Last Ease Highlight Add-on:** Highlights the answer button pressed last time during card reviews.
- **FuzzyLogic-Vehicle-Refuel-Recommender:** Python-based Mamdani fuzzy inference system for CS345 Intelligent Systems 1.
- **Messenger Chat Deletor:** Chrome extension for bulk-deleting chat messages and archiving stories with automatic safety filters.
- **TreeViz-CLI:** Terminal-based interactive visualization tool for exploring tree data structures from the command line.
- **SharePoint Video Skip Arrow:** Browser extension mapping arrow keys to native SharePoint 10-second video seeking.
- **LeetCode Problem Solving:** Practice repository and problem solving supporting CSIT221 Data Structures and Algorithms coursework.

---

## Installation & Setup

### Prerequisites
- Python 3.10+ (tested with Python 3.14 on macOS)

### Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/sigmacoy/Bacalla-Streamlit-SmallPortfolio.git
cd Bacalla-Streamlit-SmallPortfolio

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install streamlit pandas numpy altair

# 4. Run the Streamlit application
streamlit run app.py
```

The app will be available locally at `http://localhost:8501`.

---

## License & Credits
Designed and maintained by Mc Cauley Bacalla.  
Institution: Cebu Institute of Technology - University.

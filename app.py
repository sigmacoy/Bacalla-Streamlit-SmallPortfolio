import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# ---------------------------------------------------------
# Page Configuration & Setup
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mc Cauley Bacalla | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Theme State Evaluation (at top before CSS injection)
is_dark = st.session_state.get("dark_mode_toggle", False)

# Custom Minimalist CSS for typography, layout, and theme toggling
theme_css = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}}

/* Sidebar Light/Dark Switch Button: precision horizontal alignment with headerNoPadding */
.st-key-theme_switch_wrapper {{
    position: absolute !important;
    top: 0 !important;
    left: 20px !important;
    height: 60px !important;
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: flex-start !important;
    z-index: 1000 !important;
    margin: 0 !important;
    padding: 0 !important;
    width: auto !important;
}}

.st-key-theme_switch_wrapper .stElementContainer {{
    display: flex !important;
    align-items: center !important;
    margin: 0 !important;
    padding: 0 !important;
    height: 100% !important;
}}

.st-key-theme_switch_wrapper [data-testid="stCheckbox"] {{
    display: flex !important;
    align-items: center !important;
    margin: 0 !important;
    padding: 0 !important;
    min-height: unset !important;
}}

.st-key-theme_switch_wrapper label {{
    display: flex !important;
    align-items: center !important;
    margin: 0 !important;
    padding: 0 !important;
    cursor: pointer !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    line-height: 1 !important;
}}

.st-key-theme_switch_wrapper label > div:first-of-type {{
    transform: translateY(-1.25px) !important;
}}

.metric-card {{
    background-color: {"#18181B" if is_dark else "#F4F4F5"};
    border: 1px solid {"#27272A" if is_dark else "#E4E4E7"};
    border-radius: 8px;
    padding: 16px;
    text-align: center;
}}

.project-card {{
    background-color: {"#18181B" if is_dark else "#FFFFFF"};
    border: 1px solid {"#27272A" if is_dark else "#E4E4E7"};
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 16px;
    transition: border-color 0.15s ease;
}}

.project-card:hover {{
    border-color: {"#52525B" if is_dark else "#A1A1AA"};
}}

.badge {{
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 500;
    background-color: {"#27272A" if is_dark else "#F4F4F5"};
    color: {"#E4E4E7" if is_dark else "#27272A"};
    border: 1px solid {"#3F3F46" if is_dark else "#E4E4E7"};
    margin-right: 4px;
    margin-bottom: 4px;
}}

.badge-primary {{
    background-color: {"#FAFAFA" if is_dark else "#18181B"};
    color: {"#09090B" if is_dark else "#FAFAFA"};
    border: 1px solid {"#FAFAFA" if is_dark else "#18181B"};
}}

.divider {{
    border-bottom-color: {"#27272A" if is_dark else "#E4E4E7"} !important;
}}

/* Center main content container with balanced, symmetrical margins */
.block-container,
[data-testid="stMainBlockContainer"] {{
    max-width: 1040px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
    padding-top: 3rem !important;
    padding-bottom: 2rem !important;
    width: 100% !important;
}}

[data-testid="stMain"] {{
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
}}
""" + ("""
/* Dark Mode Comprehensive Overrides */
html, body, .stApp, [data-testid="stAppViewContainer"] {
    background-color: #09090B !important;
    color: #F4F4F5 !important;
}

header[data-testid="stHeader"] {
    background-color: #09090B !important;
}

/* Sidebar styling in Dark Mode */
[data-testid="stSidebar"] {
    background-color: #121214 !important;
    border-right: 1px solid #27272A !important;
}

[data-testid="stSidebarContent"] {
    background-color: #121214 !important;
}

[data-testid="stSidebar"] p, 
[data-testid="stSidebar"] span, 
[data-testid="stSidebar"] label, 
[data-testid="stSidebar"] h1, 
[data-testid="stSidebar"] h2, 
[data-testid="stSidebar"] h3, 
[data-testid="stSidebar"] li {
    color: #E4E4E7 !important;
}

[data-testid="stSidebarCollapseButton"] button {
    color: #A1A1AA !important;
}

[data-testid="stSidebarCollapseButton"] button:hover {
    color: #FAFAFA !important;
}

/* Sidebar collapsed / expand button - high visibility when headerNoPadding is closed */
[data-testid="stSidebarCollapsedControl"] {
    background-color: #18181B !important;
    border: 1px solid #3F3F46 !important;
    border-radius: 6px !important;
}

[data-testid="stSidebarCollapsedControl"] button,
button[data-testid="stExpandSidebarButton"],
[data-testid="stSidebarCollapsedControl"] button[kind="headerNoPadding"] {
    background-color: #18181B !important;
    color: #FAFAFA !important;
    border: none !important;
}

[data-testid="stSidebarCollapsedControl"] button svg,
button[data-testid="stExpandSidebarButton"] svg,
[data-testid="stSidebarCollapsedControl"] button[kind="headerNoPadding"] svg {
    fill: #FAFAFA !important;
    stroke: #FAFAFA !important;
    color: #FAFAFA !important;
}

[data-testid="stSidebarCollapsedControl"]:hover,
[data-testid="stSidebarCollapsedControl"] button:hover {
    background-color: #27272A !important;
    border-color: #71717A !important;
}

/* Headings and Typography */
h1, h2, h3, h4, h5, h6 {
    color: #FAFAFA !important;
}

p, li {
    color: #D4D4D8 !important;
}

strong, b {
    color: #FFFFFF !important;
}

.stCaption, [data-testid="stCaptionContainer"] p {
    color: #A1A1AA !important;
}

.project-card h3, .project-card h4 {
    color: #FAFAFA !important;
}

.project-card p {
    color: #D4D4D8 !important;
}

/* Metrics */
[data-testid="stMetricValue"] {
    color: #FAFAFA !important;
}
[data-testid="stMetricLabel"] p {
    color: #A1A1AA !important;
}
[data-testid="stMetricDelta"] {
    color: #A1A1AA !important;
}

/* Complete Coursework & Subject Curriculum Expanders */
[data-testid="stExpander"] {
    background-color: #18181B !important;
    border: 1px solid #27272A !important;
    border-radius: 8px !important;
}
[data-testid="stExpander"] summary {
    background-color: #18181B !important;
    color: #FAFAFA !important;
}
[data-testid="stExpander"] summary:hover {
    color: #FFFFFF !important;
}
[data-testid="stExpander"] summary svg {
    fill: #A1A1AA !important;
}
[data-testid="stExpander"] details {
    background-color: #18181B !important;
    border-color: #27272A !important;
}
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p,
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] li {
    color: #D4D4D8 !important;
}
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] strong,
[data-testid="stExpander"] [data-testid="stMarkdownContainer"] b {
    color: #FAFAFA !important;
}

/* Tabs */
button[data-baseweb="tab"] {
    color: #A1A1AA !important;
    background-color: transparent !important;
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: #FAFAFA !important;
    border-bottom-color: #FAFAFA !important;
}

/* Placeholders in inputs, textareas, and selectboxes (gray in dark mode) */
::placeholder {
    color: #71717A !important;
    -webkit-text-fill-color: #71717A !important;
    opacity: 1 !important;
}
input::placeholder, textarea::placeholder {
    color: #71717A !important;
    -webkit-text-fill-color: #71717A !important;
    opacity: 1 !important;
}
[data-testid="stTextInputRootElement"] input::placeholder,
[data-testid="stTextAreaRootElement"] textarea::placeholder,
[data-baseweb="input"] input::placeholder,
[data-baseweb="textarea"] textarea::placeholder {
    color: #71717A !important;
    -webkit-text-fill-color: #71717A !important;
    opacity: 1 !important;
}

/* Input Fields & Textareas */
[data-testid="stTextInputRootElement"],
[data-testid="stTextInputRootElement"] input,
[data-testid="stTextAreaRootElement"],
[data-testid="stTextAreaRootElement"] textarea,
[data-baseweb="input"],
[data-baseweb="input"] input,
[data-baseweb="textarea"],
[data-baseweb="textarea"] textarea {
    background-color: #18181B !important;
    color: #FAFAFA !important;
    -webkit-text-fill-color: #FAFAFA !important;
    border-color: #3F3F46 !important;
}

/* Filter by Tool / Stack (st.multiselect) & Selectboxes */
[data-baseweb="select"] {
    background-color: #18181B !important;
    border-color: #3F3F46 !important;
    color: #FAFAFA !important;
}
[data-baseweb="select"] > div {
    background-color: #18181B !important;
    border-color: #3F3F46 !important;
    color: #FAFAFA !important;
}
[data-baseweb="select"] input {
    color: #FAFAFA !important;
    -webkit-text-fill-color: #FAFAFA !important;
}
[data-baseweb="select"] input::placeholder {
    color: #71717A !important;
    -webkit-text-fill-color: #71717A !important;
}
[data-baseweb="tag"] {
    background-color: #27272A !important;
    color: #FAFAFA !important;
    border: 1px solid #3F3F46 !important;
}
[data-baseweb="tag"] span {
    color: #FAFAFA !important;
}
[data-baseweb="tag"] [role="button"] svg {
    fill: #A1A1AA !important;
}
[data-baseweb="tag"] [role="button"]:hover svg {
    fill: #FAFAFA !important;
}
[data-baseweb="popover"], [data-baseweb="menu"] {
    background-color: #18181B !important;
    border: 1px solid #3F3F46 !important;
}
[data-baseweb="menu"] li {
    background-color: #18181B !important;
    color: #FAFAFA !important;
}
[data-baseweb="menu"] li:hover,
[data-baseweb="menu"] li[aria-selected="true"] {
    background-color: #27272A !important;
    color: #FAFAFA !important;
}

/* Form Controls & Segmented Control (Rating in Send Feedback Form) */
[data-testid="stButtonGroup"] button,
[data-testid="stSegmentedControl"] button,
button[data-variant="segmented_control"],
button[kind="segmented_control"] {
    background-color: #18181B !important;
    color: #E4E4E7 !important;
    border-color: #3F3F46 !important;
}

[data-testid="stButtonGroup"] button *,
button[data-variant="segmented_control"] * {
    color: #E4E4E7 !important;
    -webkit-text-fill-color: #E4E4E7 !important;
}

/* Selected Button in Segmented Control (e.g. Rating button 5) in Dark Mode: pure black text */
[data-testid="stButtonGroup"] button[data-selected],
[data-testid="stButtonGroup"] button[aria-checked="true"],
[data-testid="stButtonGroup"] button[aria-pressed="true"],
[data-testid="stSegmentedControl"] button[data-selected],
button[data-variant="segmented_control"][data-selected],
button[kind="segmented_controlActive"] {
    background-color: #FAFAFA !important;
    color: #000000 !important;
    border-color: #FAFAFA !important;
    font-weight: 700 !important;
}

[data-testid="stButtonGroup"] button[data-selected] *,
[data-testid="stButtonGroup"] button[data-selected] p,
[data-testid="stButtonGroup"] button[data-selected] div,
[data-testid="stButtonGroup"] button[data-selected] span,
[data-testid="stButtonGroup"] button[aria-checked="true"] *,
[data-testid="stButtonGroup"] button[aria-pressed="true"] *,
[data-testid="stSegmentedControl"] button[data-selected] *,
button[data-variant="segmented_control"][data-selected] *,
button[data-variant="segmented_control"][data-selected] p,
button[data-variant="segmented_control"][data-selected] div,
button[data-variant="segmented_control"][data-selected] span,
button[kind="segmented_controlActive"] *,
button[kind="segmented_controlActive"] p,
button[kind="segmented_controlActive"] div,
button[kind="segmented_controlActive"] span {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    font-weight: 700 !important;
}

/* Submit Message Button in Send Feedback Form */
[data-testid="stFormSubmitButton"] button,
button[kind="primaryFormSubmit"],
button[kind="secondaryFormSubmit"],
button[data-testid*="FormSubmit"] {
    background-color: #FAFAFA !important;
    color: #09090B !important;
    border: 1px solid #FAFAFA !important;
    font-weight: 600 !important;
}
[data-testid="stFormSubmitButton"] button *,
button[kind="primaryFormSubmit"] *,
button[kind="secondaryFormSubmit"] * {
    color: #09090B !important;
}
[data-testid="stFormSubmitButton"] button:hover,
button[kind="primaryFormSubmit"]:hover,
button[kind="secondaryFormSubmit"]:hover {
    background-color: #E4E4E7 !important;
    color: #09090B !important;
    border-color: #E4E4E7 !important;
}

/* Standard Buttons & Secondary Buttons */
button[kind="secondary"] {
    background-color: #18181B !important;
    color: #FAFAFA !important;
    border-color: #3F3F46 !important;
}
button[kind="secondary"]:hover {
    background-color: #27272A !important;
    border-color: #71717A !important;
}
button[kind="secondary"]:disabled {
    background-color: #18181B !important;
    color: #52525B !important;
    border-color: #27272A !important;
}
a[kind="secondary"] {
    background-color: #18181B !important;
    color: #FAFAFA !important;
    border-color: #3F3F46 !important;
}
a[kind="secondary"]:hover {
    background-color: #27272A !important;
    border-color: #71717A !important;
}

/* Dataframe, Footer, and Links */
[data-testid="stDataFrame"] {
    border-color: #27272A !important;
}
div[style*="border-top: 1px solid"] {
    border-top-color: #27272A !important;
}
a[style*="color: #2563EB"] {
    color: #60A5FA !important;
}

/* Protect VegaLite Chart from dark mode disruption */
[data-testid="stVegaLiteChart"] {
    background-color: transparent !important;
}
""" if is_dark else "") + "\n</style>"

st.markdown(theme_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "feedback_list" not in st.session_state:
    st.session_state["feedback_list"] = [
        {
            "name": "Academic Peer / Reviewer",
            "email": "peer.review@cit.edu",
            "category": "Project Inquiry",
            "rating": 5,
            "message": "Strong fundamentals in deterministic logic and software engineering design patterns.",
        }
    ]

# ---------------------------------------------------------
# Data Definitions: Skills & Projects
# ---------------------------------------------------------
# Concrete numbers representing Practical Projects Built & Coursework Units
skills_data = [
    {"Skill": "Python", "Category": "Languages & AI", "Projects Built": 4, "Course Units": 6, "Primary Domain": "Applied AI, Quantitative Methods, Scripting"},
    {"Skill": "TypeScript & JavaScript", "Category": "Web & Serverless", "Projects Built": 5, "Course Units": 6, "Primary Domain": "Automata Verification Engine & Extensions"},
    {"Skill": "MySQL & PostgreSQL", "Category": "Databases & Backend", "Projects Built": 3, "Course Units": 6, "Primary Domain": "Information Management 2, FEFO Systems"},
    {"Skill": "Java (JavaFX & Swing)", "Category": "Desktop & Systems", "Projects Built": 4, "Course Units": 9, "Primary Domain": "CodeChum++, +inHealth Ergonomics"},
    {"Skill": "Kotlin & Android Studio", "Category": "Mobile Engineering", "Projects Built": 2, "Course Units": 3, "Primary Domain": "MyRoutine Habit Tracker & Widgets"},
    {"Skill": "Swift & SwiftUI", "Category": "Desktop & Systems", "Projects Built": 1, "Course Units": 3, "Primary Domain": "PomodoroTimer macOS Menu Bar Utility"},
    {"Skill": "HTML5 & CSS", "Category": "Frontend & Extensions", "Projects Built": 4, "Course Units": 6, "Primary Domain": "Browser Add-ons, Labelscript UI"},
    {"Skill": "Automata & Discrete Math", "Category": "Theoretical CS", "Projects Built": 2, "Course Units": 6, "Primary Domain": "Formal Grammars, State Transitions, Verification"},
]
df_skills = pd.DataFrame(skills_data)

projects_data = [
    {
        "id": "p1",
        "title": "I Will Pass Automata Theory",
        "category": "Theory & Web",
        "role": "Lead Developer, Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["Antigravity", "TypeScript", "JavaScript", "Google Identity Services API", "Google Token Verification API", "Vercel Analytics API", "Vercel Serverless"],
        "description": "A vercel website useful for verifying answers for CS313 Automata Theory using correct math formulas and algorithms. Independent from AI. Closed source code and restricted to private closed friends only.",
        "outcome": "Deterministic mathematical verification engine for automata transitions, context-free grammars, and formal proofs without probabilistic output.",
        "link": "https://i-will-pass-automata-theory.vercel.app/",
        "access_note": "Closed source code / Private friends-only access",
        "highlights": "Algorithmic state transition checks, Google Token Verification gatekeeper, and low-latency serverless computation.",
    },
    {
        "id": "p2",
        "title": "Labelscript",
        "category": "Browser Extensions",
        "role": "Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["JavaScript", "HTML", "CSS", "Chrome Extension API"],
        "description": "A minimal, productivity-focused browser extension that lets you convert selected text to Unicode superscripts and quickly insert frequently used text snippets via right-click context menu.",
        "outcome": "Lightweight productivity extension eliminating repetitive manual Unicode formatting.",
        "link": "https://github.com/sigmacoy/labelscript",
        "access_note": "Open Source Repository",
        "highlights": "Clean manifest V3 implementation, context menu event handlers, and direct clipboard buffer insertion.",
    },
    {
        "id": "p3",
        "title": "MyRoutine",
        "category": "Mobile Apps",
        "role": "Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["Kotlin", "Android Studio", "App Widgets", "AlarmManager"],
        "description": "A mobile habit tracker + widget + notification reminder built in Kotlin to encourage productivity and consistency.",
        "outcome": "Capstone habit management application with glanceable home-screen widgets and recurring push notifications.",
        "link": "https://github.com/sigmacoy/PBD3-Final-Capstone",
        "access_note": "Open Source Repository",
        "highlights": "Android AppWidgetProvider synchronization, local persistence, and background notification alarms.",
    },
    {
        "id": "p4",
        "title": "Clinic Inventory System",
        "category": "Enterprise & Web",
        "role": "Developer (2-Man Team)",
        "role_category": "Team Developer",
        "tools": ["PHP", "CSS", "MySQL", "XAMPP", "FEFO Logic"],
        "description": "A clinic pharmacy management system with FEFO (First-Expired, First-Out) batch deduction, supplier tracking, patient registration, low-stock alerts, expiry and discard controls, and full audit-logged dispensation traceability.",
        "outcome": "Strict audit-logged inventory platform preventing pharmaceutical wastage and tracking batch dispensations.",
        "link": "https://github.com/sigmacoy/IM1-Final-Capstone",
        "access_note": "Open Source Repository",
        "highlights": "Relational schema design, automated FEFO inventory subtraction triggers, and immutable dispensation audit trails.",
    },
    {
        "id": "p5",
        "title": "YouTube Audio Downloader",
        "category": "Browser Extensions",
        "role": "Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["Python Flask", "JavaScript (Frontend)", "yt-dlp", "ffmpeg"],
        "description": "A browser extension that downloads audio from YouTube videos as MP3 files. Uses yt-dlp and ffmpeg with a Flask backend. Built for hard-to-find compilations, J-Pop mixes, and rare tracks unavailable on streaming platforms.",
        "outcome": "Local audio extraction workflow directly accessible from the browser toolbar.",
        "link": "https://github.com/sigmacoy/yt-aud-dl",
        "access_note": "Open Source Repository",
        "highlights": "Localhost REST API communication between Flask and Chrome extension, automated ffmpeg transcoding.",
    },
    {
        "id": "p6",
        "title": "Pomodoro Timer",
        "category": "Native macOS",
        "role": "Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["Swift", "Xcode", "SwiftUI", "macOS MenuBarExtra"],
        "description": "A minimalist menu bar Pomodoro timer built with SwiftUI for macOS with notification and sound alerts without cluttering the Dock.",
        "outcome": "Distraction-free desktop utility with zero dock footprint and native macOS notification dispatching.",
        "link": "https://github.com/sigmacoy/PomodoroTimer",
        "access_note": "Open Source Repository",
        "highlights": "SwiftUI MenuBarExtra architecture, Combine publishers for interval countdowns, and native system audio alerts.",
    },
    {
        "id": "p7",
        "title": "+inHealth",
        "category": "Desktop Apps",
        "role": "Developer (5-Man Team: Backend, Frontend, Database, UI/UX)",
        "role_category": "Team Developer",
        "tools": ["Java", "Java Swing", "OOP Design Patterns", "Multithreading", "JDBC", "MySQL (XAMPP)", "Nutritional API"],
        "description": "Our capstone project for OOP 2: +inHealth is a health tracking application designed to help users monitor, understand, and improve their overall well-being by tracking both their daily meal consumption and physical activities while encouraging desk workers to stay active. This project required the strict implementation of Java Swing, OOP design patterns, multithreading, and SQL database management using JDBC with XAMPP.",
        "outcome": "Modular multi-tier desktop health tracking system combining multithreaded reminder routines, nutritional database logging via JDBC, and active desktop exercise prompts.",
        "link": "https://github.com/Gianne818/tinHealth",
        "access_note": "Academic Capstone (5-Man Team)",
        "highlights": "Java Swing architecture, strict OOP design patterns, background multithreaded timers, and JDBC relational database operations on XAMPP MySQL.",
    },
    {
        "id": "p8",
        "title": "CodeChum++",
        "category": "Desktop Apps",
        "role": "Front-end Developer",
        "role_category": "Team Developer",
        "tools": ["Java", "Java Swing", "Process Execution", "LeetCode-Style UI"],
        "description": "Our capstone project for OOP 1: CodeChum++ is an offline code judging system designed with a LeetCode-style interface, built using Java Swing. It provides an efficient workspace to write, run, and evaluate code instantly without an internet connection.",
        "outcome": "Zero-dependency offline code evaluation environment providing instant local test-case verification and split-pane code editor interface.",
        "link": "https://github.com/leetawn/CodeChum-plus-plus",
        "access_note": "Academic Capstone (Team Developer)",
        "highlights": "Custom Java Swing layout with LeetCode-style pane organization, local process compilation and execution, and test-case comparison runner.",
    },
    {
        "id": "p9",
        "title": "WattWise",
        "category": "Enterprise & Simulation",
        "role": "Collaborative Developer (10-Person Team)",
        "role_category": "Team Developer",
        "tools": ["Python", "JavaScript", "Software Simulation", "Energy Modeling", "Full-Stack"],
        "description": "A software-based energy monitoring system created for ES038 Technopreneurship by a 10-person collaborative team. Uses a simulated smart-breaker environment, so no physical hardware is needed to track, monitor, and optimize power consumption.",
        "outcome": "Comprehensive smart energy platform allowing households and facilities to audit simulated electrical load, detect peak consumption, and test automated breaker policies safely.",
        "link": "No repository yet",
        "access_note": "Technopreneurship Startup Capstone (10-Person Team)",
        "highlights": "Simulated circuit telemetry, smart-breaker event dispatching, software-only hardware emulation, and cross-functional team coordination.",
    },
    {
        "id": "p10",
        "title": "Pretty Nails by Atasha",
        "category": "Client Web & Booking",
        "role": "Lead Developer, Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["Antigravity", "TypeScript", "JavaScript", "Vercel Serverless", "Google Identity Services API", "Google Token Verification API"],
        "description": "An ongoing client website with optimized mobile view for a Nail Salon Business Owner. Functions as a booking website landing page featuring appointment scheduling and automated direct messaging to the owner's Messenger account for real-time customer management.",
        "outcome": "Production-ready automated salon appointment booking system streamlining customer reservations and direct notification delivery to the business owner.",
        "link": "https://github.com/sigmacoy/pretty-nails-by-atasha",
        "access_note": "Active Client Project / Open Source Repository",
        "highlights": "Mobile-first responsive design, Vercel Serverless booking endpoints, Google Identity verification, and automated Messenger notification dispatching.",
    },
]

# ---------------------------------------------------------
# Verified Academic & Technical Certifications
# ---------------------------------------------------------
certificates_data = [
    {
        "title": "Introduction to SQL",
        "issuer": "Sololearn",
        "date": "Oct 23, 2026",
        "image": "assets/certifications/introduction-to-sql.jpg",
        "link": "https://www.sololearn.com/en/certificates/CC-DUK6PAZB",
    },
    {
        "title": "Introduction to Python",
        "issuer": "Sololearn",
        "date": "Oct 9, 2026",
        "image": "assets/certifications/introduction-to-python-oct26.jpeg",
        "link": "https://www.sololearn.com/en/certificates/CC-WHPGSYZD",
    },
    {
        "title": "C# Intermediate",
        "issuer": "Sololearn",
        "date": "August 28, 2026",
        "image": "assets/certifications/c#-intermediate-aug26.jpeg",
        "link": "https://www.sololearn.com/en/certificates/CC-V96UPVOW",
    },
    {
        "title": "Introduction to C#",
        "issuer": "Sololearn",
        "date": "Aug 19, 2026",
        "image": "assets/certifications/introduction-to-c#.jpeg",
        "link": "https://www.sololearn.com/en/certificates/CC-OSXJMWBO",
    },
    {
        "title": "Parangal Academic Achiever 2026",
        "issuer": "Cebu Institute of Technology - University",
        "date": "May 28, 2026",
        "image": "assets/certifications/parangal-2026.jpeg",
        "link": None,
    },
    {
        "title": "CITU Java Object-Oriented Programming Certification",
        "issuer": "CodeChum",
        "date": "May 28, 2026",
        "image": "assets/certifications/citu-java-oop-certification.jpeg",
        "link": "https://citu.codechum.com/student/certificates/28429",
    },
    {
        "title": "Parangal Academic Achiever 2025",
        "issuer": "Cebu Institute of Technology - University",
        "date": "May 9, 2025",
        "image": "assets/certifications/parangal-2025.jpeg",
        "link": None,
    },
    {
        "title": "C Programming 2",
        "issuer": "CodeChum",
        "date": "April 29, 2025",
        "image": "assets/certifications/c-programming-2.jpeg",
        "link": "https://citu.codechum.com/student/certificates/9276",
    },
    {
        "title": "CITU C Programming 1 Certification",
        "issuer": "CodeChum",
        "date": "April 26, 2025",
        "image": "assets/certifications/citu-c-programming-1.jpeg",
        "link": "https://citu.codechum.com/student/certificates/9707",
    },
    {
        "title": "AI Ready ASEAN",
        "issuer": "ASEAN Foundation",
        "date": "December 2, 2025",
        "image": "assets/certifications/ai-class-ready.jpeg",
        "link": None,
    },
    {
        "title": "C++ Intermediate",
        "issuer": "Sololearn",
        "date": "September 27, 2025",
        "image": "assets/certifications/c++-intermediate.jpeg",
        "link": "https://www.sololearn.com/certificates/CC-UKIK68VZ",
    },
    {
        "title": "Java Intermediate",
        "issuer": "Sololearn",
        "date": "August 26, 2025",
        "image": "assets/certifications/java-intermediate.jpeg",
        "link": "https://www.sololearn.com/certificates/CC-DTI9TXO2",
    },
    {
        "title": "Introduction to Java",
        "issuer": "Sololearn",
        "date": "August 22, 2025",
        "image": "assets/certifications/introduction-to-java.jpeg",
        "link": "https://www.sololearn.com/en/certificates/CC-1ISXWAME",
    },
    {
        "title": "Introduction to CSS",
        "issuer": "Sololearn",
        "date": "March 26, 2025",
        "image": "assets/certifications/introduction-to-css.jpeg",
        "link": "https://www.sololearn.com/en/certificates/CC-DVC6XKUV",
    },
]

# ---------------------------------------------------------
# Sidebar Component: Profile & Explicit Fast Navigation
# ---------------------------------------------------------
with st.sidebar:
    with st.container(key="theme_switch_wrapper"):
        st.toggle(
            "",
            value=is_dark,
            key="dark_mode_toggle",
        )
    
    st.image("assets/my-pic2.png", use_container_width=True, caption="")
    
    st.markdown("### Student Profile")
    st.markdown(
        """
        **Name:** Mc Cauley Bacalla  
        **Program:** BS in Computer Science  
        **Year Level:** 3  
        **Class Section:** F1  
        **Institution:** Cebu Institute of Technology - University  
        **Location:** Cebu City, Philippines  
        """
    )
    
    st.markdown("---")
    st.markdown("### Quick Navigation")
    st.markdown(
        """
        - [About](#about-mc-cauley-bacalla)
        - [Autobiography](#autobiography)
        - [Skills & Metrics](#skills-technical-coursework)
        - [Projects Showcase](#projects-showcase)
        - [Connect & Feedback](#connect-feedback)
        """
    )
    
    st.markdown("---")
    st.markdown("### View Controls")
    layout_mode = st.radio(
        "Project Layout Density",
        options=["Standard 2-Column Grid", "Compact Directory View"],
        index=0,
        help="Adjust the display density of the project cards.",
    )
    
    st.markdown("---")
    resume_summary = """# Curriculum Vitae & Portfolio Summary
Name: Mc Cauley Bacalla
Program: BS in Computer Science - Year 3 (Section F1)
Institution: Cebu Institute of Technology - University (PACUCOA Level IV accredited)
Focus: Software Engineer / AI Engineer
Location: Cebu City, Philippines
Email: mccauley.bacalla@cit.edu
LinkedIn: https://www.linkedin.com/in/mc-cauley-bacalla-a4274a363/

Core Skills:
- Languages & Stacks: Python, TypeScript, JavaScript, Java, Kotlin, Swift, PHP, C, C++, HTML/CSS
- Databases: MySQL, PostgreSQL
- Coursework: Automata Theory (CS313), Information Management 2, Applied AI & Quantitative Methods, Design & Analysis of Algorithms

Certifications (14 Verified Credentials):
- Sololearn: Introduction to SQL, Introduction to Python, C# Intermediate, Introduction to C#, C++ Intermediate, Java Intermediate, Introduction to Java, Introduction to CSS
- CodeChum: CITU Java OOP, CITU C Programming 1, C Programming 2
- Institutional Honors: Parangal Academic Achiever (2025, 2026), AI Ready ASEAN

Projects:
1. I Will Pass Automata Theory - Closed private verification tool for CS313 Automata Theory
2. Labelscript - Productivity browser extension for Unicode superscripts and context snippets
3. MyRoutine - Kotlin mobile habit tracker with home-screen widgets and reminders
4. Clinic Inventory System - PHP/MySQL pharmacy inventory with FEFO batch deduction
5. YouTube Audio Downloader - Flask and yt-dlp/ffmpeg local audio extraction tool
6. Pomodoro Timer - Minimalist SwiftUI macOS menu bar timer
7. +inHealth - Java Swing desktop health and physical activity tracking suite
8. CodeChum++ - Standalone offline Java Swing code judge environment
9. WattWise - Software-based energy monitoring system with simulated smart-breaker environment
10. Pretty Nails by Atasha - Client salon booking landing page with automated Messenger notifications
"""
    st.download_button(
        label="Download Summary (.md)",
        data=resume_summary,
        file_name="Mc_Cauley_Bacalla_Portfolio_Summary.md",
        mime="text/markdown",
        use_container_width=True,
    )
    
    st.caption("My Minimalist Portfolio")

# ---------------------------------------------------------
# Header & Hero Section: About Mc Cauley Bacalla
# ---------------------------------------------------------
st.markdown('<a id="about-mc-cauley-bacalla"></a>', unsafe_allow_html=True)

st.title("Mc Cauley Bacalla")
st.markdown(
    """
    <div style="margin-top: 0px; margin-bottom: 15px;">
        <span class="badge badge-primary">BS Computer Science - Year 3</span>
        <span class="badge">Cebu Institute of Technology - University</span>
        <span class="badge">Aspiring Software Engineer / AI Engineer</span>
        <span class="badge">Officer - Google Developer Groups on Campus</span>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write(
    """
    Computer Science student at Cebu Institute of Technology - University (PACUCOA Level IV accredited), 
    focused on pursuing a career as a **Software Engineer** at a fintech company or **AI Engineer**. Self-learner who enjoys 
    solving problems through repetitions and pattern recognition. Officer of a school organization called **Google Developer Groups on Campus** in the Technology Department.
    """
)

m_col1, m_col2, m_col3, m_col4 = st.columns(4)
with m_col1:
    st.metric(label="Featured Projects", value="10", delta="Documented")
with m_col2:
    st.metric(label="Year Level", value="3rd Year", delta="Regular Student")
with m_col3:
    st.metric(label="Class Section", value="F1", delta="BSCS")
with m_col4:
    st.metric(label="Theory Focus", value="CS313", delta="Studying hard!")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Autobiography Section
# ---------------------------------------------------------
st.markdown('<a id="autobiography"></a>', unsafe_allow_html=True)
st.header("Autobiography")
st.write("Background, academic education, focus areas, and milestones.")

tab_bg, tab_edu, tab_interest, tab_milestones, tab_certs, tab_more = st.tabs([
    "Background & Philosophy",
    "Academic Education",
    "Focus Areas & Goals",
    "Key Milestones",
    "Certificates",
    "More",
])

with tab_bg:
    st.subheader("Background")
    st.write(
        """
        I am a third-year Computer Science student at Cebu Institute of Technology - University. 
        My approach to software development is grounded in disciplined practice: I learn through repetition, 
        deconstructing algorithms, and recognizing recurring patterns across systems.
        
        Whether building native desktop applications in Java and Swift, designing relational database schemas 
        with strict FEFO constraints, or developing specialized tools for formal language verification, 
        I prioritize reliability, deterministic outcomes, and clear design principles.
        """
    )
    st.info("**Core Principle:** Fundamentals first.")
    st.info("**Motto:** Keizoku wa chikara nari (Continuity is power / perseverance is strength).")

with tab_edu:
    st.subheader("Academic Education")
    st.markdown(
        """
        - **Degree:** Bachelor of Science in Computer Science
        - **Institution:** Cebu Institute of Technology - University (PACUCOA Level IV accredited)
        - **Current Academic Standing:** 3rd Year Undergraduate (First Semester)
        - **Class Section:** F1
        """
    )
    
    st.markdown("#### Programming & Architectural Foundations")
    st.write(
        """
        In my Computer Science curriculum, I have gained the fundamentals of programming and it all began with **C** for our Introduction to Programming concepts, then advanced to **C++** for implementing Data Structures and Algorithms, and utilized **Java** for Object-Oriented Programming.

        Our coursework utilized **CodeChum**, an online assessment platform specifically for onsite laboratory sessions. All programming quizzes, examinations, and activities were exclusively administered and completed during these supervised in-person labs, with the platform enabling real-time code validation and immediate feedback on our implementations.

        Our capstone project for OOP 1 was called **CodeChum++**, an offline code judging system designed with a LeetCode-style interface. This project was developed using Java Swing.

        For OOP 2 it was **+inHealth**, a health tracking application designed to help users monitor, understand, and improve their overall well-being by tracking both their daily meal consumption and physical activities. This project required the strict implementation of Java Swing, OOP design patterns, multithreading, and SQL database management using JDBC with XAMPP.
        """
    )
    
    cap_col1, cap_col2 = st.columns(2)
    with cap_col1:
        st.markdown(
            """
            **OOP 1 Capstone: CodeChum++**  
            An offline code judging system designed with a LeetCode-style interface, developed using Java Swing for local laboratory environments without internet access.
            """
        )
    with cap_col2:
        st.markdown(
            """
            **OOP 2 Capstone: +inHealth**  
            A health tracking application to monitor daily meals and desktop activities, developed using Java Swing, OOP design patterns, multithreading, and JDBC with XAMPP MySQL.
            """
        )
    
    st.markdown("#### Complete Coursework & Subject Curriculum")
    st.write("Comprehensive record of subjects, foundational domains, and practical capstones completed across each academic semester:")

    with st.expander("First Year - First Semester", expanded=True):
        st.markdown(
            """
            - **CSIT111 Introduction to Computing**  
              Number systems: binary, hexadecimal, octal representations, base conversions, complements arithmetic, computer hardware architecture fundamentals, computing history, and digital data representations.
            - **CSIT121 Fundamentals of Programming**  
              Core fundamentals of C, memory address manipulation, pointers, references, stack vs. heap memory allocation, control flow, algorithmic problem-solving, and foundational sorting algorithms (Bubble Sort, Insertion Sort, Selection Sort).
            """
        )

    with st.expander("First Year - Second Semester"):
        st.markdown(
            """
            - **CS132 Introduction to Computer Systems**  
              Comprehensive digital logic and hardware systems:
              1. *Review of Computer Data and Number Systems:* Base N counting and conversion, binary arithmetic, and complements.
              2. *Switching Operations:* Logic gates, digital circuit representations, Boolean functions and expressions, derived logic gates and equivalent circuits.
              3. *Simplification of Boolean Expressions:* Boolean algebra theorems, Karnaugh Map (K-Map) method.
              4. *Combinational Logic Circuits (CLSs):* Design procedure, analysis and design of simple CLSs, CLS implementations with Small Scale Integrated (SSI) circuits.  
              *Final Project:* Designed and implemented a digital binary arithmetic adder circuit to sum two numbers in binary.
            - **CSIT112 Discrete Structures 1**  
              Propositional and predicate logic, set theory, relations, functions, mathematical induction, and formal proofs.
            - **CSIT122 Intermediate Programming**  
              Continuation of programming fundamentals: advanced C/C++ concepts, modular architecture, recursion, structured data types, dynamic memory management, and file I/O operations.
            - **CSIT201 Platform-based Development 2 (Web)**  
              Web development fundamentals covering semantic HTML5, modern CSS3 styling, JavaScript DOM manipulation, event handling, and client-side web interactions.
            - **MATH136 Differential and Integral Calculus**  
              Limits, continuity, differentiation rules, optimization, related rates, integration techniques, definite integrals, and engineering applications.
            """
        )

    with st.expander("Second Year - First Semester"):
        st.markdown(
            """
            - **CS231 Discrete Structures 2**  
              Advanced discrete mathematics: recurrence relations, advanced combinatorics, graph theory modeling, trees, connectivity, and discrete probability.
            - **CS243 Computer Organization and Architecture**  
              CPU architecture, instruction set architectures, Assembly language fundamentals, register operations, instruction pipelining, cache memory hierarchy, and machine cycle execution.
            - **CSIT104 Platform-based Development 1 (Multimedia)**  
              Digital multimedia principles, visual asset production, Canva workflows, color theory, and frontend UI/UX interaction design fundamentals.
            - **CSIT221 Data Structures and Algorithms**  
              Comprehensive data structures and algorithms implemented completely from scratch in C++: Arrays, Linked Lists (Singly, Doubly, Circular), Stacks, Queues, Binary Trees, Binary Search Trees (BST), Tree Traversals (Inorder, Preorder, Postorder, Level-order), and Graphs, including graph representations, Breadth-First Search (BFS), Depth-First Search (DFS), and Dijkstra's Shortest Path algorithm.
            - **CSIT227 Object-Oriented Programming 1**  
              Core object-oriented principles in Java: encapsulation, inheritance, polymorphism, abstraction, class hierarchies, and interface design.  
              *Capstone Project:* **CodeChum++** — an offline code judging system designed with a LeetCode-style interface, developed using Java Swing.
            """
        )

    with st.expander("Second Year - Second Semester"):
        st.markdown(
            """
            - **CS234 Special Topics in Mathematics**  
              Linear Algebra: systems of linear equations, matrices, Gaussian elimination, determinants, vector spaces, linear transformations, eigenvalues, and eigenvectors.
            - **CS244 Design and Analysis of Algorithms**  
              Rigorous algorithmic analysis and complex data structures implemented from scratch:
              - *Advanced Tree Structures:* Balanced search trees including Red-Black Trees, Splay Trees, and 2-3-4 Trees (Tree24).
              - *Hashing & Tables:* Hash tables implemented from scratch with collision resolution strategies.
              - *Dynamic Programming & Recursion:* Complex recursion problems, Longest Increasing Subsequence (LIS), Fibonacci optimization, and memoization.
              - *Complexity Analysis:* Rigorous manual time and space complexity analysis (Big-O, Big-Omega, Big-Theta) and algorithm optimization.
              - *Tractability:* Introduction to NP-completeness and polynomial-time verifications.
            - **CSIT226 Information Management 1**  
              Relational database design, Entity-Relationship (ER) modeling, normalization (1NF to 3NF/BCNF), SQL queries, and transactional integrity.  
              *Capstone Project:* **Clinic Inventory System** — pharmacy management system with FEFO batch deduction and audit logs.
            - **CSIT228 Object-Oriented Programming 2**  
              Advanced software engineering in Java: strict OOP design patterns, multithreading, and SQL database management using JDBC with XAMPP.  
              *Capstone Project:* **+inHealth** — desktop health and meal tracking suite with active exercise reminders.
            - **CSIT238 Human Computer Interaction**  
              User-centered design principles, mobile UI/UX ergonomics, usability heuristics, cognitive walkthroughs, wireframing, and interactive prototyping.  
              *Capstone Project:* <a href="https://www.figma.com/make/awZvpGYhb83ANgNiOuVZ8g/Wireframe?t=CszizxSgOFKzvbJ9-20&fullscreen=1&preview-route=%2Flogin" target="_blank" style="color: #2563EB; text-decoration: underline; font-weight: 600;">WildMarket</a> — a mobile app task, job, and selling marketplace within a community. Interactive prototype built in Figma Make.
            - **CSIT284 Platform-based Development 3 (Mobile)**  
              Native Android application engineering in Kotlin using Android Studio: activity lifecycles, background services, notifications, and app widgets.  
              *Capstone Project:* **MyRoutine** — habit tracker with interactive home-screen widgets and recurring reminders.
            """,
            unsafe_allow_html=True,
        )

    with st.expander("Third Year - First Semester (Current)", expanded=True):
        st.markdown(
            """
            - **CS313 Automata Theory and Formal Languages**  
              Formal computation models: Deterministic Finite Automata (DFA), Non-Deterministic Finite Automata (NFA), Regular Expressions, Regular Languages, Context-Free Grammars (CFG), Regular Grammars, Pushdown Automata (PDA), and Turing Machines.  
              *Independent Verification Tool:* **I Will Pass Automata Theory** — closed private verification platform independent from AI.
            - **CS345 Intelligent Systems 1**  
              Foundations of computational intelligence: fuzzy logic, fuzzy inference systems, linguistic variables, and Artificial Neural Networks (ANN).  
              *Coursework Repository:* This <a href="https://github.com/sigmacoy/CS345-IS1" target="_blank" style="color: #2563EB; text-decoration: underline; font-weight: 600;">repository</a> is all my work/assignment/required output for this course.
            - **CSIT212 Quantitative Methods**  
              Applied statistics and probability modeling: Normal distribution, exponential distribution, Poisson distribution, Bayes' theorem, permutations, combinations, Probability Density Functions (PDF), Cumulative Distribution Functions (CDF), and statistical hypothesis analysis.
            - **CSIT321 Applications Development and Emerging Technologies**  
              Modern scalable backend architectures, microservices, cloud deployments, and emerging web technologies.  
              *Capstone Project:* <a href="https://github.com/sigmacoy/pretty-nails-by-atasha" target="_blank" style="color: #2563EB; text-decoration: underline; font-weight: 600;">Pretty Nails by Atasha</a> — ongoing client appointment booking landing page with automated Messenger notifications and mobile-optimized scheduling for a nail salon business owner.
            - **CSIT327 Information Management 2**  
              Advanced relational database administration: complex SQL querying, indexing, stored procedures, transactions, and hands-on application development using PostgreSQL and MySQL.
            - **ES038 Technopreneurship**  
              Collaborative technology entrepreneurship and startup engineering in a 10-person team:  
              *Capstone Project:* **WattWise** — a software-based energy monitoring system utilizing a simulated smart-breaker environment, eliminating the need for physical hardware.
            """,
            unsafe_allow_html=True,
        )

with tab_interest:
    st.subheader("Goals & Focus Areas")
    st.write(
        """
        **Primary Goal:** To secure a role in an overseas company and dedicate hard work toward its long-term success.
        """
    )
    int_col1, int_col2, int_col3 = st.columns(3)
    with int_col1:
        st.markdown("**Software Engineering**")
        st.caption("Constructing robust, maintainable full-stack systems and standalone desktop tools with clean separation of concerns.")
    with int_col2:
        st.markdown("**AI Engineering & Applied Math**")
        st.caption("Leveraging Python and quantitative methods for applied artificial intelligence, mathematical verification, and problem-solving.")
    with int_col3:
        st.markdown("**Database Systems**")
        st.caption("Designing reliable relational backends in MySQL and PostgreSQL with strict business logic validation and audit logging.")

with tab_milestones:
    st.subheader("Timeline & Project Evolution")
    st.write("Chronological development timeline across academic capstones, browser utilities, developer tools, and client platforms based on repository starting dates:")
    milestones_data = [
        {"Date": "Nov 20, 2025", "Project": "CodeChum++", "Category": "Academic Capstone (OOP 1)", "Detail": "Offline code judging environment in Java Swing with a LeetCode-style interface."},
        {"Date": "Dec 18, 2025", "Project": "PomodoroTimer", "Category": "macOS Utility", "Detail": "Minimalist menu bar Pomodoro timer built with SwiftUI for macOS with zero dock footprint."},
        {"Date": "Mar 29, 2026", "Project": "YouTube Audio Downloader", "Category": "Browser Extension & Python", "Detail": "Browser extension and Flask backend extracting YouTube audio to MP3 using yt-dlp and ffmpeg."},
        {"Date": "Apr 10, 2026", "Project": "+inHealth", "Category": "Academic Capstone (OOP 2)", "Detail": "Health and meal tracking desktop app in Java Swing using OOP design patterns, multithreading, and JDBC with XAMPP MySQL."},
        {"Date": "Apr 12, 2026", "Project": "TreeViz-CLI", "Category": "Terminal Utility", "Detail": "Command-line interactive visualization tool for exploring tree data structures from scratch."},
        {"Date": "Apr 24, 2026", "Project": "MyRoutine", "Category": "Mobile App (Kotlin)", "Detail": "Android habit tracker with interactive home-screen widgets and recurring push notifications."},
        {"Date": "Apr 24, 2026", "Project": "Clinic Inventory System", "Category": "Full-Stack Web (IM1)", "Detail": "Clinic pharmacy system featuring automated FEFO batch deduction, supplier tracking, and audit logging."},
        {"Date": "May 19, 2026", "Project": "Anki Last Ease Highlight Add-on", "Category": "Productivity Add-on", "Detail": "Anki add-on highlighting the last-selected answer button during card reviews."},
        {"Date": "May 30, 2026", "Project": "Messenger Chat Deletor", "Category": "Browser Extension", "Detail": "Chrome extension for bulk-deleting chat messages and archiving stories with automatic safety skipping."},
        {"Date": "Sep 19, 2026", "Project": "FuzzyLogic-Vehicle-Refuel-Recommender", "Category": "Intelligent Systems (CS345)", "Detail": "Python Mamdani fuzzy logic inference system evaluating vehicle fuel levels and distance to next gas station."},
        {"Date": "Oct 4, 2026", "Project": "SharePoint Video Skip Arrow", "Category": "Browser Extension", "Detail": "Extension mapping arrow keys to SharePoint's native 10-second skip buttons and spacebar play/pause."},
        {"Date": "Oct 9, 2026", "Project": "Labelscript", "Category": "Browser Extension", "Detail": "Productivity browser extension converting selected text to Unicode superscripts via right-click context menu."},
        {"Date": "Oct 11, 2026", "Project": "I Will Pass Automata Theory", "Category": "Theory & Serverless", "Detail": "Deterministic mathematical verification tool for CS313 Automata Theory, independent from AI."},
        {"Date": "Oct 23, 2026", "Project": "Pretty Nails by Atasha", "Category": "Client Web & Booking", "Detail": "Client booking landing page for nail salon business with automated Messenger notifications."},
    ]
    st.dataframe(
        pd.DataFrame(milestones_data),
        use_container_width=True,
        hide_index=True,
        column_config={
            "Date": st.column_config.TextColumn("Date", width=125),
            "Project": st.column_config.TextColumn("Project", width=220),
            "Category": st.column_config.TextColumn("Category", width=190),
            "Detail": st.column_config.TextColumn("Detail"),
        },
    )

with tab_certs:
    st.subheader("Certifications & Academic Honors")
    st.write("Verified technical certifications from Sololearn and CodeChum, alongside institutional academic achiever honors from CIT-U:")
    
    for i in range(0, len(certificates_data), 2):
        c_col1, c_col2 = st.columns(2, gap="medium")
        with c_col1:
            c1 = certificates_data[i]
            st.image(c1["image"], use_container_width=True)
            st.markdown(
                f"""
                <div style="margin-top: 4px; margin-bottom: 8px;">
                    <strong style="font-size: 0.95rem;">{c1['title']}</strong><br>
                    <span style="font-size: 0.82rem; color: #71717A;">
                        Issuer: {c1['issuer']} • Date: {c1['date']}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if c1.get("link"):
                st.link_button("Verify Credential", url=c1["link"], use_container_width=True, key=f"cert_link_{i}")
            else:
                st.button("Institutional Credential", disabled=True, use_container_width=True, key=f"cert_btn_{i}")
            st.markdown("<br>", unsafe_allow_html=True)
            
        with c_col2:
            if i + 1 < len(certificates_data):
                c2 = certificates_data[i + 1]
                st.image(c2["image"], use_container_width=True)
                st.markdown(
                    f"""
                    <div style="margin-top: 4px; margin-bottom: 8px;">
                        <strong style="font-size: 0.95rem;">{c2['title']}</strong><br>
                        <span style="font-size: 0.82rem; color: #71717A;">
                            Issuer: {c2['issuer']} • Date: {c2['date']}
                        </span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                if c2.get("link"):
                    st.link_button("Verify Credential", url=c2["link"], use_container_width=True, key=f"cert_link_{i+1}")
                else:
                    st.button("Institutional Credential", disabled=True, use_container_width=True, key=f"cert_btn_{i+1}")
                st.markdown("<br>", unsafe_allow_html=True)

with tab_more:
    st.subheader("Side Projects & Developer Tools")
    st.write("Additional independent tools, browser extensions, terminal utilities, and academic prototypes:")
    
    more_projects = [
        {
            "title": "Anki Last Ease Highlight Add-on",
            "category": "Productivity & Learning Add-on",
            "desc": "Anki add-on that highlights the answer button you pressed last time for each card during review.",
            "link": "https://github.com/sigmacoy/anki-last-ease-highlight-addon",
        },
        {
            "title": "FuzzyLogic-Vehicle-Refuel-Recommender",
            "category": "Intelligent Systems Prototype (CS345)",
            "desc": "A Python-based fuzzy logic inference system built from scratch for CS345 Intelligent Systems 1. It evaluates vehicle fuel levels and distance to the next gas station to calculate optimal refuel urgency using Mamdani.",
            "link": "https://github.com/sigmacoy/FuzzyLogic-Vehicle-Refuel-Recommender",
        },
        {
            "title": "Messenger Chat Deletor",
            "category": "Browser Extension & Privacy Automation",
            "desc": "A Chrome extension that bulk-deletes chat messages and deletes archive stories. Marketplace conversations and video stories are automatically skipped.",
            "link": "https://github.com/sigmacoy/messenger-peace-of-mind",
        },
        {
            "title": "TreeViz-CLI",
            "category": "Terminal Data Structures Utility",
            "desc": "A terminal-based interactive visualization tool for learning and exploring tree data structures - no GUI, runs entirely in the command line.",
            "link": "https://github.com/sigmacoy/Terminal-Tree-Viz",
        },
        {
            "title": "SharePoint Video Skip Arrow",
            "category": "Browser Extension & Workflow",
            "desc": "Nobody wants to stretch their fingers for cumbersome default shortcuts just to seek through a video. This lightweight browser extension maps the Left Arrow (<-) and Right Arrow (->) keys directly to SharePoint's native 10-second skip buttons, alongside the Spacebar for quick play and pause, working exclusively on *.sharepoint.com sites.",
            "link": "https://github.com/sigmacoy/sharepoint-video-skip-arrow",
        },
    ]
    
    for i in range(0, len(more_projects), 2):
        col_m1, col_m2 = st.columns(2, gap="medium")
        with col_m1:
            mp = more_projects[i]
            st.markdown(
                f"""
                <div class="project-card" style="padding: 16px; margin-bottom: 10px; min-height: 200px;">
                    <h4 style="margin: 0; padding-bottom: 2px; font-size: 1rem;">{mp['title']}</h4>
                    <p style="color: #71717A; font-size: 0.78rem; margin-top: 2px; margin-bottom: 8px;">
                        <em>{mp['category']}</em>
                    </p>
                    <p style="font-size: 0.88rem; line-height: 1.45; color: #27272A; margin-bottom: 10px; text-align: justify;">
                        {mp['desc']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.link_button("GitHub Link", url=mp["link"], use_container_width=True, key=f"btn_more_{i}")
            st.markdown("<br>", unsafe_allow_html=True)
            
        with col_m2:
            if i + 1 < len(more_projects):
                mp2 = more_projects[i + 1]
                st.markdown(
                    f"""
                    <div class="project-card" style="padding: 16px; margin-bottom: 10px; min-height: 200px;">
                        <h4 style="margin: 0; padding-bottom: 2px; font-size: 1rem;">{mp2['title']}</h4>
                        <p style="color: #71717A; font-size: 0.78rem; margin-top: 2px; margin-bottom: 8px;">
                            <em>{mp2['category']}</em>
                        </p>
                        <p style="font-size: 0.88rem; line-height: 1.45; color: #27272A; margin-bottom: 10px; text-align: justify;">
                            {mp2['desc']}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.link_button("GitHub Link", url=mp2["link"], use_container_width=True, key=f"btn_more_{i+1}")
                st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Skills Section: Concrete Numerical Metrics (Projects & Units)
# ---------------------------------------------------------
st.markdown('<a id="skills-technical-coursework"></a>', unsafe_allow_html=True)
st.header("Skills & Technical Coursework")
st.write(
    """
    Overview of technical stacks mapped against practical completed projects and academic coursework units.
    Use the slider below to filter stacks by minimum completed project implementations.
    """
)

min_proj_count = st.slider(
    "Filter Stacks by Minimum Completed Projects",
    min_value=1,
    max_value=5,
    value=2,
    step=1,
    help="Filter data to show technologies utilized across at least this number of distinct projects.",
)

filtered_skills = df_skills[df_skills["Projects Built"] >= min_proj_count].sort_values(by="Projects Built", ascending=False)

skill_col1, skill_col2 = st.columns([1, 1.25], gap="large")

with skill_col1:
    st.subheader(f"Projects Completed per Stack (>= {min_proj_count} Projects)")
    chart = (
        alt.Chart(filtered_skills)
        .mark_bar(color="#18181B", cornerRadiusTopLeft=3, cornerRadiusTopRight=3)
        .encode(
            x=alt.X("Skill:N", sort=None, title="Technical Stack", axis=alt.Axis(labelAngle=-25, labelLimit=180)),
            y=alt.Y("Projects Built:Q", title="Completed Projects", axis=alt.Axis(tickMinStep=1)),
            tooltip=["Skill", "Category", "Projects Built", "Course Units"],
        )
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)
    st.caption("Quantified metric: Number of independent software projects and capstones completed per technology.")

with skill_col2:
    st.subheader("Stack Metrics Breakdown")
    table_df = filtered_skills[["Skill", "Category", "Projects Built", "Course Units"]].rename(
        columns={"Projects Built": "Projects", "Course Units": "Course Units"}
    )
    st.dataframe(
        table_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Skill": st.column_config.TextColumn("Skill", width=190),
            "Category": st.column_config.TextColumn("Category", width=160),
            "Projects": st.column_config.NumberColumn("Projects", width=85, format="%d"),
            "Course Units": st.column_config.NumberColumn("Course Units", width=105, format="%d"),
        },
    )
    st.write(f"Displaying **{len(filtered_skills)}** of **{len(df_skills)}** technical domains.")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Projects Showcase Section: Interactive Filters & Cards
# ---------------------------------------------------------
st.markdown('<a id="projects-showcase"></a>', unsafe_allow_html=True)
st.header("Projects Showcase")
st.write("Explore all 10 software projects across client web apps, theory, browser extensions, mobile, enterprise, and desktop applications.")

f_col1, f_col2, f_col3 = st.columns([1.5, 1.2, 1], gap="small")

with f_col1:
    search_query = st.text_input(
        "Search Projects",
        placeholder="Type keyword, title, or tool (e.g. Kotlin, Swift, Automata, FEFO)...",
    )

with f_col2:
    all_tools_list = sorted(list(set([tool for proj in projects_data for tool in proj["tools"]])))
    selected_tools = st.multiselect(
        "Filter by Tool / Stack",
        options=all_tools_list,
        default=[],
        help="Select one or more technologies to filter projects.",
    )

with f_col3:
    role_filter = st.selectbox(
        "Filter by Role",
        options=["All Roles", "Solo Developer", "Team Developer"],
        index=0,
    )

# Filter evaluation
filtered_projects = []
for p in projects_data:
    matches_search = (
        not search_query
        or search_query.lower() in p["title"].lower()
        or search_query.lower() in p["description"].lower()
        or any(search_query.lower() in t.lower() for t in p["tools"])
        or search_query.lower() in p["role"].lower()
    )
    
    matches_tools = not selected_tools or any(tool in p["tools"] for tool in selected_tools)
    
    matches_role = (
        role_filter == "All Roles"
        or (role_filter == "Solo Developer" and "Solo" in p["role"])
        or (role_filter == "Team Developer" and ("Team" in p["role"] or "2-Man" in p["role"] or "5-Man" in p["role"]))
    )
    
    if matches_search and matches_tools and matches_role:
        filtered_projects.append(p)

status_col, reset_col = st.columns([3, 1])
with status_col:
    st.write(f"Displaying **{len(filtered_projects)}** of **{len(projects_data)}** projects matching criteria.")
with reset_col:
    if st.button("Reset Project Filters", use_container_width=True):
        st.rerun()

if not filtered_projects:
    st.warning("No projects found matching the current search and filter criteria. Adjust your search parameters.")
elif layout_mode == "Compact Directory View":
    compact_df = pd.DataFrame([
        {
            "Title": p["title"],
            "Category": p["category"],
            "Role": p["role"],
            "Access": p["access_note"],
            "Tools": ", ".join(p["tools"]),
            "Link": p["link"],
        }
        for p in filtered_projects
    ])
    st.dataframe(compact_df, use_container_width=True, hide_index=True)
else:
    for i in range(0, len(filtered_projects), 2):
        col_left, col_right = st.columns(2, gap="medium")
        
        # Left card
        with col_left:
            p = filtered_projects[i]
            st.markdown(
                f"""
                <div class="project-card">
                    <h3 style="margin: 0; padding-bottom: 4px;">{p['title']}</h3>
                    <p style="color: #71717A; font-size: 0.85rem; margin-top: 2px; margin-bottom: 10px;">
                        <strong>Role:</strong> {p['role']} • <em>{p['category']}</em>
                    </p>
                    <p style="font-size: 0.95rem; line-height: 1.5; color: #27272A; margin-bottom: 12px; text-align: justify; text-justify: inter-word;">
                        {p['description']}
                    </p>
                    <p style="font-size: 0.8rem; color: #71717A; margin-bottom: 4px;">
                        <strong>Status:</strong> {p['access_note']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            st.markdown(
                "".join([f'<span class="badge">{t}</span>' for t in p["tools"]]),
                unsafe_allow_html=True,
            )
            
            st.write(f"**Outcome:** {p['outcome']}")
            if p["title"] == "I Will Pass Automata Theory":
                b_col1, b_col2 = st.columns([1, 1])
                with b_col1:
                    st.link_button(
                        label="Launch Vercel Site",
                        url=p["link"],
                        use_container_width=True,
                    )
                with b_col2:
                    st.button(
                        label="Closed Source",
                        disabled=True,
                        use_container_width=True,
                        help="This project repository is closed source and restricted to private closed friends only.",
                        key=f"btn_closed_{p['id']}_{i}",
                    )
            elif p["title"] == "WattWise":
                st.button(
                    label="No Repository Yet",
                    disabled=True,
                    use_container_width=True,
                    help="This project repository is not publicly available yet.",
                    key=f"btn_norepo_{p['id']}_{i}",
                )
            else:
                st.link_button(
                    label="GitHub Link",
                    url=p["link"],
                    use_container_width=True,
                )
            
            st.markdown("<br>", unsafe_allow_html=True)
            
        # Right card
        if i + 1 < len(filtered_projects):
            with col_right:
                p = filtered_projects[i + 1]
                st.markdown(
                    f"""
                    <div class="project-card">
                        <h3 style="margin: 0; padding-bottom: 4px;">{p['title']}</h3>
                        <p style="color: #71717A; font-size: 0.85rem; margin-top: 2px; margin-bottom: 10px;">
                            <strong>Role:</strong> {p['role']} • <em>{p['category']}</em>
                        </p>
                        <p style="font-size: 0.95rem; line-height: 1.5; color: #27272A; margin-bottom: 12px; text-align: justify; text-justify: inter-word;">
                            {p['description']}
                        </p>
                        <p style="font-size: 0.8rem; color: #71717A; margin-bottom: 4px;">
                            <strong>Status:</strong> {p['access_note']}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                
                st.markdown(
                    "".join([f'<span class="badge">{t}</span>' for t in p["tools"]]),
                    unsafe_allow_html=True,
                )
                
                st.write(f"**Outcome:** {p['outcome']}")
                if p["title"] == "I Will Pass Automata Theory":
                    b_col1, b_col2 = st.columns([1, 1])
                    with b_col1:
                        st.link_button(
                            label="Launch Vercel Site",
                            url=p["link"],
                            use_container_width=True,
                        )
                    with b_col2:
                        st.button(
                            label="Closed Source",
                            disabled=True,
                            use_container_width=True,
                            help="This project repository is closed source and restricted to private closed friends only.",
                            key=f"btn_closed_r_{p['id']}_{i}",
                        )
                elif p["title"] == "WattWise":
                    st.button(
                        label="No Repository Yet",
                        disabled=True,
                        use_container_width=True,
                        help="This project repository is not publicly available yet.",
                        key=f"btn_norepo_r_{p['id']}_{i}",
                    )
                else:
                    st.link_button(
                        label="GitHub Link",
                        url=p["link"],
                        use_container_width=True,
                    )
                
                st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Contact & Feedback Form Section
# ---------------------------------------------------------
st.markdown('<a id="connect-feedback"></a>', unsafe_allow_html=True)
# st.header("Connect & Feedback")
# st.write("Reach out directly via email, connect on LinkedIn, or send a message through the form below.")

contact_col1, contact_col2 = st.columns([1, 1.2], gap="large")

with contact_col1:
    st.subheader("Contact Information")
    st.markdown(
        """
        - **Institutional Email:** [mccauley.bacalla@cit.edu](mailto:mccauley.bacalla@cit.edu)
        - **Personal Email:** [macoybacalla9@gmail.com](mailto:macoybacalla9@gmail.com)
        - **Direct Message:** [Send Email via Gmail Web](https://mail.google.com/mail/?view=cm&fs=1&to=macoybacalla9@gmail.com&su=Hello&body=Hi%20there)
        - **LinkedIn Profile:** [linkedin.com/in/mc-cauley-bacalla-a4274a363](https://www.linkedin.com/in/mc-cauley-bacalla-a4274a363/)
        - **GitHub Profile:** [github.com/sigmacoy](https://github.com/sigmacoy)
        """
    )
    st.caption("Feel free to reach out directly through any of the channels above.")

with contact_col2:
    st.subheader("Send Feedback / Inquiry")
    with st.form(key="portfolio_feedback_form", clear_on_submit=True):
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            sender_name = st.text_input("Your Name", placeholder="e.g. Jun Albert S. Pardillo")
        with row1_col2:
            sender_email = st.text_input("Your Email", placeholder="e.g. junpardillo@gmail.com")
        
        row2_col1, row2_col2 = st.columns([1.1, 1])
        with row2_col1:
            category = st.selectbox(
                "Topic",
                options=["General Feedback", "Project Discussion", "Software / AI Collaboration", "Academic Discussion", "Other / None"],
                index=0,
            )
        with row2_col2:
            rating_choice = st.segmented_control("Rating", options=[1, 2, 3, 4, 5], default=5)
            rating = rating_choice if rating_choice is not None else 5
        
        message = st.text_area("Your Message or Comments", placeholder="Write your message or project inquiry here...", height=90)
        
        submitted = st.form_submit_button("Submit Message", use_container_width=True)
        
        if submitted:
            if not sender_name.strip() or not message.strip():
                st.error("Please provide both your name and message before submitting.")
            else:
                st.session_state["feedback_list"].append({
                    "name": sender_name,
                    "email": sender_email if sender_email.strip() else "Not provided",
                    "category": category,
                    "rating": rating,
                    "message": message,
                })
                st.success(f"Thank you, {sender_name}. Your message has been logged to the session state.")
                st.toast("Message submitted successfully.")

with st.expander(f"Session Feedback Log ({len(st.session_state['feedback_list'])} entries)"):
    for idx, fb in enumerate(reversed(st.session_state["feedback_list"]), 1):
        st.markdown(f"**Submission #{idx} from {fb['name']}** ({fb['category']} • Rating: {fb['rating']}/5)")
        st.caption(f"Email: {fb['email']}")
        st.write(f"> {fb['message']}")
        st.markdown("---")

# ---------------------------------------------------------
# Footer Section
# ---------------------------------------------------------
st.markdown(
    """
    <div style="border-top: 1px solid #E4E4E7; margin-top: 5rem; padding-top: 0.4rem; padding-bottom: 0.1rem; text-align: center;">
        <span style="color: #71717A; font-size: 0.75rem;">
            Mc Cauley Bacalla • BS in Computer Science (Year 3) • Section F1 • Cebu Institute of Technology - University
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
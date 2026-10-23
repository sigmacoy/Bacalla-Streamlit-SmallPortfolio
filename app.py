import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# Page Configuration & Setup
# ---------------------------------------------------------
st.set_page_config(
    page_title="Portfolio & Autobiography | Minimalist Showcase",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom Minimalist CSS for typography and subtle card styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Subtle container borders and spacing */
    .metric-card {
        background-color: #F4F4F5;
        border: 1px solid #E4E4E7;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
    }
    
    .project-card {
        background-color: #FFFFFF;
        border: 1px solid #E4E4E7;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 16px;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    
    .project-card:hover {
        border-color: #A1A1AA;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    
    .badge {
        display: inline-block;
        padding: 2px 10px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
        background-color: #F4F4F5;
        color: #27272A;
        border: 1px solid #E4E4E7;
        margin-right: 4px;
        margin-bottom: 4px;
    }
    
    .badge-primary {
        background-color: #18181B;
        color: #FAFAFA;
        border: 1px solid #18181B;
    }
    
    .divider {
        margin: 2rem 0;
        border-bottom: 1px solid #E4E4E7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Session State Initialization
# ---------------------------------------------------------
if "feedback_list" not in st.session_state:
    st.session_state["feedback_list"] = [
        {
            "name": "Prof. Alan Turing (Placeholder)",
            "email": "turing@cs.edu",
            "category": "Academic Review",
            "rating": 5,
            "message": "Excellent algorithmic foundations in your automata project. Keep up the strong analytical rigor!",
        }
    ]

if "bookmarked_projects" not in st.session_state:
    st.session_state["bookmarked_projects"] = set(["I Will Pass Automata Theory"])

# ---------------------------------------------------------
# Data Definitions: Skills & Projects
# ---------------------------------------------------------
skills_data = [
    {"Skill": "TypeScript / JavaScript", "Category": "Languages & Web", "Proficiency": 92, "Years": 3, "Focus": "Frontend & Serverless"},
    {"Skill": "Python / Flask", "Category": "Backend & Tools", "Proficiency": 88, "Years": 3, "Focus": "APIs, yt-dlp, Automation"},
    {"Skill": "Java / JavaFX / Swing", "Category": "Software Engineering", "Proficiency": 85, "Years": 2, "Focus": "Desktop GUIs & Code Runners"},
    {"Skill": "Kotlin & Android Studio", "Category": "Mobile Systems", "Proficiency": 82, "Years": 2, "Focus": "Widgets & Habit Reminders"},
    {"Skill": "Swift & SwiftUI", "Category": "Mobile Systems", "Proficiency": 78, "Years": 1, "Focus": "macOS Menu Bar Utilities"},
    {"Skill": "PHP & MySQL (XAMPP)", "Category": "Backend & Tools", "Proficiency": 80, "Years": 2, "Focus": "FEFO & Pharmacy Inventory"},
    {"Skill": "HTML5 & Modern CSS", "Category": "Languages & Web", "Proficiency": 90, "Years": 3, "Focus": "Minimalist UI & Chrome Exts"},
    {"Skill": "Automata & Discrete Math", "Category": "Theory & Algorithms", "Proficiency": 95, "Years": 2, "Focus": "Formal Verification & DFA/NFA"},
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
        "description": "Closed private website useful for verifying answers for CS313 Automata Theory using exact math formulas and algorithms. Completely independent from AI.",
        "outcome": "High-accuracy deterministic verification engine for automata transitions, context-free grammars, and formal proofs without stochastic hallucinations.",
        "link": "https://i-will-pass-automata-theory.vercel.app/",
        "is_live": True,
        "highlights": "Custom formula engine, Google OAuth session gating, and low-latency serverless computation on Vercel.",
    },
    {
        "id": "p2",
        "title": "Labelscript",
        "category": "Browser Extensions",
        "role": "Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["JavaScript", "HTML", "CSS", "Chrome Extension API"],
        "description": "A minimal, productivity-focused browser extension that lets you convert selected text to Unicode superscripts and quickly insert frequently used text snippets via right-click context menu.",
        "outcome": "Lightweight, zero-overhead browser utility saving everyday repetitive typing and technical notation formatting.",
        "link": "https://github.com/sigmacoy/labelscript",
        "is_live": True,
        "highlights": "Clean manifest V3 implementation, context menu event handlers, and instant clipboard/input replacement.",
    },
    {
        "id": "p3",
        "title": "MyRoutine",
        "category": "Mobile Apps",
        "role": "Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["Kotlin", "Android Studio", "App Widgets", "AlarmManager"],
        "description": "A mobile habit tracker + interactive home-screen widget + notification reminder to encourage productivity and consistency.",
        "outcome": "Published capstone habit formation tool providing glanceable daily streaks and proactive reminder notifications.",
        "link": "https://github.com/sigmacoy/PBD3-Final-Capstone",
        "is_live": True,
        "highlights": "Native Android widget lifecycle synchronization, Room local persistence, and background notification scheduling.",
    },
    {
        "id": "p4",
        "title": "Clinic Inventory System",
        "category": "Enterprise & Web",
        "role": "Developer (Two-Man Developer)",
        "role_category": "Team Developer",
        "tools": ["PHP", "CSS", "MySQL", "XAMPP", "FEFO Logic"],
        "description": "A clinic pharmacy management system with FEFO (First-Expired, First-Out) batch deduction, supplier tracking, patient registration, low-stock alerts, expiry controls, and full audit-logged dispensation traceability.",
        "outcome": "Production-grade medical inventory audit pipeline preventing pharmaceutical spoilage and stock discrepancies.",
        "link": "https://github.com/sigmacoy/IM1-Final-Capstone",
        "is_live": True,
        "highlights": "Normalized relational schema, automated FEFO inventory subtraction triggers, and immutable dispensation audit trails.",
    },
    {
        "id": "p5",
        "title": "YouTube Audio Downloader",
        "category": "Browser Extensions",
        "role": "Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["Python Flask", "JavaScript (Frontend)", "yt-dlp", "ffmpeg"],
        "description": "A browser extension that downloads audio from YouTube videos as MP3 files. Powered by yt-dlp and ffmpeg with a Flask backend. Ideal for hard-to-find compilations, J-Pop mixes, and rare unstreamable tracks.",
        "outcome": "High-fidelity local audio archiving pipeline directly accessible from the browser toolbar.",
        "link": "https://github.com/sigmacoy/yt-aud-dl",
        "is_live": True,
        "highlights": "Localhost REST API communication with Flask, multi-threaded audio extraction, and dynamic ffmpeg conversion.",
    },
    {
        "id": "p6",
        "title": "Pomodoro Timer",
        "category": "Native macOS",
        "role": "Solo Developer",
        "role_category": "Solo Developer",
        "tools": ["Swift", "Xcode", "SwiftUI", "macOS MenuBarExtra"],
        "description": "A minimalist menu bar Pomodoro timer built with SwiftUI for macOS with notification and sound alerts without cluttering your Dock.",
        "outcome": "Distraction-free desktop companion with zero dock footprint and seamless native system audio cues.",
        "link": "https://github.com/sigmacoy/PomodoroTimer",
        "is_live": True,
        "highlights": "SwiftUI MenuBarExtra architecture, Combine publishers for interval countdowns, and native UserNotifications.",
    },
    {
        "id": "p7",
        "title": "tinHealth",
        "category": "Desktop Apps",
        "role": "Developer (5-Man Team: Backend, Frontend, DB Operations, UI)",
        "role_category": "Team Developer",
        "tools": ["Java", "JavaFX", "Nutritional API", "SQLite / MySQL"],
        "description": "+inHealth is a Java/JavaFX health tracking desktop app that encourages desk workers to maintain physical activity, hydration, and nutritional balance throughout the workday.",
        "outcome": "Comprehensive multi-tier desktop software with API-backed nutrient calculations and scheduled desk workout prompts.",
        "link": "https://github.com/Gianne818/tinHealth",
        "is_live": True,
        "highlights": "Modular MVC architecture, robust class hierarchy, external REST nutritional endpoint parsing, and responsive JavaFX styling.",
    },
    {
        "id": "p8",
        "title": "CodeChum++",
        "category": "Desktop Apps",
        "role": "Front-end Developer",
        "role_category": "Team Developer",
        "tools": ["Java", "Java Swing", "ProcessBuilder", "Custom Syntax Canvas"],
        "description": "CodeChum++ is a lightweight, standalone code-judging environment built with Java Swing. It provides an efficient workspace to write, run, and evaluate code instantly without an active internet connection.",
        "outcome": "Zero-dependency offline code judge enabling computer science laboratory assessments in low-connectivity classrooms.",
        "link": "https://github.com/leetawn/CodeChum-plus-plus",
        "is_live": True,
        "highlights": "Custom Swing syntax rendering, sandboxed process execution via Java ProcessBuilder, and test-case comparison runner.",
    },
]

# ---------------------------------------------------------
# Sidebar Component: Profile, Fast Navigation, & Meta Info
# ---------------------------------------------------------
with st.sidebar:
    st.image("assets/avatar.svg", use_container_width=True, caption="Student Photo Stand-In (Placeholder)")
    
    st.markdown("### 🎓 Student Profile")
    st.markdown(
        """
        **Name:** [Your Name Placeholder]  
        **Program:** [BS Computer Science Placeholder]  
        **Year Level:** [Year 3 Placeholder]  
        **Class Section:** [Section CS-301 Placeholder]  
        **Location:** [Cebu / Philippines Placeholder]  
        """
    )
    
    st.markdown("---")
    st.markdown("### 🧭 Quick Navigation")
    st.markdown(
        """
        - [About & Identity](#your-name)
        - [Autobiography & Milestones](#autobiography-journey)
        - [Core Skills & Analytics](#technical-skills-proficiencies)
        - [Projects Showcase (8)](#featured-projects-portfolio)
        - [Contact & Feedback](#get-in-touch-feedback)
        """
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ View Controls")
    layout_mode = st.radio(
        "Project Card Density",
        options=["Standard 2-Column Grid", "Compact Directory View"],
        index=0,
        help="Adjust the visual density of the project cards.",
    )
    
    show_raw_specs = st.checkbox(
        "Show Technical Architecture Snippets",
        value=True,
        help="Toggle architectural deep-dives under each project.",
    )
    
    st.markdown("---")
    # Extra: Download Button for Resume / Portfolio Markdown
    resume_summary = f"""# Curriculum Vitae & Portfolio Summary
Name: [Your Name Placeholder]
Program: [BS Computer Science - Year 3 Placeholder]
Section: [Section CS-301 Placeholder]

## Core Technical Skills
- Languages: TypeScript, JavaScript, Python, Java, Kotlin, Swift, PHP, HTML/CSS
- Systems & Theory: Automata Theory, Discrete Mathematics, FEFO Logistics, Sandboxed Execution
- Tools: Antigravity, Android Studio, Xcode, Flask, Vercel Serverless, MySQL

## Selected Featured Projects
1. I Will Pass Automata Theory - Formal proof and DFA/NFA verification engine
2. Labelscript - Productivity Chrome extension for Unicode superscripts & snippets
3. MyRoutine - Kotlin mobile habit tracker with home-screen widgets & push alerts
4. Clinic Inventory System - PHP/MySQL pharmacy inventory with FEFO batch deduction
5. YouTube Audio Downloader - Flask + yt-dlp/ffmpeg local audio extraction extension
6. Pomodoro Timer - Minimalist SwiftUI macOS menu bar timer
7. tinHealth - JavaFX desktop health and desk-ergonomics tracking suite
8. CodeChum++ - Standalone offline Java code judge and workbench
"""
    st.download_button(
        label="📄 Download CV / Portfolio (.md)",
        data=resume_summary,
        file_name="Portfolio_Summary_YourName.md",
        mime="text/markdown",
        use_container_width=True,
    )
    
    st.caption("Designed with Streamlit • Minimalist Edition")

# ---------------------------------------------------------
# Header & Hero Section: About You
# ---------------------------------------------------------
hero_col1, hero_col2 = st.columns([1, 2.5], gap="large")

with hero_col1:
    st.image("assets/avatar.svg", caption="[Photo Stand-In / Avatar Placeholder]", use_container_width=True)

with hero_col2:
    st.title("[Your Name Placeholder]")
    st.markdown(
        """
        <div style="margin-top: -10px; margin-bottom: 15px;">
            <span class="badge badge-primary">BS Computer Science - Year 3</span>
            <span class="badge">Section CS-301</span>
            <span class="badge">Software Engineer & Systems Builder</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        **Hello!** I am a third-year Computer Science student passionate about **deterministic software systems, developer tooling, 
        and clean minimalism**. From constructing math-rigorous automata verification tools to engineering lightweight macOS menu bar utilities 
        and offline code-judging environments, I enjoy building software that solves concrete problems with high reliability and zero bloat.
        """
    )
    st.caption("📍 University Campus / City • 💻 Active Open-Source Contributor • ✉️ student.placeholder@university.edu")
    
    # Hero Quick Stats using st.metric
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.metric(label="Projects", value="8+", delta="All Open")
    with m_col2:
        st.metric(label="Tech Stacks", value="7", delta="Multi-Platform")
    with m_col3:
        st.metric(label="Theory Focus", value="CS313", delta="100% Deterministic")
    with m_col4:
        st.metric(label="Section", value="CS-301", delta="AY 2024-2025")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Autobiography Section: Tabs Organization
# ---------------------------------------------------------
st.header("Autobiography & Journey")
st.write("An overview of my background, academic development, core engineering passions, and milestones.")

tab_bg, tab_edu, tab_interest, tab_milestones = st.tabs([
    "📖 Background & Philosophy",
    "🎓 Academic Education",
    "🎯 Technical Interests",
    "🏆 Key Milestones & Timeline",
])

with tab_bg:
    st.subheader("My Background")
    st.write(
        """
        *[Placeholder Biography]* My journey into computer science began with curiosity about how complex software can remain resilient, 
        fast, and elegant under constraints. Over the past three years of rigorous academic and practical projects, I have transitioned 
        from writing introductory scripts to engineering multi-platform applications spanning browser extensions, native desktop GUIs, 
        Android applications, and serverless web microservices.
        
        I believe in the **Unix philosophy**: software should do one thing well, maintain clear interfaces, and prioritize clarity over 
        unnecessary complexity. Whether designing an offline code judging engine or an automata verification platform, my primary objective 
        is precision and developer ergonomics.
        """
    )
    st.info("💡 **Core Principle:** Build tools that are independent, reproducible, and verifiable by mathematical definition.")

with tab_edu:
    st.subheader("Academic Education")
    st.write(
        """
        - **Degree:** Bachelor of Science in Computer Science *(Placeholder)*
        - **Current Academic Standing:** 3rd Year Undergraduate *(Placeholder)*
        - **Section:** Section CS-301 *(Placeholder)*
        - **Institutional Honors:** Dean's Lister Candidate *(Placeholder)*
        """
    )
    st.markdown("#### Relevant Coursework Completed")
    edu_col1, edu_col2 = st.columns(2)
    with edu_col1:
        st.markdown(
            """
            - **CS313:** Automata Theory & Formal Languages (Deterministic & Non-Deterministic Finite Automata, Turing Machines)
            - **CS211:** Data Structures and Algorithms (Algorithm Complexity, Balanced Trees, Graph Traversals)
            - **IM101:** Information Management & Relational Database Systems (Normalized Schemas, FEFO Logic, Transactions)
            """
        )
    with edu_col2:
        st.markdown(
            """
            - **PBD103:** Mobile Application Development (Kotlin, Android Architecture Components, Background Services)
            - **SE102:** Software Engineering (Class Hierarchies, Design Patterns, Agile Scrum Collaboration)
            - **OS101:** Operating Systems & Low-Level Process Control (Concurrency, Process Execution, POSIX)
            """
        )

with tab_interest:
    st.subheader("Technical Interests & Passions")
    st.write(
        """
        My engineering interests center around systems that enhance human productivity and intellectual clarity:
        """
    )
    int_col1, int_col2, int_col3 = st.columns(3)
    with int_col1:
        st.markdown("**1. Formal Computation & Theory**")
        st.caption("Verifying computational correctness, discrete proofs, and grammar solvers without relying on probabilistic AI models.")
    with int_col2:
        st.markdown("**2. Offline-First Desktop Utilities**")
        st.caption("Creating native tools (Java Swing, Swift, Kotlin) that function flawlessly without internet connectivity or external telemetry.")
    with int_col3:
        st.markdown("**3. Lightweight Micro-Extensions**")
        st.caption("Building browser add-ons and status-bar monitors that streamline workflow bottlenecks with minimal CPU/RAM overhead.")

with tab_milestones:
    st.subheader("Milestones & Evolution")
    milestones_data = [
        {"Year": "2023 Q1", "Milestone": "First Collaborative Desktop System", "Detail": "Contributed to tinHealth 5-man team; implemented JavaFX UI and nutritional API integration."},
        {"Year": "2023 Q3", "Milestone": "Enterprise Inventory Capstone", "Detail": "Co-engineered PHP/MySQL clinic management system featuring FEFO logic and audit trails."},
        {"Year": "2023 Q4", "Milestone": "Offline Code Judge Architecture", "Detail": "Developed CodeChum++ front-end and test-runner UI in Java Swing for offline lab evaluations."},
        {"Year": "2024 Q1", "Milestone": "Mobile & Native System Expansion", "Detail": "Published MyRoutine Android habit tracker and PomodoroTimer SwiftUI macOS menu bar app."},
        {"Year": "2024 Q3", "Milestone": "Browser Utility Deployment", "Detail": "Released Labelscript (Unicode superscript inserter) and YouTube Audio Downloader (yt-dlp + Flask)."},
        {"Year": "2024 Q4", "Milestone": "Automata Verification System", "Detail": "Architected 'I Will Pass Automata Theory' using TypeScript, Google Auth API, and Vercel Serverless."},
    ]
    st.dataframe(pd.DataFrame(milestones_data), use_container_width=True, hide_index=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Skills Section: Text, Numeric Slider, Chart, & Data Table
# ---------------------------------------------------------
st.header("Technical Skills & Proficiencies")
st.write(
    """
    Below is a breakdown of technical competencies across programming languages, backend frameworks, and theoretical computer science. 
    Use the interactive slider below to filter skills based on self-assessed proficiency ratings.
    """
)

# Interactive Slider Widget
min_rating = st.slider(
    "Filter Skills by Minimum Proficiency Rating (%)",
    min_value=70,
    max_value=95,
    value=75,
    step=5,
    help="Filter the chart and table below to show only competencies at or above this proficiency threshold.",
)

filtered_skills = df_skills[df_skills["Proficiency"] >= min_rating].sort_values(by="Proficiency", ascending=False)

skill_col1, skill_col2 = st.columns([1.5, 1], gap="medium")

with skill_col1:
    st.subheader(f"📊 Proficiency Distribution (≥ {min_rating}%)")
    # Streamlit Bar Chart Component
    chart_data = filtered_skills.set_index("Skill")[["Proficiency"]]
    st.bar_chart(chart_data, color="#18181B", height=320)
    st.caption("Rating scale: 0 to 100 based on hands-on project implementations and coursework mastery.")

with skill_col2:
    st.subheader("📋 Skills Specification Table")
    st.dataframe(
        filtered_skills[["Skill", "Category", "Proficiency", "Years"]],
        use_container_width=True,
        hide_index=True,
    )
    st.write(f"Showing **{len(filtered_skills)}** of **{len(df_skills)}** recorded competencies.")

# Code snippet component demonstrating an automata transition check
with st.expander("🔍 View Sample Code Snippet (CS313 Deterministic Transition Logic)"):
    st.write("A simplified excerpt demonstrating state transition lookup for deterministic finite automata (DFA):")
    st.code(
        """
def verify_dfa_transition(states, alphabet, transition_table, start_state, accept_states, input_string):
    current_state = start_state
    for symbol in input_string:
        if symbol not in alphabet:
            return False, f"Invalid symbol '{symbol}' not in alphabet."
        current_state = transition_table.get((current_state, symbol))
        if current_state is None:
            return False, "Trap / dead state reached."
    is_accepted = current_state in accept_states
    return is_accepted, f"Ended at state {current_state} (Accepted: {is_accepted})"
        """,
        language="python",
    )

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Projects Showcase Section: Interactive Filters & Cards
# ---------------------------------------------------------
st.header("Featured Projects Portfolio")
st.write("Explore all 8 software projects across theory, browser extensions, mobile, enterprise, and native platforms.")

# Interactive Filter Controls Row
f_col1, f_col2, f_col3 = st.columns([1.5, 1.2, 1], gap="small")

with f_col1:
    search_query = st.text_input(
        "🔍 Search Projects",
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

# Filter logic
filtered_projects = []
for p in projects_data:
    # Search query match
    matches_search = (
        not search_query
        or search_query.lower() in p["title"].lower()
        or search_query.lower() in p["description"].lower()
        or any(search_query.lower() in t.lower() for t in p["tools"])
        or search_query.lower() in p["role"].lower()
    )
    
    # Tools multiselect match
    matches_tools = not selected_tools or any(tool in p["tools"] for tool in selected_tools)
    
    # Role match
    matches_role = (
        role_filter == "All Roles"
        or (role_filter == "Solo Developer" and "Solo" in p["role"])
        or (role_filter == "Team Developer" and "Team" in p["role"] or "Two-Man" in p["role"] or "5 Man" in p["role"])
    )
    
    if matches_search and matches_tools and matches_role:
        filtered_projects.append(p)

# Filter status summary with a reset button
status_col, reset_col = st.columns([3, 1])
with status_col:
    st.write(f"Displaying **{len(filtered_projects)}** of **{len(projects_data)}** projects matching your filters.")
with reset_col:
    if st.button("Reset Project Filters", use_container_width=True):
        st.rerun()

# Render Projects
if not filtered_projects:
    st.warning("No projects found matching the current search and filter criteria. Try adjusting your selections.")
elif layout_mode == "Compact Directory View":
    # Compact View: DataFrame representation
    compact_df = pd.DataFrame([
        {
            "Title": p["title"],
            "Category": p["category"],
            "Role": p["role"],
            "Tools": ", ".join(p["tools"]),
            "Link": p["link"],
        }
        for p in filtered_projects
    ])
    st.dataframe(compact_df, use_container_width=True, hide_index=True)
else:
    # Standard 2-Column Responsive Grid View
    for i in range(0, len(filtered_projects), 2):
        col_left, col_right = st.columns(2, gap="medium")
        
        # Left card
        with col_left:
            p = filtered_projects[i]
            st.markdown(
                f"""
                <div class="project-card">
                    <div style="display: flex; justify-content: space-between; align-items: baseline;">
                        <h3 style="margin: 0; padding-bottom: 4px;">{p['title']}</h3>
                    </div>
                    <p style="color: #71717A; font-size: 0.85rem; margin-top: 2px; margin-bottom: 10px;">
                        <strong>Role:</strong> {p['role']} • <em>{p['category']}</em>
                    </p>
                    <p style="font-size: 0.95rem; line-height: 1.5; color: #27272A; margin-bottom: 12px;">
                        {p['description']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            # Tools badges
            st.markdown(
                "".join([f'<span class="badge">{t}</span>' for t in p["tools"]]),
                unsafe_allow_html=True,
            )
            
            # Outcome & Link Row
            st.write(f"**Outcome:** {p['outcome']}")
            b_col1, b_col2 = st.columns([1, 1])
            with b_col1:
                st.link_button(
                    label="🔗 Launch / View Repo",
                    url=p["link"],
                    use_container_width=True,
                )
            with b_col2:
                # Extra: Bookmark Button linked to session state
                is_fav = p["title"] in st.session_state["bookmarked_projects"]
                star_label = "⭐ Bookmarked" if is_fav else "☆ Bookmark"
                if st.button(star_label, key=f"bm_{p['id']}", use_container_width=True):
                    if is_fav:
                        st.session_state["bookmarked_projects"].remove(p["title"])
                    else:
                        st.session_state["bookmarked_projects"].add(p["title"])
                    st.rerun()
            
            if show_raw_specs:
                with st.expander(f"⚙️ Architectural Highlights ({p['title']})"):
                    st.write(f"**Implementation Highlights:** {p['highlights']}")
            
            st.markdown("<br>", unsafe_allow_html=True)
            
        # Right card (if exists)
        if i + 1 < len(filtered_projects):
            with col_right:
                p = filtered_projects[i + 1]
                st.markdown(
                    f"""
                    <div class="project-card">
                        <div style="display: flex; justify-content: space-between; align-items: baseline;">
                            <h3 style="margin: 0; padding-bottom: 4px;">{p['title']}</h3>
                        </div>
                        <p style="color: #71717A; font-size: 0.85rem; margin-top: 2px; margin-bottom: 10px;">
                            <strong>Role:</strong> {p['role']} • <em>{p['category']}</em>
                        </p>
                        <p style="font-size: 0.95rem; line-height: 1.5; color: #27272A; margin-bottom: 12px;">
                            {p['description']}
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
                b_col1, b_col2 = st.columns([1, 1])
                with b_col1:
                    st.link_button(
                        label="🔗 Launch / View Repo",
                        url=p["link"],
                        use_container_width=True,
                    )
                with b_col2:
                    is_fav = p["title"] in st.session_state["bookmarked_projects"]
                    star_label = "⭐ Bookmarked" if is_fav else "☆ Bookmark"
                    if st.button(star_label, key=f"bm_{p['id']}", use_container_width=True):
                        if is_fav:
                            st.session_state["bookmarked_projects"].remove(p["title"])
                        else:
                            st.session_state["bookmarked_projects"].add(p["title"])
                        st.rerun()
                
                if show_raw_specs:
                    with st.expander(f"⚙️ Architectural Highlights ({p['title']})"):
                        st.write(f"**Implementation Highlights:** {p['highlights']}")
                
                st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Contact & Feedback Form Section
# ---------------------------------------------------------
st.header("Get in Touch & Feedback")
st.write(
    """
    Have questions about any of the projects, want to collaborate, or have feedback on this portfolio? 
    Submit the form below and it will dynamically store your entry into active session state.
    """
)

contact_col1, contact_col2 = st.columns([1, 1.2], gap="large")

with contact_col1:
    st.subheader("📬 Contact Details")
    st.markdown(
        """
        - **Student Name:** [Your Name Placeholder]
        - **Program & Section:** [BS Computer Science - Year 3 Placeholder] • Section [CS-301 Placeholder]
        - **Institutional Email:** `student.placeholder@university.edu`
        - **GitHub Profile:** [`github.com/sigmacoy`](https://github.com/sigmacoy)
        - **Automata Verification Engine:** [`i-will-pass-automata-theory.vercel.app`](https://i-will-pass-automata-theory.vercel.app/)
        - **Status:** Open for Software Engineering Internships & Academic Collaborations
        """
    )
    st.markdown("---")
    st.markdown("##### 📌 Bookmarked Projects This Session:")
    if st.session_state["bookmarked_projects"]:
        for bm in st.session_state["bookmarked_projects"]:
            st.markdown(f"- ⭐ **{bm}**")
    else:
        st.caption("No projects currently bookmarked. Click 'Bookmark' on any project card above!")

with contact_col2:
    st.subheader("💬 Interactive Feedback Form")
    # Streamlit Form Component with submit response
    with st.form(key="portfolio_feedback_form", clear_on_submit=True):
        sender_name = st.text_input("Your Full Name", placeholder="e.g. Dr. Ada Lovelace")
        sender_email = st.text_input("Your Email Address", placeholder="e.g. ada@analytical-engine.org")
        category = st.selectbox(
            "Topic / Category",
            options=["General Feedback", "Project Inquiry / Automata", "Code Collaboration", "Academic Discussion"],
        )
        rating = st.slider("Overall Portfolio Rating", min_value=1, max_value=5, value=5, help="1 = Needs Work, 5 = Outstanding")
        message = st.text_area("Your Message or Comments", placeholder="Write your message or project critique here...")
        
        submitted = st.form_submit_button("Send Message & Submit Feedback", use_container_width=True)
        
        if submitted:
            if not sender_name.strip() or not message.strip():
                st.error("Please fill in both your name and message before submitting.")
            else:
                # Append to session state list
                st.session_state["feedback_list"].append({
                    "name": sender_name,
                    "email": sender_email if sender_email.strip() else "Not provided",
                    "category": category,
                    "rating": rating,
                    "message": message,
                })
                # Positive interactive responses: success, balloons, and toast
                st.success(f"🎉 Thank you, **{sender_name}**! Your feedback has been received and logged to the session state.")
                st.balloons()
                st.toast("Feedback message sent successfully!", icon="🚀")

# Expander to review logged session feedback entries
with st.expander(f"📋 View Active Session Feedback Log ({len(st.session_state['feedback_list'])} entries)"):
    for idx, fb in enumerate(reversed(st.session_state["feedback_list"]), 1):
        st.markdown(f"**#{idx} from {fb['name']}** ({fb['category']} • Rating: {'⭐' * fb['rating']})")
        st.caption(f"Email: {fb['email']}")
        st.write(f"> {fb['message']}")
        st.markdown("---")

# ---------------------------------------------------------
# Footer Section
# ---------------------------------------------------------
st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
f_left, f_right = st.columns([2, 1])
with f_left:
    st.caption("© 2024 [Your Name Placeholder] • Section [CS-301 Placeholder] • BS Computer Science")
with f_right:
    st.caption("Built with Streamlit • Minimalist Architecture")

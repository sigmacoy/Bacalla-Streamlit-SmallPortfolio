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

# Custom Minimalist CSS for typography and subtle card styling
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
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
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 16px;
        transition: border-color 0.15s ease;
    }
    
    .project-card:hover {
        border-color: #A1A1AA;
    }
    
    .badge {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 4px;
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
    
    /* Minimize main container bottom padding */
    .block-container {
        padding-bottom: 0.5rem !important;
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
        "role": "Developer (Two-Man Developer)",
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
        "role": "Developer (5-Man Team: Backend, Frontend, DB Operations, UI Behavior, Class Diagrams)",
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
        "link": "https://github.com/sigmacoy",
        "access_note": "Technopreneurship Startup Capstone (10-Person Team)",
        "highlights": "Simulated circuit telemetry, smart-breaker event dispatching, software-only hardware emulation, and cross-functional team coordination.",
    },
]

# ---------------------------------------------------------
# Sidebar Component: Profile & Explicit Fast Navigation
# ---------------------------------------------------------
with st.sidebar:
    st.image("assets/avatar.svg", use_container_width=True, caption="")
    
    st.markdown("### Student Profile")
    st.markdown(
        """
        **Name:** Mc Cauley Bacalla  
        **Program:** BS in Computer Science  
        **Year Level:** 3  
        **Class Section:** F1  
        **Institution:** Cebu Institute of Technology - University  
        **(PACUCOA Level IV accredited)**  
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
"""
    st.download_button(
        label="Download Summary (.md)",
        data=resume_summary,
        file_name="Mc_Cauley_Bacalla_Portfolio_Summary.md",
        mime="text/markdown",
        use_container_width=True,
    )
    
    st.caption("Minimalist Portfolio")

# ---------------------------------------------------------
# Header & Hero Section: About Mc Cauley Bacalla
# ---------------------------------------------------------
st.markdown('<a id="about-mc-cauley-bacalla"></a>', unsafe_allow_html=True)
hero_col1, hero_col2 = st.columns([1, 2.5], gap="large")

with hero_col1:
    st.image("assets/avatar.svg", caption="", use_container_width=True)

with hero_col2:
    st.title("Mc Cauley Bacalla")
    st.markdown(
        """
        <div style="margin-top: -10px; margin-bottom: 15px;">
            <span class="badge badge-primary">BS in Computer Science - Year 3</span>
            <span class="badge">Section F1</span>
            <span class="badge">Cebu Institute of Technology - University</span>
            <span class="badge">Aspiring Software Engineer / AI Engineer</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        Computer Science student at Cebu Institute of Technology - University (PACUCOA Level IV accredited), 
        focused on pursuing a career as a **Software Engineer** at a fintech company or **AI Engineer**. Self-learner who enjoys 
        solving problems through repetitions and pattern recognition.
        """
    )

    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.metric(label="Featured Projects", value="9", delta="Documented")
    with m_col2:
        st.metric(label="Year Level", value="3rd Year", delta="CIT-U")
    with m_col3:
        st.metric(label="Class Section", value="F1", delta="BSCS")
    with m_col4:
        st.metric(label="Theory Focus", value="CS313", delta="Independent from AI")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Autobiography Section
# ---------------------------------------------------------
st.markdown('<a id="autobiography"></a>', unsafe_allow_html=True)
st.header("Autobiography")
st.write("Background, academic education, focus areas, and milestones.")

tab_bg, tab_edu, tab_interest, tab_milestones = st.tabs([
    "Background & Philosophy",
    "Academic Education",
    "Focus Areas & Goals",
    "Key Milestones",
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
            - **CSIT284 Platform-based Development 3 (Mobile)**  
              Native Android application engineering in Kotlin using Android Studio: activity lifecycles, background services, notifications, and app widgets.  
              *Capstone Project:* **MyRoutine** — habit tracker with interactive home-screen widgets and recurring reminders.
            """
        )

    with st.expander("Third Year - First Semester (Current)", expanded=True):
        st.markdown(
            """
            - **CS313 Automata Theory and Formal Languages**  
              Formal computation models: Deterministic Finite Automata (DFA), Non-Deterministic Finite Automata (NFA), Regular Expressions, Regular Languages, Context-Free Grammars (CFG), Regular Grammars, Pushdown Automata (PDA), and Turing Machines.  
              *Independent Verification Tool:* **I Will Pass Automata Theory** — closed private verification platform independent from AI.
            - **CS345 Intelligent Systems 1**  
              Foundations of computational intelligence: fuzzy logic, fuzzy inference systems, linguistic variables, and Artificial Neural Networks (ANN).
            - **CSIT212 Quantitative Methods**  
              Applied statistics and probability modeling: Normal distribution, exponential distribution, Poisson distribution, Bayes' theorem, permutations, combinations, Probability Density Functions (PDF), Cumulative Distribution Functions (CDF), and statistical hypothesis analysis.
            - **CSIT321 Applications Development and Emerging Technologies**  
              Modern scalable backend architectures, microservices, cloud deployments, and emerging web technologies.
            - **CSIT327 Information Management 2**  
              Advanced relational database administration: complex SQL querying, indexing, stored procedures, transactions, and hands-on application development using PostgreSQL and MySQL.
            - **ES038 Technopreneurship**  
              Collaborative technology entrepreneurship and startup engineering in a 10-person team:  
              *Capstone Project:* **WattWise** — a software-based energy monitoring system utilizing a simulated smart-breaker environment, eliminating the need for physical hardware.
            """
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
    milestones_data = [
        {"Year": "2023 Q1", "Milestone": "Desktop Collaboration (+inHealth)", "Detail": "Contributed to 5-man team; developed JavaFX UI behavior and nutritional API integration."},
        {"Year": "2023 Q3", "Milestone": "Enterprise Pharmacy Management", "Detail": "Co-engineered PHP/MySQL clinic system featuring automated FEFO batch deduction and audit logs."},
        {"Year": "2023 Q4", "Milestone": "Offline Code Judging Environment", "Detail": "Developed CodeChum++ front-end and test-runner interface in Java Swing for offline lab evaluations."},
        {"Year": "2024 Q1", "Milestone": "Mobile & Native Desktop Development", "Detail": "Built MyRoutine Kotlin habit tracker with widgets and PomodoroTimer SwiftUI macOS menu bar app."},
        {"Year": "2024 Q3", "Milestone": "Productivity Browser Extensions", "Detail": "Released Labelscript (Unicode superscript utility) and YouTube Audio Downloader (yt-dlp + Flask)."},
        {"Year": "2024 Q4", "Milestone": "Automata Verification System", "Detail": "Engineered 'I Will Pass Automata Theory' using TypeScript, Google Auth APIs, and Vercel Serverless."},
    ]
    st.dataframe(pd.DataFrame(milestones_data), use_container_width=True, hide_index=True)

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

skill_col1, skill_col2 = st.columns([1.4, 1], gap="medium")

with skill_col1:
    st.subheader(f"Projects Completed per Stack (>= {min_proj_count} Projects)")
    chart = (
        alt.Chart(filtered_skills)
        .mark_bar(color="#18181B", cornerRadiusTopLeft=3, cornerRadiusTopRight=3)
        .encode(
            x=alt.X("Skill:N", sort=None, title="Technical Stack", axis=alt.Axis(labelAngle=-25, labelLimit=200)),
            y=alt.Y("Projects Built:Q", title="Completed Projects", axis=alt.Axis(tickMinStep=1)),
            tooltip=["Skill", "Category", "Projects Built", "Course Units"],
        )
        .properties(height=300)
    )
    st.altair_chart(chart, use_container_width=True)
    st.caption("Quantified metric: Number of independent software projects and capstones completed per technology.")

with skill_col2:
    st.subheader("Stack Metrics Breakdown")
    st.dataframe(
        filtered_skills[["Skill", "Category", "Projects Built", "Course Units"]],
        use_container_width=True,
        hide_index=True,
    )
    st.write(f"Displaying **{len(filtered_skills)}** of **{len(df_skills)}** technical domains.")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# Projects Showcase Section: Interactive Filters & Cards
# ---------------------------------------------------------
st.markdown('<a id="projects-showcase"></a>', unsafe_allow_html=True)
st.header("Projects Showcase")
st.write("Explore all 8 software projects across theory, browser extensions, mobile, enterprise, and desktop applications.")

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
        or (role_filter == "Team Developer" and ("Team" in p["role"] or "Two-Man" in p["role"] or "5-Man" in p["role"]))
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
                    <p style="font-size: 0.95rem; line-height: 1.5; color: #27272A; margin-bottom: 12px;">
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
                        <p style="font-size: 0.95rem; line-height: 1.5; color: #27272A; margin-bottom: 12px;">
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
st.header("Connect & Feedback")
st.write("Reach out directly via email, connect on LinkedIn, or send a message through the form below.")

contact_col1, contact_col2 = st.columns([1, 1.2], gap="large")

with contact_col1:
    st.subheader("Contact Information")
    st.markdown(
        """
        - **Name:** Mc Cauley Bacalla
        - **Institution:** Cebu Institute of Technology - University
        - **Accreditation:** PACUCOA Level IV accredited
        - **Program & Section:** BS in Computer Science (Year 3) • Section F1
        - **Institutional Email:** [mccauley.bacalla@cit.edu](mailto:mccauley.bacalla@cit.edu)
        - **Personal Email:** [macoybacalla9@gmail.com](mailto:macoybacalla9@gmail.com)
        - **Direct Message:** [Send Email via Gmail Web](https://mail.google.com/mail/?view=cm&fs=1&to=macoybacalla9@gmail.com&su=Hello&body=Hi%20there)
        - **LinkedIn Profile:** [linkedin.com/in/mc-cauley-bacalla-a4274a363](https://www.linkedin.com/in/mc-cauley-bacalla-a4274a363/)
        - **GitHub Profile:** [github.com/sigmacoy](https://github.com/sigmacoy)
        """
    )
    st.info("Actively open for software engineering discussions, academic projects, and professional inquiries.")

with contact_col2:
    st.subheader("Send Feedback / Inquiry")
    with st.form(key="portfolio_feedback_form", clear_on_submit=True):
        sender_name = st.text_input("Your Full Name", placeholder="e.g. Alex Morgan")
        sender_email = st.text_input("Your Email Address", placeholder="e.g. alex@example.com")
        category = st.selectbox(
            "Topic / Category",
            options=["General Inquiry", "Project Discussion", "Software / AI Collaboration", "Academic Discussion"],
        )
        rating = st.slider("Portfolio Rating", min_value=1, max_value=5, value=5, help="1 = Needs Revision, 5 = Excellent")
        message = st.text_area("Your Message or Comments", placeholder="Write your message or project inquiry here...")
        
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
    <div style="border-top: 1px solid #E4E4E7; margin-top: 0.75rem; padding-top: 0.4rem; padding-bottom: 0.1rem; text-align: center;">
        <span style="color: #71717A; font-size: 0.75rem;">
            Mc Cauley Bacalla • BS in Computer Science (Year 3) • Section F1 • Cebu Institute of Technology - University
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)
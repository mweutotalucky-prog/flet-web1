import os
import flet as ft
import threading
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get port from environment variable (Render sets this)
PORT = int(os.getenv("PORT", 8551))

def main(page: ft.Page):

    # =========================================================
    # PAGE SETTINGS (Optimized for Fixed Header Layout)
    # =========================================================
    page.title = "Matheus T Medusalem - Mining Engineering Portfolio | Task Management App"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#f0f7ff"
    page.scroll = None

    # =========================================================
    # MODERN MINING ENGINEERING PALETTE (Blue/Teal/Slate)
    # =========================================================
    PRIMARY_BLUE = "#1a5f7a"           # Deep Mining Blue
    ACCENT_TEAL = "#2c8c6e"            # Safety Green/Teal
    DEEP_SLATE = "#2c3e50"             # Dark slate for text/buttons
    LIGHT_BG = "#f0f7ff"               # Light blue-tint background
    SECTION_BLUE = "#e3f0f5"
    SECTION_DEEP = "#cde5ef"
    BG_WHITE = "#ffffff"
    TEXT_GREY = "#3a5a6e"
    AVATAR_BG = "#e3f0f5"
    SUBTEXT_GREY = "#6b8da8"
    CARD_BG = "#fafeff"
    BORDER_COLOR = "#b8d4e3"
    
    DARK_CARD_BG = "#1a5f7a"
    DARK_TEXT_WHITE = "#ffffff"
    NAV_INACTIVE = "#c5dce8"
    OVERLAY_TEAL = "#2c8c6e"
    PROGRESS_TRACK = "#e3f0f5"
    SHADOW_BLUE = "#b8d4e3"
    CERT_HINT = "#c5dce8"

    # Global variable to track active dialog
    active_dialog = None

    def open_certificate_zoom(title: str, image_file: str):
        global active_dialog
        
        # Create dialog content
        zoom_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(title, color=PRIMARY_BLUE, weight=ft.FontWeight.BOLD),
            content=ft.Container(
                width=900,
                height=620,
                bgcolor=BG_WHITE,
                padding=10,
                border_radius=8,
                content=ft.Image(src=f"/images/{image_file}", fit="contain"),
            ),
            actions=[
                ft.TextButton(
                    "Close", 
                    on_click=lambda e: close_certificate_zoom(),
                    style=ft.ButtonStyle(color=PRIMARY_BLUE)
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        
        active_dialog = zoom_dialog
        page.show_dialog(zoom_dialog)
        page.update()

    def close_certificate_zoom():
        global active_dialog
        if active_dialog:
            active_dialog.open = False
            active_dialog.update()
            active_dialog = None

    def get_uniform_border(width: int, color: str):
        return ft.Border(
            top=ft.BorderSide(width, color),
            bottom=ft.BorderSide(width, color),
            left=ft.BorderSide(width, color),
            right=ft.BorderSide(width, color),
        )

    # =========================================================
    # PREMIUM COMPONENT BUILDERS
    # =========================================================
    def create_section_header(title: str, subtitle: str):
        return ft.Column(
            spacing=8,
            controls=[
                ft.Text(
                    title, 
                    size=28, 
                    weight=ft.FontWeight.BOLD, 
                    color=PRIMARY_BLUE, 
                    style=ft.TextStyle(letter_spacing=1.2)
                ),
                ft.Text(subtitle, size=15, color=TEXT_GREY),
                ft.Container(height=4, width=60, bgcolor=ACCENT_TEAL, border_radius=2),
                ft.Container(height=15)
            ]
        )

    def create_skill_chip(label: str, level: float):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=ft.Padding(16, 12, 16, 12),
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column([
                ft.Row([
                    ft.Text(label, weight=ft.FontWeight.W_600, color=DEEP_SLATE, size=14),
                    ft.Text(f"{int(level*100)}%", weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE, size=12)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                ft.Container(height=6),
                ft.Stack([
                    ft.Container(height=4, bgcolor=PROGRESS_TRACK, border_radius=2, expand=True),
                    ft.Container(height=4, bgcolor=PRIMARY_BLUE, border_radius=2, width=120 * level)
                ])
            ])
        )

    def create_info_card(title: str, body: str, icon=ft.Icons.CHECK_CIRCLE):
        return ft.Container(
            bgcolor=BG_WHITE,
            padding=20,
            border_radius=8,
            border=get_uniform_border(1, BORDER_COLOR),
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row([
                        ft.Icon(icon, color=PRIMARY_BLUE, size=24),
                        ft.Text(title, size=16, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                    ]),
                    ft.Text(body, color=TEXT_GREY, size=13),
                ],
            ),
        )

    # =========================================================
    # NAVIGATION SYSTEM
    # =========================================================
    current_page_key = {"value": "overview"}
    nav_buttons = {}

    def build_page_view(section_control, page_key):
        return ft.Column(
            key=f"page-{page_key}",
            expand=True,
            scroll=ft.ScrollMode.ALWAYS,
            spacing=0,
            controls=[section_control],
        )

    def navigate_to(page_key):
        current_page_key["value"] = page_key
        page_switcher.content = build_page_view(portfolio_pages[page_key], page_key)
        for key, button in nav_buttons.items():
            button.style = ft.ButtonStyle(
                color=BG_WHITE if key == page_key else NAV_INACTIVE,
                overlay_color=OVERLAY_TEAL,
            )
        page.update()

    # =========================================================
    # SECTIONS DEFINITIONS
    # =========================================================
    
    # 1. Overview Section
    hero_section = ft.Container(
        key="overview",
        bgcolor=LIGHT_BG,
        padding=ft.Padding(50, 60, 50, 60),
        content=ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 7},
                    spacing=15,
                    controls=[
                        ft.Text(
                            "MINING ENGINEERING STUDENT @ UNAM ONGWEDIVA CAMPUS", 
                            size=13, 
                            weight=ft.FontWeight.W_600, 
                            color=ACCENT_TEAL, 
                            style=ft.TextStyle(letter_spacing=1.5)
                        ),
                        ft.Text("Matheus T Medusalem", size=42, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                        ft.Text("Student Number: 224061321", size=16, weight=ft.FontWeight.W_500, color=ACCENT_TEAL),
                        ft.Text("Student Developer | Aspiring Mining Engineer", size=14, color=TEXT_GREY, italic=True),
                        ft.Divider(color=PRIMARY_BLUE, thickness=1.5),
                        ft.Text("Phone: +264 81 637 4993  |  Email: matheusmedusalem247@gmail.com", size=14, weight=ft.FontWeight.W_500, color=DEEP_SLATE),
                        ft.Text("GitHub: Group6-ChecklistApp", size=14, weight=ft.FontWeight.W_500, color=DEEP_SLATE),
                        ft.Text("Mining Engineering student specializing in practical workshop experience (Welding, Bricklaying, Electrical systems, Machining, Electronics) and software development for mine safety and operational productivity improvements. This portfolio documents my contributions to the Group6 ChecklistApp - a mobile task management and safety checklist application.", size=16, color=TEXT_GREY),
                        ft.Container(height=10),
                        ft.ElevatedButton(
                            "Download CV (PDF)",
                            icon=ft.Icons.DOWNLOAD,
                            bgcolor=PRIMARY_BLUE,
                            color=BG_WHITE,
                            url="/Matheus T Medusalem CV pdf.pdf",
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
                        ),
                        ft.Container(height=5),
                        ft.TextButton(
                            "View GitHub Repository",
                            icon=ft.Icons.CODE,
                            url="https://github.com/pombilihamwoomo-dot/Group6-ChecklistApp",
                            style=ft.ButtonStyle(color=ACCENT_TEAL),
                        ),
                    ],
                ),
                ft.Column(
                    col={"sm": 12, "md": 5},
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=280,
                            height=280,
                            border_radius=140,
                            bgcolor=AVATAR_BG,
                            alignment=ft.Alignment(0, 0),
                            border=get_uniform_border(4, PRIMARY_BLUE),
                            content=ft.Image(src="/images/profile.jpg.jpeg", width=280, height=280, border_radius=140, fit="cover"),
                        ),
                        ft.Container(height=12),
                        ft.Text("Mining Engineering & Mine Safety Systems 2026", size=12, color=SUBTEXT_GREY, italic=True),
                        ft.Container(
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=8,
                                controls=[
                                    ft.Icon(ft.Icons.SCHOOL, size=14, color=PRIMARY_BLUE),
                                    ft.Text("UNAM Ongwediva Engineering Campus", size=11, color=TEXT_GREY),
                                ]
                            )
                        ),
                    ],
                ),
            ]
        ),
    )

    # 2. Skills Section
    skills_section = ft.Container(
        key="skills",
        bgcolor=SECTION_BLUE,
        padding=40,
        content=ft.Column([
            create_section_header("TECHNICAL SKILLS MATRIX", "Integrated expertise across workshop trades, software development, and mine safety systems."),
            ft.ResponsiveRow([
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Workshop & Practical Skills", weight=ft.FontWeight.BOLD, color=ACCENT_TEAL, size=16),
                    create_skill_chip("Welding", 0.85),
                    create_skill_chip("Bricklaying", 0.82),
                    create_skill_chip("Electrical Systems", 0.88),
                    create_skill_chip("Machining", 0.80),
                    create_skill_chip("Electronics", 0.78),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Software Development", weight=ft.FontWeight.BOLD, color=ACCENT_TEAL, size=16),
                    create_skill_chip("JavaScript", 0.82),
                    create_skill_chip("Python", 0.78),
                    create_skill_chip("React Native", 0.80),
                    create_skill_chip("Firebase", 0.75),
                    create_skill_chip("HTML & CSS", 0.85),
                ]),
                ft.Column(col={"sm": 12, "md": 4}, spacing=10, controls=[
                    ft.Text("Engineering & Design Tools", weight=ft.FontWeight.BOLD, color=ACCENT_TEAL, size=16),
                    create_skill_chip("MATLAB", 0.85),
                    create_skill_chip("AutoCAD", 0.80),
                    create_skill_chip("Git & GitHub", 0.88),
                    create_skill_chip("Canva", 0.82),
                ]),
            ], spacing=20)
        ])
    )

    # 3. Individual Portfolio Reflection Section
    contribution_section = ft.Container(
        key="contribution",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("CHECKLISTAPP - PROJECT MANAGER CONTRIBUTION", "Reflection, evidence, lessons learned, challenges, and showcase material."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Project Management Role",
                                "Led a 16-member team in developing a mobile task management and safety checklist application using React Native and Firebase.",
                                ft.Icons.LEADERBOARD,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Key Responsibilities",
                                "Requirements gathering, task allocation, team coordination, GitHub repository management, version control, React Native development, Firebase integration, quality assurance, stakeholder communication, and progress reporting.",
                                ft.Icons.TASK_ALT,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "What I Learned",
                                "I strengthened my leadership abilities, project coordination skills, and technical expertise in full-stack mobile development while managing a large team under semester constraints.",
                                ft.Icons.LIGHTBULB,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            content=create_info_card(
                                "Challenges Addressed",
                                "Coordinating a 16-member team with varying skill levels was the main challenge. I addressed it through structured task allocation, regular stand-ups, and rigorous GitHub workflow management.",
                                ft.Icons.TROUBLESHOOT,
                            ),
                        ),
                    ],
                ),
                ft.Container(
                    bgcolor=LIGHT_BG,
                    padding=20,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column([
                                ft.Text("Leadership Experience", size=18, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                ft.Text("Choir Chairperson - Developed leadership, organization, and team management skills.", color=TEXT_GREY, size=13),
                            ]),
                            ft.TextButton("Leadership Video", icon=ft.Icons.VIDEO_LIBRARY, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", style=ft.ButtonStyle(color=ACCENT_TEAL)),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 4. Project Timeline Section
    timeline_section = ft.Container(
        key="timeline",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("CHECKLISTAPP PROJECT TIMELINE", "Weekly log of my specific contributions as Project Manager for the semester group project."),
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=25,
                    border_radius=10,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=15,
                        controls=[
                            ft.Text("Week 1-2: Role Assignment & Project Charter", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                            ft.Text("Assigned as Project Manager for Group6 ChecklistApp. Led initial meetings, defined project scope, and contributed to project charter documentation with a 16-member team.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 3-4: Requirements Gathering & Task Allocation", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                            ft.Text("Facilitated requirements gathering sessions with stakeholders, allocated tasks based on team member strengths, and established communication protocols.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 5-6: GitHub Setup & Development Kickoff", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                            ft.Text("Set up GitHub repository structure, implemented branch protection rules, conducted code reviews, and established version control workflow for the entire team.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 7-8: Firebase Integration & Quality Assurance", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                            ft.Text("Led Firebase integration efforts, performed quality assurance testing, coordinated with the Lead Developer on technical decisions, and ensured feature completeness.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Week 9-10: Progress Reporting & Stakeholder Communication", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                            ft.Text("Prepared progress reports for stakeholders, facilitated team presentations, and coordinated final development sprint for feature completion.", color=TEXT_GREY),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("Final Week: Documentation & Final Project Delivery", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                            ft.Text("Compiled project documentation, collected evidence of contributions, delivered final presentation, and submitted the completed ChecklistApp.", color=TEXT_GREY),
                        ],
                    ),
                ),
            ],
        ),
    )

    # 5. Projects Section
    project_section = ft.Container(
        key="projects",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("CHECKLISTAPP - MOBILE TASK MANAGEMENT SYSTEM", "Core features and project management achievements."),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("1. Task Management System", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                                    ft.Text("Mobile application for task creation, assignment, tracking, and completion with real-time updates and safety checklist integration.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("TECHNICAL SPECIFICATIONS:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                            ft.Text("• Frontend: React Native with TypeScript", size=12, font_family="monospace", color=PRIMARY_BLUE),
                                            ft.Text("• Backend: Firebase Firestore DB", size=12, font_family="monospace", color=PRIMARY_BLUE),
                                            ft.Text("• Authentication: Firebase Auth", size=12, font_family="monospace", color=PRIMARY_BLUE),
                                            ft.Text("• Push Notifications: Firebase Cloud Messaging", size=12, font_family="monospace", color=PRIMARY_BLUE),
                                        ])
                                    ),
                                    ft.Text("Enables teams to manage tasks efficiently with built-in safety checklists and real-time collaboration features.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("React Native", size=11, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Firebase", size=11, color=BG_WHITE), bgcolor=ACCENT_TEAL, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=CARD_BG,
                            padding=25,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("2. Safety Checklist Module", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                                    ft.Text("Pre-configured safety checklists for mining operations with completion tracking, compliance verification, and audit logging.", color=TEXT_GREY, size=14),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=12,
                                        border_radius=6,
                                        content=ft.Column([
                                            ft.Text("SAFETY FEATURES:", size=11, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                            ft.Text("• Dynamic checklist generation", size=12, font_family="monospace", color=PRIMARY_BLUE),
                                            ft.Text("• Compliance scoring system", size=12, font_family="monospace", color=PRIMARY_BLUE),
                                            ft.Text("• Real-time audit trail", size=12, font_family="monospace", color=PRIMARY_BLUE),
                                            ft.Text("• Offline mode support", size=12, font_family="monospace", color=PRIMARY_BLUE),
                                        ])
                                    ),
                                    ft.Text("Improves operational safety through structured checklist enforcement and detailed compliance reporting.", color=TEXT_GREY, size=12),
                                    ft.Row([
                                        ft.Container(content=ft.Text("Safety First", size=11, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=5, border_radius=4),
                                        ft.Container(content=ft.Text("Compliance", size=11, color=DEEP_SLATE), bgcolor=LIGHT_BG, padding=5, border_radius=4),
                                    ])
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 6. Technical Blog Section with videos
    blog_section = ft.Container(
        key="blog",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("TECHNICAL BLOG: MINING ENGINEERING CONCEPTS", "Written technical explanations with embedded video content."),
                
                # First Blog Post with Video
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=22,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Text("Mine Ventilation Principles", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                            ft.Text("Proper airflow management is critical for underground mine safety, controlling dust, temperature, and hazardous gas concentrations.", color=TEXT_GREY, size=13),
                            ft.Container(
                                bgcolor=LIGHT_BG,
                                padding=14,
                                border_radius=6,
                                content=ft.Text("Q = A × v   |   P = ρ × g × h", font_family="monospace", size=14, color=PRIMARY_BLUE),
                            ),
                            ft.Text("Where Q is airflow (m³/s), A is cross-sectional area (m²), v is air velocity (m/s), P is pressure (Pa), ρ is air density (kg/m³), g is gravity (m/s²), and h is height difference (m).", color=TEXT_GREY, size=13),
                            
                            # Embedded Video
                            ft.Container(
                                height=250,
                                border_radius=8,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                bgcolor=PRIMARY_BLUE,
                                content=ft.Video(
                                    playlist=ft.VideoMedia(
                                        src="https://www.youtube.com/watch?v=7d9KfKQ-4rM",
                                        title="Mine Ventilation Principles Explained"
                                    ),
                                    autoplay=False,
                                    show_controls=True,
                                    aspect_ratio=16/9,
                                    expand=True,
                                ),
                            ),
                            ft.Text("Watch this video to understand how mine ventilation systems work and why they're crucial for underground safety.", color=TEXT_GREY, size=12, italic=True),
                        ],
                    ),
                ),
                
                # Second Blog Post with Video
                ft.Container(
                    bgcolor=BG_WHITE,
                    padding=22,
                    border_radius=8,
                    border=get_uniform_border(1, BORDER_COLOR),
                    content=ft.Column(
                        spacing=12,
                        controls=[
                            ft.Text("Software Testing for Safety Systems", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                            ft.Text("In the ChecklistApp project, structured testing methodologies ensured that safety checklists functioned correctly under various conditions.", color=TEXT_GREY, size=13),
                            ft.Container(
                                bgcolor=LIGHT_BG,
                                padding=14,
                                border_radius=6,
                                content=ft.Text("Test Coverage = (Lines Tested / Total Lines) × 100%", font_family="monospace", size=14, color=PRIMARY_BLUE),
                            ),
                            ft.Text("Comprehensive testing strategies include unit testing, integration testing, user acceptance testing, and regression testing for reliable safety features.", color=TEXT_GREY, size=13),
                            
                            # Embedded Video
                            ft.Container(
                                height=250,
                                border_radius=8,
                                clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                bgcolor=PRIMARY_BLUE,
                                content=ft.Video(
                                    playlist=ft.VideoMedia(
                                        src="https://www.youtube.com/watch?v=4f7LpW2bP7w",
                                        title="Software Testing Best Practices for Safety Systems"
                                    ),
                                    autoplay=False,
                                    show_controls=True,
                                    aspect_ratio=16/9,
                                    expand=True,
                                ),
                            ),
                            ft.Text("Learn about software testing methodologies essential for safety-critical applications like the ChecklistApp.", color=TEXT_GREY, size=12, italic=True),
                        ],
                    ),
                ),
                
                # Third Blog Post with Video
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Rock Mechanics Fundamentals", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                                    ft.Text("Understanding rock behavior under stress is essential for designing safe underground excavations and preventing collapses.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("σ = F/A  |  ε = ΔL/L", font_family="monospace", size=14, color=PRIMARY_BLUE),
                                    ),
                                    ft.Text("Where σ is stress (MPa), F is force (N), A is area (mm²), ε is strain, ΔL is change in length (m), and L is original length (m).", color=TEXT_GREY, size=13),
                                    
                                    # Embedded Video
                                    ft.Container(
                                        height=200,
                                        border_radius=8,
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                        bgcolor=PRIMARY_BLUE,
                                        content=ft.Video(
                                            playlist=ft.VideoMedia(
                                                src="https://www.youtube.com/watch?v=PtF7BlK0vKw",
                                                title="Rock Mechanics in Mining Engineering"
                                            ),
                                            autoplay=False,
                                            show_controls=True,
                                            aspect_ratio=16/9,
                                            expand=True,
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=22,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Text("Safety Management Systems", size=18, weight=ft.FontWeight.BOLD, color=ACCENT_TEAL),
                                    ft.Text("Implementing effective safety management systems reduces workplace incidents and improves operational efficiency.", color=TEXT_GREY, size=13),
                                    ft.Container(
                                        bgcolor=LIGHT_BG,
                                        padding=14,
                                        border_radius=6,
                                        content=ft.Text("Risk Score = Probability × Severity", font_family="monospace", size=14, color=PRIMARY_BLUE),
                                    ),
                                    ft.Text("Risk assessment involves identifying hazards, evaluating risks, implementing controls, and monitoring effectiveness for continuous improvement.", color=TEXT_GREY, size=13),
                                    
                                    # Embedded Video
                                    ft.Container(
                                        height=200,
                                        border_radius=8,
                                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                                        bgcolor=PRIMARY_BLUE,
                                        content=ft.Video(
                                            playlist=ft.VideoMedia(
                                                src="https://www.youtube.com/watch?v=wXhOgK4KiRw",
                                                title="Safety Management in Mining Operations"
                                            ),
                                            autoplay=False,
                                            show_controls=True,
                                            aspect_ratio=16/9,
                                            expand=True,
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                ),
            ],
        ),
    )

    # 7. Experience / Leadership Section
    leadership_section = ft.Container(
        key="experience",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("LEADERSHIP & PRACTICAL EXPERIENCE", "Active contributions to student leadership and practical workshop experience."),
                ft.Text("Bridging academic mining theory with hands-on workshop experience while leading teams in software development projects.", size=15, color=TEXT_GREY),
                ft.ResponsiveRow(
                    spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.WORKSPACE_PREMIUM, color=PRIMARY_BLUE, size=28),
                                ft.Text("Choir Chairperson", size=16, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                ft.Text("Led choir activities, organized rehearsals, managed team dynamics, and coordinated performances. Developed strong leadership, communication, and organizational skills.", color=TEXT_GREY, size=13),
                                ft.Text("• Team management of 20+ members", size=12, color=TEXT_GREY),
                                ft.Text("• Event coordination and planning", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.SCIENCE, color=PRIMARY_BLUE, size=28),
                                ft.Text("Workshop Practical Experience", size=16, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                ft.Text("Hands-on experience in welding, bricklaying, electrical systems, machining, and electronics from technical training and coursework.", color=TEXT_GREY, size=13),
                                ft.Text("• Structural welding and fabrication", size=12, color=TEXT_GREY),
                                ft.Text("• Electrical circuit installation", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.CODE, color=PRIMARY_BLUE, size=28),
                                ft.Text("GitHub Repository Manager", size=16, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                ft.Text("Managed GitHub repository for 16-member team, established version control protocols, conducted code reviews, and maintained workflow efficiency.", color=TEXT_GREY, size=13),
                                ft.Text("• Branch protection rules", size=12, color=TEXT_GREY),
                                ft.Text("• Pull request management", size=12, color=TEXT_GREY),
                            ])
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=8,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column([
                                ft.Icon(ft.Icons.GRADIENT, color=PRIMARY_BLUE, size=28),
                                ft.Text("MATLAB & Engineering Software", size=16, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                ft.Text("Completed MATLAB certifications with 100% scores. Proficient in AutoCAD, Canva, and engineering design tools for mining applications.", color=TEXT_GREY, size=13),
                                ft.Text("• 7 MATLAB certifications completed", size=12, color=TEXT_GREY),
                                ft.Text("• AutoCAD for mining layouts", size=12, color=TEXT_GREY),
                            ])
                        ),
                    ]
                )
            ]
        )
    )

    # 8. MATLAB Achievement Hub Section
    certificate_data = [
        {"title": "MATLAB Onramp", "file": "Matlab onramp certificate_page-0001.jpg"},
        {"title": "Simulink Onramp", "file": "Simulink onramp certificate_page-0001.jpg"},
        {"title": "Explore Data with MATLAB Plots", "file": "Explore data with matlab plotscertificate_page-0001.jpg"},
        {"title": "Calculations with Vectors and Matrices", "file": "Calculations with vectors and matrices certificate_page-0001.jpg"},
        {"title": "Make and Manipulate Matrices", "file": "Make and manipulate matrices certificate_page-0001.jpg"},
        {"title": "Signal Segmentation with Deep Learning", "file": "Signal segmentation with deep learning certificate_page-0001.jpg"},
        {"title": "The How and Why of Writing Functions", "file": "The how and why of writing functions certificate_page-0001.jpg"},
    ]

    cert_cards = []
    for cert in certificate_data:
        img_control = ft.Image(
            src=f"/images/{cert['file']}",
            height=150,
            fit="contain", 
            scale=1.0,
            animate_scale=ft.Animation(400, ft.AnimationCurve.EASE_OUT),
        )

        card_design = ft.Container(
            bgcolor=DARK_CARD_BG,
            padding=15,
            border_radius=10,
            border=get_uniform_border(1, ACCENT_TEAL),
            on_click=lambda e, title=cert["title"], file=cert["file"]: open_certificate_zoom(title, file),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        height=150,
                        width=320,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        border_radius=6,
                        bgcolor=BG_WHITE,
                        alignment=ft.Alignment(0, 0),
                        content=img_control,
                    ),
                    ft.Container(height=6),
                    ft.Text(cert["title"], weight=ft.FontWeight.BOLD, color=DARK_TEXT_WHITE, text_align=ft.TextAlign.CENTER, size=13, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS),
                    ft.Text("Click to zoom", color=CERT_HINT, size=11, text_align=ft.TextAlign.CENTER),
                ],
            ),
        )

        hover_stack = ft.Stack(
            height=230,
            controls=[
                ft.Container(top=10, left=0, right=0, animate_position=ft.Animation(300, ft.AnimationCurve.EASE_OUT), content=card_design)
            ]
        )

        def make_hover_handler(stack_wrapper, target_img):
            inner_move_container = stack_wrapper.controls[0]
            def handle_hover(e):
                if e.data == "true":
                    inner_move_container.top = 0  
                    inner_move_container.shadow = ft.BoxShadow(blur_radius=12, color=ACCENT_TEAL)
                    target_img.scale = 1.05  
                else:
                    inner_move_container.top = 10  
                    inner_move_container.shadow = None
                    target_img.scale = 1.0
                inner_move_container.update()
                target_img.update()
            return handle_hover

        card_design.on_hover = make_hover_handler(hover_stack, img_control)
        cert_cards.append(ft.Container(col={"sm": 12, "md": 4}, content=hover_stack))

    certification_section = ft.Container(
        key="certificates",
        bgcolor=SECTION_DEEP,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                create_section_header("MATLAB ACHIEVEMENT HUB", "Proof of completion for MATLAB and Simulink courses - All completed with 100%."),
                ft.Text("Click any certificate to zoom in and inspect the completion proof clearly.", size=13, color=SUBTEXT_GREY),
                ft.ResponsiveRow(spacing=20, run_spacing=10, controls=cert_cards),
            ],
        ),
    )

    # 9. GitHub Evidence & Documentation Section
    github_section = ft.Container(
        key="github",
        bgcolor=LIGHT_BG,
        padding=40,
        content=ft.Column(
            spacing=20,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column([
                            ft.Text("GITHUB EVIDENCE & DOCUMENTATION", size=28, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                            ft.Text("Verifiable individual contribution records for the ChecklistApp semester project team.", size=15, color=TEXT_GREY),
                        ]),
                        ft.IconButton(icon=ft.Icons.CODE, icon_color=PRIMARY_BLUE, tooltip="GitHub Evidence", url="https://github.com/pombilihamwoomo-dot/Group6-ChecklistApp")
                    ]
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Commit History",
                                "Screenshots showing commits authored by Matheus T Medusalem for project planning, code reviews, and documentation.",
                                ft.Icons.COMMIT,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Pull Request Logs",
                                "Document code reviews performed, merge approvals, and repository management activities for the 16-member team.",
                                ft.Icons.MERGE,
                            ),
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 4},
                            content=create_info_card(
                                "Impact Summary",
                                "My project management and technical contributions ensured on-time delivery, code quality, and comprehensive documentation for the ChecklistApp.",
                                ft.Icons.INSIGHTS,
                            ),
                        ),
                    ],
                ),
                ft.ResponsiveRow(
                    spacing=20,
                    run_spacing=20,
                    controls=[
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.CHECKLIST, color=PRIMARY_BLUE), ft.Text("Group6-ChecklistApp", size=16, weight=ft.FontWeight.BOLD, color=DEEP_SLATE)]),
                                    ft.Text("Mobile task management and safety checklist application built with React Native and Firebase for team productivity and operational safety.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("React Native", size=10, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Firebase", size=10, color=BG_WHITE), bgcolor=ACCENT_TEAL, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Task Management", size=10, color=DEEP_SLATE), bgcolor=LIGHT_BG, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("16 Member Team", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Repository", style=ft.ButtonStyle(color=ACCENT_TEAL), url="https://github.com/pombilihamwoomo-dot/Group6-ChecklistApp")
                                    ])
                                ]
                            )
                        ),
                        ft.Container(
                            col={"sm": 12, "md": 6},
                            bgcolor=BG_WHITE,
                            padding=20,
                            border_radius=10,
                            border=get_uniform_border(1, BORDER_COLOR),
                            content=ft.Column(
                                spacing=12,
                                controls=[
                                    ft.Row([ft.Icon(ft.Icons.DESCRIPTION, color=PRIMARY_BLUE), ft.Text("Project Documentation", size=16, weight=ft.FontWeight.BOLD, color=DEEP_SLATE)]),
                                    ft.Text("Comprehensive project documentation including requirements, design specifications, test plans, and final delivery evidence.", size=13, color=TEXT_GREY),
                                    ft.Row(wrap=True, spacing=5, controls=[
                                        ft.Container(content=ft.Text("Documentation", size=10, color=BG_WHITE), bgcolor=PRIMARY_BLUE, padding=4, border_radius=4),
                                        ft.Container(content=ft.Text("Evidence", size=10, color=BG_WHITE), bgcolor=ACCENT_TEAL, padding=4, border_radius=4),
                                    ]),
                                    ft.Divider(color=BORDER_COLOR),
                                    ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, controls=[
                                        ft.Text("PDF Available", size=11, color=SUBTEXT_GREY),
                                        ft.TextButton("View Documentation", style=ft.ButtonStyle(color=ACCENT_TEAL))
                                    ])
                                ]
                            )
                        ),
                    ],
                ),
            ],
        ),
    )

    # 10. Advanced Contact Section
    name_field = ft.TextField(
        label="Your Full Name",
        border_color=PRIMARY_BLUE,
        focused_border_color=ACCENT_TEAL,
        text_style=ft.TextStyle(color=DEEP_SLATE)
    )
    email_field = ft.TextField(
        label="Email Address",
        border_color=PRIMARY_BLUE,
        focused_border_color=ACCENT_TEAL,
        text_style=ft.TextStyle(color=DEEP_SLATE)
    )
    subject_field = ft.Dropdown(
        label="Subject (Reason for Contact)",
        border_color=PRIMARY_BLUE,
        focused_border_color=ACCENT_TEAL,
        options=[
            ft.dropdown.Option("Project Collaboration"),
            ft.dropdown.Option("ChecklistApp Inquiry"),
            ft.dropdown.Option("Mining Engineering Opportunity"),
            ft.dropdown.Option("Internship/Job Opportunity"),
            ft.dropdown.Option("Technical Question"),
            ft.dropdown.Option("Other"),
        ],
        text_style=ft.TextStyle(color=DEEP_SLATE)
    )
    message_field = ft.TextField(
        label="Detailed Message",
        multiline=True,
        min_lines=5,
        max_lines=8,
        border_color=PRIMARY_BLUE,
        focused_border_color=ACCENT_TEAL,
        text_style=ft.TextStyle(color=DEEP_SLATE)
    )
    consent_checkbox = ft.Checkbox(
        label="I consent to having Matheus T Medusalem store my submitted information for the purpose of responding to my inquiry.",
        fill_color=PRIMARY_BLUE,
        check_color=BG_WHITE,
        value=False
    )

    def handle_submit_message(e):
        # Validation
        if not name_field.value or not email_field.value or not message_field.value or not subject_field.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please fill out all required fields (Name, Email, Subject, and Message)."),
                    bgcolor=ACCENT_TEAL,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        elif "@" not in email_field.value or "." not in email_field.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please enter a valid email address."),
                    bgcolor=ACCENT_TEAL,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        elif not consent_checkbox.value:
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text("Please consent to the data storage policy before submitting."),
                    bgcolor=ACCENT_TEAL,
                    action="Close",
                    action_color=BG_WHITE
                )
            )
        else:
            # Simulate sending message
            page.show_snack_bar(
                ft.SnackBar(
                    content=ft.Text(f"Thank you {name_field.value}! Your message regarding '{subject_field.value}' has been received. I'll respond to {email_field.value} soon."),
                    bgcolor=PRIMARY_BLUE,
                    action="Dismiss",
                    action_color=BG_WHITE,
                    duration=5000
                )
            )
            # Clear form after submission
            name_field.value = ""
            email_field.value = ""
            subject_field.value = None
            message_field.value = ""
            consent_checkbox.value = False
            page.update()

    def clear_form():
        name_field.value = ""
        email_field.value = ""
        subject_field.value = None
        message_field.value = ""
        consent_checkbox.value = False
        page.update()
        page.show_snack_bar(
            ft.SnackBar(
                content=ft.Text("Form cleared successfully."),
                bgcolor=PRIMARY_BLUE,
                action="Close",
                action_color=BG_WHITE
            )
        )

    contact_section = ft.Container(
        key="contact",
        bgcolor=BG_WHITE,
        padding=40,
        content=ft.Column([
            create_section_header("GET IN TOUCH", "Collaborate on mining engineering projects, ChecklistApp development, or research opportunities."),
            ft.ResponsiveRow(
                spacing=30,
                controls=[
                    ft.Column(
                        col={"sm": 12, "md": 5},
                        spacing=20,
                        controls=[
                            ft.Text("Available for mining engineering consultation, software development collaborations, and research opportunities in mine safety and operational productivity.", color=TEXT_GREY, size=15),
                            ft.Divider(color=BORDER_COLOR),
                            ft.Text("📍 Namibia (UNAM Ongwediva Engineering Campus)", color=DEEP_SLATE, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("✉️ matheusmedusalem247@gmail.com", color=DEEP_SLATE, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("📱 +264 81 637 4993", color=DEEP_SLATE, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("🐙 Group6-ChecklistApp", color=DEEP_SLATE, weight=ft.FontWeight.W_500, size=14),
                            ft.Text("⏱ Response time: 24-48 hours", color=TEXT_GREY, size=13),
                            ft.Card(
                                elevation=2,
                                content=ft.Container(
                                    bgcolor=SECTION_BLUE,
                                    padding=15,
                                    border_radius=8,
                                    content=ft.Column([
                                        ft.Text("Preferred Contact Methods:", weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                        ft.Text("• Email for project proposals", size=13, color=TEXT_GREY),
                                        ft.Text("• LinkedIn for professional networking", size=13, color=TEXT_GREY),
                                        ft.Text("• Phone for urgent matters", size=13, color=TEXT_GREY),
                                    ])
                                )
                            )
                        ]
                    ),
                    ft.Container(
                        col={"sm": 12, "md": 7},
                        bgcolor=CARD_BG,
                        padding=30,
                        border_radius=12,
                        border=get_uniform_border(1, BORDER_COLOR),
                        content=ft.Column(
                            spacing=20,
                            controls=[
                                ft.Text("Send a Message About ChecklistApp or Collaboration", size=18, weight=ft.FontWeight.BOLD, color=DEEP_SLATE),
                                name_field,
                                email_field,
                                subject_field,
                                message_field,
                                consent_checkbox,
                                ft.Divider(color=BORDER_COLOR),
                                ft.Row([
                                    ft.ElevatedButton(
                                        "Submit Message",
                                        icon=ft.Icons.SEND,
                                        bgcolor=PRIMARY_BLUE,
                                        color=BG_WHITE,
                                        on_click=handle_submit_message,
                                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6))
                                    ),
                                    ft.TextButton(
                                        "Clear Form",
                                        on_click=lambda e: clear_form(),
                                        style=ft.ButtonStyle(color=ACCENT_TEAL)
                                    )
                                ], alignment=ft.MainAxisAlignment.END)
                            ]
                        )
                    )
                ]
            )
        ])
    )

    portfolio_pages = {
        "overview": hero_section,
        "skills": skills_section,
        "contribution": contribution_section,
        "timeline": timeline_section,
        "projects": project_section,
        "blog": blog_section,
        "experience": leadership_section,
        "certificates": certification_section,
        "github": github_section,
        "contact": contact_section,
    }

    page_switcher = ft.AnimatedSwitcher(
        content=build_page_view(hero_section, "overview"),
        duration=220,
        reverse_duration=160,
        switch_in_curve=ft.AnimationCurve.EASE_OUT,
        switch_out_curve=ft.AnimationCurve.EASE_IN,
        transition=ft.AnimatedSwitcherTransition.FADE,
        expand=True,
    )

    def make_nav_button(label, page_key):
        button = ft.TextButton(
            label,
            style=ft.ButtonStyle(
                color=BG_WHITE if page_key == current_page_key["value"] else NAV_INACTIVE,
                overlay_color=OVERLAY_TEAL,
            ),
            on_click=lambda e, target=page_key: navigate_to(target),
        )
        nav_buttons[page_key] = button
        return button

    # =========================================================
    # STICKY NAVBAR PANEL
    # =========================================================
    header_navbar = ft.Container(
        bgcolor=PRIMARY_BLUE,
        padding=ft.Padding(40, 15, 40, 15),
        border=ft.Border(bottom=ft.BorderSide(1, ACCENT_TEAL)),
        shadow=ft.BoxShadow(blur_radius=10, color=SHADOW_BLUE, offset=ft.Offset(0, 2)),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Row([
                    ft.Container(width=12, height=12, bgcolor=BG_WHITE, border_radius=6),
                    ft.Text("MATHEUS T MEDUSALEM", weight=ft.FontWeight.BOLD, size=16, color=BG_WHITE, style=ft.TextStyle(letter_spacing=1.1))
                ], spacing=10),
                ft.Row([
                    make_nav_button("Overview", "overview"),
                    make_nav_button("Skills", "skills"),
                    make_nav_button("Portfolio", "contribution"),
                    make_nav_button("Timeline", "timeline"),
                    make_nav_button("Projects", "projects"),
                    make_nav_button("Blog", "blog"),
                    make_nav_button("Experience", "experience"),
                    make_nav_button("MATLAB Hub", "certificates"),
                    make_nav_button("GitHub", "github"),
                    make_nav_button("Contact", "contact"),
                ], spacing=10, wrap=True)
            ]
        )
    )

    # =========================================================
    # RENDER DIRECT TO MAIN PAGE WINDOW
    # =========================================================
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[
                header_navbar,
                page_switcher
            ]
        )
    )

if __name__ == "__main__":
    try:
        ft.app(
            target=main,
            host="0.0.0.0",  # Listen on all interfaces for Render
            port=PORT,
            view=ft.AppView.WEB_BROWSER,
            assets_dir="assets",
        )
    except Exception as e:
        print(f"Error: {e}", flush=True)
        import traceback
        traceback.print_exc()
"""All portfolio content lives here. Edit this file; never the HTML."""

PROFILE = {
    "name": "Camille C. Contemprato",
    "title": "IT Support & Application Support Specialist",
    "tagline": (
        "Three years keeping enterprise devices, systems, and data running "
        "for the people who rely on them."
    ),
    "location": "Biñan City, Laguna, Philippines",
    "stack": ["Python", "Java", "C#"],
    "bio": [
        "I'm an IT support specialist with 3+ years of experience across service "
        "desk operations, end-user support, and live production systems. I've "
        "managed high-volume ticket queues with strict SLA targets, enrolled and "
        "secured devices with Microsoft Intune, and supported web-based HRIS "
        "applications for multiple enterprise clients.",
        "I enjoy finding the root cause of a problem, writing Python code to "
        "automate fixes, and documenting solutions so the next person can resolve "
        "issues faster. I hold an ITIL Foundation certification and a BS in "
        "Information Technology from Cavite State University.",
    ],
    "contact_blurb": (
        "I'm open to IT support, service desk, and application support roles. "
        "The fastest way to reach me is email."
    ),
    "github": "https://github.com/xXxNyxXxxx",
    "linkedin": "https://linkedin.com/in/camille-contemprato",
    "email": "millecontemprato02@gmail.com",
}

SKILLS = {
    "IT support": [
        "Windows, basic macOS & Linux",
        "Hardware & software troubleshooting",
        "Device setup & deployment",
        "Preventive maintenance",
        "TeamViewer & AnyDesk",
        "Basic networking (IP, DNS)",
    ],
    "Service desk & access": [
        "Ivanti ticketing",
        "Incident logging & escalation",
        "SLA compliance",
        "IT asset management (ITAMS)",
        "Active Directory (basic)",
        "Password resets & user provisioning",
    ],
    "Enterprise platforms": [
        "Microsoft 365",
        "Microsoft Intune (MDM)",
        "ManageEngine",
        "Trellix & Duo",
        "Forescout",
        "PowerShell scripts",
    ],
    "Data & business systems": [
        "SQL (CRUD, joins)",
        "Data validation & migration",
        "HRIS: Payroll, Employee Records, Attendance",
        "Microsoft Excel",
    ],
    "Development": [
        "HTML, CSS, Bootstrap",
        "JavaScript",
        "Java, C#, ASP.NET, Python",
        "Spring Boot, Node.js, React, Flask",
        "Git & GitHub",
    ],
    "Documentation & process": [
        "Process flows & workflows",
        "User guides & manuals",
        "Requirements gathering",
        "User training",
    ],
}

# Work projects are described without client names. Add a "github" or "live"
# URL only when a public link exists; the page hides buttons for empty values.
PROJECTS = [
    {
        "id": "hris-implementation",
        "title": "HRIS System Implementation",
        "summary": "Payroll, employee records, and attendance modules configured to client requirements.",
        "description": (
            "Supported web-based HRIS applications from business planning through "
            "deployment to live production, configuring each module around the "
            "client's own requirements."
        ),
        "highlights": [
            "Implemented Payroll, Employee Records, and Attendance modules",
            "Gathered business requirements and translated them into system configurations",
            "Ran test cases before and after deployment to confirm stability",
            "Delivered user training and client-facing demonstrations",
        ],
        "tech": ["HRIS", "SQL", "Web applications", "Documentation"],
        "github": None,
        "live": None,
        "featured": True,
    },
    {
        "id": "sql-data-migration",
        "title": "SQL Data Migration & Cleanup",
        "summary": "Migrating, validating, and correcting records in live production databases.",
        "description": (
            "Handled data corrections and migration work across HR and payroll "
            "systems, focused on keeping production data accurate and consistent."
        ),
        "highlights": [
            "Wrote SQL queries (CRUD operations and joins) for updates and corrections",
            "Analysed discrepancies between HR and payroll data",
            "Validated records after changes to protect data integrity",
        ],
        "tech": ["SQL", "Data validation", "Data migration"],
        "github": None,
        "live": None,
        "featured": True,
    },
    {
        "id": "production-support",
        "title": "Multi-Client Production Support",
        "summary": "Resolving live-system issues for several enterprise clients under tight deadlines.",
        "description": (
            "Provided ongoing support for live systems and client databases, "
            "working to resolve issues quickly and keep downtime low."
        ),
        "highlights": [
            "Supported multiple enterprise clients at the same time",
            "Identified root causes and delivered fixes with minimal supervision",
            "Wrote technical documentation to speed up later support work",
        ],
        "tech": ["Production support", "SQL", "Troubleshooting", "Documentation"],
        "github": None,
        "live": None,
        "featured": True,
    },
    {
        "id": "device-and-access-management",
        "title": "Enterprise Device & Access Management",
        "summary": "Securing and deploying to company devices with Intune, Trellix, Duo, and ManageEngine.",
        "description": (
            "As a service desk analyst, I managed how company devices were "
            "configured, secured, and supplied with software."
        ),
        "highlights": [
            "Enforced security policies and device compliance through Microsoft Intune",
            "Administered Trellix and Duo for endpoint protection and secure sign-in",
            "Deployed applications remotely with ManageEngine",
            "Ran PowerShell scripts for Microsoft 365 and Intune provisioning tasks",
        ],
        "tech": ["Intune", "Microsoft 365", "Trellix", "Duo", "ManageEngine", "PowerShell"],
        "github": None,
        "live": None,
        "featured": True,
    },
    {
        "id": "service-desk-operations",
        "title": "Service Desk Operations",
        "summary": "High-volume ticket handling across chat, email, and phone with strict SLAs.",
        "description": (
            "Delivered Level 1 and 2 support for hardware, software, and network "
            "issues, keeping tickets prioritised and within SLA."
        ),
        "highlights": [
            "Managed and prioritised the ticket queue in Ivanti",
            "Supported users by chat, email, inbound calls, TeamViewer, and AnyDesk",
            "Tracked IT assets in ITAMS and submitted regular service and asset reports",
            "Documented incidents and fixes to grow the knowledge base",
        ],
        "tech": ["Ivanti", "SLA management", "ITAMS", "Remote support"],
        "github": None,
        "live": None,
        "featured": True,
    },
    {
        "id": "portfolio-website",
        "title": "This Portfolio Website",
        "summary": "A Flask site where all content lives in one Python data file.",
        "description": (
            "A responsive dark-mode portfolio built with Flask and Jinja2. Pages "
            "are generated from a single data file, so adding a project needs no "
            "HTML changes."
        ),
        "highlights": [
            "Dynamic project pages through slug-based routing",
            "Secrets kept in environment variables, debug off in production",
            "Version-controlled on GitHub and deployed to a live host",
        ],
        "tech": ["Python", "Flask", "Jinja2", "Bootstrap 5", "Git"],
        "github": "https://github.com/xXxNyxXxxx/portfolio",
        "live": "https://camille-portfolio.onrender.com",
        "featured": True,
    },
]

EXPERIENCE = [
    {
        "role": "Service Desk Analyst",
        "company": "Trends Group Inc.",
        "period": "October 2024 to April 2026",
        "points": [
            "Handled high-volume Level 1 and 2 tickets in Ivanti across chat, email, and calls, keeping to SLA targets",
            "Managed devices with Microsoft Intune and administered Trellix and Duo for security and sign-in",
            "Deployed software remotely with ManageEngine and ran PowerShell scripts for Microsoft 365 and Intune tasks",
            "Tracked IT assets in ITAMS and submitted regular service and asset reports",
            "Carried out preventive maintenance and component-level hardware checks on laptops and desktops",
        ],
    },
    {
        "role": "Junior Application Specialist",
        "company": "ACLT Computing Inc.",
        "period": "July 2023 to March 2024",
        "points": [
            "Supported web-based HRIS applications from planning through live production",
            "Implemented Payroll, Employee Records, and Attendance modules to client requirements",
            "Wrote SQL queries for data corrections and validation, and analysed HR and payroll discrepancies",
            "Provided production support under tight deadlines and ran test cases before and after deployment",
            "Wrote user guides and process flows, and delivered user training and client demonstrations",
        ],
    },
    {
        "role": "IT Support Specialist",
        "company": "Philippine Industrial Equipment Technical Institute Inc.",
        "period": "March 2021 to December 2022",
        "points": [
            "Provided on-site and remote IT support for hardware, software, and basic network issues",
            "Delivered Level 1 and 2 support for BSRS, a TESDA-accredited system, to staff and instructors",
            "Built, configured, and maintained desktops and laptops, including upgrades and preventive maintenance",
            "Helped non-technical staff and instructors get comfortable with mobile devices and applications",
            "Assisted with basic CCTV monitoring and troubleshooting",
        ],
    },
]

CREDENTIALS = [
    {"name": "ITIL Foundation Certification", "detail": ""},
    {
        "name": "BS in Information Technology",
        "detail": "Cavite State University, Carmona Campus (2017 to 2022)",
    },
]
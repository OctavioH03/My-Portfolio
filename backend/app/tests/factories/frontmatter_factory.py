from datetime import date

def general_frontmatter_factory(**overrides: dict) -> dict:
    base_content = {
        "id": "resume",
        "section": "resume",
        "title": "Resume",
        "last_reviewed": date(2026, 5, 25),
        "tags": ["resume"],
        "related": ["bio", "airise", "jj_internship", "os_kernel", "github_insights_tool", "better_sense", "contact"],
        "summary": "Dense factual resume content for grounded answers about credentials and skills."
    }
    return {**base_content, **overrides}

def experience_frontmatter_factory(**overrides: dict) -> dict:
    base_content = {
        "id": "jj_internship",
        "section": "experience",
        "title": "Johnson & Johnson",
        "last_reviewed": date(2026, 5, 25),
        "organization": "Johnson & Johnson",
        "location": "New Brunswick, NJ",
        "employment_type": "Intern",
        "date_start": date(2025, 5, 1),
        "date_end": date(2025, 8, 1),
        "stack": ["Python", "SQL", "Oracle", "Multithreading"],
        "skills": ["Problem Solving", "Communication", "Teamwork", "Leadership"],
        "tags": ["experience"],
        "related": [],
        "summary": "Built an end-to-end Python automation pipeline for J&J's ERP Application Maintenance and Automation team that parsed, embedded, and clustered 400+ OMP log files daily — reducing log noise by 99% and increasing throughput 4x via multithreading."
    }
    return {**base_content, **overrides}

def project_frontmatter_factory(**overrides: dict) -> dict:
    base_content = {
        "id": "airise",
        "section": "project",
        "title": "AiRise",
        "last_reviewed": date(2026, 5, 25),
        "status": "Completed",
        "date_start": date(2025, 1, 1),
        "date_end": date(2025, 12, 1),
        "stack": ["Python", "React", "TypeScript", "PostgreSQL"],
        "skills": ["Problem Solving", "Communication", "Teamwork", "Leadership"],
        "links": {"github": "https://github.com/airise", "website": "https://airise.com"},
        "tags": ["project"],
        "related": [],
        "summary": "Cross-platform AI fitness app where I owned the C#/.NET API layer, Gemini-powered personalization, and KMP health-data integration on an 8-person Agile team."   
    }
    return {**base_content, **overrides}   
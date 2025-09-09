# app/data/projects.py
def get_projects():
    return [
        {
            "id": "appointments-app",
            "title": "Appointments App",
            "subtitle": "Full‑stack scheduling (Next.js + Express + AWS CDK)",
            "tech": [
                "TypeScript",
                "Express.js",
                "Next.js",
                "AWS CDK",
                "AWS RDS",
                "AWS Lambda",
                "PostgreSQL",
                "Docker",
            ],
            "bullets": [
                "Full-stack CRUD appointments app with Next.js frontend on Vercel and Express API deployed via AWS CDK",
                "Infrastructure as Code (CDK) allows for repeatable deployments and clear documentation of the stack",
                "Designed with production best practices: typed API, auth-ready patterns, and CI/CD for frontend and infrastructure",
            ],
            "links": {
                "repo": "https://github.com/and-rs/appointments",
                "demo": "https://appointments-jet.vercel.app",
            },
            "media": [
                {
                    "type": "image",
                    "src": "appointments-22681398",
                    "alt": "Appointments dashboard UI",
                }
            ],
            "order": 1,
        },
        {
            "id": "caminatas",
            "title": "Caminatas",
            "subtitle": "Business site for trekking company (FastAPI + HTMX)",
            "tech": [
                "Python",
                "FastAPI",
                "HTMX",
                "Jinja",
                "Tailwind",
            ],
            "bullets": [
                "Server-rendered web app focused on performance with FastAPI, HTMX, Jinja, and Tailwind CSS",
                "Progressive enhancement approach delivers fast page loads with minimal JavaScript",
                "Currently implementing content management and scheduling features for a trekking business",
            ],
            "links": {
                "repo": "https://github.com/and-rs/caminatas",
            },
            "media": [
                {
                    "type": "image",
                    "src": "caminatas-f4d77df8",
                    "alt": "Caminatas homepage",
                }
            ],
            "order": 2,
        },
    ]

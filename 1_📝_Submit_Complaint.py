import streamlit as st
from agent import ask_agent
import sqlite3
import uuid
from datetime import datetime


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Submit Civic Complaint",
    page_icon="📝",
    layout="centered"
)


# -----------------------------
# Database Setup
# -----------------------------

def create_database():

    conn = sqlite3.connect("complaints.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS complaints (
            complaint_id TEXT PRIMARY KEY,
            issue_type TEXT,
            severity TEXT,
            city TEXT,
            district TEXT,
            state TEXT,
            complaint TEXT,
            department TEXT,
            reason TEXT,
            action TEXT,
            status TEXT,
            created_at TEXT
        )
    """)

    conn.commit()

    conn.close()


create_database()


# -----------------------------
# Title
# -----------------------------

st.title("📝 Submit a Civic Complaint")

st.write(
    "Submit a civic complaint and let AI identify "
    "the appropriate department for routing."
)

st.divider()


# -----------------------------
# User Input
# -----------------------------

category = st.selectbox(
    "🏷️ Select your civic issue",
    [
        "Roads and Potholes",
        "Garbage and Waste",
        "Streetlights",
        "Water Supply",
        "Drainage and Sewage",
        "Public Toilets",
        "Other"
    ]
)


# -----------------------------
# Location
# -----------------------------

st.subheader("📍 Location")

city = st.text_input(
    "City",
    placeholder="Example: Nagercoil"
)

district = st.text_input(
    "District",
    placeholder="Example: Kanyakumari"
)

state = st.text_input(
    "State",
    placeholder="Example: Tamil Nadu"
)


# -----------------------------
# Complaint Description
# -----------------------------

st.subheader("📝 Describe Your Problem")

question = st.text_area(
    "Civic Complaint",
    placeholder="Example: There are many deep potholes on my street.",
    height=150
)


# -----------------------------
# Submit Complaint
# -----------------------------

if st.button(
    "🚀 Analyze and Route Complaint",
    use_container_width=True
):

    if not question or not city or not district or not state:

        st.warning(
            "⚠️ Please complete all fields before submitting."
        )

    else:

        # -----------------------------
        # Prepare Complaint for AI
        # -----------------------------

        full_question = f"""
Issue Category:
{category}

Location:
City: {city}
District: {district}
State: {state}

Citizen Complaint:
{question}
"""


        # -----------------------------
        # AI Analysis
        # -----------------------------

        with st.spinner(
            "🤖 AI is analyzing your complaint..."
        ):

            result = ask_agent(
                full_question
            )


        # -----------------------------
        # Generate Complaint ID
        # -----------------------------

        complaint_id = (
            "CIV-"
            + datetime.now().strftime("%Y%m%d")
            + "-"
            + str(uuid.uuid4())[:6].upper()
        )


        # -----------------------------
        # Save Complaint to Database
        # -----------------------------

        conn = sqlite3.connect(
            "complaints.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO complaints
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                complaint_id,
                result["issue_type"],
                result["severity"],
                city,
                district,
                state,
                question,
                result["department"],
                result["reason"],
                result["action"],
                "Submitted",
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )
        )

        conn.commit()

        conn.close()


        # -----------------------------
        # Display Success
        # -----------------------------

        st.success(
            "✅ Complaint analyzed successfully!"
        )


        # -----------------------------
        # AI Analysis Result
        # -----------------------------

        st.subheader(
            "🔍 AI Analysis"
        )


        st.write(
            "Issue Type:",
            result["issue_type"]
        )

        st.write(
            "Severity:",
            result["severity"]
        )


        # -----------------------------
        # Responsible Department
        # -----------------------------

        st.subheader(
            "🏛️ Responsible Department"
        )


        st.info(
            result["department"]
        )


        st.write(
            "**Why:**",
            result["reason"]
        )


        st.write(
            "**Recommended Action:**",
            result["action"]
        )


        st.divider()


        # -----------------------------
        # Complaint Routing
        # -----------------------------

        st.subheader(
            "📤 Complaint Routing"
        )


        st.success(
            f"Complaint routed to: "
            f"{result['department']}"
        )


        # -----------------------------
        # Complaint ID
        # -----------------------------

        st.subheader(
            "🎫 Complaint ID"
        )


        st.code(
            complaint_id
        )


        st.write(
            "Status: 🟡 Submitted"
        )


        st.caption(
            "Keep this Complaint ID to track your complaint."
        )
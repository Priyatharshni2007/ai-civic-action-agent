import streamlit as st
import sqlite3


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Track Civic Complaint",
    page_icon="🔎",
    layout="centered"
)


# ---------------------------------
# Title
# ---------------------------------

st.title("🔎 Track Your Civic Complaint")

st.write(
    "Enter your Complaint ID to check the current status "
    "of your civic complaint."
)

st.divider()


# ---------------------------------
# Complaint ID Input
# ---------------------------------

complaint_id_input = st.text_input(
    "🎫 Enter Complaint ID",
    placeholder="Example: CIV-20260726-ABC123"
)


# ---------------------------------
# Track Button
# ---------------------------------

if st.button(
    "🔍 Track Complaint",
    use_container_width=True
):

    if not complaint_id_input:

        st.warning(
            "⚠️ Please enter your Complaint ID."
        )

    else:

        # ---------------------------------
        # Connect to Database
        # ---------------------------------

        conn = sqlite3.connect(
            "complaints.db"
        )

        cursor = conn.cursor()


        # ---------------------------------
        # Search Complaint
        # ---------------------------------

        cursor.execute(
            """
            SELECT *
            FROM complaints
            WHERE complaint_id = ?
            """,
            (complaint_id_input.strip(),)
        )


        complaint = cursor.fetchone()

        conn.close()


        # ---------------------------------
        # Complaint Found
        # ---------------------------------

        if complaint:

            (
                complaint_id,
                issue_type,
                severity,
                city,
                district,
                state,
                complaint_text,
                department,
                reason,
                action,
                status,
                created_at
            ) = complaint


            st.success(
                "✅ Complaint Found!"
            )


            # ---------------------------------
            # Complaint Details
            # ---------------------------------

            st.subheader(
                "🎫 Complaint Details"
            )


            st.write(
                "**Complaint ID:**",
                complaint_id
            )

            st.write(
                "**Issue:**",
                issue_type
            )

            st.write(
                "**Severity:**",
                severity
            )

            st.write(
                "**Location:**",
                f"{city}, {district}, {state}"
            )

            st.write(
                "**Your Complaint:**",
                complaint_text
            )

            st.write(
                "**Assigned Department:**",
                department
            )


            st.divider()


            # ---------------------------------
            # Current Status
            # ---------------------------------

            st.subheader(
                "📊 Current Status"
            )


            if status == "Submitted":

                st.info(
                    "🟡 Your complaint has been submitted "
                    "and is waiting for department assignment."
                )

            elif status == "Assigned":

                st.info(
                    "🔵 Your complaint has been assigned "
                    "to the responsible department."
                )

            elif status == "In Progress":

                st.warning(
                    "🟠 Action is currently in progress."
                )

            elif status == "Resolved":

                st.success(
                    "🟢 Your complaint has been resolved!"
                )


            st.write(
                "**Current Status:**",
                status
            )


            # ---------------------------------
            # Complaint Progress
            # ---------------------------------

            st.subheader(
                "📈 Complaint Progress"
            )


            progress_steps = [
                "Submitted",
                "Assigned",
                "In Progress",
                "Resolved"
            ]


            current_index = progress_steps.index(
                status
            )


            for index, step in enumerate(
                progress_steps
            ):

                if index < current_index:

                    st.success(
                        f"✅ {step}"
                    )

                elif index == current_index:

                    st.info(
                        f"🔵 {step} — Current Status"
                    )

                else:

                    st.write(
                        f"⚪ {step}"
                    )


            st.divider()


            # ---------------------------------
            # Complaint Information
            # ---------------------------------

            st.subheader(
                "ℹ️ Complaint Information"
            )


            st.write(
                "**AI Recommended Action:**",
                action
            )

            st.write(
                "**Submitted At:**",
                created_at
            )


        # ---------------------------------
        # Complaint Not Found
        # ---------------------------------

        else:

            st.error(
                "❌ Complaint ID not found. "
                "Please check the ID and try again."
            )
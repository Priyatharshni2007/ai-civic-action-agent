import streamlit as st
import sqlite3


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="Department Dashboard",
    page_icon="🏛️",
    layout="wide"
)


# ---------------------------------
# Title
# ---------------------------------

st.title("🏛️ Department Dashboard")

st.write(
    "View, analyze, and manage civic complaints "
    "routed by the AI Civic Action Agent."
)

st.divider()


# ---------------------------------
# Connect to Database
# ---------------------------------

conn = sqlite3.connect("complaints.db")

cursor = conn.cursor()


# ---------------------------------
# Get All Complaints
# ---------------------------------

cursor.execute(
    """
    SELECT *
    FROM complaints
    ORDER BY created_at DESC
    """
)

complaints = cursor.fetchall()

conn.close()


# ---------------------------------
# Dashboard Statistics
# ---------------------------------

if complaints:

    total_complaints = len(complaints)

    submitted_count = sum(
        1 for complaint in complaints
        if complaint[10] == "Submitted"
    )

    assigned_count = sum(
        1 for complaint in complaints
        if complaint[10] == "Assigned"
    )

    progress_count = sum(
        1 for complaint in complaints
        if complaint[10] == "In Progress"
    )

    resolved_count = sum(
        1 for complaint in complaints
        if complaint[10] == "Resolved"
    )


    # ---------------------------------
    # Statistics Cards
    # ---------------------------------

    st.subheader("📊 Complaint Overview")

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:

        st.metric(
            "📋 Total",
            total_complaints
        )


    with col2:

        st.metric(
            "🟡 Submitted",
            submitted_count
        )


    with col3:

        st.metric(
            "🔵 Assigned",
            assigned_count
        )


    with col4:

        st.metric(
            "🟠 In Progress",
            progress_count
        )


    with col5:

        st.metric(
            "🟢 Resolved",
            resolved_count
        )


    st.divider()


    # ---------------------------------
    # Filter Complaints
    # ---------------------------------

    st.subheader("🔎 Filter Complaints")


    filter_option = st.selectbox(
        "Select Status",
        [
            "All",
            "Submitted",
            "Assigned",
            "In Progress",
            "Resolved"
        ]
    )


    # ---------------------------------
    # Display Complaints
    # ---------------------------------

    displayed_complaints = complaints


    if filter_option != "All":

        displayed_complaints = [

            complaint
            for complaint in complaints

            if complaint[10] == filter_option

        ]


    st.write(
        f"Showing {len(displayed_complaints)} complaint(s)"
    )


    # ---------------------------------
    # Complaint Details
    # ---------------------------------

    for complaint in displayed_complaints:


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


        with st.expander(

            f"🎫 {complaint_id} | "
            f"{issue_type} | "
            f"{status}"

        ):


            # ---------------------------------
            # Complaint Information
            # ---------------------------------

            st.subheader(
                "📋 Complaint Information"
            )


            col1, col2 = st.columns(2)


            with col1:

                st.write(
                    "**Complaint ID:**",
                    complaint_id
                )

                st.write(
                    "**Issue Type:**",
                    issue_type
                )

                st.write(
                    "**Severity:**",
                    severity
                )


            with col2:

                st.write(
                    "**Location:**",
                    f"{city}, {district}, {state}"
                )

                st.write(
                    "**Submitted At:**",
                    created_at
                )

                st.write(
                    "**Current Status:**",
                    status
                )


            st.divider()


            # ---------------------------------
            # Citizen Complaint
            # ---------------------------------

            st.subheader(
                "📝 Citizen Complaint"
            )


            st.write(
                complaint_text
            )


            st.divider()


            # ---------------------------------
            # AI Analysis
            # ---------------------------------

            st.subheader(
                "🤖 AI Analysis"
            )


            st.write(
                "**Assigned Department:**",
                department
            )


            st.write(
                "**AI Reason:**",
                reason
            )


            st.write(
                "**Recommended Action:**",
                action
            )


            st.divider()


            # ---------------------------------
            # Status Update
            # ---------------------------------

            st.subheader(
                "🔄 Update Complaint Status"
            )


            status_options = [

                "Submitted",
                "Assigned",
                "In Progress",
                "Resolved"

            ]


            new_status = st.selectbox(

                "Select New Status",

                status_options,

                index=status_options.index(status),

                key="status_" + complaint_id

            )


            if st.button(

                "🔄 Update Status",

                key="update_" + complaint_id,

                use_container_width=True

            ):


                conn = sqlite3.connect(
                    "complaints.db"
                )

                cursor = conn.cursor()


                cursor.execute(

                    """
                    UPDATE complaints
                    SET status = ?
                    WHERE complaint_id = ?
                    """,

                    (
                        new_status,
                        complaint_id
                    )

                )


                conn.commit()

                conn.close()


                st.success(

                    f"✅ Complaint {complaint_id} "
                    f"updated to {new_status}."

                )


                st.rerun()


else:

    # ---------------------------------
    # No Complaints
    # ---------------------------------

    st.info(
        "📭 No complaints have been submitted yet."
    )
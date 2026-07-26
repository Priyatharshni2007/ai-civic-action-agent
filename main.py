import streamlit as st


# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="AI Civic Action Agent",
    page_icon="🇮🇳",
    layout="centered"
)


# ---------------------------------
# Home Page
# ---------------------------------

def home_page():

    st.title("🇮🇳 AI Civic Action Agent")

    st.subheader(
        "One Voice, Many Services"
    )

    st.write(
        "An AI-powered civic complaint management system "
        "that transforms a citizen's voice into intelligent "
        "civic action."
    )

    st.divider()


    # ---------------------------------
    # Problem
    # ---------------------------------

    st.header("🚨 The Problem")

    st.write(
        "Citizens often face difficulty identifying the correct "
        "government department for civic issues. Complaints may "
        "be misdirected, delayed, or difficult to track."
    )


    st.divider()


    # ---------------------------------
    # Our Solution
    # ---------------------------------

    st.header("💡 Our Solution")

    st.write(
        "AI Civic Action Agent acts as an intelligent bridge "
        "between citizens and government departments. "
        "The AI analyzes a complaint, identifies its severity, "
        "determines the responsible department, recommends action, "
        "and enables end-to-end complaint tracking."
    )


    st.divider()


    # ---------------------------------
    # How It Works
    # ---------------------------------

    st.header("⚙️ How One Voice, Many Services Works")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.info(
            "👤 STEP 1\n\n"
            "Citizen Reports\n\n"
            "A citizen submits a civic complaint "
            "with location and problem details."
        )


    with col2:

        st.info(
            "🤖 STEP 2\n\n"
            "AI Analysis\n\n"
            "AI identifies the issue, severity, "
            "responsible department, and recommended action."
        )


    with col3:

        st.info(
            "🏛️ STEP 3\n\n"
            "Smart Routing\n\n"
            "The complaint is automatically routed "
            "to the appropriate department."
        )


    col4, col5, col6 = st.columns(3)


    with col4:

        st.info(
            "🎫 STEP 4\n\n"
            "Complaint ID\n\n"
            "A unique Complaint ID is generated "
            "for every submitted complaint."
        )


    with col5:

        st.info(
            "🔄 STEP 5\n\n"
            "Department Action\n\n"
            "Departments review complaints and "
            "update their progress."
        )


    with col6:

        st.info(
            "🔎 STEP 6\n\n"
            "Citizen Tracking\n\n"
            "Citizens can track their complaint "
            "status until resolution."
        )


    st.divider()


    # ---------------------------------
    # Key Features
    # ---------------------------------

    st.header("🚀 Key Features")

    feature_col1, feature_col2 = st.columns(2)


    with feature_col1:

        st.success(
            "🤖 AI-Powered Complaint Analysis"
        )

        st.success(
            "🏛️ Intelligent Department Routing"
        )

        st.success(
            "⚠️ AI-Based Severity Detection"
        )


    with feature_col2:

        st.success(
            "🎫 Unique Complaint ID"
        )

        st.success(
            "📊 Department Management Dashboard"
        )

        st.success(
            "🔎 Real-Time Complaint Tracking"
        )


    st.divider()


    # ---------------------------------
    # Impact
    # ---------------------------------

    st.header("🌍 Expected Impact")

    st.write(
        "Our system aims to reduce complaint misrouting, "
        "improve transparency, help departments prioritize "
        "civic issues, and give citizens a simple way to "
        "track the progress of their complaints."
    )


    st.divider()


    # ---------------------------------
    # Technology Stack
    # ---------------------------------

    st.header("🛠️ Technology Stack")

    tech_col1, tech_col2, tech_col3, tech_col4 = st.columns(4)


    with tech_col1:

        st.write("🐍 **Python**")


    with tech_col2:

        st.write("🤖 **Google Gemini AI**")


    with tech_col3:

        st.write("🌐 **Streamlit**")


    with tech_col4:

        st.write("🗄️ **SQLite**")


    st.divider()


    # ---------------------------------
    # Navigation
    # ---------------------------------

    st.header("🚀 Explore the System")

    st.write(
        "Use the sidebar to experience the complete "
        "citizen-to-department civic action workflow."
    )


    st.success(
        "👈 Select a service from the sidebar to get started."
    )


    st.caption(
        "AI Civic Action Agent | One Voice, Many Services"
    )

# ---------------------------------
# Page Navigation
# ---------------------------------

home = st.Page(
    home_page,
    title="Home",
    icon="🏠"
)


submit = st.Page(
    "pages/1_📝_Submit_Complaint.py",
    title="Submit Complaint",
    icon="📝"
)


track = st.Page(
    "pages/2_🔎_Track_Complaint.py",
    title="Track Complaint",
    icon="🔎"
)


dashboard = st.Page(
    "pages/3_🏛️_Department_Dashboard.py",
    title="Department Dashboard",
    icon="🏛️"
)


# ---------------------------------
# Navigation
# ---------------------------------

pg = st.navigation(
    [
        home,
        submit,
        track,
        dashboard
    ]
)


# ---------------------------------
# Run Selected Page
# ---------------------------------

pg.run()
import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path
import uuid

st.set_page_config(
    page_title="Student Registration Portal",
    page_icon="🎓",
    layout="wide"
)

# FILE

EXCEL_FILE = Path("students.xlsx")



# CUSTOM CSS

st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 25px;
    font-weight: 600;
    margin-top: 20px;
}

.success-box {
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #cccccc;
    margin-top: 30px;
}

.registration-id {
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# SAVE DATA

def save_student(student):

    new_student = pd.DataFrame([student])

    if EXCEL_FILE.exists():

        old_data = pd.read_excel(EXCEL_FILE)

        updated_data = pd.concat(
            [old_data, new_student],
            ignore_index=True
        )

    else:

        updated_data = new_student

    updated_data.to_excel(
        EXCEL_FILE,
        index=False,
        sheet_name="Students"
    )

# REGISTRATION PAGE

def registration_page():

    st.markdown(
        '<div class="main-title">🎓 Student Registration Portal</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Build your profile and begin your journey 🚀'
        '</div>',
        unsafe_allow_html=True
    )

    # Progress
    st.progress(0.0)

    # PERSONAL INFORMATION

    st.markdown(
        '<div class="section-title">👤 Personal Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "Full Name *",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "Email Address *",
            placeholder="example@gmail.com"
        )

        phone = st.text_input(
            "Phone Number",
            placeholder="Enter your phone number"
        )

    with col2:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=18
        )

        gender = st.selectbox(
            "Gender",
            [
                "Select",
                "Male",
                "Female",
                "Other"
            ]
        )

        city = st.text_input(
            "City",
            placeholder="Enter your city"
        )


    # ACADEMIC INFORMATION

    st.markdown(
        '<div class="section-title">📚 Academic Information</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        college = st.text_input(
            "College Name *",
            placeholder="Enter your college"
        )

        course = st.selectbox(
            "Course",
            [
                "Select",
                "Information Science and Engineering",
                "Computer Science Engineering",
                "Electronics and Communication Engineering",
                "Mechanical Engineering",
                "Civil Engineering",
                "Other"
            ]
        )

    with col2:

        year = st.selectbox(
            "Current Year",
            [
                "Select",
                "1st Year",
                "2nd Year",
                "3rd Year",
                "4th Year"
            ]
        )

        cgpa = st.number_input(
            "CGPA",
            min_value=0.0,
            max_value=10.0,
            value=0.0,
            step=0.01
        )

    # SKILLS

    st.markdown(
        '<div class="section-title">💡 Skills & Interests</div>',
        unsafe_allow_html=True
    )

    st.write("Select the skills you currently know:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        python_skill = st.checkbox("Python")

    with col2:
        sql_skill = st.checkbox("SQL")

    with col3:
        data_analysis = st.checkbox("Data Analysis")

    with col4:
        ml_skill = st.checkbox("Machine Learning")


    career_goal = st.selectbox(
        "Career Goal",
        [
            "Select",
            "Software Developer",
            "Data Analyst",
            "Data Scientist",
            "Machine Learning Engineer",
            "Web Developer",
            "Other"
        ]
    )

    # ABOUT YOU

    st.markdown(
        '<div class="section-title">📝 About You</div>',
        unsafe_allow_html=True
    )

    about = st.text_area(
        "Tell us something about yourself",
        placeholder="Write a short introduction..."
    )

    # PROFILE PHOTO

    st.markdown(
        '<div class="section-title">📸 Profile Photo</div>',
        unsafe_allow_html=True
    )

    photo = st.file_uploader(
        "Upload your photo",
        type=["jpg", "jpeg", "png"]
    )

    # DECLARATION

    st.markdown(
        '<div class="section-title">🔐 Declaration</div>',
        unsafe_allow_html=True
    )

    agree = st.checkbox(
        "I confirm that the information provided is correct."
    )

    # REGISTER

    st.write("")

    register = st.button(
        "🚀 Register Now",
        type="primary",
        use_container_width=True
    )


    if register:

        # Validation

        if not name.strip():

            st.error("❌ Please enter your full name.")
            return

        if not email.strip():

            st.error("❌ Please enter your email.")
            return

        if not college.strip():

            st.error("❌ Please enter your college name.")
            return

        if gender == "Select":

            st.error("❌ Please select your gender.")
            return

        if course == "Select":

            st.error("❌ Please select your course.")
            return

        if year == "Select":

            st.error("❌ Please select your current year.")
            return

        if career_goal == "Select":

            st.error("❌ Please select your career goal.")
            return

        if not agree:

            st.warning(
                "⚠️ Please accept the declaration."
            )
            return

        # SKILLS

        skills = []

        if python_skill:
            skills.append("Python")

        if sql_skill:
            skills.append("SQL")

        if data_analysis:
            skills.append("Data Analysis")

        if ml_skill:
            skills.append("Machine Learning")

        if not skills:
            skills.append("None")

        # REGISTRATION ID

        registration_id = (
            "STU-" +
            datetime.now().strftime("%Y%m%d") +
            "-" +
            uuid.uuid4().hex[:4].upper()
        )

        # SAVE STUDENT

        student = {

            "Registration ID":
                registration_id,

            "Name":
                name,

            "Age":
                age,

            "Gender":
                gender,

            "Email":
                email,

            "Phone":
                phone,

            "City":
                city,

            "College":
                college,

            "Course":
                course,

            "Year":
                year,

            "CGPA":
                cgpa,

            "Skills":
                ", ".join(skills),

            "Career Goal":
                career_goal,

            "About":
                about,

            "Registration Time":
                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
        }


        try:

            save_student(student)

            # DON'T DISPLAY STUDENT INFORMATION

            st.markdown(
                """
                <div class="success-box">

                <h1>🎉 Registration Successful!</h1>

                <p>
                Thank you for registering.
                </p>

                <p>
                Your registration has been submitted successfully.
                </p>

                <div class="registration-id">
                Registration ID Generated
                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.balloons()

        except Exception as e:

            st.error(
                "❌ Something went wrong while saving your registration."
            )

            st.error(str(e))

# ADMIN PAGE

def admin_page():

    st.title("🔐 Admin Dashboard")

    st.write(
        "This area is for authorized administrators only."
    )

    password = st.text_input(
        "Admin Password",
        type="password"
    )

    if st.button("Login"):

        if password == "Admin@123":

            st.session_state["admin"] = True

        else:

            st.error("❌ Incorrect password.")


    if st.session_state.get("admin", False):

        st.success("✅ Admin login successful.")

        if EXCEL_FILE.exists():

            df = pd.read_excel(EXCEL_FILE)

            # Dashboard metrics

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "👨‍🎓 Total Students",
                    len(df)
                )

            with col2:

                today = datetime.now().strftime("%Y-%m-%d")

                today_count = df[
                    df["Registration Time"].astype(str).str.startswith(today)
                ].shape[0]

                st.metric(
                    "📅 Today's Registrations",
                    today_count
                )

            with col3:

                if len(df) > 0:

                    average_cgpa = round(
                        df["CGPA"].mean(),
                        2
                    )

                else:

                    average_cgpa = 0

                st.metric(
                    "📊 Average CGPA",
                    average_cgpa
                )


            st.divider()

            st.subheader("📋 Registered Students")

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )


            # Download Excel

            excel_data = EXCEL_FILE.read_bytes()

            st.download_button(
                "📥 Download Student Data",
                data=excel_data,
                file_name="students.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        else:

            st.info(
                "No student registrations yet."
            )

        if st.button("Logout"):

            st.session_state["admin"] = False

            st.rerun()

# SIDEBAR

st.sidebar.title("🎓 Student Portal")

page = st.sidebar.radio(
    "Navigation",
    [
        "📝 Registration",
        "🔐 Admin"
    ]
)


if page == "📝 Registration":

    registration_page()

else:

    admin_page()
import streamlit as st
import csv
import os
from utils.helper import get_deadline_status
import subprocess
import sys


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Scholarship Finder",
    page_icon="🎓"
)


# --------------------------------------------------
# Main Title
# --------------------------------------------------

st.title("🎓 Smart Scholarship & Government Scheme Finder")

st.write(
    "Find scholarship schemes based on your basic details."
)


# --------------------------------------------------
# Introduction Box
# --------------------------------------------------

st.markdown(
    """
    <div style="
        padding: 15px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 20px;
    ">
        <h4>🎓 Find Scholarships Easily</h4>
        <p>
        Enter your basic details to find scholarship schemes
        matching your education and state.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Refresh Scholarship Data
# --------------------------------------------------

if st.button("🔄 Refresh Latest Scholarship Data"):

    with st.spinner("Updating scholarship data..."):

        
        result = subprocess.run(
    [
        sys.executable,
        os.path.join(
            "scraper",
            "scraper.py"
        )
    ],
    capture_output=True,
    text=True,
    cwd=os.path.dirname(__file__)
)

    if result.returncode == 0:

        st.success(
            "✅ Scholarship data updated successfully!"
        )

    else:

        st.error(
            "❌ Unable to update scholarship data."
        )

        st.code(result.stderr)


# --------------------------------------------------
# Read Scholarship result
# --------------------------------------------------

file_path = os.path.join(
    os.path.dirname(__file__),
    "data",
    "scraped_scholarships.csv"
)


try:

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        scholarships = list(reader)


except FileNotFoundError:

    st.error(
        "❌ Scholarship data file not found."
    )

    st.info(
        "Please click '🔄 Refresh Latest Scholarship Data' "
        "to create the latest scholarship data."
    )

    st.stop()


except Exception as e:

    st.error(
        "❌ Unable to read scholarship data."
    )

    st.code(str(e))

    st.stop()


# --------------------------------------------------
# Student Details
# --------------------------------------------------

st.header("Student Details")


name = st.text_input(
    "Enter your name"
)


education = st.selectbox(
    "Select your education",
    [
        "Graduation",
        "Post Graduation",
        "School"
    ]
)


course = st.text_input(
    "Enter your course"
)


state = st.selectbox(
    "Select your state",
    [
        "Maharashtra",
        "Other"
    ]
)


category = st.selectbox(
    "Select your category",
    [
        "Open",
        "OBC",
        "EBC",
        "DNT",
        "SC",
        "ST"
    ]
)


income = st.number_input(
    "Enter annual family income (₹)",
    min_value=0,
    step=1000
)


# --------------------------------------------------
# Find Scholarships
# --------------------------------------------------

if st.button("🔍 Find Scholarships"):

    if name == "" or course == "":

        st.warning(
            "Please enter your name and course."
        )

    else:

        # ------------------------------------------
        # Student Summary
        # ------------------------------------------

        st.subheader("👤 Student Summary")


        col1, col2 = st.columns(2)


        with col1:

            st.write(
                "**Name:**",
                name
            )

            st.write(
                "**Education:**",
                education
            )

            st.write(
                "**Course:**",
                course
            )


        with col2:

            st.write(
                "**State:**",
                state
            )

            st.write(
                "**Category:**",
                category
            )

            st.write(
                "**Annual Income:** ₹",
                f"{income:,}"
            )


        # ------------------------------------------
        # Matching Scholarships
        # ------------------------------------------

        st.subheader(
            "🎯 Matching Scholarships"
        )


        found = False

        matching_count = 0


        for scholarship in scholarships:

            # --------------------------------------
            # State Matching
            # --------------------------------------

            state_match = (
                scholarship["State"] == state
                or scholarship["State"] == "All India"
            )


            # --------------------------------------
            # Education Matching
            # --------------------------------------

            education_match = True


            if (
                education == "School"
                and
                scholarship["Scheme Type"] != "Pre Matric"
            ):

                education_match = False


            elif (
                education == "Graduation"
                and
                scholarship["Scheme Type"] != "Post Matric"
                ):

                education_match = False


            elif (
                education == "Post Graduation"
                and
                scholarship["Scheme Type"] != "Post Matric"
                ):

                education_match = False


            # --------------------------------------
            # Final Matching
            # --------------------------------------

            if state_match and education_match:

                found = True

                matching_count += 1


                # ----------------------------------
                # Deadline Calculation
                # ----------------------------------
                
                status = get_deadline_status(
                    scholarship["Application Deadline"]
                )


                # ----------------------------------
                # Status
                # ----------------------------------

                


                # ----------------------------------
                # Scholarship Card
                # ----------------------------------

                st.markdown("---")


                st.subheader(
                    f"🎓 {scholarship['Scholarship Name']}"
                )


                col1, col2 = st.columns(2)


                with col1:

                    st.write(
                        "📍 **State:**",
                        scholarship["State"]
                    )

                    st.write(
                        "📚 **Scheme Type:**",
                        scholarship["Scheme Type"]
                    )


                with col2:

                    st.write(
                        "📅 **Application Deadline:**",
                        scholarship["Application Deadline"]
                    )


                # ----------------------------------
                # Status Display
                # ----------------------------------

                if status == "Active":

                    st.success(
                        "🟢 Status: Active"
                    )

                elif status == "Due Soon":

                    st.warning(
                        "🟠 Status: Due Soon"
                    )

                elif status == "Expired":

                    st.error(
                        "🔴 Status: Expired"
                    )

                else:

                    st.info(
                        "🔵 Status: Date Unavailable"
                    )


                # ----------------------------------
                # Application Link
                # ----------------------------------

                if (
                    scholarship["Application Link"]
                    != "Not Found"
                ):

                    st.link_button(
                        "🔗 Apply / View Details",
                        scholarship["Application Link"]
                    )


        # ------------------------------------------
        # Matching Count
        # ------------------------------------------

        st.info(
            f"🎯 Matching Scholarships: {matching_count}"
        )


        # ------------------------------------------
        # No Match
        # ------------------------------------------

        if not found:

            st.info(
                "No matching scholarships found."
            )


        # ------------------------------------------
        # Eligibility Verification
        # ------------------------------------------

        st.info(
            "ℹ️ Potential Match: "
            "This scholarship is matched based on the "
            "student's state and education level."
        )


        st.warning(
            "⚠️ Category and income eligibility should be "
            "verified according to the official scholarship "
            "guidelines on the NSP portal."
        )


        # ------------------------------------------
        # Final Verification Note
        # ------------------------------------------

        st.caption(
            "Please verify final eligibility and "
            "application details on the official "
            "NSP portal."
        )
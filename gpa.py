import streamlit as st

def calculate_gpa(subjects):
    total_credit_hours = 0
    total_quality_points = 0

    for subject in subjects:
        credit_hours = subject["credit_hours"]
        quality_points = subject["quality_points"]
        total_credit_hours += credit_hours
        total_quality_points += quality_points

    if total_credit_hours == 0:
        return 0
    else:
        gpa = total_quality_points / total_credit_hours
        return round(gpa, 2)

st.title("GPA Calculator")

# Ask user for number of subjects
num_subjects = st.number_input("Enter number of subjects:", min_value=0, max_value=10, step=1)

# Collect subject details based on user input
subjects = []
for i in range(num_subjects):
    st.header(f"Subject {i + 1}")
    credit_hours = st.number_input(f"Enter credit hours for Subject {i + 1}:", key=f"credit_{i}", min_value=0)
    quality_points = st.number_input(f"Enter quality points for Subject {i + 1}:", key=f"quality_{i}", min_value=0.0)
    subjects.append({"credit_hours": credit_hours, "quality_points": quality_points})

# Add a button to calculate GPA
calculate_button = st.button("Calculate GPA")

# Calculate and display GPA upon button press
if calculate_button:
    gpa = calculate_gpa(subjects)
    st.write(f"Calculated GPA: {gpa}")

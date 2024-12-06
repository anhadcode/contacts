import streamlit as st
import pandas as pd
import os

# Filepath for the CSV file
csv_file = "Offline University Contact List - Staff.csv"

# Load data
def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        # Create an empty dataframe with the required columns if the file doesn't exist
        columns = [
            "University", "Tier", "Contact Name", "Email", "Designation", 
            "Status", "Who is contacting?", "Contact Date", "Follow up Date", 
            "Feedback/Comments", "Notes"
        ]
        return pd.DataFrame(columns=columns)

# Save data to the CSV file
def save_data(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)

# Load data into a dataframe
data = load_data(csv_file)

# Streamlit app
st.title("University Data Entry App")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Add New Entry", "View/Edit Existing Records", "Summary"])

if menu == "Add New Entry":
    st.header("Add New Entry")
    
    # Data entry form
    with st.form("entry_form"):
        university = st.text_input("University")
        tier = st.selectbox("Tier",['Tier 1','Tier 2', 'Tier 3'])
        contact_name = st.text_input("Contact Name")
        email = st.text_input("Email")
        designation = st.text_input("Designation")
        status = st.selectbox("Status", ["Not Contacted", "In Progress", "Terminated", "Successful"])
        who_is_contacting = st.selectbox("Who is contacting?",['Guru', 'Anhad','Arjun', 'Sumit', 'Kanupriya'])
        contact_date = st.date_input("Contact Date")
        follow_up_date = st.date_input("Follow Up Date")
        feedback = st.text_area("Feedback/Comments")
        notes = st.text_area("Notes")
        
        # Submit button
        submitted = st.form_submit_button("Add Entry")
    
    if submitted:
        # Append new record to the dataframe
        new_entry = {
            "University": university,
            "Tier": tier,
            "Contact Name": contact_name,
            "Email": email,
            "Designation": designation,
            "Status": status,
            "Who is contacting?": who_is_contacting,
            "Contact Date": contact_date,
            "Follow up Date": follow_up_date,
            "Feedback/Comments": feedback,
            "Notes": notes,
        }
        new_entry_df = pd.DataFrame([new_entry])
        data = pd.concat([data, new_entry_df], ignore_index=True)
        save_data(data, csv_file)
        st.success("Entry added successfully!")

elif menu == "View/Edit Existing Records":
    st.header("View or Edit Existing Records")
    
    if data.empty:
        st.warning("No data available. Please add new entries.")
    else:
        # Display data in an editable table
        edited_data = st.dataframe(data)
        save_button = st.button("Save Changes")
        
        

elif menu == "Summary":
    st.header("Summary of Data")
    
    if data.empty:
        st.warning("No data available.")
    else:
        st.write("### Total Entries")
        st.write(len(data))
        
        st.write("### Data Overview")
        st.dataframe(data)

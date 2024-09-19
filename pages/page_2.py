import streamlit as st
import pandas as pd
import sqlalchemy

st.title("Sign Up")
username = st.text_input("Username: ")
emailId = st.text_input("Email address: ")
password = st.text_input("Password: ")
splChars = ["'", "=", "+", "-", "*", "/", "^", "@", "#", "$", "%", "&", "(", ")"]
engine = sqlalchemy.create_engine("mysql+pymysql://root:monadarling123@localhost:3306/accounts")

if st.button("Sign Up"):
    df_new = pd.DataFrame({"username": [username], "email": [emailId], "password": [password]})

    try:
        # Read the existing data from the Excel file
        df_existing = pd.read_sql("ultimate-nse-fetcher", con=engine)
    except FileNotFoundError:
        # If the file doesn't exist, create an empty DataFrame
        df_existing = pd.DataFrame(columns=["username", "email", "password"])

    # Validation checks
    if "`" in username:
        st.error("No ` sign allowed")
        st.stop()

    elif username in df_existing.username.values:
        st.error("Username Already Exists")
        st.stop()

    elif emailId in df_existing.email.values:
        st.error("Email Account Already Exists")
        st.stop()

    else:
        # Append the new data to the existing DataFrame
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)

        # Save the updated DataFrame back to the Excel file
        df_combined.to_sql("ultimate-nse-fetcher", con=engine, if_exists="append", index=False)

        # Successful registration, switch to another page
        st.success("Sign Up Successful!")
        st.switch_page("pages/page_3.py")

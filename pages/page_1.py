import streamlit as st
import pandas as pd
import sqlalchemy

st.title("Log In")
usernameOrEmail = st.text_input("Username or Email Address: ")
password = st.text_input("Password: ")
engine = sqlalchemy.create_engine("mysql+pymysql://root:monadarling123@localhost:3306/accounts")

if st.button("Log In"):
    df = pd.read_sql("ultimate-nse-fetcher", con=engine)
    print(df)

    if not ((df['username'] == usernameOrEmail).any() or (df['email'] == usernameOrEmail).any()):
        st.error("Username or Email is wrong.")
        st.stop()

    user_row = df[(df['username'] == usernameOrEmail) | (df['email'] == usernameOrEmail)]

    if user_row['password'].values[0] == password:
        st.switch_page("pages/page_3.py")

    else:
        st.error("Password is wrong.")
        st.stop()

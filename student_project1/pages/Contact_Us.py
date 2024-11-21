import streamlit as st
import pandas

from project_send_email import project_send_email

st.header("Contact Me")

data = pandas.read_csv("student_project1/topics.csv")


with st.form(key="project_email"):
    user_email= st.text_input("Your Email Address")

    selected_topic = st.selectbox("What topic do you want to discuss!",
    data["topic"])

    raw_message = st.text_area("Text")

    message = f"""\
Subject: New Email from{user_email}

From: {user_email}
Topic {selected_topic}
{raw_message}
"""

    button = st.form_submit_button("Submit")
    if button:
        project_send_email(message)
        st.info("Your email was sent successfully!")

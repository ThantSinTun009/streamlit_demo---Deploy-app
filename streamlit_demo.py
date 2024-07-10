import streamlit as st

st.header(':blue[Registration Form]', divider='rainbow')

st.subheader(":blue[Student's ID] :sunglasses:", divider='rainbow')
title = st.text_input("Enter Your Student ID", "SBL - A####")
st.write(":blue[Your StudentID is]", title)

st.subheader(":blue[Class Name] :sunglasses:", divider='rainbow')
title1 = st.text_input("Enter Your Class Name", "AI Foundation")
st.write(":blue[You are a student of ]", title1, " class.")
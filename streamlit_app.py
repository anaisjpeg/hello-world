import streamlit as st

st.header('st.button')

if st.button(":orange[Hello]", help="cc"):
    st.write("Why hello")
else:
    st.write("Goodbye")
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import time, datetime

st.header('st.button')

if st.button(":orange[Hello]", help="cc"):
    st.write("Why hello")
else:
    st.write("Goodbye")

st.header('st.write')

st.subheader('Display text')
st.write('Hello')

st.subheader('Display numbers')
st.write(1234)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

st.caption('dataframe 1')

st.write('ceci est une dataframe :', df, 'fin de la dataframe', 1234)

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

st.latex('cc')

st.code('import pandas as pd')

st.header("st.slider")

age = st.slider(
     label="How old are you ?",
     min_value=0,
     max_value=130,
)
st.write("I'm", age, "years old")

range_value = st.slider(
     label="Select a range of values",
     min_value=0.00,
     max_value=100.0,
     value=(25.0,75.0)
)
st.write("Values :", range_value)

range_time = st.slider(
     label="Select a range of values",
     min_value=time(0,0),
     max_value=time(23,59),
     value=(time(11,30),time(12,45))
)
st.write("Values :", range_time)

range_datetime = st.slider(
     label="When do you start ?",
     min_value=datetime(2019,12,18,9,30),
     max_value=datetime(2020,1,15,9,30),
     value=datetime(2020,1,1,9,30),
     format="MM/DD/YY - HH:mm"
)
st.write("Values :", range_datetime)

st.header("st.line_chart")

df3 = pd.DataFrame(np.random.randn(20, 3),
                   columns=['a', 'b', 'c'])

st.line_chart(df3)

st.header("st.selectbox")

selection = st.selectbox(label="What is your favorite color?",
                         options=["Red", "Green", "Blue"])

st.write("Your favorite color is ", selection)

st.header("st.multiselect")
multiselection = st.multiselect(label="What are your favorite colors?",
                                options= ("Green", "Blue", "Red"),
                                default= ("Green", "Red"))
st.write("You selected:", multiselection)

st.header("st.checkbox")
st.write("What would you like to order?")

glace = st.checkbox(label="Ice cream")
coffee = st.checkbox(label="Coffee")
cola = st.checkbox(label="Cola")

if glace:
    st.write("Here's some more!")

if coffee:
    st.write("Have a good day!")

if cola:
    st.write("Enjoy your drink!")
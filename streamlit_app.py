import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

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
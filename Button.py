import streamlit as st

st.header('st.button')

if st.button('Bonjour!'):
     st.write('It Means "Hello" in French')
else:
     st.write('')
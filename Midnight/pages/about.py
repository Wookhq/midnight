import streamlit as st
from modules.project_data.contributors import *
from modules.sidebar.sidebar import InitSidebar

InitSidebar()

st.write("Credit :")

for i in CONTRIBUTORS :
    st.write(CONTRIBUTORS[i])
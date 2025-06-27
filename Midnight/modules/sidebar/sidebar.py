import streamlit as st


def InitSidebar():

    st.sidebar.caption("Version M-0.2.3")

    st.sidebar.page_link("main.py", label="Home")
    st.sidebar.page_link("pages/testpage.py", label="test page")


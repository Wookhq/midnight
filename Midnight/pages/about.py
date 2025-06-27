import streamlit as st
from modules.project_data.contributors import *
from modules.sidebar.sidebar import InitSidebar

InitSidebar()

st.title("About")

st.write("This project is forked from Klilos modding tool, Rewrite gui to work with Linux")
st.subheader("Why?")

st.write("roblox mods work in linux now")

st.header("Special thanks to :")


def Cncol(contributors, cols_per_row=3):
    total = len(contributors)
    rows = (total + cols_per_row - 1) // cols_per_row
    for row in range(rows):
        cols = st.columns(cols_per_row, border=True)
        for i in range(cols_per_row):
            idx = row * cols_per_row + i
            if idx >= total:
                continue
            c = contributors[idx]
            with cols[i]:
                st.write(f"[{c.name}]({c.url})" if c.url else c.name)
                if c.text:
                    st.write(c.text)

# dont ask why, if its work, its work.
Cncol(FEATURE_SUGGESTIONS)
st.write("they are Klilos modding tool contributors")

st.caption("idk i just take the bio on ur discord")
st.caption("open a PR or issue if you want to change it")
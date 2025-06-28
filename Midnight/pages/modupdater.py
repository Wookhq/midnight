import streamlit as st
from modules.sidebar.sidebar import InitSidebar

InitSidebar()

from pathlib import Path
from modules.mod_updater import ModUpdater
from modules.deployments import DeployHistory

# this shit gonna be hard

@st.cache_data
def load_deploy():
    deploy = DeployHistory()
    print(deploy)
    return deploy.player_deployments[-10:]

deploys = load_deploy()
sober_cp = "Sober compatible" # SOBER CP 💀💀
obj = object()
options = [(sober_cp, obj)] + [
    (f"{d.file_version} ({d.guid})", d) for d in deploys
]
col1, col2 = st.columns(2)
labels, values = zip(*options)

with col1:
    mod_path = st.text_input("Path to the mod folder", placeholder="e.g : ~/sigmafolder/Blue-star-modz")

with col2:
    mod_ver_display = st.selectbox("Mod version", options=labels)
    selected = values[labels.index(mod_ver_display)]

    if selected is obj:
        mod_ver = "do sum"
    else:
        mod_ver = selected.file_version

    if st.button("Update"):
        print("sigma! its do nothing!")



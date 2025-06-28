import streamlit as st
from modules.sidebar.sidebar import InitSidebar

InitSidebar()

from pathlib import Path
from modules.mod_updater import ModUpdater
from modules.deployments import DeployHistory

# this shit gonna be hard


def UpdateMod(modpath: Path, version, ForceOverWrite : False):
    history = DeployHistory()
    target_version = next(
        (v for v in reversed(history.studio_deployments) if v.file_version.minor == version),
        None
    )
    if not target_version:
        raise Exception(f"Version {version} not found")
    if ModUpdater.check_for_updates(modpath, target_version):  # fixed here
        print(f"Updating {modpath} to version {version}...")
        ModUpdater.update_mod(modpath, target_version)
        print("Update completed ✅")
    else:
        print("Mod is already up-to-date ❎")





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
        mod_ver = "do sum"  # custom logic i think
    else:
        mod_ver = selected  

    if st.button("Update"):
        # if isinstance(mod_ver, str):
        #     st.write("Selected version:", mod_ver)
        # else:
        #     st.write("Selected version:", mod_ver.file_version)
        #     st.write("GUID:", mod_ver.guid)
        #     st.write("Binary Type:", mod_ver.binary_type)
        UpdateMod()



import streamlit as st

from modules.project_data import ProjectData
from modules.localization import Localizer
from modules.filesystem import Resources, Directories
from modules.mod_updater import ModUpdater
from modules.interfaces.config import ConfigInterface
from modules.deployments import LatestVersion
from modules import filesystem
from modules.logger import Logger

# this shit gonna be hard
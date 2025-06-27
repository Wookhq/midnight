from dataclasses import dataclass
from typing import Optional
import os

@dataclass
class Contributor:
    name: str
    url: Optional[str] = None,
    text : Optional[str] = None,


CONTRIBUTORS: list[Contributor] = sorted([], key=lambda item: item.name.casefold())

FEATURE_SUGGESTIONS: list[Contributor] = sorted([
    Contributor("Vortex", r"https://github.com/VolVortex"),
    Contributor("return_request", r"https://github.com/returnrqt"),
    Contributor("kw_roblox"),
    Contributor("NetSoftworks", r"https://github.com/netsoftwork"),
    Contributor("dooM", "https://github.com/MistressDoom", "download my mods"),
    Contributor("Toast"),
    Contributor("Xale", r"https://github.com/fakexale", "i code, for fun, sometimes, my home, with my brain"),
    Contributor("Klilo",r"https://github.com/TheKliko", "Roblox modder and programmer")
], key=lambda item: item.name.casefold())

SPECIAL_THANKS: list[Contributor] = sorted([], key=lambda item: item.name.casefold())
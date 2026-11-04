"""Estate IQ - Real Estate Investment Advisor.
Run from the project root with: streamlit run app/app.py
"""
import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

st.set_page_config(
    page_title="Estate IQ · Real Estate Investment Advisor",
    page_icon=str(ROOT / "assets" / "estate_iq_mark.png"),
    layout="wide",
    initial_sidebar_state="collapsed",
)

from core import theme  # noqa: E402

theme.inject_css()

PAGES = [
    ("Home", "views/home.py", True),
    ("Analyse", "views/predict.py", False),
    ("Market Atlas", "views/market_atlas.py", False),
    ("Insights", "views/insights.py", False),
    ("AI Advisor", "views/advisor_page.py", False),
    ("Performance", "views/performance.py", False),
    ("About", "views/about.py", False),
]

nav = st.navigation(
    [
        st.Page(path, title=label, default=is_default)
        for label, path, is_default in PAGES
    ],
    position="hidden",
)

with st.container(key="topnav"):
    cols = st.columns(
        [1.7, 0.8, 0.8, 1.15, 0.9, 1.1, 1.1, 0.8],
        vertical_alignment="center",
    )

    with cols[0]:
        st.markdown(
            '<div class="brand">'
            '<span class="brand-mark"></span>'
            '<span class="brand-text">Estate IQ</span>'
            '</div>',
            unsafe_allow_html=True,
        )

    for col, (label, page_path, _is_default) in zip(cols[1:], PAGES):
        with col:
            if st.button(
                label,
                key=f"nav_{label.lower().replace(' ', '_')}",
                use_container_width=True,
            ):
                st.switch_page(page_path)

nav.run()
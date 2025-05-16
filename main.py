import streamlit as st
from src.personal.projects_overview import show as show_projects_overview

st.set_page_config(
    page_title="Kasper Atkinson", 
    page_icon="src/assets/Short_LOGO.png"
)

about_page = st.Page("src/personal/homepage.py", title="About Me", icon=":material/home:")
CV_page = st.Page("src/personal/resume_page.py", title="Cirriculum Vitae", icon=":material/description:")

projects_page = st.Page(show_projects_overview, title="All Projects", icon=":material/build:")
webstite_page = st.Page("pages/website_page.py", title="Portfolio Website")
kart_page = st.Page("pages/kart_page.py", title="Go-Karting")
bruh_page = st.Page("pages/bruh_page.py", title="Bruh Moment")
sizing_page = st.Page("pages/sizing_page.py", title="Propulsion Sizing")

pg = st.navigation(
    {
        "Personal": [about_page, CV_page],
        "Projects": [projects_page, webstite_page, kart_page, bruh_page, sizing_page],
    }
)

pg.run()
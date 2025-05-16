import streamlit as st

def show():
    st.title("Projects")

    projects = [
        {
            "name": "Propulsion Sizing",
            "image": "src/assets/Short_LOGO.png",
            "blurb": "A tool for sizing propulsion systems for model aircraft.",
            "page": "pages/sizing_page.py"
        },
        {
            "name": "Go-Karting",
            "image": "src/assets/download.png",
            "blurb": "A tool for sizing propulsion systems for model aircraft.",
            "page": "pages/kart_page.py"
        },
        {
            "name": "Porfolio Website",
            "image": "src/assets/download.png",
            "blurb": "A tool for sizing propulsion systems for model aircraft.",
            "page": "pages/website_page.py"
        },
        {
            "name": "Bruh moment",
            "image": "src/assets/Headshot.jpg",
            "blurb": "If you know, you know. It is never possible to be too careful when avoiding a bruh moment.",
            "page": "pages/bruh_page.py"
        },
    ]

    projects_per_row = 3
    for i in range(0, len(projects), projects_per_row):
        row_projects = projects[i:i+projects_per_row]
        while len(row_projects) < projects_per_row:
            row_projects.append(None)
        cols = st.columns(projects_per_row)
        for idx, project in enumerate(row_projects):
            with cols[idx]:
                if project is not None:
                    st.image(project["image"], use_container_width=False, width=200)
                    if st.button(
                        label=f"**{project['name']}**",
                        key=f"btn_{project['name']}",
                        help=project["name"],
                    ):
                        st.switch_page(project["page"])
                    st.caption(project["blurb"])
                else:
                    st.empty()
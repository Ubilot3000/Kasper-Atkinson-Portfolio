import streamlit as st

st.write("# Cirriculum Vitae")

st.markdown(
    """
    ## Education
    - **Cornell University** (Ithaca, NY)  
      Bachelor of Science in Mechanical Engineering, Expected May 2027

    ## Experience
    - **Design Build Fly** (Ithaca, NY)  
      *Team Lead*, August 2022 - Present  
      - Lead a team of 20 students in the design and construction of an unmanned aerial vehicle for the AIAA DBF competition.
      - Managed project timelines and deliverables, ensuring successful completion of all phases of the project.

    ## Skills
    - Programming: Python, MATLAB, Java
    - Software: SolidWorks, Fusion360, ANSYS
    - 

    ## Languages
    - English (C2)
    - Polish (C2)
    - French (B2)
    - German (B1)
    """
)

st.download_button(
    label="Download CV",
    data=open("src/assets/IROP_CV.pdf", "rb").read(),
    file_name="Kasper_Atkinson_CV.pdf",
    mime="application/pdf"
)

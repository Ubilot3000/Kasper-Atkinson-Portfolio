import streamlit as st

st.write("# About Me")

col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed

with col1:
    st.image("src/assets/Headshot.jpg", width=500)

with col2:
    st.markdown(
        """
        Heyo! I’m Kasper.

        I’m a learner. Every time I approach an obstacle, something I don’t quite understand, it excites me. 
        I become motivated by the pursuit of the unknown. Because it’s difficult, and I find the struggle rewarding.

        That’s why I am an engineer. 
        It’s also why I’m particularly interested in aerospace. 
        I search for boundaries to break and new ideas to form. 
        I hope to be on the cutting edge of the unknown.
        """
    )

st.markdown(
    """
    At Cornell’s Design Build Fly, I’ve had three years of experience as a member, subteam lead, and now full-lead, working through every part of the design cycle. 
    From the time rules come out in August, to our compeition in April, I am non-stop at work: ideating, redesigning, improvising. 
    Everything always breaks the first time around. Then the second. Then, if you’re unlucky, the third. But I couldn’t imagine anything different. 
    Never do I learn so much in such a short time, and never is it as rewarding.    
    """
)
import streamlit as st
import base64
import streamlit as st
import time
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def show_pdf(file_path):
    with open(file_path, "rb") as file:
        base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

def plot_prop_iterations(df):
    # Get unique diameters and pitches
    diameters = [col for col in df.columns if col != 'Pitch']
    pitches = df['Pitch'].values
    
    # Create base figure
    fig = go.Figure()
    plot_container = st.empty()
    
    # Initialize empty lists for each diameter's data
    diameter_data = {diameter: {'x': [], 'y': []} for diameter in diameters}
    
    # Add a trace for each diameter with smoother line interpolation
    for diameter in diameters:
        fig.add_trace(
            go.Scatter(
                x=[],
                y=[],
                mode='lines+markers',
                name=f'{diameter}" Diameter',
                marker=dict(size=6),  # Smaller markers
                line=dict(shape='spline', smoothing=1.3)  # Smoother lines
            )
        )
    
    # Update layout with animation settings
    fig.update_layout(
        title='Propeller Static Thrust as a Function of Propeller Geometry',
        xaxis_title='Pitch (inches)',
        yaxis_title='Static Thrust (g)',
        width=800,
        height=600,
        showlegend=True,
        transition_duration=500,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.80
        ),
        transition=dict(
            duration=300,
            easing='cubic-in-out'
        )
    )
    
    # Update data diameter by diameter, pitch by pitch
    for i, diameter in enumerate(diameters):
        for pitch in pitches:
            # Update current diameter's data
            thrust = df[df['Pitch'] == pitch][diameter].values[0]
            diameter_data[diameter]['x'].append(pitch)
            diameter_data[diameter]['y'].append(thrust)
            
            # Update only the current diameter's trace
            fig.data[i].x = diameter_data[diameter]['x']
            fig.data[i].y = diameter_data[diameter]['y']
            
            # Display updated figure
            plot_container.plotly_chart(fig, use_container_width=True)
            time.sleep(0.05)  # Adjust animation speed


st.markdown(
    """
        # Propulsion Sizing
        **Background:**
    
        Finishing my freshmen year with a summer to look forward to, I found myself thinking about what skills
        I wanted to develop. I had a few ideas, but nothing concrete. Looking through old folders on my project team's
        shared drive, I stumbled upon an old end-of-semester report detailing the sizing of the propulsion system.
        As a freshman, I had no experience with it. Our previous leardership had been in charge of the process. However,
        I was determined to learn more about it. I spent the summer researching and learning about electric propulsion.


    """
)

df = pd.read_csv("src/assets/thrust_itr_data.csv")
plot_prop_iterations(df)

st.empty_space = st.empty()

st.markdown(
    """
        **Goals:**

        Setting out to learn, I wanted to give myself a few goals to work towards, as well as some structure.
        To that end, I laid out three main targets:
        - Learn about the sizing process and the factors that affect it. Identify the key parameters and their relationships.
        - Create a tool that can be used to size the propulsion system for future projects. This tool should be easy to use and
        understand, and should be able to handle a variety of inputs.
        - Document the process and the tool, so that future team members can understand and use it. This documentation should
        be clear and concise, and should include examples of how to use the tool.
    """
)

st.empty_space = st.empty()

st.markdown(
    """
        **Process:**

        I started with what I half-knew: eCalc, the current website we used to compute electrical performance. Although
        the code I had to work from was written in Java and outdated, I used it as a starting point. Slowly, I began 
        to understand the tens of inputs and outputs that eCalc provided. As my knowed
    """
)

st.image("src/assets/eCalc.png", caption="Parameter input page of eCalc.", use_container_width=True)



# Display the PDF from your assets folder
show_pdf("src/assets/Prop_Sizing.pdf")
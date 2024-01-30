# Import necessary libraries
import streamlit as st
from openai import OpenAI

# Set the API key for OpenAI
client = OpenAI(api_key=st.secrets.keyy)

# Streamlit app title and page configuration
st.set_page_config(
    page_title="EssayExpress Pro 📝",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header and subheader with styling
st.markdown("<h1 style='color: #ff6757;'>EssayExpress Pro</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #ff6757;'>Turbocharge Your Essay Writing Genius with Custom Key Points in Minutes!</h3>", unsafe_allow_html=True)
st.markdown("<p style='color: #ff6757; font-size: small;'>Note: Basically it tells you what to write and how to write (Key point brainstorming), but writing depends on your creativity</p>", unsafe_allow_html=True)

# Sidebar section for user input
st.sidebar.header("User Input")
topic = st.sidebar.text_input("What is the topic?", "Enter the topic here")
point_no = st.sidebar.number_input("How many points will be in the essay?", min_value=1, value=3)
subp_no = st.sidebar.number_input("How many subpoints will be in the essay?", min_value=1, value=2)

# Function to interact with OpenAI API
def generate_essay(user_prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_prompt}]
    )
    return completion.choices[0].message.content

# Execute the OpenAI function with user input
user_prompt = st.secrets.prmpt
response = generate_essay(user_prompt)

# Display the output in a container with styling
st.markdown("<h2 style='color: #7041ce; margin-top: 20px;'>Generated Essay:</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='color: #7041ce; font-weight: bold;'>{response}</p>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='font-family: Montserrat; color: #7041ce; font-size: small; margin-top: 50px; text-align: center;'>Developed by Md. Taseen Alam</p>", unsafe_allow_html=True)

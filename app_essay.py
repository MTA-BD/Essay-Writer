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
user_prompt = f"Suppose you are an expert in English language and Essay writing with an experience of 30 years. Now you have to help me in writing an essay about {topic} Begin by writing an awesome title for the essay. Then, you have to write an extraordinary and unique Topic sentence for the essay. Write the topic sentence in different sections. Then write an introduction paragraph. Then write {point_no} points on the topic sentence for the essay. Then add the description for each point. Remember to provide the descriptions in more than {subp_no} subpoints for each main point. Remember that the main points of the essay must be related and led by the Topic sentence. Keep the main points unique from one another. Remember to give information in the essay where needed. Add reference to the information. But don't use information too much. Add one real quote of a famous person completely related to the point of the essay. Don't give any kind of unreal quote which was not told by any speaker. Also, the reference of the quote, that means by whom, where, and when the quote was told, must be added beside the quote. Remember to give an idea of the main idea of the essay and the ideas of each main point in the introduction paragraph. You must write the introduction paragraph as like as the reader will be highly interested in the essay. But don't give the spoiler and the whole thing in the intro paragraph; so that the reader will be interested to read the whole paragraph. At last, write a conclusion point. In the conclusion paragraph, summarize the whole essay in a few sentences. But keep in mind that the intro and conclusion para won't be completely the same. Bold and Highlight the words which are like the ornaments of the sentences or the artistic words, which will bear the witness of language proficiency, of the introduction and conclusion para. Also write real quotes for the intro and the conclusion paragraph. If you use any artistic word or sentences, give the explanation of those in understandable and easy language; so that I can understand them properly."
response = generate_essay(user_prompt)

# Display the output in a container with styling
st.markdown("<h2 style='color: #7041ce; margin-top: 20px;'>Generated Essay:</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='color: #7041ce; font-weight: bold;'>{response}</p>", unsafe_allow_html=True)

# Footer
st.markdown("<p style='font-family: Montserrat; color: #7041ce; font-size: small; margin-top: 50px; text-align: center;'>Developed by Md. Taseen Alam</p>", unsafe_allow_html=True)

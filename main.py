import streamlit as st
import random
from post_generator import generate_post
from llm_helper import llm

# Initialize session state for history if not present
if "post_history" not in st.session_state:
    st.session_state.post_history = []

# ----------------- UI Config --------------------
st.set_page_config(page_title="Streamlit", layout="centered")

# ----------------- Custom CSS --------------------
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #1E90FF;
        text-align: center;
        padding: 10px;
    }
    .stApp {
        background-color: var(--background-color);
        transition: background-color 0.5s ease;
    }
    div.stButton > button {
        background-color: #add8e6;
        color: #003366;
        font-size: 16px;
        height: 3em;
        width: 15em;
        border-radius: 10px;
        border: 2px solid #1E90FF;
        margin: auto;
        display: block;
        transition: 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #87cefa;
        border-color: #4682B4;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- Header --------------------
st.markdown('<div class="title">💡 LinkedIn Post Generator 💡</div>', unsafe_allow_html=True)

st.markdown("#### 📢 Say it better. Say it brilliantly..")

# ----------------- Dark Mode Toggle --------------------
dark_mode = st.toggle("🌙 Dark Mode")
if dark_mode:
    st.markdown("""
        <style>
            .stApp {
                --background-color: #1e1e1e;
                --text-color: #ffffff;
            }
            .title {
                color: #87CEFA;
            }
            h1, h2, h3, h4, h5, h6, p, label, .css-10trblm, .css-1v0mbdj, .css-1kyxreq {
                color: white !important;
            }
            .stTextInput, .stSelectbox, .stTextArea {
                background-color: #2e2e2e !important;
                color: white !important;
            }
            div.stButton > button {
                background-color: #4682B4;
                color: white;
                border-color: #87CEFA;
            }
            div.stButton > button:hover {
                background-color: #5daee3;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            .stApp {
                --background-color: #ffffff;
                --text-color: #000000;
            }
            .title {
                color: #1E90FF;
            }
            h1, h2, h3, h4, h5, h6, p, label, .css-10trblm, .css-1v0mbdj, .css-1kyxreq {
                color: black !important;
            }
        </style>
    """, unsafe_allow_html=True)

# ----------------- Input Selection --------------------
tags = [
    "Python", "Data Science", "AI", "Machine Learning", "Web Development",
    "Startups", "Leadership", "Open Source", "Career", "Cloud",
    "Education", "Productivity", "Mental Health", "Motivation"
]
languages = ["English", "Hinglish", "Marathi", "Gujarati", "French"]
tones = ["Professional", "Casual", "Motivational", "Witty"]

col1, col2 = st.columns(2)

with col1:
    selected_length = st.selectbox("🧵 Choose Post Length", ["Short", "Medium", "Long"])
with col2:
    selected_language = st.selectbox("🌍 Choose Language", languages)

selected_tone = st.selectbox("🎭 Choose Tone/Style", tones)

selected_option = st.radio("📌 Choose Topic Type", ["Select from list", "Write my own"])
if selected_option == "Select from list":
    selected_tag = st.selectbox("Choose a Topic", tags)
else:
    selected_tag = st.text_input("Enter your custom topic")

# ----------------- Inspire Me --------------------
if st.button("💡 Inspire Me!"):
    selected_length = random.choice(["Short", "Medium", "Long"])
    selected_language = random.choice(languages)
    selected_tone = random.choice(tones)
    selected_tag = random.choice(tags)
    st.success(f"Inspired! Length: {selected_length}, Language: {selected_language}, Tone: {selected_tone}, Tag: {selected_tag}")

# ----------------- Generate Post --------------------
if st.button("🛠️ Generate Post"):
    if selected_option == "Write my own" and not selected_tag.strip():
        st.warning("Please enter a custom topic before generating.")
    else:
        with st.spinner("Crafting your post... ⏳"):
            post = generate_post(selected_length, selected_language, selected_tag, selected_tone)
            st.success("Here you go..")
            st.text_area("📄 Your LinkedIn Post", post, height=200, disabled=False)

            # 🎉 Animation (Confetti)
            st.balloons()

            # 🕘 Save to History
            st.session_state.post_history.append(post)

            # 🔎 Hashtag Suggestions
            with st.expander("🔖 Suggested Hashtags"):
                tag_prompt = f"""
                Generate 5 to 7 relevant hashtags for a LinkedIn post with the following topic: {selected_tag}.
                Use popular but meaningful hashtags related to the topic.
                Return only the hashtags.
                """
                tags_response = llm.invoke(tag_prompt)
                hashtags = tags_response.content.strip()
                st.markdown(hashtags)

# ----------------- Post History --------------------
if st.session_state.post_history:
    st.markdown("## 📜 Your Post History")
    for i, p in enumerate(reversed(st.session_state.post_history[-5:]), 1):
        st.markdown(f"**{i}.** {p}")

# ----------------- Footer --------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("🔷 *Built for creators who want to shine on LinkedIn!!*", unsafe_allow_html=True)

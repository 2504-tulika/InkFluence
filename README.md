<h1 align="center">💡 LinkedIn Post Generator</h1>
<p align="center">
  Effortlessly craft creative, professional, and personalized LinkedIn posts in seconds.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/LLM-Llama 3-blueviolet?logo=openai" />
  <img src="https://img.shields.io/badge/Groq-Accelerated-success?logo=groq" />
</p>

---

## 🎯 Features

- 🌗 **Dark Mode Toggle** for a smoother user experience
- 📝 **Multi-language Support** – English, Hinglish, Marathi, Gujarati, French
- 🎭 **Tone & Style Selector** – Professional, Casual, Motivational, Witty
- 📌 **Topic & Tag Selection**
- 💡 **“Inspire Me” Button** to auto-generate random post parameters
- 🎉 **Post Animation** – Balloons on generation!
- 🕘 **Post History Tracking**
- 🔖 **Hashtag Suggestions** using LLM
- ✍️ **Editable Post Field** so you can tweak your output easily

---

## 🖼️ UI Preview

| Home Interface | Post Generated | Hashtag Suggestions |
| -------------- | -------------- | ------------------- |
| ![UI 1](Screenshots\Home Interface.png) | ![UI 2](Screenshots\Post Generated.png) | ![UI 3](Screenshots\Suggested Hashtags.png) |

---

## 🧠 How It Works

1. User selects language, tone, length, and topic.
2. Post is generated using LLM (Llama 3.2 via Groq Cloud).
3. Suggestions and hashtags are also dynamically generated.
4. Post is saved and can be edited or reused from history.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **LLM Integration:** LangChain + Llama 3 via Groq Cloud
- **Backend:** Python
- **Styling:** Custom CSS

---

## 📦 Installation

```bash
git clone https://github.com/your-username/linkedin-post-generator.git
To get started we first need to get an API_KEY from here: https://console.groq.com/keys.
Inside `.env` update the value of `GROQ_API_KEY` with the API_KEY you created. 
pip install -r requirements.txt
streamlit run main.py

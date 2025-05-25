# WikiAnswerAI 📚🔍🤖

**WikiAnswerAI** is an AI-powered question-answering application designed to make Wikipedia searches more effective.
Users can enter a specific topic title and filter relevant pages. Based on the retrieved content, the user can ask a question, and the system generates a clear answer derived from Wikipedia, along with references to the source content.

---
## 📸 Screenshots

* #### Search & Filter
![WikiAnswerAI](https://github.com/user-attachments/assets/46b2fcd8-ef14-411a-90a1-752694bc83ee)

* #### Question
![WikiAnswerAI](https://github.com/user-attachments/assets/969bffb5-0307-4427-9a35-6a4d96c08a58)

* #### Answer & Sources
![WikiAnswerAI](https://github.com/user-attachments/assets/d5a575f4-d760-414f-9f96-a2e9f53bd0d5)

---

## 🖥️ Demo

🔗 [WikiAnswerAI](https://wikianswerai.streamlit.app)

---

## 🚀 Features

* Content filtering from Wikipedia based on the topic title
* Generates meaningful answers based on the filtered content
* Splits content into manageable chunks
* Converts the chunks into embeddings and performs semantic similarity analysis
* Displays the source snippets that support the answer
* Easy-to-use Streamlit interface
* Supports both **OpenAI** and **Gemini** LLM models for answering questions

---

## 🌟 Why WikiAnswerAI?

Even if the desired information exists in a Wikipedia article, it can sometimes be difficult to locate. Reading the entire text or extracting a meaningful answer can be time-consuming.
**WikiAnswerAI** was developed to address this issue by:

* Retrieving content based on specific titles
* Analyzing meaningful paragraphs within the content
* Providing direct answers to user questions with cited sources

---

## 🔧 Installation & Run

```bash
git clone https://github.com/furkankarakuz/WikiAnswerAI.git
cd WikiAnswerAI
pip install -r requirements.txt
streamlit run app/main.py
```

---

## 📄 License

This project is licensed under the Apache License 2.0

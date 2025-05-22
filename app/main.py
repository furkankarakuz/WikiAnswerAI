import streamlit as st
from components.sidebar import sidebar_block
from utils import init_session_state, widget_control, get_documents, ask_question

st.set_page_config(page_title="WikiAnswerAI", page_icon="app/images/icon.png")

st.image("app/images/banner.png", use_container_width=True)
st.divider()

init_session_state()

with st.sidebar:
    model_info, chunk_info = sidebar_block()

documents = []
st.subheader("Filter :mag:")
subject_text = st.text_input("Search Subject For Filter", key="subject_text")

load_max_doc = st.slider("Max Load Document", 1, 10, 5, 1, key="max_doc")
select_lang = st.radio("Language", options=["EN", "TR"], key="language")

subject_button = st.button("Search", key="subject_button")
st.html("<br>")


if subject_button or (st.session_state["response"] and st.session_state["ask_button"]):
    if subject_button:
        get_documents.clear()
        st.session_state["response"] = ""

    if (message := widget_control()):
        st.toast(message, icon="⚠️")

    else:
        documents = get_documents(subject_text, select_lang, load_max_doc)
        st.subheader("Question :question:")

        question_text = st.text_area("Write Your Question", key="question_text", value=st.session_state["question_text"])
        ask_button = st.button("Ask Button", key="ask_button", on_click=ask_question, args=(documents, model_info, chunk_info))


if st.session_state["ask_button"] and st.session_state["response"]:
    st.html("<br>")
    st.subheader("Answer :memo:")
    st.write(st.session_state["response"]["answer"])

    st.html("<br>")
    st.subheader("Sources :books:")

    for title, url in st.session_state["response"]["source"].items():
        st.html(f"<a href='{url}' target='_blank'><b>{title}</b></a>")

import os
import sys
import streamlit as st


process_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if process_dir not in sys.path:
    sys.path.append(process_dir)


def init_session_state():
    defaults = {"model_type": "GPT", "model_name": "gpt-4o", "api_key": "", "subject_text": "", "question_text": "", "language": "EN", "response": "", "ask_button": ""}

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def widget_control(control_type="wiki_control"):
    if not (st.session_state["model_name"] and st.session_state["api_key"]):
        return "Select a model and / or Write Your API Key"

    elif not st.session_state["subject_text"]:
        return "Write Text For Filter"

    if control_type == "search_control":
        if not st.session_state["question_text"]:
            return "Write Your Question"


@st.cache_data
def get_documents(*args):
    from process.rag_process import wiki_search
    st.session_state["response"] = ""
    return wiki_search(*args)


def ask_question(*_args):
    from process.rag_process import RagWiki
    if (message := widget_control("search_control")):
        st.toast(message, icon="⚠️")
        st.session_state["response"] = ""
    else:
        rw = RagWiki(*_args)
        st.session_state["response"] = rw.get_answer(st.session_state["question_text"])

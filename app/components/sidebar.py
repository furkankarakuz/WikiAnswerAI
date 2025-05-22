import streamlit as st


def sidebar_block():
    model_dict = {"GPT": ["gpt-4o", "gpt-4-turbo", "gpt-4", "gpt-3.5-turbo", "Other"], "Gemini": ["gemini-2.0-flash", "gemini-2.0-flash-lite", "gemini-1.5-flash", "gemini-1.5-pro", "Other"]}

    with st.popover("Select Model :point_down:"):
        model_type = st.radio("Model", options=["GPT", "Gemini"], key="model_type")

        if model_type:
            model_name = st.selectbox(f"Select {model_type} Model :robot_face:", options=model_dict[model_type], key="model_name")
            other_model = st.empty()
            if model_name == "Other":
                other_model = st.empty()
                other_model = other_model.text_input(f"Write {model_type} Model", key="other_model")
                model_name = other_model

                del other_model

            else:
                other_model.empty()

            api_key = st.text_input("API Key :key:", type="password", key="api_key")

    st.html("<h3>Model Detail</h3><hr>")
    st.write(f"Selected Model :robot_face: : {model_name}")

    if api_key:
        st.write(f"API KEY :key: : {api_key[:3]+(' * '*len(api_key[3:10]))+'...'}")

    st.html("<br><h3>Settings ⚙️<h3><hr>")
    chunk_size = st.slider("Chunk Size", 250, 3000, 1000, 250, key="chunk_size")
    chunk_overlap = st.slider("Chunk Size", 0, 500, 200, 100, key="chunk_overlap")

    model_info = {"model_type": model_type, "model_name": model_name, "api_key": api_key}
    chunk_info = {"chunk_size": chunk_size, "chunk_overlap": chunk_overlap}

    return model_info, chunk_info

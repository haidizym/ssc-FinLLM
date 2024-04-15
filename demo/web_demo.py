import os

import streamlit as st
import torch
from transformers.utils import logging

from transformers import AutoTokenizer, AutoModelForCausalLM  # isort: skip
from openxlab.model import download

logger = logging.get_logger(__name__)

model_name = "./ssc-finllim-model"

os.system(f'git clone https://code.openxlab.org.cn/zhuyamei/ssc-FinLLM.git {model_name}')
os.system(f'sudo apt-get update && sudo apt-get install git-lfs')
os.system(f'cd {model_name}  && git lfs install && git lfs pull')

def on_btn_click():
    del st.session_state.messages


@st.cache_resource
def load_model():
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True, torch_dtype=torch.float16)
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    model = model.eval()
    return model, tokenizer


def main():
    # torch.cuda.empty_cache()
    print("load model begin.")
    model, tokenizer = load_model()
    print("load model end.")

    user_avator = "assets/user.png"
    robot_avator = "assets/robot.png"

    st.title("FinLLM-ssc")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message.get("avatar")):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("请输入问题？"):
        # Display user message in chat message container
        with st.chat_message("user", avatar=user_avator):
            st.markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt, "avatar": user_avator})

        with st.chat_message("robot", avatar=robot_avator):
            message_placeholder = st.empty()
            for response, history in model.stream_chat(tokenizer, prompt, [], temperature=0.1):
                # Display robot response in chat message container
                message_placeholder.markdown(response + "▌")
            # response, history = model.chat(tokenizer, prompt, history=[])
            message_placeholder.markdown(response)  # pylint: disable=undefined-loop-variable
        # Add robot response to chat history
        st.session_state.messages.append(
            {
                "role": "robot",
                "content": response,  # pylint: disable=undefined-loop-variable
                "avatar": robot_avator,
            }
        )
        torch.cuda.empty_cache()


if __name__ == "__main__":
    main()

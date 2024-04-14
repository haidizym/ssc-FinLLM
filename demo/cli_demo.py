import os
import platform
import signal

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from openxlab.model import download

model_name = "./ssc-finllim-model"

os.system(f'git clone https://code.openxlab.org.cn/zhuyamei/ssc-FinLLM.git {model_name}')
os.system(f'cd {model_name} && git lfs pull')

model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True,
                                             torch_dtype=torch.float16)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = model.eval()

os_name = platform.system()
clear_command = 'cls' if os_name == 'Windows' else 'clear'
stop_stream = False


def build_prompt(history):
    prompt = "欢迎使用 FinLLM-ssc 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序"
    for query, response in history:
        prompt += f"\n\n用户：{query}"
        prompt += f"\n\nFinLLM-ssc：{response}"
    return prompt


def signal_handler(signal, frame):
    global stop_stream
    stop_stream = True


def main():
    history = []
    global stop_stream
    print("欢迎使用 FinLLM-ssc 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
    while True:
        query = input("\n用户：")
        if query.strip() == "stop":
            break
        if query.strip() == "clear":
            history = []
            os.system(clear_command)
            print("欢迎使用 FinLLM-ssc 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序")
            continue
        count = 0
        for response, history in model.stream_chat(tokenizer, query, history=history, temperature=0.1):
            if stop_stream:
                stop_stream = False
                break
            else:
                count += 1
                if count % 8 == 0:
                    os.system(clear_command)
                    print(build_prompt(history), flush=True)
                    signal.signal(signal.SIGINT, signal_handler)
        os.system(clear_command)
        print(build_prompt(history), flush=True)


if __name__ == "__main__":
    main()

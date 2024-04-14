from openai import OpenAI
import json
import random
import os

from uitls.logger import get_logger
from uitls.uitl import read_json

client = OpenAI(api_key="sk-Ym7O*********",
                base_url="https://api.fe8.cn/v1")
logger = get_logger()


def get_selected_sample(entry):
    entry_announcement = entry.get("text", "")
    entry_announcement = entry_announcement[:4000]

    entry_title = entry.get("title", "")

    title_text = f"{entry_title} {entry_announcement}"
    return title_text


def get_gpt_answer(prompt):
    messages = [{"role": "system", "content": "请你扮演金融行业的专家。"},
                {"role": "user", "content": prompt}]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4",
    )

    return chat_completion.choices[0].message.content


def build_data(announcement_data, json_file_path, output_txt_file_path):
    all_contents = []
    json_data = read_json(json_file_path)
    for entry in announcement_data:
        selected_data = random.choice(json_data)
        title_text = get_selected_sample(entry)

        prompt = (
            f"以下提供一道json格式的金融行业的问答题请你学习，它包括以下字段："
            f"领域分类、评测问题、答案，"
            f"金融行业问答题的领域分类包括了人力资源管理、企业管理分析、公司财务分析、公告事实理解、决策过程分析、市场分析、影响评估、战略规划分析、"
            f"投资分析、文本情绪识别、法律合规性评估、经营效率分析、资产管理分析、资本市场基础知识、逻辑推理拓展、金融基本知识16类。"
            f"问题文本里包含了金融行业的相关背景，"
            f"参考问答题具体内容如下：{selected_data} 现在给你一份公司公告和公告标题，具体内容如下:{title_text}"
            f"参照给的问答题样例，请你分析公告内容和公告标题，生成json格式的5道金融行业问答题，"
            f"要求生成的5道问答题领域分类各不相同且内容字段包括对应公告标题、领域分类、问题、答案。问题和答案要逻辑清晰。")

        answer = get_gpt_answer(prompt)
        all_contents.append(answer)

    with open(output_txt_file_path, 'w', encoding='utf-8') as output_txt_file:
        for content in all_contents:
            output_txt_file.write(content + '\n')

    logger.info(f"所有生成数据已保存到 {output_txt_file_path}")


def main():
    announcement_json_file_path = './data/4家公告预处理后.json'
    announcement_data = read_json(announcement_json_file_path)

    subjective_data_path = './data/subjective_data.json'
    subjective_out_path = './out/subjective_gpt4_out.txt'
    build_data(announcement_data, subjective_data_path, subjective_out_path)

    objective_data_path = './data/objective_data.json'
    objective_out_path = './out/objective_gpt4_out.txt'
    build_data(announcement_data, objective_data_path, objective_out_path)


if __name__ == '__main__':
    main()


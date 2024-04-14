import json
import random

from uitls.uitl import read_json

paths = [r"./out/subject_out.jsonl", r"./out/object_out.jsonl"]
info_path = r"./data/4家代表性上海知名上市公司全年公告数据集.json"

templates = ["多选题：{content}  \n {A}  {B} {C} {D} \n 请选择正确的一个或多个答案。 请选择正确的一个或多个答案。"]


infos = read_json(info_path)

outs = []

for path in paths:
    datas = []
    with open(path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            print(line)
            data = json.loads(line)
            datas.append(data)

    question_tmp = "{question} \n 公告： {info}"

    count = 0
    for i in datas:
        in_flag = False
        for j in infos:
            if i["公告标题"].replace("：", ":").replace("'", "").replace("（", "(").replace("）", ")") in j["title"]:
                in_flag = True

                content = question_tmp.format(question=i["问题"], info=j["text"])

                A = ""
                B = ""
                C = ""
                D = ""

                if i["选项A"] is not None and i["选项A"] != "":
                    A = "选项A: " + str(i["选项A"])

                if i["选项B"] is not None and i["选项B"] != "":
                    B = "选项B: " + str(i["选项B"])

                if "选项C" in i and i["选项C"] is not None and i["选项C"] != "":
                    C = "选项C: " + str(i["选项C"])

                if "选项D" in i and i["选项D"] is not None and i["选项D"] != "":
                    D = "选项D: " + str(i["选项D"])

                template = random.choice(templates)

                question = template.format(content=content, A=A, B=B, C=C, D=D)

                out = {"conversation": [{
                    "system": "请使用自己的话回答内容，不能重复语料中的话，尽可能生动和有创造性。",
                    "input": question,
                    "output": str(i["答案"]) + "。" + str(i["推理过程"])
                }]}

                outs.append(out)

                break
        if not in_flag:
            count += 1

    print(count)

with open("./out/train_data_pt.json", 'w+', encoding="utf-8") as f:
    json.dump(outs, f, ensure_ascii=False)




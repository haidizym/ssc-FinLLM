import json

from openpyxl.reader.excel import load_workbook




'''
格式示例：

第一题：
{ 
'题目类型': '金融行业多项选择题',
'对应公告标题': '关于使用闲置募集资金进行现金管理的进展公告',
'领域分类': '企业管理分析',
'问题': '金龙鱼闲置募集资金进行现金管理的操作，体现出的公司治理理念是什么？',
'选项A': '风险管理',
'选项B': '保证流动性',
'选项C': '资本利润最大化',
'选项D': '资产保值增值',
'答案': 'A、B、C、D',
'推理过程': '有效进行现金管理可以反映公司治理具备风险管理的能力(A选项正确)，同时保证公司运营的流动性(B选项正确)。另外，投资安全性高、流动性好、满足保本要求的投资产品，目的是对资本进行利润最大化(C选项正确)，同时保证资产的保值和增值(D选项正确)。综上，答案为：A、B、C、D。'
}”
'''

def read_json_data(f_path):
    datas = []
    json_flag = False
    json_str = ""
    with open(f_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            if line.strip() == "{":
                json_flag = True

            if line.strip() == "}" or line.strip() == "},":
                json_str += line.replace(",", "")
                json_str = json_str.replace("\'", "\"").replace("\n", "")

                data = {}
                try:
                    data = json.loads(json_str)
                    datas.append(data)
                except:
                    # 格式无法识别的会打印出来
                    print(json_str)

                json_flag = False
                json_str = ""

            if json_flag:
                json_str += line

    return datas


def main():
    objective_path = r"./out/objective_gpt4_out.txt"
    datas = read_json_data(objective_path)
    with open("./out/object_out.jsonl", 'w+', encoding="utf-8") as f:
        for data in datas:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

    objective_path = r"./out/subjective_gpt4_out.txt"
    datas = read_json_data(objective_path)
    with open("./out/subject_out.jsonl", 'w+', encoding="utf-8") as f:
        for data in datas:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

if __name__ == '__main__':
    main()




<div align="center"> 

#  ssc-FinLLM-金融大模型

</div>

<p align="center">
  <a href="https://github.com/haidizym/ssc-FinLLM">
    <img src="logo.png" alt="Logo" width="30%">
  </a>


<h3 align="center">ssc-FinLLM</h3>

  <p align="center">
      简体中文
    <br />
    <br />
    <a href="https://github.com/haidizym/ssc-FinLLM"><strong>探索本项目的文档 »</strong></a>
    <a href="https://www.bilibili.com/video/BV1Z1421D7Hq"><strong>b站视频介绍»</strong></a>
    <br />
    <br />
  </p>

</p>

<!-- 本篇README.md面向开发者 -->

**ssc-FinLLM** 是能够支持 **金融咨询-金融nlp任务-简单金融计算--金融研判** 金融链路的金融大模型，由书生·浦语2.0（InternLM2）指令微调而来，欢迎大家star~⭐⭐。
目前已经开源的 `LLM` 微调配置如下：

<div align="center">

|         模型          |   类型   |
| :-------------------: | :------: |
|   InternLM2_7B_chat   |  QLORA   |
||          ……           |    ……    |

</div>

欢迎大家为本项目做出贡献~

---

金融大模型（Financial large language  Model）是一个综合性的概念，金融大模型是一种高度先进的人工智能系统，旨在为金融行业提供深度支持和智能解决方案。这种模型集成了多项功能，能够应对金融领域的各种需求和挑战。
- 首先，金融咨询是金融大模型的核心功能之一，它能够为用户提供实时的金融市场分析、投资建议以及风险管理策略等服务。这些咨询服务基于大量历史数据和实时信息，通过复杂的算法进行深度分析，为用户提供科学、个性化的金融决策支持。
- 其次，金融NLP（自然语言处理）任务是金融大模型的另一个重要功能。通过NLP技术，该模型能够理解和处理自然语言中的金融信息，包括但不限于新闻文章、研报、社交媒体内容等。这使得金融机构能够自动化地提取重要信息，进行情感分析，从而更好地理解市场趋势和投资者情绪。
- 简单金融计算也是金融大模型的基础功能之一。它可以执行各种金融计算，如利率计算、投资回报率预测、财务建模等。这些计算能力为金融分析师提供了强大的工具，使他们能够快速、准确地完成复杂的计算任务，提高工作效率。
- 最后，金融推理研判是金融大模型的高级功能，涉及对金融市场的深入理解和预测。通过分析历史数据、市场行为和宏观经济指标，该模型能够对市场走势进行推理和研判，帮助用户在复杂多变的金融环境中做出明智的投资决策。
综上所述，金融大模型通过集成金融咨询、金融NLP任务、简单金融计算和金融推理研判等多项功能，为金融行业的各方参与者提供了全面、高效的智能支持和解决方案，极大地增强了金融决策的科学性和精准度。



## 目录

- [ssc-FinLLM-金融大模型](#ssc-FinLLM-金融大模型)
  - [目录](#目录)
  - [开发前的配置要求](#开发前的配置要求)
  - [**使用指南**](#使用指南)
    - [数据构建](#数据构建)
    - [使用到的框架](#使用到的框架)
    - [作者（排名不分先后）](#作者排名不分先后)
    - [版权说明](#版权说明)
    - [特别鸣谢](#特别鸣谢)

###### 开发前的配置要求

- 硬件：RTX 4090（针对InternLM2_7B_chat+qlora微调+deepspeed zero2优化）

###### **使用指南**

1. Clone the repo

```sh
git clone https://github.com/haidizym/ssc-FinLLM
```

2. 依次阅读或者选择感兴趣的部分阅读：
   - [数据构建](#数据构建)
   - [微调指南](#微调指南)
   - [部署指南](#部署指南)
   - 查看更多详情

### 数据构建

- 请阅读[数据构建指南](generate_tutorial.md)查阅


### 使用到的框架

- [Xtuner](https://github.com/InternLM/xtuner)：用于微调
- [Transformers](https://github.com/huggingface/transformers)
- [Pytorch](https://pytorch.org/)
- [LMDeploy](https://github.com/InternLM/lmdeploy/)：用于量化部署
- [Stremlit](https://streamlit.io/)：用于构建Demo
- [DeepSpeed](https://github.com/microsoft/DeepSpeed)：并行训练
- …


### 作者（排名不分先后）


### 版权说明

该项目签署了 MIT 授权许可，详情请参阅 [LICENSE](https://github.com/haidizym/ssc-FinLLM/blob/main/LICENSE)

### 特别鸣谢

- [上海计算机软件技术开发中心](https://www.sscenter.sh.cn/)
- [上海人工智能实验室](https://www.shlab.org.cn/)



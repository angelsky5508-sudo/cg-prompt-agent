# 🎬 UE5 Cinematic Prompt Optimizer with RAG

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Gradio](https://img.shields.io/badge/Gradio-4.0-orange.svg)](https://gradio.app/)
[![RAG](https://img.shields.io/badge/RAG-Query%20Rewriting-green.svg)](#)

> **将模糊的创作灵感，精准转化为 UE5 电影级提示词**  
> 一个基于 **RAG + Query Rewriting (HyDE)** 的智能提示词优化工具，专为 Unreal Engine 5 影视创作者打造。

---

## 📌 项目背景

在使用 AI 生成 UE5 场景时，我发现一个核心痛点：  
**从「脑海中的画面」到「AI 能理解的 Prompt」之间，存在巨大的语义鸿沟。**  
直接输入简单的想法（例如“赛博朋克街道”），生成的画面往往不够专业、缺乏电影感。

因此我开发了这个工具，它利用 **RAG 架构** 和一个 **高质量的电影美学知识库**，自动将用户的模糊需求，重构为**细节丰富、风格统一、可直接用于 UE5 渲染** 的专业提示词。

---

## ✨ 核心功能

| 功能 | 描述 |
|------|------|
| 🔍 **智能查询改写 (Query Rewriting)** | 基于 HyDE 思想，将简短的用户输入扩展为详细的、结构化描述，提高检索命中率。 |
| 📚 **RAG 知识库检索** | 内置电影摄影、光影、构图等专业术语库（支持 `.xlsx` / `.csv` 扩展），通过向量相似度匹配最相关概念。 |
| 🎨 **Prompt 重构与优化** | 结合检索结果和改写后的查询，生成 **UE5 就绪** 的高质量 Prompt，包含光照、材质、镜头等关键要素。 |
| 🖥️ **一键启动 WebUI** | 基于 Gradio 构建的交互界面，无需命令行，团队成员均可快速体验。 |

---

## 🧠 技术架构

```mermaid
graph LR
    A[用户输入想法] --> B(LLM Query Rewriting)
    B --> C{Embedding}
    C --> D[(Vector DB)]
    D --> E[Top-K 检索]
    E --> F[Prompt 融合与重构]
    F --> G[输出 UE5 Prompt]
技术亮点：

非传统 RAG：不是直接检索用户输入，而是先让 LLM 改写查询，使检索更精准。

轻量向量存储：使用 pandas + sentence-transformers 管理小型知识库，无需外部向量数据库。

可插拔设计：知识库文件可随时替换，方便扩展到其他领域（如 Blender、Stable Diffusion）。

🚀 快速开始
环境要求
Python 3.9+

pip

安装步骤
克隆仓库

bash
git clone https://github.com/angelsky5508-sudo/cg-prompt-agent.git
cd cg-prompt-agent
安装依赖

bash
pip install -r requirements.txt
如果暂无 requirements.txt，可手动安装：pip install gradio pandas sentence-transformers openai（根据你实际使用的 LLM 调整）

准备知识库
确保 data.xlsx 包含至少两列：category（概念类别）和 description（高质量描述）。样例格式可在仓库中找到。

运行应用

bash
python app.py
终端会显示本地地址（通常是 http://127.0.0.1:7860），打开即可使用。

🧪 使用示例
输入（用户想法）
“一个在雨中战斗的赛博朋克女战士”

输出（优化后的 UE5 Prompt）
text
Cinematic shot, cyberpunk female warrior fighting in heavy rain, neon reflections on wet asphalt, 
high-tech armor with glowing accents, volumetric lighting, raindrops hitting the ground, 
motion blur, depth of field, shot on Arri Alexa, 8K, Unreal Engine 5 render.
✨ 工具自动添加了 “cinematic shot”, “volumetric lighting”, “shot on Arri Alexa” 等专业电影术语，显著提升了生成的画面质量。

📁 项目结构
text
.
├── app.py                # Gradio WebUI 主程序
├── data.xlsx             # 知识库（电影/艺术概念）
├── requirements.txt      # Python 依赖
├── .gitignore
└── README.md
🎯 项目价值（与岗位契合点）
岗位要求	本项目体现
RAG 架构与 Prompt 优化	实现了 查询改写 + 向量检索 的完整 RAG 流程，并针对性优化 Prompt 生成质量。
Vibe Coding 快速原型	3 天内完成从想法到可演示的 Gradio WebUI，体现快速交付能力。
需求收斂與專案範圍界定	明确定位“UE5 电影提示词”这一细分场景，不追求大而全，专注解决一个核心痛点。
Ownership	项目已应用于实际创作流程，并为团队提供了可见的效率提升。
🔮 未来改进方向
支持多模态知识库（图片 + 文本），实现“以图搜 Prompt”

增加更多 LLM 选项（如本地部署的 LLaMA）

提供 API 服务，方便集成到其他工具链

📄 许可证
MIT © [你的名字]

🙏 致谢
项目灵感来自实际 UE5 创作中的团队协作需求

RAG 架构参考了 LangChain 与 HyDE 论文的思想

Made with ❤️ by angelsky5508-sudo

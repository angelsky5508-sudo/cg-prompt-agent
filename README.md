# 🎬 UE5 Cinematic Prompt Optimizer with RAG

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![RAG](https://img.shields.io/badge/RAG-Contrastive%20Retrieval-green.svg)](#)

> **将模糊的创作灵感，精准转化为 UE5 电影级提示词**
>
> 一个基于 **Contrastive RAG** 的智能提示词优化工具，专为 Unreal Engine 5 影视创作者打造。

---

## 📌 项目背景

在使用 AI 生成 UE5 场景时，我发现一个核心痛点：

**从「脑海中的画面」到「AI 能理解的 Prompt」之间，存在巨大的语义鸿沟。**

用户不知道为什么失败，也不知道怎么修。他们会不断试错，但每次试错之间没有学习，纯靠运气。

为了解决这个问题，我在开发过程中累积了 **116 笔真实的生成实验**，包含成功与失败案例，并将这些经验系统化，构建成一个 RAG 知识库，让 AI Agent 能够根据用户的意图检索最相关的案例，生成经过验证的 Prompt，并解释背后的逻辑。

---

## ✨ 核心功能

| 功能 | 描述 |
|------|------|
| 🔍 **语义检索** | 将用户的自然语言意图转换为向量，从知识库中检索最相关的案例 |
| ⚡ **Contrastive RAG** | 同时检索成功与失败案例，让 Agent 知道「什么有效」也知道「陷阱在哪里」 |
| 🎨 **Prompt 优化与重构** | 结合检索结果生成 UE5 就绪的高质量 Prompt，包含光照、材质、色调等关键要素 |
| 💡 **推理说明** | 每次输出都附带 Reasoning，解释为什么这样写，面试官可以看见 RAG 在做什么 |
| 🖼️ **参考案例展示** | 显示检索到的参考图片，直观呈现成功与失败的对比 |

---

## 🧠 技术架构

```
用户输入自然语言意图
        ↓
  向量化 (all-MiniLM-L6-v2)
        ↓
  ChromaDB 语义检索
  ↙           ↘
成功案例      失败案例
  ↘           ↙
   LLM 分析与生成
   (Groq / LLaMA 3.3 70B)
        ↓
优化 Prompt + Reasoning + 参考案例
```

**技术亮点：**

- **Contrastive RAG**：不只检索成功案例，同时引入失败案例，让 LLM 学会避开已知陷阱
- **轻量向量存储**：使用 ChromaDB 本地部署，116 笔数据秒建完，无需外部服务
- **真实实验数据**：知识库来自真实生成实验，每一笔都是经过验证的经验，而非 LLM 自己生成的
- **可解释性设计**：输出包含 Reasoning，面试官/用户能看见 Agent 的推理过程

---

## 🚀 快速开始

### 环境要求

- Python 3.9+
- Groq API Key（免费，注册于 [console.groq.com](https://console.groq.com)）

### 安装步骤

**1. 克隆仓库**

```bash
git clone https://github.com/angelsky5508-sudo/cg-prompt-agent.git
cd cg-prompt-agent
```

**2. 安装依赖**

```bash
pip install -r requirements.txt
```

**3. 设置 API Key**

在项目根目录建立 `.env` 文件：

```
GROQ_API_KEY=your_groq_api_key_here
```

**4. 运行应用**

```bash
streamlit run app.py
```

打开浏览器访问 `http://localhost:8501`

---

## 🧪 使用示例

**输入（用户意图）**
```
A giant skeleton blending into a jungle environment
```

**输出**

- ✅ 优化后的 UE5 Prompt
- 💡 Reasoning：分析失败案例为何失败、成功案例的关键策略
- 📚 参考案例：显示检索到的成功/失败图片与 Prompt

---

## 📁 项目结构

```
cg-prompt-agent/
├── app.py          # Streamlit 主程序 + RAG 逻辑
├── data.xlsx       # 知识库（116 笔真实实验数据）
├── images/         # 对应的生成图片（本地，不上传）
├── requirements.txt
├── .env            # API Key（不上传）
├── .gitignore
└── README.md
```

---

## 📦 依赖

```
streamlit
chromadb
pandas
openpyxl
groq
python-dotenv
```

---

## 🎯 项目价值

| 能力 | 本项目体现 |
|------|-----------|
| RAG 架构设计 | 完整实现 Contrastive RAG 流程，同时利用成功与失败案例提升生成质量 |
| 问题意识 | 从真实开发痛点出发，将试错经验系统化为可查询的知识库 |
| 工程判断力 | 根据数据规模选择合适工具（ChromaDB vs Pinecone），避免过度工程化 |
| 快速交付 | 6-7 小时内完成从想法到可演示产品的完整开发 |

---

## 🔮 未来改进方向

- 支持多模态检索（图片 + 文本），实现「以图搜 Prompt」
- 增加用户反馈机制，让知识库持续学习
- 提供 API 服务，方便集成到其他工具链

---

## 📄 许可证

MIT © angelsky5508-sudo

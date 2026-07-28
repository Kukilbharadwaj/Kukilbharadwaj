<!-- ═══════════════════════ HEADER ═══════════════════════ -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0F2027,40:203A43,100:7C3AED&height=220&section=header&text=Kukil%20Bharadwaj&fontSize=52&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=AI%20Engineer%20%C2%B7%20LLM%20Applications%20%C2%B7%20RAG%20%C2%B7%20Agentic%20Systems&descAlignY=57&descSize=18" width="100%" alt="banner"/>
</div>

<div align="center">
  <a href="https://kukilbharadwaj.netlify.app">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=23&pause=900&color=00E5FF&center=true&vCenter=true&width=780&lines=Building+production-grade+LLM+systems.;RAG+pipelines+that+actually+retrieve+the+right+chunk.;Multi-agent+graphs+with+tools%2C+guardrails+%26+evals.;85%25+resolution+accuracy+%C2%B7+sub-4s+p99+%C2%B7+10K%2B+queries%2Fmonth." alt="Typing SVG" />
  </a>
</div>

<div align="center">
  <a href="https://linkedin.com/in/kukil-bharadwaj"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://kukilbharadwaj.netlify.app"><img src="https://img.shields.io/badge/Portfolio-7C3AED?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/></a>
  <a href="mailto:kukilbharadwaj24@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/Kukilbharadwaj"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <br/>
  <img src="https://komarev.com/ghpvc/?username=Kukilbharadwaj&style=for-the-badge&color=7C3AED&label=PROFILE+VIEWS" alt="views"/>
  <img src="https://img.shields.io/badge/Based%20in-Bengaluru,%20India-00E5FF?style=for-the-badge&logo=googlemaps&logoColor=white" alt="location"/>
  <img src="https://img.shields.io/badge/Open%20to-AI%20Engineer%20Roles-2ea44f?style=for-the-badge&logo=statuspage&logoColor=white" alt="status"/>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="divider"/>

<!-- ═══════════════════════ ABOUT ═══════════════════════ -->
## <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px"/> &nbsp;`whoami`

<table>
<tr>
<td width="58%" valign="top">

I'm an **AI Engineer** who ships LLM systems that survive contact with real users — not notebooks.

- 🧠 &nbsp;Specialize in **RAG pipelines** and **multi-agent architectures** running in production
- 🌏 &nbsp;Built a **multilingual hybrid RAG** chatbot → **60% → 85%** query resolution, **−45%** human escalations
- ⚡ &nbsp;Obsessed with the unglamorous half: **evals, guardrails, latency, observability**
- 📄 &nbsp;Published researcher — **ICSSSM-2025 (Atlantis Press)**
- 🏆 &nbsp;**Top 5 / 200+ teams** — Google GenAI Exchange Hackathon 2024
- 🎯 &nbsp;Currently going deep on **MCP tool-calling**, **voice agents (Pipecat)** and **LoRA fine-tuning**
- 📬 &nbsp;Reach me → **kukilbharadwaj24@gmail.com**

</td>
<td width="42%" valign="top">

<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="100%" alt="coding"/>

</td>
</tr>
</table>

```python
class KukilBharadwaj:
    role      = "AI Engineer"
    location  = "Bengaluru, IN"
    focus     = ["RAG", "Agentic AI", "LLM Serving", "Evals"]

    def stack(self) -> dict:
        return {
            "orchestration": ["LangGraph", "LangChain", "CrewAI", "MCP"],
            "retrieval":     ["Pinecone", "FAISS", "ChromaDB", "BM25 Hybrid"],
            "serving":       ["FastAPI", "vLLM", "Ollama", "Docker", "Redis"],
            "quality":       ["RAGAS", "DeepEval", "LangSmith", "Guardrails"],
        }

    def build(self, problem):
        while not problem.solved:
            problem.retrieve().reason().act().evaluate()   # measure, then ship
        return "production"
```

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="divider"/>

<!-- ═══════════════════════ ARCHITECTURE ═══════════════════════ -->
## 🧬 &nbsp;How I Architect an AI System

> The diagram below is live Mermaid — it renders natively on GitHub. This is the reference shape of the agentic RAG stack I build.

```mermaid
flowchart LR
    U([👤 User]) --> GR{{"🛡️ Guardrails<br/>in"}}
    GR --> SUP["🧠 Supervisor Agent<br/><i>LangGraph</i>"]

    SUP -->|route| RAG["📚 Retrieval Agent"]
    SUP -->|route| TOOL["🔧 Tool Agent<br/><i>MCP</i>"]
    SUP -->|route| ANL["📈 Analysis Agent"]

    RAG --> HYB["⚡ Hybrid Search<br/>BM25 + Dense"]
    HYB --> VDB[("🗄️ Pinecone / FAISS")]
    HYB --> RRK["🎯 Cross-Encoder<br/>Rerank"]

    TOOL --> API[("🌐 External APIs")]
    ANL --> SQL[("🐘 PostgreSQL")]

    RRK --> CTX["🧩 Context Assembly"]
    API --> CTX
    SQL --> CTX

    CTX --> LLM["🤖 LLM<br/><i>vLLM / Ollama / API</i>"]
    LLM --> EVAL{{"🧪 RAGAS · DeepEval"}}
    EVAL -->|fail| SUP
    EVAL -->|pass| OUT([✅ Response])

    LLM -.trace.-> OBS["👁️ LangSmith / Langfuse"]

    classDef agent fill:#7C3AED,stroke:#00E5FF,stroke-width:2px,color:#fff
    classDef data fill:#0F2027,stroke:#00E5FF,stroke-width:2px,color:#fff
    classDef gate fill:#203A43,stroke:#2ea44f,stroke-width:2px,color:#fff
    class SUP,RAG,TOOL,ANL,LLM agent
    class VDB,SQL,API,HYB,RRK,CTX data
    class GR,EVAL,OBS gate
```

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="divider"/>

<!-- ═══════════════════════ STACK ═══════════════════════ -->
## ⚙️ &nbsp;Tech Arsenal

<div align="center">

<img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,fastapi,postgres,redis,docker,git,github,githubactions,aws,gcp,linux,vscode&theme=dark&perline=7" alt="skills"/>

<br/><br/>

**🧠 LLM & Agentic AI**

<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/LlamaIndex-7C3AED?style=flat-square&logo=meta&logoColor=white"/>
<img src="https://img.shields.io/badge/CrewAI-FF5A5F?style=flat-square&logo=crew&logoColor=white"/>
<img src="https://img.shields.io/badge/MCP-000000?style=flat-square&logo=anthropic&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenAI%20SDK-412991?style=flat-square&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Pipecat-00E5FF?style=flat-square&logo=audiomack&logoColor=black"/>
<img src="https://img.shields.io/badge/Tool%20Calling-2ea44f?style=flat-square&logo=zapier&logoColor=white"/>

**🔍 Retrieval & Vector Search**

<img src="https://img.shields.io/badge/Pinecone-000000?style=flat-square&logo=pinecone&logoColor=white"/>
<img src="https://img.shields.io/badge/FAISS-0467DF?style=flat-square&logo=meta&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square&logo=databricks&logoColor=white"/>
<img src="https://img.shields.io/badge/BM25%20Hybrid-4B32C3?style=flat-square&logo=elasticsearch&logoColor=white"/>
<img src="https://img.shields.io/badge/Cross--Encoder%20Rerank-FFD21E?style=flat-square&logo=huggingface&logoColor=black"/>

**🧪 Evaluation, Guardrails & Observability**

<img src="https://img.shields.io/badge/RAGAS-6E56CF?style=flat-square&logo=testcafe&logoColor=white"/>
<img src="https://img.shields.io/badge/DeepEval-1DB954?style=flat-square&logo=checkmarx&logoColor=white"/>
<img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/Langfuse-0A0A0A?style=flat-square&logo=grafana&logoColor=white"/>
<img src="https://img.shields.io/badge/Guardrails-D32F2F?style=flat-square&logo=shieldsdotio&logoColor=white"/>
<img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"/>

**🏗️ Model Development & Serving**

<img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/LoRA%20%2F%20QLoRA-FF6F00?style=flat-square&logo=pytorchlightning&logoColor=white"/>
<img src="https://img.shields.io/badge/Unsloth-00C853?style=flat-square&logo=speedtest&logoColor=white"/>
<img src="https://img.shields.io/badge/vLLM-EF4444?style=flat-square&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white"/>

</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="divider"/>

<!-- ═══════════════════════ PROJECTS ═══════════════════════ -->
## 🚀 &nbsp;Featured Work

<div align="center">
  <a href="https://github.com/Kukilbharadwaj/AetherCare">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Kukilbharadwaj&repo=AetherCare&theme=tokyonight&hide_border=true&bg_color=0D1117" alt="AetherCare"/>
  </a>
  <a href="https://github.com/Kukilbharadwaj/FinSage">
    <img src="https://github-readme-stats.vercel.app/api/pin/?username=Kukilbharadwaj&repo=FinSage&theme=tokyonight&hide_border=true&bg_color=0D1117" alt="FinSage"/>
  </a>
</div>

<details open>
<summary><b>🏥 &nbsp;AetherCare — Multimodal Hospital AI Assistant</b></summary>

<br/>

> Production-ready hospital assistant orchestrating real hospital APIs through an agent graph — appointments, symptom-driven doctor discovery, labs, pharmacy and patient support.

| | |
|---|---|
| **Stack** | `LangGraph` `Pipecat` `MCP Tool-Calling` `Guardrails` `LangSmith` `FastAPI` |
| **Highlight** | **sub-4s p99** response latency across multi-tool reasoning chains |
| **Why it's hard** | Voice + text multimodality, tool fan-out, and safety gates on medical intent |

</details>

<details>
<summary><b>💹 &nbsp;FinSage — Multi-Agent Financial Intelligence System</b></summary>

<br/>

> A LangGraph multi-agent system that fuses live market data, financial rule APIs and RAG pipelines via MCP tool-calling for real-time investment intelligence.

| | |
|---|---|
| **Stack** | `LangGraph` `MCP` `RAG` `Market Data APIs` `FastAPI` |
| **Highlight** | **90% task-completion accuracy** on multi-step reasoning |
| **Why it's hard** | Chaining price → technical indicators → financial context without hallucinating numbers |

</details>

<details>
<summary><b>🌾 &nbsp;Multilingual Hybrid RAG Support Assistant</b> <i>(Arodos Technologies)</i></summary>

<br/>

> Hybrid retrieval chatbot serving **10K+ monthly queries** in multiple languages, evaluated continuously with RAGAS.

| | |
|---|---|
| **Stack** | `BM25 + Pinecone Hybrid` `PostgreSQL` `RAGAS` `LangChain` `GCP` |
| **Highlight** | Resolution **60% → 85%**, human escalations **−45%** |
| **Why it's hard** | Multilingual embeddings + sparse/dense fusion tuned against a real eval set |

</details>

<details>
<summary><b>📄 &nbsp;LLM Document Intelligence Pipeline</b> <i>(Arodos Technologies)</i></summary>

<br/>

> End-to-end pipeline for unstructured PDFs — guided data capture, validation and auto-filling, powered by a LoRA fine-tune.

| | |
|---|---|
| **Stack** | `LoRA / Unsloth` `FastAPI` `AWS` `PostgreSQL` |
| **Highlight** | **+40% workflow efficiency**; led development end-to-end |
| **Why it's hard** | Layout-noisy PDFs → structured, human-verifiable output |

</details>

<details>
<summary><b>🔎 &nbsp;LLM-Enabled ERP Semantic Search</b> <i>(Vasp Technologies)</i></summary>

<br/>

> Semantic search across ERP data, shipped as Dockerized microservices with CI/CD.

| | |
|---|---|
| **Stack** | `LangChain` `Docker` `FastAPI` `PostgreSQL` |
| **Highlight** | **sub-1s** search latency · support chatbot cut resolution time **25%** |
| **Bonus** | Real-time face-recognition attendance (PyTorch + OpenCV) for **200+ students**, errors **−50%** |

</details>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="divider"/>

<!-- ═══════════════════════ IMPACT ═══════════════════════ -->
## 📈 &nbsp;Impact, In Numbers

<div align="center">

| 🎯 Metric | 📊 Result | 🧩 Where |
|:---|:---:|:---|
| Chatbot query resolution | **60% → 85%** | Multilingual Hybrid RAG |
| Human-escalated support queries | **−45%** | Multilingual Hybrid RAG |
| Monthly queries served | **10K+** | Production, GCP |
| Agentic response latency | **sub-4s p99** | AetherCare |
| Multi-step task completion | **90%** | FinSage |
| Document workflow efficiency | **+40%** | LoRA doc pipeline |
| ERP semantic search latency | **<1s** | Dockerized microservices |
| Manual tracking effort | **−55%** | Analytics platform, 150+ users |
| Hackathon rank | **Top 5 / 200+** | Google GenAI Exchange 2024 |

</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="divider"/>

<!-- ═══════════════════════ RESEARCH ═══════════════════════ -->
## 🏆 &nbsp;Research & Recognition

<table>
<tr>
<td width="50%" valign="top">

### 📜 Publication
**Dyslexia Chatbot Architecture Using RL-based Seq2Seq Model**
<br/>*ICSSSM-2025 · Atlantis Press*

Designed and evaluated a therapeutic Seq2Seq chatbot enhanced with reinforcement learning across **500+ test samples**.

</td>
<td width="50%" valign="top">

### 🥇 Google GenAI Exchange Hackathon 2024
**Top 5 out of 200+ teams**

Built an AI-driven conversational agent to make insurance more accessible, for **PolicyBazaar**.

</td>
</tr>
</table>

<div align="center">
  <img src="https://github-profile-trophy.vercel.app/?username=Kukilbharadwaj&theme=algolia&no-frame=true&no-bg=true&column=7&margin-w=8&margin-h=8" alt="trophies"/>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="divider"/>

<!-- ═══════════════════════ STATS ═══════════════════════ -->
## 📊 &nbsp;GitHub Analytics

<div align="center">

<img width="49%" src="https://github-readme-stats.vercel.app/api?username=Kukilbharadwaj&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00E5FF&icon_color=7C3AED&include_all_commits=true&count_private=true" alt="stats"/>
<img width="41%" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Kukilbharadwaj&layout=compact&theme=tokyonight&hide_border=true&bg_color=0D1117&title_color=00E5FF&langs_count=8" alt="top langs"/>

<br/>

<img width="60%" src="https://streak-stats.demolab.com?user=Kukilbharadwaj&theme=tokyonight&hide_border=true&background=0D1117&ring=00E5FF&fire=7C3AED&currStreakLabel=00E5FF" alt="streak"/>

<br/><br/>

<img width="95%" src="https://github-readme-activity-graph.vercel.app/graph?username=Kukilbharadwaj&theme=tokyo-night&hide_border=true&bg_color=0D1117&color=00E5FF&line=7C3AED&point=FFFFFF&area=true" alt="activity graph"/>

</div>

### 🐍 &nbsp;Contribution Snake

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/output/snake-dark.svg"/>
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/output/snake.svg"/>
    <img alt="contribution snake" src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/output/snake.svg"/>
  </picture>
</div>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="100%" alt="divider"/>

<!-- ═══════════════════════ CONNECT ═══════════════════════ -->
## 🤝 &nbsp;Let's Build Something

<div align="center">

**Open to AI Engineer / LLM Engineer roles — available for immediate joining.**

<a href="mailto:kukilbharadwaj24@gmail.com"><img src="https://img.shields.io/badge/Say%20Hi-kukilbharadwaj24@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://linkedin.com/in/kukil-bharadwaj"><img src="https://img.shields.io/badge/Connect-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://kukilbharadwaj.netlify.app"><img src="https://img.shields.io/badge/Explore-Portfolio-7C3AED?style=for-the-badge&logo=vercel&logoColor=white"/></a>

<br/><br/>

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" alt="quote"/>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7C3AED,60:203A43,100:0F2027&height=140&section=footer&text=Retrieve%20%C2%B7%20Reason%20%C2%B7%20Act%20%C2%B7%20Evaluate&fontSize=20&fontColor=ffffff&fontAlignY=72" width="100%" alt="footer"/>

<div align="center"><sub>⭐ If any of this is useful to you, a star or a hello is always welcome.</sub></div>

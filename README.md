<!-- ══════════════════════════════ HERO ══════════════════════════════ -->
<div align="center">
  <img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/hero.svg" width="100%" alt="Kukil Bharadwaj — AI Engineer"/>
</div>

<div align="center">
  <a href="https://linkedin.com/in/kukil-bharadwaj"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="https://kukilbharadwaj.netlify.app"><img src="https://img.shields.io/badge/Portfolio-7C3AED?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"/></a>
  <a href="mailto:kukilbharadwaj24@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <a href="https://github.com/Kukilbharadwaj?tab=repositories"><img src="https://img.shields.io/badge/Repositories-181717?style=for-the-badge&logo=github&logoColor=white" alt="Repos"/></a>
  <img src="https://komarev.com/ghpvc/?username=Kukilbharadwaj&style=for-the-badge&color=00E5FF&label=VISITORS" alt="views"/>
</div>

<div align="center">
  <sub>
    <a href="#-whoami"><b>whoami</b></a> &nbsp;·&nbsp;
    <a href="#-how-i-architect-ai-systems"><b>architecture</b></a> &nbsp;·&nbsp;
    <a href="#️-anatomy-of-one-agent-turn"><b>agent loop</b></a> &nbsp;·&nbsp;
    <a href="#️-tech-arsenal"><b>stack</b></a> &nbsp;·&nbsp;
    <a href="#-featured-work"><b>work</b></a> &nbsp;·&nbsp;
    <a href="#-impact-in-numbers"><b>impact</b></a> &nbsp;·&nbsp;
    <a href="#-research--recognition"><b>research</b></a> &nbsp;·&nbsp;
    <a href="#-lets-build-something"><b>contact</b></a>
  </sub>
</div>

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ ABOUT ══════════════════════════════ -->
## <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="28px"/> &nbsp;`whoami`

<table>
<tr>
<td width="57%" valign="top">

I'm an **AI Engineer** who ships LLM systems that survive contact with real users — not notebooks.

Most of my work lives in the gap between *"the demo works"* and *"10,000 people used it this month."* That gap is retrieval quality, tool reliability, latency budgets, guardrails and honest evals.

- 🧠 &nbsp;**RAG pipelines** & **multi-agent architectures** in production
- 🌏 &nbsp;Multilingual hybrid RAG → **60% → 85%** resolution, **−45%** escalations
- ⚡ &nbsp;Obsessed with the unglamorous half: **evals, guardrails, latency, tracing**
- 📄 &nbsp;Published researcher — **ICSSSM-2025 · Atlantis Press**
- 🏆 &nbsp;**Top 5 / 200+ teams** — Google GenAI Exchange Hackathon 2024
- 🔭 &nbsp;Going deep on **MCP tool-calling**, **voice agents (Pipecat)**, **LoRA fine-tuning**
- 📬 &nbsp;**kukilbharadwaj24@gmail.com**

</td>
<td width="43%" valign="top">

<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="100%" alt="coding"/>

</td>
</tr>
</table>

```python
from dataclasses import dataclass, field

@dataclass
class KukilBharadwaj:
    role:     str  = "AI Engineer"
    based_in: str  = "Bengaluru, India"
    focus:    list = field(default_factory=lambda: ["RAG", "Agentic AI", "Serving", "Evals"])

    stack = {
        "orchestration": ["LangGraph", "LangChain", "CrewAI", "MCP"],
        "retrieval":     ["Pinecone", "FAISS", "ChromaDB", "BM25 hybrid", "cross-encoder"],
        "serving":       ["FastAPI", "vLLM", "Ollama", "Docker", "Redis"],
        "quality":       ["RAGAS", "DeepEval", "LangSmith", "Langfuse", "Guardrails"],
    }

    def build(self, problem):
        while not problem.solved:                        # ship > speculate
            problem.retrieve().rerank().reason().act()
            if problem.eval_score < 0.90:
                continue                                 # measure, then iterate
        return "production"
```

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ ARCHITECTURE ══════════════════════════════ -->
## 🧬 &nbsp;How I Architect AI Systems

> Rendered live by GitHub's Mermaid engine — this is the reference shape of the agentic RAG stack I build and run.

```mermaid
flowchart LR
    U([👤 User]) --> GI{{"🛡️ Guardrails IN<br/>PII · injection · scope"}}
    GI --> SUP["🧠 Supervisor Agent<br/><i>LangGraph state machine</i>"]

    SUP -->|route| RAG["📚 Retrieval Agent"]
    SUP -->|route| TOOL["🔧 Tool Agent<br/><i>MCP</i>"]
    SUP -->|route| ANL["📈 Analytics Agent"]

    RAG --> HYB["⚡ Hybrid Search<br/>BM25 ⊕ Dense"]
    HYB --> VDB[("🗄️ Pinecone / FAISS")]
    HYB --> RRK["🎯 Cross-Encoder Rerank<br/>24 → top-5"]

    TOOL --> API[("🌐 Hospital / Market APIs")]
    ANL --> SQL[("🐘 PostgreSQL")]

    RRK --> CTX["🧩 Context Assembly<br/>dedupe · budget · cite"]
    API --> CTX
    SQL --> CTX

    CTX --> LLM["🤖 LLM<br/><i>vLLM · Ollama · API</i>"]
    LLM --> EV{{"🧪 RAGAS · DeepEval<br/>faithfulness ≥ 0.90"}}
    EV -->|regenerate| SUP
    EV -->|pass| GO{{"🛡️ Guardrails OUT"}}
    GO --> OUT([✅ Grounded Response])

    LLM -.trace.-> OBS["👁️ LangSmith / Langfuse"]
    CACHE[("⚡ Redis semantic cache")] -.hit.-> OUT
    GI -.lookup.-> CACHE

    classDef agent fill:#7C3AED,stroke:#00E5FF,stroke-width:2px,color:#fff
    classDef data  fill:#0F2027,stroke:#00E5FF,stroke-width:2px,color:#fff
    classDef gate  fill:#16283A,stroke:#2ea44f,stroke-width:2px,color:#fff
    class SUP,RAG,TOOL,ANL,LLM agent
    class VDB,SQL,API,HYB,RRK,CTX,CACHE data
    class GI,GO,EV,OBS gate
```

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ AGENT TURN ══════════════════════════════ -->
## ⏱️ &nbsp;Anatomy of One Agent Turn

<div align="center">
  <img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/terminal.svg" width="94%" alt="agent trace"/>
</div>

<details>
<summary><b>🔬 &nbsp;See the same turn as a sequence diagram — where the latency budget actually goes</b></summary>

<br/>

```mermaid
sequenceDiagram
    autonumber
    participant U as 👤 User
    participant G as 🛡️ Guardrails
    participant S as 🧠 Supervisor
    participant R as 📚 Retriever
    participant M as 🔧 MCP Tools
    participant L as 🤖 LLM
    participant E as 🧪 Evaluator

    U->>G: query (any language)
    G->>S: sanitized intent
    Note over S: route in ~40ms

    par retrieval and tools run concurrently
        S->>R: hybrid search
        R-->>S: 24 cands → rerank → top-5 (~380ms)
    and
        S->>M: find_doctor(specialty)
        M-->>S: 200 OK (~412ms)
    end

    S->>L: assembled context + tool results
    L-->>S: draft (ttft 240ms)
    S->>E: faithfulness / relevancy
    alt score >= 0.90
        E-->>U: grounded answer · p99 3.8s
    else score < 0.90
        E->>S: regenerate with tighter context
    end
```

**Design rules I hold to:** parallelize every independent I/O · cap the context budget before the model sees it · never let an eval failure reach the user · trace every span, or you're debugging blind.

</details>

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ STACK ══════════════════════════════ -->
## ⚙️ &nbsp;Tech Arsenal

<div align="center">

<img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,fastapi,postgres,redis,docker,git,github,githubactions,aws,gcp,linux,vscode&theme=dark&perline=7" alt="skills"/>

<br/><br/>

<table>
<tr>
<td valign="top" width="50%">

**🧠 LLM & Agentic AI**

<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white"/>
<img src="https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/LlamaIndex-7C3AED?style=flat-square&logo=meta&logoColor=white"/>
<img src="https://img.shields.io/badge/CrewAI-FF5A5F?style=flat-square&logo=crew&logoColor=white"/>
<img src="https://img.shields.io/badge/MCP-000000?style=flat-square&logo=anthropic&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenAI%20SDK-412991?style=flat-square&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/Pipecat-00E5FF?style=flat-square&logo=audiomack&logoColor=black"/>
<img src="https://img.shields.io/badge/Tool%20Calling-2ea44f?style=flat-square&logo=zapier&logoColor=white"/>

</td>
<td valign="top" width="50%">

**🔍 Retrieval & Vector Search**

<img src="https://img.shields.io/badge/Pinecone-000000?style=flat-square&logo=pinecone&logoColor=white"/>
<img src="https://img.shields.io/badge/FAISS-0467DF?style=flat-square&logo=meta&logoColor=white"/>
<img src="https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square&logo=databricks&logoColor=white"/>
<img src="https://img.shields.io/badge/BM25%20Hybrid-4B32C3?style=flat-square&logo=elasticsearch&logoColor=white"/>
<img src="https://img.shields.io/badge/Cross--Encoder%20Rerank-FFD21E?style=flat-square&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/Semantic%20Cache-DC382D?style=flat-square&logo=redis&logoColor=white"/>

</td>
</tr>
<tr>
<td valign="top">

**🧪 Evals, Guardrails & Observability**

<img src="https://img.shields.io/badge/RAGAS-6E56CF?style=flat-square&logo=testcafe&logoColor=white"/>
<img src="https://img.shields.io/badge/DeepEval-1DB954?style=flat-square&logo=checkmarx&logoColor=white"/>
<img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/Langfuse-0A0A0A?style=flat-square&logo=grafana&logoColor=white"/>
<img src="https://img.shields.io/badge/Guardrails-D32F2F?style=flat-square&logo=shieldsdotio&logoColor=white"/>
<img src="https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white"/>

</td>
<td valign="top">

**🏗️ Model Development & Serving**

<img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/LoRA%20%2F%20QLoRA-FF6F00?style=flat-square&logo=pytorchlightning&logoColor=white"/>
<img src="https://img.shields.io/badge/Unsloth-00C853?style=flat-square&logo=speedtest&logoColor=white"/>
<img src="https://img.shields.io/badge/vLLM-EF4444?style=flat-square&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white"/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white"/>

</td>
</tr>
</table>

</div>

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ PROJECTS ══════════════════════════════ -->
## 🚀 &nbsp;Featured Work

<table>
<tr>
<td width="50%" valign="top">

### 🏥 [AetherCare](https://github.com/Kukilbharadwaj/AetherCare)
**Multimodal hospital AI assistant** — orchestrates appointment scheduling, patient verification, lab reports, admissions, pharmacy and symptom-based doctor discovery through natural conversation.

<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white"/> <img src="https://img.shields.io/badge/FastMCP-000000?style=flat-square&logo=anthropic&logoColor=white"/> <img src="https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white"/> <img src="https://img.shields.io/badge/Guardrails-D32F2F?style=flat-square&logo=shieldsdotio&logoColor=white"/> <img src="https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white"/> <img src="https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/>

`sub-4s p99` &nbsp;·&nbsp; <img src="https://img.shields.io/github/last-commit/Kukilbharadwaj/AetherCare?style=flat-square&color=00E5FF&label=updated"/>

</td>
<td width="50%" valign="top">

### 💹 [FinSage](https://github.com/Kukilbharadwaj/FinSage-Multi-Agent-Financial-Intelligence-System)
**Multi-agent financial intelligence** — real-time insight across stocks, mutual funds, taxation, salary planning, insurance, loans and retirement, grounded in live market data.

<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white"/> <img src="https://img.shields.io/badge/RAG-7C3AED?style=flat-square&logo=readthedocs&logoColor=white"/> <img src="https://img.shields.io/badge/MCP-000000?style=flat-square&logo=anthropic&logoColor=white"/> <img src="https://img.shields.io/badge/Pinecone-000000?style=flat-square&logo=pinecone&logoColor=white"/> <img src="https://img.shields.io/badge/Langfuse-0A0A0A?style=flat-square&logo=grafana&logoColor=white"/>

`90% task completion` &nbsp;·&nbsp; <img src="https://img.shields.io/github/last-commit/Kukilbharadwaj/FinSage-Multi-Agent-Financial-Intelligence-System?style=flat-square&color=00E5FF&label=updated"/>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🧰 [WINDLASS](https://github.com/Kukilbharadwaj/WINDLASS)
**A framework, not a demo** — modular Python framework for production AI apps: LLM agents, RAG pipelines, MCP, tool calling, guardrails, evaluation and observability behind one extensible API.

<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Agents-2ea44f?style=flat-square&logo=zapier&logoColor=white"/> <img src="https://img.shields.io/badge/RAG-7C3AED?style=flat-square&logo=readthedocs&logoColor=white"/> <img src="https://img.shields.io/badge/Evaluation-6E56CF?style=flat-square&logo=testcafe&logoColor=white"/>

`framework` &nbsp;·&nbsp; <img src="https://img.shields.io/github/last-commit/Kukilbharadwaj/WINDLASS?style=flat-square&color=00E5FF&label=updated"/>

</td>
<td width="50%" valign="top">

### ☎️ [Phonecall Voice Agent](https://github.com/Kukilbharadwaj/Phonecall_Voice_Agent)
**Real-time voice AI over the phone** — full duplex pipeline with VAD, streaming STT, LLM and TTS, wired to live telephony.

<img src="https://img.shields.io/badge/Pipecat-00E5FF?style=flat-square&logo=audiomack&logoColor=black"/> <img src="https://img.shields.io/badge/Twilio-F22F46?style=flat-square&logo=twilio&logoColor=white"/> <img src="https://img.shields.io/badge/Groq-F55036?style=flat-square&logo=groq&logoColor=white"/> <img src="https://img.shields.io/badge/Whisper-412991?style=flat-square&logo=openai&logoColor=white"/> <img src="https://img.shields.io/badge/Silero%20VAD-4B32C3?style=flat-square&logo=soundcloud&logoColor=white"/>

`real-time` &nbsp;·&nbsp; <img src="https://img.shields.io/github/last-commit/Kukilbharadwaj/Phonecall_Voice_Agent?style=flat-square&color=00E5FF&label=updated"/>

</td>
</tr>
</table>

<details>
<summary><b>🗂️ &nbsp;More from the lab</b></summary>

<br/>

| Repo | What it is |
|:---|:---|
| [**AstraQuery**](https://github.com/Kukilbharadwaj/AstraQuery-AI-Powered-Natural-Language-Analytics-Engine) | Multi-agent NL→SQL pipeline — plain-English querying with generation, validation and AI-driven result analysis |
| [**Vectorless-RAG**](https://github.com/Kukilbharadwaj/Vectorless-RAG) | RAG without embeddings or a vector DB — LLM-powered contextual retrieval |
| [**CryptoSense**](https://github.com/Kukilbharadwaj/CryptoSense-Multi-Agent-Crypto-Intelligence-System) | Multi-agent crypto intelligence with real-time LLM analysis |
| [**HybridRAG**](https://github.com/Kukilbharadwaj/HybridRAG) | Hybrid sparse + dense retrieval experiments |
| [**Medical Report Analyzer**](https://github.com/Kukilbharadwaj/Medical_Report_Analyzer) | Automated medical report analysis, summarization and clinical insight extraction |
| [**Data-Analysis-Multi-Agent**](https://github.com/Kukilbharadwaj/Data-Analysis-Multi-Agent) | Agentic data-analysis workflows |
| [**PolicyGen**](https://github.com/Kukilbharadwaj/policy-gen) | The Google GenAI Hackathon Top-5 build — personalized insurance guidance |
| [**3D Object Detection**](https://github.com/Kukilbharadwaj/3D-OBJECT-DETECTION-USING-YOLO-ALGORITHM-ON-LIDAR-DATASET) · [**SAM2 Zero-Shot**](https://github.com/Kukilbharadwaj/zero-shot-object-detection-using-sam2) · [**Brain Tumor Detection**](https://github.com/Kukilbharadwaj/brain_tumor_detection) | Computer-vision work — LiDAR 3D detection, zero-shot segmentation, medical imaging |

</details>

### 💼 &nbsp;Shipped in Production

<details>
<summary><b>🌏 &nbsp;Multilingual Hybrid RAG Support Assistant</b> &nbsp;<code>10K+ queries/mo</code> &nbsp;<i>· Arodos</i></summary>

<br/>

> Hybrid retrieval chatbot serving **10K+ monthly queries** across languages, evaluated continuously with RAGAS.

| | |
|---|---|
| **Stack** | `BM25 + Pinecone hybrid` · `PostgreSQL` · `RAGAS` · `LangChain` · `GCP` |
| **Result** | Resolution **60% → 85%** · human escalations **−45%** |
| **Hard part** | Multilingual embeddings + sparse/dense fusion tuned against a real eval set, not vibes |

</details>

<details>
<summary><b>📄 &nbsp;LLM Document Intelligence Pipeline</b> &nbsp;<code>+40% efficiency</code> &nbsp;<i>· Arodos</i></summary>

<br/>

> End-to-end pipeline for unstructured PDFs — guided data capture, validation and auto-filling, powered by a LoRA fine-tune.

| | |
|---|---|
| **Stack** | `LoRA / Unsloth` · `FastAPI` · `AWS` · `PostgreSQL` |
| **Result** | **+40% workflow efficiency** · led development end-to-end |
| **Hard part** | Layout-noisy PDFs → structured, human-verifiable output with a review loop |

</details>

<details>
<summary><b>🔎 &nbsp;LLM-Enabled ERP Semantic Search</b> &nbsp;<code>&lt;1s latency</code> &nbsp;<i>· Vasp</i></summary>

<br/>

> Semantic search across ERP data, shipped as Dockerized microservices with CI/CD.

| | |
|---|---|
| **Stack** | `LangChain` · `Docker` · `FastAPI` · `PostgreSQL` |
| **Result** | **sub-1s** search latency · support chatbot cut resolution time **25%** |
| **Bonus** | Real-time face-recognition attendance (PyTorch + OpenCV) for **200+ students**, errors **−50%** |

</details>

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ IMPACT ══════════════════════════════ -->
## 📈 &nbsp;Impact, In Numbers

<div align="center">
  <img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/metrics.svg" width="94%" alt="impact metrics"/>
</div>

<br/>

<details>
<summary><b>📊 &nbsp;Full metric table — every number, and where it came from</b></summary>

<br/>

| 🎯 Metric | 📊 Result | 🧩 Where |
|:---|:---:|:---|
| Chatbot query resolution | **60% → 85%** | Multilingual hybrid RAG · Arodos |
| Human-escalated support queries | **−45%** | Multilingual hybrid RAG · Arodos |
| Monthly queries served | **10K+** | Production on GCP |
| Agentic response latency | **sub-4s p99** | AetherCare |
| Multi-step task completion | **90%** | FinSage |
| Document workflow efficiency | **+40%** | LoRA doc pipeline · AWS |
| ERP semantic search latency | **<1s** | Dockerized microservices · Vasp |
| Manual tracking effort | **−55%** | Analytics platform · 150+ users |
| Attendance errors / admin effort | **−50% / −40%** | Face recognition · 200+ students |
| Issue resolution time | **−25%** | ERP support chatbot |
| Hackathon rank | **Top 5 / 200+** | Google GenAI Exchange 2024 |

</details>

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ JOURNEY ══════════════════════════════ -->
## 🛤️ &nbsp;The Path So Far

```mermaid
timeline
    title From CSE undergrad to production AI systems
    2019 - 2023 : B.Tech Computer Science and Engineering
                : Assam Science and Technology University
    2024 - 2025 : AI/ML Engineer · Vasp Technologies
                : LLM-enabled ERP semantic search · sub-1s
                : Face-recognition attendance · 200+ students
                : Dockerized microservices + CI/CD
    2025 : AI/ML Engineer · Arodos Technologies
         : Multilingual hybrid RAG · 60% to 85% resolution
         : LoRA document pipeline on AWS · +40% efficiency
         : Analytics platform · 150+ users
    2025 - Now : Independent AI systems work
               : AetherCare · multimodal hospital agent
               : FinSage · multi-agent financial intelligence
               : ICSSSM-2025 publication
```

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ RESEARCH ══════════════════════════════ -->
## 🏆 &nbsp;Research & Recognition

<table>
<tr>
<td width="50%" valign="top">

### 📜 Publication
**Dyslexia Chatbot Architecture Using RL-based Seq2Seq Model**
<br/><i>ICSSSM-2025 · Atlantis Press</i>

Designed and evaluated a therapeutic Seq2Seq chatbot enhanced with reinforcement learning across **500+ test samples**.

</td>
<td width="50%" valign="top">

### 🥇 Google GenAI Exchange Hackathon 2024
**Top 5 out of 200+ teams**

Built an AI-driven conversational agent to make insurance more accessible, for **PolicyBazaar** — the build lives on as [**PolicyGen**](https://github.com/Kukilbharadwaj/policy-gen).

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ STATS ══════════════════════════════ -->
## 📊 &nbsp;GitHub Analytics

<div align="center">

<img width="94%" src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/stats.svg" alt="GitHub stats"/>

<br/><br/>

<img width="60%" src="https://streak-stats.demolab.com?user=Kukilbharadwaj&theme=tokyonight&hide_border=true&background=0D1117&ring=00E5FF&fire=7C3AED&currStreakLabel=00E5FF" alt="streak"/>

<br/><br/>

<img width="95%" src="https://github-readme-activity-graph.vercel.app/graph?username=Kukilbharadwaj&theme=tokyo-night&hide_border=true&bg_color=0D1117&color=00E5FF&line=7C3AED&point=FFFFFF&area=true" alt="activity graph"/>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/output/snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/output/snake.svg"/>
  <img width="95%" alt="contribution snake" src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/output/snake.svg"/>
</picture>

</div>

<img src="https://raw.githubusercontent.com/Kukilbharadwaj/Kukilbharadwaj/main/assets/divider.svg" width="100%" alt=""/>

<!-- ══════════════════════════════ CONTACT ══════════════════════════════ -->
## 🤝 &nbsp;Let's Build Something

<div align="center">

**Open to AI Engineer / LLM Engineer roles — available for immediate joining.**

<br/>

<a href="mailto:kukilbharadwaj24@gmail.com"><img src="https://img.shields.io/badge/Say%20Hi-kukilbharadwaj24@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<a href="https://linkedin.com/in/kukil-bharadwaj"><img src="https://img.shields.io/badge/Connect-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://kukilbharadwaj.netlify.app"><img src="https://img.shields.io/badge/Explore-Portfolio-7C3AED?style=for-the-badge&logo=vercel&logoColor=white"/></a>

<br/><br/>

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&theme=tokyonight" alt="quote"/>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7C3AED,60:203A43,100:0F2027&height=140&section=footer&text=Retrieve%20%C2%B7%20Rerank%20%C2%B7%20Reason%20%C2%B7%20Act%20%C2%B7%20Evaluate&fontSize=20&fontColor=ffffff&fontAlignY=72" width="100%" alt="footer"/>

<div align="center"><sub>⭐ If any of this is useful to you, a star or a hello is always welcome.</sub></div>

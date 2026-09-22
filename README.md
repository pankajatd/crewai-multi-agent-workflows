# 🤖 CrewAI Tutorial & Autonomous Multi-Agent Workflows

A comprehensive guide and reference implementation for building autonomous multi-agent AI systems using **[CrewAI](https://www.crewai.com/)** and **Google Gemini LLMs**. This repository covers everything from basic single-agent tasks in Jupyter Notebooks to enterprise-grade, YAML-configured multi-agent marketing crews.

---

## 📋 Table of Contents
- [Overview](#overview)
- [Key Features & Modules](#key-features--modules)
- [Repository Structure](#repository-structure)
- [Tech Stack](#tech-stack)
- [Prerequisites & Setup](#prerequisites--setup)
- [Environment Variables](#environment-variables)
- [Usage & Running Modules](#usage--running-modules)
- [Security Notice](#security-notice)

---

## 🌟 Overview

Multi-agent AI framework enables multiple AI agents to collaborate seamlessly, delegate tasks, and solve complex problems. This repository acts as both a step-by-step tutorial series and a production template for building modular CrewAI projects.

### Highlights:
- **Notebook Tutorials**: Learn CrewAI fundamentals incrementally.
- **YAML-Driven Agent Configuration**: Separate business logic from agent definitions and prompt instructions.
- **Structured JSON Output**: Enforce strict data schemas using **Pydantic** models.
- **Google Gemini Integration**: Powered by fast, highly capable Gemini models (`gemini-2.0-flash`, `gemini-2.5-flash`).

---

## 🚀 Key Features & Modules

### 1. 📓 Interactive Notebook Tutorials
* `1_email-agent.ipynb`: Introduction to single-agent creation for automated email drafting.
* `2_email-agent_with_tool.ipynb`: Enhancing agents with custom tools for external interactions.
* `3_crew.ipynb`: Orchestrating multi-agent teams with sequential task processing.
* `4_crew_with_tools.ipynb`: Building advanced multi-agent crews equipped with web search (`SerperDevTool`), website scraping (`ScrapeWebsiteTool`), and file reader tools.

### 2. ⚙️ Declarative YAML Workflows (`5_yaml.py`)
* Implements `@CrewBase`, `@agent`, `@task`, and `@crew` decorators.
* Decouples agent backstories and task goals into clean YAML files (`config/agents.yaml` and `config/tasks.yaml`).
* Executes an automated blog research & content creation workflow.

### 3. 💼 Enterprise Marketing Crew (`marketing-crew/`)
* **Autonomous Marketing Department**:
  * 🎯 **Head of Marketing**: Market research & strategy formulation.
  * 📱 **Social Media Creator**: Content calendars, post drafts, reel scripts.
  * ✍️ **Blog Content Writer**: Long-form blog posts & article research.
  * 🔍 **SEO Specialist**: Search engine optimization & keyword integration.
* Uses **CrewAI Planning Mode** (`planning=True`) and agent delegation.
* Returns strictly typed JSON outputs validated via Pydantic (`Content` schema).

---

## 📁 Repository Structure

```text
crewai-tutorial/
├── config/                     # YAML configuration for Blog Crew
│   ├── agents.yaml             # Blog Crew agent roles, goals, and backstories
│   └── tasks.yaml              # Blog Crew task definitions and expected outputs
├── marketing-crew/             # Autonomous Marketing Crew implementation
│   ├── config/
│   │   ├── agents.yaml         # Marketing team agent configurations
│   │   └── tasks.yaml          # Marketing strategy & content creation tasks
│   └── crew.py                 # Full marketing crew execution pipeline & Pydantic schema
├── 1_email-agent.ipynb         # Notebook 1: Basic Email Agent
├── 2_email-agent_with_tool.ipynb # Notebook 2: Email Agent with Tools
├── 3_crew.ipynb                # Notebook 3: Basic Multi-Agent Crew
├── 4_crew_with_tools.ipynb     # Notebook 4: Multi-Agent Crew with Search & Tools
├── 5_yaml.py                   # Modular Crew implementation using decorators & YAML
├── main.py                     # Entry point & environment setup verification
├── pyproject.toml              # Project dependencies & Python requirements
├── uv.lock                     # Locked dependency tree (UV package manager)
├── .env.example                # Environment variables template
└── README.md                   # Project documentation
```

---

## 🛠️ Tech Stack

- **Core Framework**: [CrewAI](https://github.com/crewAIInc/crewAI) (`crewai[google-genai,tools]`)
- **LLM Provider**: Google Gemini (`gemini/gemini-2.0-flash`, `gemini/gemini-2.5-flash`)
- **Search & Tools**: `SerperDevTool`, `ScrapeWebsiteTool`, `DirectoryReadTool`, `FileWriterTool`, `FileReadTool`
- **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/)
- **Vector Storage**: LanceDB
- **Package Management**: [`uv`](https://github.com/astral-sh/uv) / `pip`

---

## ⚙️ Prerequisites & Setup

### Prerequisites
- **Python 3.11+** installed.
- (Recommended) [**uv** package manager](https://github.com/astral-sh/uv) installed.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/crewai-tutorial.git
   cd crewai-tutorial
   ```

2. **Set up virtual environment & install dependencies**:

   Using **uv** (Fastest):
   ```bash
   uv venv
   # Activate virtual environment:
   # On Windows (PowerShell):
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate

   uv sync
   ```

   *Or using standard **pip**:*
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows PowerShell
   pip install -e .
   ```

---

## 🔑 Environment Variables

Copy the `.env.example` file to create your own `.env` file:

```bash
cp .env.example .env
```

Open `.env` and fill in your API keys:

```env
# Google Gemini API Key
GEMINI_API_KEY=your_gemini_api_key_here

# Serper API Key (for Google Search capabilities)
SERPER_API_KEY=your_serper_api_key_here
```

> **Note**: Obtain a free Gemini API key from [Google AI Studio](https://aistudio.google.com/) and a Serper API key from [Serper.dev](https://serper.dev/).

---

## 🏃 Usage & Running Modules

### Running the Python Scripts

- **Test Environment Setup**:
  ```bash
  python main.py
  ```

- **Run Blog Crew (YAML Workflow)**:
  ```bash
  python 5_yaml.py
  ```

- **Run Enterprise Marketing Crew**:
  ```bash
  python marketing-crew/crew.py
  ```

### Running the Jupyter Notebooks

Launch Jupyter Notebook or VS Code to run the interactive tutorials in order:
```bash
jupyter lab
# or
jupyter notebook
```

---

## 🔒 Security Notice

- The `.env` file is excluded from git version control via `.gitignore` to prevent leaking private API keys.
- Always verify that `.env` is untracked before committing changes.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

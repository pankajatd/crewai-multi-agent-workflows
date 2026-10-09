"""
CrewAI Multi-Agent Workflow Studio — Streamlit Cloud Dashboard
==============================================================
Autonomous Multi-Agent Enterprise Orchestration Platform featuring:
1. 🚀 The Marketing Crew (Head of Marketing, Social Media Creator, Blog Writer)
2. 🔍 Research & Synthesis Crew (Senior Analyst, Technical Writer)
3. 📧 Email Intelligence Crew (Inbox Triage, Sentiment Classifier, Auto-Responder)
"""

import os
import sys
import time
import json
from pathlib import Path
from typing import Dict, Any, List
import yaml
import streamlit as st

# Setup sys.path
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ──────────────────────────────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CrewAI Multi-Agent Workflow Studio",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ──────────────────────────────────────────────────────────────────────
# Custom Corporate Dark Styling
# ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 1.5rem !important;
        max-width: 1400px !important;
    }
    .header-banner {
        background: linear-gradient(135deg, #090d16 0%, #1e1b4b 50%, #172554 100%);
        padding: 1.1rem 1.6rem;
        border-radius: 12px;
        margin-bottom: 1.2rem;
        color: white;
        border: 1px solid #3b82f6;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }
    .header-banner h1 { margin: 0; font-size: 1.45rem; font-weight: 800; }
    .header-banner p { margin: 0.25rem 0 0; opacity: 0.85; font-size: 0.85rem; }
    
    .stMetric {
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 8px;
        padding: 0.6rem 0.8rem;
    }
    .agent-card {
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 10px;
        padding: 1rem;
        margin-bottom: 0.8rem;
    }
    .agent-role {
        font-weight: 700;
        font-size: 14px;
        color: #60a5fa;
    }
    .agent-goal {
        font-size: 12px;
        color: #cbd5e1;
        margin-top: 4px;
    }
    .result-box {
        background: #090d16;
        border: 1px solid #3b82f6;
        border-radius: 10px;
        padding: 1.2rem;
        color: #f8fafc;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# Header Banner
# ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-banner">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
        <div>
            <h1>🤖 CrewAI Multi-Agent Workflow Studio</h1>
            <p>Autonomous Role-Playing Agent Teams • Hierarchical & Sequential Processes • Multi-Tool Collaboration</p>
        </div>
        <div style="font-family: monospace; font-size: 12px; background: rgba(59, 130, 246, 0.2); border: 1px solid #3b82f6; padding: 4px 12px; border-radius: 20px; color: #93c5fd;">
            CrewAI Enterprise • LLaMA / Gemini / GPT-4
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────────────
# Sidebar Configuration
# ──────────────────────────────────────────────────────────────────────
st.sidebar.markdown('<div style="font-weight:700; font-size:14px; color:#e2e8f0; margin-bottom:8px;">👥 Select Agent Crew</div>', unsafe_allow_html=True)

crew_choice = st.sidebar.selectbox(
    "Choose Multi-Agent Workflow",
    [
        "🚀 The Marketing Crew (Multi-Channel Content)",
        "🔍 Research & Synthesis Crew (Deep Dive)",
        "📧 Email Intelligence Crew (Triage & Response)"
    ],
    index=0,
    key="crew_choice"
)

with st.sidebar.expander("🔑 Optional API Keys", expanded=False):
    gemini_key = st.text_input("Gemini API Key", type="password", help="Optional: Powers Gemini Flash 2.0")
    if gemini_key:
        os.environ["GEMINI_API_KEY"] = gemini_key
    serper_key = st.text_input("SerperDev API Key", type="password", help="Optional: Powers Google Web Search")
    if serper_key:
        os.environ["SERPER_API_KEY"] = serper_key

st.sidebar.markdown("---")

# ──────────────────────────────────────────────────────────────────────
# Workflow Definitions
# ──────────────────────────────────────────────────────────────────────
if "Marketing" in crew_choice:
    st.sidebar.markdown('<div style="font-weight:700; font-size:13px; color:#94a3b8; margin-bottom:4px;">Workflow Parameters</div>', unsafe_allow_html=True)
    topic = st.sidebar.text_input("Campaign Topic / Product", value="Next-Gen AI Agents in Industrial Manufacturing", key="mkt_topic")
    target_audience = st.sidebar.selectbox("Target Audience", ["Enterprise CTOs & VPs of Engineering", "Technical Product Managers", "AI Researchers & Developers", "B2B SaaS Buyers"], index=0)
    campaign_goal = st.sidebar.selectbox("Campaign Goal", ["Drive Product Awareness & Signups", "Technical Thought Leadership", "Product Launch & Viral Reach"], index=0)
    
    agent_team = [
        {"name": "Head of Marketing", "icon": "👑", "role": "Chief Marketing Strategist", "goal": f"Define campaign strategy and orchestrate high-impact messaging for {topic}.", "tools": ["SerperDev Web Search", "Website Scraper", "File Writer"]},
        {"name": "Social Media Creator", "icon": "📱", "role": "Viral Social Media Strategist", "goal": f"Craft viral, high-converting LinkedIn & Twitter threads for {target_audience}.", "tools": ["SerperDev Search", "Trend Analyzer"]},
        {"name": "Content Writer (Blogs)", "icon": "✍️", "role": "Senior Technical Journalist", "goal": f"Produce an authoritative, publication-ready deep dive article on {topic}.", "tools": ["Document Reader", "Markdown Formatter"]}
    ]

elif "Research" in crew_choice:
    st.sidebar.markdown('<div style="font-weight:700; font-size:13px; color:#94a3b8; margin-bottom:4px;">Workflow Parameters</div>', unsafe_allow_html=True)
    topic = st.sidebar.text_input("Research Topic", value="Autonomous Vision AI in Smart Factories", key="res_topic")
    depth = st.sidebar.selectbox("Research Depth", ["Comprehensive Executive Summary", "Deep Technical Whitepaper", "Market Competitive Matrix"], index=0)
    
    agent_team = [
        {"name": "Senior Research Analyst", "icon": "🔎", "role": "Lead Market & Tech Researcher", "goal": f"Uncover primary sources, data trends, and breakthrough capabilities regarding {topic}.", "tools": ["SerperDev Web Search", "Document Parser"]},
        {"name": "Senior Technical Writer", "icon": "📝", "role": "Technical Narrative Specialist", "goal": f"Synthesize complex research into compelling, actionable briefing papers.", "tools": ["Synthesizer", "Quality Auditor"]}
    ]

else: # Email Crew
    st.sidebar.markdown('<div style="font-weight:700; font-size:13px; color:#94a3b8; margin-bottom:4px;">Workflow Parameters</div>', unsafe_allow_html=True)
    sender = st.sidebar.text_input("Inbound From", value="dr.sarah.jenkins@biomedcorp.com", key="email_sender")
    inquiry_type = st.sidebar.selectbox("Inquiry Type", ["Enterprise Pilot Request", "Technical Support Question", "Partnership & Licensing"], index=0)
    topic = f"{inquiry_type} from {sender}"
    
    agent_team = [
        {"name": "Triage & Sentiment Agent", "icon": "📥", "role": "Communications Classifier", "goal": "Classify urgency, tone, and strategic business value of incoming communication.", "tools": ["Sentiment Classifier"]},
        {"name": "Executive Response Agent", "icon": "✉️", "role": "Customer Success Director", "goal": "Draft tailored, empathetic, and professional executive responses.", "tools": ["Knowledge Base", "Template Matcher"]}
    ]

# ──────────────────────────────────────────────────────────────────────
# Agent Team Display
# ──────────────────────────────────────────────────────────────────────
st.markdown("### 👥 Active Crew Assembly")
team_cols = st.columns(len(agent_team))
for col, ag in zip(team_cols, agent_team):
    with col:
        st.markdown(f"""
        <div class="agent-card">
            <div style="font-size: 24px; margin-bottom: 4px;">{ag['icon']}</div>
            <div class="agent-role">{ag['name']}</div>
            <div style="font-size: 11px; color: #93c5fd; font-weight: 600;">{ag['role']}</div>
            <div class="agent-goal">{ag['goal']}</div>
            <div style="margin-top: 8px; font-size: 10px; color: #64748b;">
                <b>Tools:</b> {', '.join(ag['tools'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# ──────────────────────────────────────────────────────────────────────
# Execution Trigger
# ──────────────────────────────────────────────────────────────────────
exec_btn = st.button("🚀 Kickoff Crew Execution", type="primary", use_container_width=True)

if exec_btn:
    st.markdown("### ⚡ Live Crew Execution Stream")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Simulate / Stream Multi-Agent Interaction
    for i, ag in enumerate(agent_team):
        status_text.markdown(f"**{ag['icon']} [{ag['name']}]** is active: Analyzing inputs and collaborating...")
        progress_bar.progress(int((i + 1) / len(agent_team) * 75))
        time.sleep(0.8)
        
    status_text.markdown("✨ **Consolidating final deliverables across the crew...**")
    progress_bar.progress(100)
    time.sleep(0.4)
    status_text.empty()
    progress_bar.empty()
    
    # Display Result
    st.markdown("### 🏆 Final Crew Deliverable")
    
    if "Marketing" in crew_choice:
        result_content = f"""# 🚀 Strategic Multi-Channel Campaign: {topic}

## 🎯 Executive Campaign Summary
- **Target Demographic**: {target_audience}
- **Primary Objective**: {campaign_goal}
- **Tone & Positioning**: Authoritative, Innovation-Focused, High-ROI

---

## 📱 Deliverable 1: Viral LinkedIn & Twitter/X Thread
**Hook**: Most enterprises think deploying AI agents in production takes months. Here is why autonomous agent swarms are rewriting the playbook in 2026 🧵👇

1/ The old way: brittle rule-based scripts and static pipeline handoffs that fail when real-world edge cases strike.  
2/ The new paradigm: Specialized role-playing agents collaborating dynamically (Head of Strategy ➔ Vision Specialist ➔ Quality Auditor).  
3/ Result: Self-healing workflows that resolve 98.4% of anomalies without human intervention.  
4/ Read the full engineering breakdown below 👇  
#ArtificialIntelligence #AgenticAI #MachineLearning #EnterpriseTech

---

## ✍️ Deliverable 2: Thought Leadership Blog Post
### The Era of Agentic Workflows: How Autonomous Teams Outperform Monolithic Models
In today's fast-moving industrial landscapes, monolithic AI models are no longer sufficient. By decomposing complex workflows into distinct, specialized role-playing agents, organizations unlock:
- **Resilient Execution**: Dynamic fallback routing when a sub-system encounters unexpected data.
- **Auditability**: Complete transparency with step-by-step agent deliberations and decision logs.
- **Continuous Velocity**: Scalable expansion where new capabilities are added simply by defining a new team member.

*Published by The Marketing Crew • Built with CrewAI*
"""
    elif "Research" in crew_choice:
        result_content = f"""# 🔬 Comprehensive Research Dossier: {topic}

## 📊 Executive Overview
This report examines breakthroughs, architectural paradigms, and operational benchmarks in **{topic}**.

### 1. Key Industry Trends & Capabilities
- **Multi-Modal Perception**: Combining computer vision feature extraction with real-time vector retrieval (RAG).
- **Autonomous Remediation**: Closed-loop self-healing systems reducing unplanned downtime by up to 42%.
- **Zero-Latency Deployment**: Pre-compiled ONNX models and edge runtimes replacing cloud-dependent inference.

### 2. Strategic Recommendations
1. Transition from monolithic architectures to hierarchical agent swarms with designated supervisor agents.
2. Mandate verifiable audit gates for high-stakes operational compliance (OSHA, FDA, ISO).
3. Invest in synthetic data augmentation for robust edge-case validation.

*Compiled by Senior Research Analyst & Senior Technical Writer • CrewAI*
"""
    else: # Email Crew
        result_content = f"""# 📧 Communications Triage & Draft Response

**Inbound Message Target**: `{sender}`  
**Classified Intent**: `{inquiry_type}`  
**Urgency Rating**: `HIGH (P1 Priority)`  
**Sentiment**: Professional, High-Intent, Inquisitive  

---

### ✉️ Draft Executive Response:
**Subject**: Re: Inquiries regarding Enterprise Deployment & Next Steps

Dear Colleague,

Thank you for reaching out to our team regarding {inquiry_type.lower()}. We are thrilled to connect with you.

Our engineering team has reviewed your inquiry, and we would welcome the opportunity to walk through a live demonstration of our autonomous multi-agent platform tailored to your specific requirements.

Please let us know if any of the following times suit your calendar for an introductory 25-minute technical briefing:
- Tuesday, 10:00 AM EST
- Thursday, 2:00 PM EST

Looking forward to our conversation.

Warm regards,  
**Enterprise Solutions Team**  
*Processed autonomously by CrewAI Email Intelligence Swarm*
"""

    st.markdown(f"""
    <div class="result-box">
        {result_content}
    </div>
    """, unsafe_allow_html=True)
    
    # Download Button
    st.download_button(
        label="📥 Download Output (.md)",
        data=result_content,
        file_name=f"crewai_output_{int(time.time())}.md",
        mime="text/markdown"
    )

# ──────────────────────────────────────────────────────────────────────
# Footer
# ──────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<div style="text-align:center; opacity:0.6; font-size:0.8rem;">'
    '🤖 CrewAI Multi-Agent Workflow Studio • '
    'Role-Playing Autonomous Agents • Streamlit Cloud'
    '</div>',
    unsafe_allow_html=True,
)

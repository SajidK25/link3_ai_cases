# Enterprise AI Automations — Local LLM Powerhouse

> Privacy-first AI agents for real-world ISP operations. No cloud. No data leaks. Just pure local intelligence.

I am the CTO of **Link3 Technologies**, the leading ISP (Internet Service Provider) in Bangladesh. This repository is where I do my tinkering — a production-ready collection of local LLM-powered enterprise automations built for an ISP/Telecom environment. Every app runs entirely on-premise using small open-source models (Qwen2.5-1.5B) via LM Studio, keeping sensitive customer and employee data completely private.

---

## What's Inside

| App | What It Does | Stack |
|-----|-------------|-------|
| **ISP Ticket Classifier** | Hybrid keyword + LLM classifier that maps customer complaints to 50 diagnostic codes (L1–L4), auto-dispatches field technicians for critical issues | Streamlit, LM Studio, Regex |
| **ERP AI Approval Assistant** | Human-in-the-loop AI approver for leave requests, purchase orders, and HR onboarding with policy-aware JSON decisions | Streamlit, LM Studio |
| **Sales Funnel AI Closer** | Classifies B2B/B2C leads, identifies funnel stage, and generates copy-paste-ready replies to close deals faster | Streamlit, LM Studio |
| **SmartGift AI Admin** | Fuzzy product matcher — maps vague customer descriptions ("something for my brother's YouTube channel") to exact inventory items | Streamlit, LM Studio |
| **HR Leave Automation** | Playwright-powered CRM bot that reads pending leave requests and auto-approves or escalates using AI judgment | Playwright, LM Studio |
| **LLM Stress Test Suite** | Comprehensive benchmark framework testing classifier accuracy, latency, and token usage across edge cases | Python, JSON |

---

## Architecture Philosophy

```
+---------------------------------------------------------+
|  Business User (Streamlit UI / CRM / WhatsApp)         |
+------------------------+-------------------------------+
                         |
            +------------+------------+
            |                         |
            v                         v
+----------------+      +-----------------------+
| Keyword Rules  |      | Local LLM (Qwen2.5)   |
| (Deterministic |      | (Semantic Understanding|
|  ~99% conf)    |      |  ~85% conf)           |
+----------------+      +-----------------------+
            |                         |
            +------------+------------+
                         v
               +-----------------+
               | Business Action  |
               | Dispatch/Approve |
               | Reply/Recommend  |
               +-----------------+
```

**Hybrid Design:** Fast keyword rules catch obvious patterns instantly. The local LLM handles nuance, synonyms, and edge cases. Zero API costs. Zero latency from the internet.

---

## Why Local LLMs?

- **Privacy:** Customer complaints, employee records, and sales leads never leave your machine
- **Speed:** Sub-second inference on consumer GPUs / modern CPUs
- **Cost:** No per-token billing. Run 24/7 for free.
- **Offline:** Works without internet — perfect for internal enterprise networks

---

## Tech Stack

- **Python 3.11+**
- **Streamlit** — Rapid internal dashboards
- **LM Studio** — Local OpenAI-compatible LLM server
- **Playwright** — Browser automation for CRM/ERP integration
- **Qwen2.5-1.5B-Instruct** — The brain behind every app

---

## Repository Structure

```
├── app-baseline-class.py           # Original ISP classifier (hybrid keyword + LLM)
├── app-classifier1.py -> app-classifier9.py  # Iterative improvements & experiments
├── app-optimized-classifiers.py    # Production-ready optimized version
├── app-reasoning1/2.py            # Chain-of-thought reasoning prototypes
├── ERP_AI_Approval_Assistant.py   # ERP workflow automation
├── HR_Assistant.py                # HR leave approval bot (Playwright)
├── Link3_Sales_Funnel_AI_Closer.py # Sales pipeline AI
├── SmartGift_AI_Admin.py          # Retail product recommendation
├── llm_stress_test_class.py       # 50+ test case benchmark suite
├── llm_*_demo.py                  # Mini demos and prototypes
└── test_*.py                      # Unit & integration tests
```

---

## Who Is This For?

- Telecom/ISP support teams drowning in unstructured tickets
- SMEs wanting AI automation without SaaS subscriptions or data risks
- Developers prototyping enterprise LLM apps before cloud scaling
- Anyone proving that **1.5B parameter models can run real business logic**

---

## Quick Start

1. Install [LM Studio](https://lmstudio.ai/) and load **Qwen2.5-1.5B-Instruct**
2. Start the local server on `http://localhost:1234`
3. Run any app:
   ```bash
   pip install streamlit requests playwright
   streamlit run app-optimized-classifiers.py
   ```

---

## Key Results

- **50 ISP codes** classified with hybrid keyword fallback achieving near-instant deterministic responses
- **Field dispatch automation** for critical L2 physical layer issues (fiber cuts, cable damage, signal loss)
- **End-to-end CRM automation** from login to approval click
- **Stress-tested** on 50+ edge cases covering every support category

---

*Built at Link3 Technologies — proving that small, local models can power serious enterprise workflows.*

# Link3 Enterprise AI Automations — Local LLM Projects

> Privacy-first AI agents for real-world ISP operations. No cloud. No data leaks. Just pure local intelligence.

I am Rakibul Hassan, CTO of **Link3 Technologies**, the leading ISP (Internet Service Provider) in Bangladesh. This repository is where I do my tinkering — a production-ready collection of local LLM-powered enterprise automations built for an ISP/Telecom environment. Every app runs entirely on-premise using small open-source models (Qwen2.5-1.5B and Google Gemma 4 E4B) via LM Studio, keeping sensitive customer and employee data completely private.

---

## What's Inside

| App | What It Does | Stack |
|-----|-------------|-------|
| **ISP Ticket Classifier** | Hybrid keyword + LLM classifier that maps customer complaints to 50 diagnostic codes (L1–L4), auto-dispatches field technicians for critical issues | Streamlit, LM Studio, Regex |`r`n| **SLA LLM Assistant** | Intelligent service level agreement management - classifies customers into SLA tiers, assesses ticket priority, detects breach risks, and generates compliance reports | Streamlit, LM Studio |
| **ERP AI Approval Assistant** | Human-in-the-loop AI approver for leave requests, purchase orders, and HR onboarding with policy-aware JSON decisions | Streamlit, LM Studio |
| **Sales Funnel AI Closer** | Classifies B2B/B2C leads, identifies funnel stage, and generates copy-paste-ready replies to close deals faster | Streamlit, LM Studio |
| **SmartGift AI Admin** | Fuzzy product matcher — maps vague customer descriptions ("something for my brother's YouTube channel") to exact inventory items | Streamlit, LM Studio |
| **HR Leave Automation** | Playwright-powered CRM bot that reads pending leave requests and auto-approves or escalates using AI judgment | Playwright, LM Studio |
| **LLM Stress Test Suite** | Comprehensive benchmark framework testing classifier accuracy, latency, and token usage across edge cases | Python, JSON |
| **Network Monitor & Reasoning** | Combines ping, traceroute, DNS lookup with LLM analysis for network diagnostics and troubleshooting | Python, LM Studio |

---

## Architecture Philosophy

### 1. Qwen2.5-1.5B Model Architecture

```
+---------------------------------------------------------+
|  Business User (Streamlit UI / CRM / CLI)         |
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

### 2. Google Gemma 4 E4B Model Architecture

```
+---------------------------------------------------------+
|  Business User (Streamlit UI / CRM / CLI)         |
+------------------------+-------------------------------+
                          |
             +------------+------------+
             |                         |
             v                         v
+----------------+      +-----------------------+
| Keyword Rules  |      | Local LLM (Gemma 4)   |
| (Fallback Only |      | (Enhanced Reasoning  |
|  ~95% conf)    |      |  ~95% conf)           |
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

**LLM-First Design:** Gemma 4 E4B prioritizes LLM reasoning for all cases, with keyword rules as a lightweight fallback. Enhanced reasoning capabilities reduce dependency on hardcoded rules.

---

## Why Local LLMs?

- **Privacy:** Customer complaints, employee records, and sales leads never leave your machine
- **Speed:** Sub-second inference on consumer GPUs / modern CPUs
- **Cost:** No per-token billing. Run 24/7 for free.
- **Offline:** Works without internet — perfect for internal enterprise networks

---

## Tech Stack

### Qwen2.5-1.5B Model Stack
- **Python 3.11+**
- **Streamlit** — Rapid internal dashboards
- **LM Studio** — Local OpenAI-compatible LLM server
- **Playwright** — Browser automation for CRM/ERP integration
- **Qwen2.5-1.5B-Instruct** — The brain behind every app

### Google Gemma 4 E4B Model Stack
- **Python 3.11+**
- **Streamlit** — Rapid internal dashboards
- **LM Studio** — Local OpenAI-compatible LLM server
- **Playwright** — Browser automation for CRM/ERP integration
- **Google Gemma 4 E4B** — Enhanced reasoning capabilities

---

## Repository Structure

```
├── app-baseline-class.py           # Original ISP classifier (hybrid keyword + LLM)
├── app-classifier1.py -> app-classifier9.py  # Iterative improvements & experiments
├── app-optimized-classifiers.py    # Production-ready optimized version (Gemma 4 E4B)
├── app-reasoning1/2.py            # Chain-of-thought reasoning prototypes
├── ERP_AI_Approval_Assistant.py   # ERP workflow automation
├── HR_Assistant.py                # HR leave approval bot (Playwright)
├── Link3_Sales_Funnel_AI_Closer.py # Sales pipeline AI
├── SmartGift_AI_Admin.py          # Retail product recommendation
├── llm_stress_test_class.py       # 50+ test case benchmark suite
├── llm_*_demo.py                  # Mini demos and prototypes
├── sla_llm_assistant.py             # ISP SLA Assistant - LLM-powered service level agreement management
├── network_monitor.py             # Network diagnostics with LLM reasoning
├── test_*.py                      # Unit & integration tests
├── docs/sla-llm-assistant.md          # English documentation for SLA LLM Assistant
├── docs/bangla/sla-llm-assistant.md   # Bangla documentation for SLA LLM Assistant
└── README_UPDATED.md              # This updated documentation
```

---

## Who Is This For?

- Telecom/ISP support teams drowning in unstructured tickets
- SMEs wanting AI automation without SaaS subscriptions or data risks
- Developers prototyping enterprise LLM apps before cloud scaling
- Anyone proving that **1.5B parameter models can run real business logic**
- Anyone proving that **4B+ parameter models can run enhanced reasoning**

---

## Quick Start

### Qwen2.5-1.5B Model Setup
1. Install [LM Studio](https://lmstudio.ai/) and load **Qwen2.5-1.5B-Instruct**
2. Start the local server on `http://localhost:1234`
3. Run any app:
   ```bash
   pip install streamlit requests playwright
   streamlit run app-optimized-classifiers.py
   ```

### Google Gemma 4 E4B Model Setup
1. Install [LM Studio](https://lmstudio.ai/) and load **Google Gemma 4 E4B**
2. Start the local server on `http://localhost:1234`
3. Run any app:
   ```bash
   pip install streamlit requests playwright
   streamlit run app-optimized-classifiers.py
   ```

---

## Key Results

### Qwen2.5-1.5B Model Results
- **50 ISP codes** classified with hybrid keyword fallback achieving near-instant deterministic responses
- **Field dispatch automation** for critical L2 physical layer issues (fiber cuts, cable damage, signal loss)
- **End-to-end CRM automation** from login to approval click
- **Stress-tested** on 50+ edge cases covering every support category

### Google Gemma 4 E4B Model Results
- **Enhanced reasoning** capabilities reducing rule-based dependency
- **Improved accuracy** on complex and ambiguous customer complaints
- **LLM-first classification** prioritizing semantic understanding
- **Network monitoring integration** demonstrating reasoning on network diagnostics
- **Maintained performance** while reducing keyword rule complexity

---

## Model Comparison

| Feature | Qwen2.5-1.5B | Google Gemma 4 E4B |
|---------|-------------|-------------------|
| **Parameters** | 1.5B | 4B |
| **Context Window** | 8K tokens | 8K tokens |
| **Reasoning** | Basic semantic understanding | Enhanced reasoning capabilities |
| **Classification** | Hybrid (keyword + LLM) | LLM-first with keyword fallback |
| **Accuracy** | ~85% on complex cases | ~95% on complex cases |
| **Speed** | Fast inference | Slightly slower but more accurate |
| **Use Case** | Deterministic + fallback | Enhanced reasoning + analysis |

---

*Built at Link3 Technologies — proving that small, local models can power serious enterprise workflows.*

# লিংক৩ এন্টারপ্রাইজ AI অটোমেশন - লোকাল LLM প্রজেক্ট

> প্রাইভেসি-ফার্স্ট AI এজেন্টস রিয়েল-ওয়ার্ল্ড ISP অপারেশনগুলোতে। ক্লাউড নেই, ডেটা লিকস নেই, শুধু বাংলা বুদ্ধিমত্তা।

আমি রকিবুল হাসান, লিংক৩ টেকনোলজির সিটিও, বাংলাদেশের লিডিং ইন্টারনেট সার্ভিস প্রোভাইডার। এই রিপোজিটরি আমার টিংকারিংয়ের স্থান - একটি প্রোডাকশন-রেডি কালেকশন লোকাল LLM-পাওয়ার্ড এন্টারপ্রাইজ অটোমেশন যা ISP/টেলিকম এনভাইরনমেন্টের জন্য তৈরি করা হয়েছে। প্রতিটি অ্যাপ কমপ্লিটলি অন-প্রিমাইসে চলে, ছোট ওপেন-সোর্স মডেল (Qwen2.5-1.5B আর Google Gemma 4 E4B) ব্যবহার করে LM স্টুডিওর মাধ্যমে, সেনসিটিভ কাস্টমার আর এমপ্লয়ি ডেটা কমপ্লিটলি প্রাইভেট রাখে।

---

## এখানে কী আছে

আমাদের কাছে কিছু দারুণ অ্যাপ আছে যা আপনার কাজকে অনেক সহজ করে দেবে।

ISP টিকিট ক্লাসিফায়ার হলো একটি হাইব্রিড কি-ওয়ার্ড আর LLM ক্লাসিফায়ার যা কাস্টমারদের কমপ্লেইনগুলোকে ৫০টি ডায়াগনস্টিক কোডে (L1-L4) ম্যাপ করে। ক্রিটিক্যাল ইস্যুগুলোর জন্য এটি অটোমেটিক্যালি ফিল্ড টেকনিশিয়ানদের পাঠিয়ে দেয়। স্ট্রিমলিট, LM স্টুডিও আর রেগেক্স ব্যবহার করে তৈরি এই অ্যাপটি খুবই কার্যকর।

SLA LLM অ্যাসিস্ট্যান্ট হলো ইন্টেলিজেন্ট সার্ভিস লেভেল এগ্রিমেন্ট ম্যানেজমেন্ট সিস্টেম। এটি কাস্টমারদের SLA টিয়ারে ক্লাসিফাই করে, টিকিটের প্রায়োরিটি অ্যাসেস করে, ব্রিচ রিস্ক শনাক্ত করে আর কমপ্লায়েন্স রিপোর্ট জেনারেট করে। স্ট্রিমলিট আর LM স্টুডিও ব্যবহার করে এটি তৈরি।

ERP AI অ্যাপ্রুভাল অ্যাসিস্ট্যান্ট হলো হিউম্যান-ইন-দ্য-লুপ AI অ্যাপ্রুভার যা লিভ রিকুয়েস্ট, পারচেস অর্ডার আর HR অনবোর্ডিংয়ের জন্য পলিসি-অওয়্যার JSON ডিসিশন নেয়। স্ট্রিমলিট আর LM স্টুডিও দিয়ে বানানো এই সিস্টেমটি খুবই ইউজফুল।

সেলস ফানেল AI ক্লোজার হলো এমন একটি অ্যাপ যা B2B/B2C লিডস ক্লাসিফাই করে, ফানেল স্টেজ চিহ্নিত করে আর দ্রুত ডিল ক্লোজ করার জন্য কপি-পেস্ট-রেডি রিপ্লাই জেনারেট করে। স্ট্রিমলিট আর LM স্টুডিও ব্যবহার করে এটি তৈরি।

স্মার্টগিফট AI অ্যাডমিন হলো ফাজি প্রডাক্ট ম্যাচার - কাস্টমারদের ভেগ ক্রিপশন ("আমার ভাইয়ের ইউটিউব চ্যানেলের জন্য কিছু") এক্স্যাক্ট ইনভেন্টরি আইটেমে ম্যাপ করে। স্ট্রিমলিট আর LM স্টুডিও দিয়ে বানানো।

HR লিভ অটোমেশন হলো প্লেইরাইট-পাওয়ার্ড CRM বট যা পেন্ডিং লিভ রিকুয়েস্ট পড়ে আর AI জাজমেন্ট ব্যবহার করে অটোমেটিক্যালি অ্যাপ্রুভ বা এস্কেলেট করে। প্লেইরাইট আর LM স্টুডিও ব্যবহার করে এটি তৈরি।

LLM স্ট্রেস টেস্ট সুইট হলো কমপ্রিহেনসিভ বেঞ্চমার্ক ফ্রেমওয়ার্ক যা এজ কেসগুলোতে ক্লাসিফায়ার অ্যাকুরেসি, লেটেন্সি আর টোকেন ইউজেজ টেস্ট করে। পাইথন আর জ্যাকসন ব্যবহার করে বানানো।

নেটওয়ার্ক মনিটর & রিজনিং হলো এমন একটি সিস্টেম যা পিং, ট্রেসারাউট, DNS লুকআপকে LLM অ্যানালাইসিসের সাথে কানেক্ট করে নেটওয়ার্ক ডায়াগনস্টিকস আর ট্রাবলশুটিংয়ের জন্য। পাইথন আর LM স্টুডিও ব্যবহার করে তৈরি।

---

## আর্কিটেকচার ফিলোসফি

### ১. Qwen2.5-1.5B মডেল আর্কিটেকচার

বিজনেস ইউজার (স্ট্রিমলিট UI / CRM / CLI) থেকে শুরু করে, কি-ওয়ার্ড রুলস আর লোকাল LLM (Qwen2.5) একসাথে কাজ করে। কি-ওয়ার্ড রুলস (ডিটারমিনিস্টিক, ~৯৯% কনফিডেন্স) দ্রুত প্যাটার্ন ক্যাচ করে। লোকাল LLM (সেমান্টিক আন্ডারস্ট্যান্ডিং, ~৮৫% কনফিডেন্স) নুয়ান্স, সিনোনিম আর এজ কেস হ্যান্ডেল করে। এরপর বিজনেস অ্যাকশন - ডিসপাচ/অ্যাপ্রুভ, রিপ্লাই/রেকমেন্ড হয়।

হাইব্রিড ডিজাইন: দ্রুত কি-ওয়ার্ড রুলস স্পষ্ট প্যাটার্নগুলো ইনস্ট্যান্টলি ক্যাচ করে। লোকাল LLM নুয়ান্স, সিনোনিম আর এজ কেস হ্যান্ডেল করে। জিরো API কস্টস। ইন্টারনেট থেকে জিরো লেটেন্সি।

### ২. Google Gemma 4 E4B মডেল আর্কিটেকচার

বিজনেস ইউজার (স্ট্রিমলিট UI / CRM / CLI) থেকে শুরু করে, কি-ওয়ার্ড রুলস (শুধু ফলব্যাক, ~৯৫% কনফিডেন্স) আর লোকাল LLM (Gemma 4, এনহ্যান্সড রিজনিং, ~৯৫% কনফিডেন্স) একসাথে কাজ করে। LLM-ফার্স্ট ডিজাইন: Gemma 4 E4B সব কেসের জন্য LLM রিজনিংকে প্রায়োরিটি দেয়, কি-ওয়ার্ড রুলসকে লাইটওয়েট ফলব্যাক হিসেবে ব্যবহার করে। এনহ্যান্সড রিজনিং ক্যাপাবিলিটিস হার্ডকোডেড রুলের ওপর নির্ভরশীলতা কমিয়ে দেয়।

---

## লোকাল LLM কেন?

প্রাইভেসি: কাস্টমার কমপ্লেইন, এমপ্লয়ি রেকর্ড আর সেলস লিডস আপনার মেশিন ছাড়া কোথাও যায় না।

স্পিড: কনজিউমার GPUs / মডার্ন CPUs-তে সাব-সেকেন্ড ইনফারেন্স।

কস্ট: পার-টোকেন বিলিং নেই। ২৪/৭ ফ্রিতে চালানো যায়।

অফলাইন: ইন্টারনেট ছাড়াই কাজ করে - ইন্টারনাল এন্টারপ্রাইজ নেটওয়ার্কের জন্য পারফেক্ট।

---

## টেক স্ট্যাক

### Qwen2.5-1.5B মডেল স্ট্যাক
- পাইথন ৩.১১+
- স্ট্রিমলিট - র্যাপিড ইন্টারনাল ড্যাশবোর্ড
- LM স্টুডিও - লোকাল OpenAI-কমপ্যাটিবল LLM সার্ভার
- প্লেইরাইট - CRM/ERP ইন্টিগ্রেশনের জন্য ব্রাউজার অটোমেশন
- Qwen2.5-1.5B-Instruct - প্রতিটি অ্যাপের ব্রেইন

### Google Gemma 4 E4B মডেল স্ট্যাক
- পাইথন ৩.১১+
- স্ট্রিমলিট - র্যাপিড ইন্টারনাল ড্যাশবোর্ড
- LM স্টুডিও - লোকাল OpenAI-কমপ্যাটিবল LLM সার্ভার
- প্লেইরাইট - CRM/ERP ইন্টিগ্রেশনের জন্য ব্রাউজার অটোমেশন
- Google Gemma 4 E4B - এনহ্যান্সড রিজনিং ক্যাপাবিলিটিস

---

## রিপোজিটরি স্ট্রাকচার

```
├── app-baseline-class.py           # অরিজিনাল ISP ক্লাসিফায়ার (হাইব্রিড কি-ওয়ার্ড + LLM)
├── app-classifier1.py -> app-classifier9.py  # ইটারেটিভ ইমপ্রুভমেন্টস & এক্সপেরিমেন্টস
├── app-optimized-classifiers.py    # প্রোডাকশন-রেডি অপ্টিমাইজড ভার্সন (Gemma 4 E4B)
├── app-reasoning1/2.py            # চেইন-অফ-থট রিজনিং প্রোটোটাইপস
├── ERP_AI_Approval_Assistant.py   # ERP ওয়ার্কফ্লো অটোমেশন
├── HR_Assistant.py                # HR লিভ অ্যাপ্রুভাল বট (প্লেইরাইট)
├── Link3_Sales_Funnel_AI_Closer.py # সেলস পাইপলাইন AI
├── SmartGift_AI_Admin.py          # রিটেল প্রডাক্ট রেকমেন্ডেশন
├── llm_stress_test_class.py       # ৫০+ টেস্ট কেস বেঞ্চমার্ক সুইট
├── llm_*_demo.py                  # মিনি ডেমোস & প্রোটোটাইপস
├── sla_llm_assistant.py             # ISP SLA অ্যাসিস্ট্যান্ট - LLM-পাওয়ার্ড সার্ভিস লেভেল এগ্রিমেন্ট ম্যানেজমেন্ট
├── network_monitor.py             # নেটওয়ার্ক ডায়াগনস্টিকস উইথ LLM রিজনিং
├── test_*.py                      # ইউনিট & ইন্টিগ্রেশন টেস্টস
├── docs/sla-llm-assistant.md          # SLA LLM অ্যাসিস্ট্যান্টের ইংরেজি ডকুমেন্টেশন
├── docs/bangla/sla-llm-assistant.md   # SLA LLM অ্যাসিস্ট্যান্টের বাংলা ডকুমেন্টেশন
└── README_UPDATED.md              # এই আপডেটেড ডকুমেন্টেশন
```

---

## এটি কার জন্য?

- টেলিকম/ISP সাপোর্ট টিম যারা আনস্ট্রাকচার্ড টিকিটে ড্রাউনিং করছে
- SME যারা SaaS সাবস্ক্রিপশন বা ডেটা রিস্ক ছাড়াই AI অটোমেশন চায়
- ডেভেলপাররা যারা ক্লাউড স্কেলিংয়ের আগে এন্টারপ্রাইজ LLM অ্যাপ প্রোটোটাইপ করছে
- যে কেউ প্রমাণ করতে চায় যে ১.৫B প্যারামিটার মডেলস রিয়েল বিজনেস লজিক চালাতে পারে
- যে কেউ প্রমাণ করতে চায় যে ৪B+ প্যারামিটার মডেলস এনহ্যান্সড রিজনিং চালাতে পারে

---

## কীভাবে শুরু করবেন?

### Qwen2.5-1.5B মডেল সেটআপ
১. LM স্টুডিও (https://lmstudio.ai/) ইন্স্টল করুন আর Qwen2.5-1.5B-Instruct লোড করুন
২. লোকাল সার্ভার http://localhost:1234-এ চালু করুন
৩. কোনো অ্যাপ চালান:
   ```bash
   pip install streamlit requests playwright
   streamlit run app-optimized-classifiers.py
   ```

### Google Gemma 4 E4B মডেল সেটআপ
১. LM স্টুডিও (https://lmstudio.ai/) ইন্স্টল করুন আর Google Gemma 4 E4B লোড করুন
২. লোকাল সার্ভার http://localhost:1234-এ চালু করুন
৩. কোনো অ্যাপ চালান:
   ```bash
   pip install streamlit requests playwright
   streamlit run app-optimized-classifiers.py
   ```

---

## কী রেজাল্ট পাওয়া গেছে

### Qwen2.5-1.5B মডেল রেজাল্ট
- ৫০ ISP কোড হাইব্রিড কি-ওয়ার্ড ফলব্যাকে ক্লাসিফাইড, নিয়ার-ইনস্ট্যান্ট ডিটারমিনিস্টিক রেসপন্স পাওয়া গেছে
- ফিল্ড ডিসপাচ অটোমেশন ক্রিটিক্যাল L2 ফিজিক্যাল লেয়ার ইস্যুগুলোর জন্য (ফাইবার কাটস, কেবল ড্যামেজ, সিগনাল লস)
- এন্ড-টু-এন্ড CRM অটোমেশন লগিন থেকে অ্যাপ্রুভ ক্লিক পর্যন্ত
- ৫০+ এজ কেসে স্ট্রেস-টেস্টেড, প্রতিটি সাপোর্ট ক্যাটাগরি কভার করে

### Google Gemma 4 E4B মডেল রেজাল্ট
- এনহ্যান্সড রিজনিং ক্যাপাবিলিটিস রুল-বেসড নির্ভরশীলতা কমিয়ে দিচ্ছে
- কমপ্লেক্স আর অ্যাম্বিগুয়াস কাস্টমার কমপ্লেইনে ইমপ্রুভড অ্যাকুরেসি
- LLM-ফার্স্ট ক্লাসিফিকেশন সেমান্টিক আন্ডারস্ট্যান্ডিংকে প্রায়োরিটি দিচ্ছে
- নেটওয়ার্ক মনিটরিং ইন্টিগ্রেশন নেটওয়ার্ক ডায়াগনস্টিকসে রিজনিং দেখাচ্ছে
- কি-ওয়ার্ড রুল কমপ্লেক্সিটি কমিয়েও পারফরমেন্স বজায় রাখছে

---

## মডেল তুলনা

| ফিচার | Qwen2.5-1.5B | Google Gemma 4 E4B |
|---------|-------------|-------------------|
| প্যারামিটারস | ১.৫B | ৪B |
| কনটেক্সট উইন্ডো | ৮K টোকেনস | ৮K টোকেনস |
| রিজনিং | বেসিক সেমান্টিক আন্ডারস্ট্যান্ডিং | এনহ্যান্সড রিজনিং ক্যাপাবিলিটিস |
| ক্লাসিফিকেশন | হাইব্রিড (কি-ওয়ার্ড + LLM) | LLM-ফার্স্ট উইথ কি-ওয়ার্ড ফলব্যাক |
| অ্যাকুরেসি | কমপ্লেক্স কেসে ~৮৫% | কমপ্লেক্স কেসে ~৯৫% |
| স্পিড | ফাস্ট ইনফারেন্স | স্লাইটলি স্লো কিন্তু মোর অ্যাকুরেট |
| ইউজ কেস | ডিটারমিনিস্টিক + ফলব্যাক | এনহ্যান্সড রিজনিং + অ্যানালাইসিস |

---

*লিংক৩ টেকনোলজিতে তৈরি - প্রমাণ করে যে ছোট, লোকাল মডেলস গুরুতর এন্টারপ্রাইজ ওয়ার্কফ্লো পাওয়ার করতে পারে।*
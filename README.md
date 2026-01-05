# AI SOC Investigation Assistant

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/framework-FastAPI-teal)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

An **explainable SOC investigation assistant** that transforms security alerts into
structured investigation reasoning, hypotheses, and recommended next steps.

---

## 🔍 Motivation

Modern SOCs generate alerts, not investigations. This project focuses on **reasoned,
auditable investigation support** rather than automated response.

---

## 🧠 Core Principles

- Explainability first
- Human-in-the-loop decision support
- AI is optional and local
- Modular and SIEM-agnostic
- Research and education focused

---

## 🧩 SOC / DFIR Toolchain Overview

![DFIR Toolchain](docs/dfir_toolchain_diagram.png)

---

## 🔗 Wazuh → n8n → Investigation Assistant Flow

![Wazuh to Assistant Flow](docs/dfir_toolchain_diagram.png)

### 1. Wazuh (Detection)
- Generates alerts based on rules and decoders
- Sends alerts via webhook (JSON)

### 2. n8n (Normalization & Orchestration)
- Receives Wazuh alerts
- Filters by severity
- Normalizes schema
- Controls when AI is used

### 3. AI SOC Investigation Assistant (Reasoning)
- Produces structured investigation notes
- Generates hypotheses and next steps
- No automated response

### 4. Optional: Ollama (Local AI)
- Refines reasoning
- Advisory only
- No cloud dependency

### 5. Human Analyst (Slack / Ticket)
- Final decision-maker
- Reviews explainable output

---

## 🚀 Running the Assistant

```bash
pip install fastapi uvicorn
uvicorn assistant:app --host 0.0.0.0 --port 8000
```

---

## 📜 License

MIT

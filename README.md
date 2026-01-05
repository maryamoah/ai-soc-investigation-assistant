# AI SOC Investigation Assistant

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/framework-FastAPI-teal)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)

An **explainable SOC investigation assistant** that transforms security alerts into
structured investigation reasoning, hypotheses, and recommended next steps.

This project is designed for **Security Operations Centres (SOCs)** and
**security research**, with a strong emphasis on **human-in-the-loop decision support**
rather than automated response.

---

## 🔍 Motivation

Modern SOCs generate a high volume of alerts, but alerting alone does not equal investigation.
Analysts must interpret context, form hypotheses, and justify actions under uncertainty.

This project explores how **structured reasoning** and **optional local AI**
can support SOC investigations without replacing human judgment.

---

## 🧠 Core Principles

- Explainability first — all output is human-readable Markdown
- Human-in-the-loop — advisory only, no automated decisions
- AI is optional — system works fully without AI
- Modular design — integrates with Wazuh, n8n, Ollama, Slack
- Research-friendly — deterministic baseline + optional AI refinement

---

## 🧩 DFIR / SOC Toolchain Context

![DFIR Toolchain](docs/dfir_toolchain_diagram.png)

This assistant operates at the **investigation reasoning layer** of a SOC workflow.

---

## 📥 Input Model

The assistant expects normalized alert data (typically provided by n8n):

```json
{
  "summary": "Outbound connection to rare external IP",
  "source": "Wazuh",
  "severity": "Medium",
  "context": {
    "agent": "server01",
    "srcip": "192.168.1.10",
    "dstip": "45.67.89.10",
    "rule_id": "100100"
  }
}
```

---

## 📤 Output Model

The assistant produces structured investigation notes in Markdown:

```md
# SOC Investigation Notes

## Alert Summary
Outbound connection to rare external IP

## Initial Observations
- Source: Wazuh
- Severity: Medium

## Hypotheses
- Possible misconfiguration
- Opportunistic scanning
- Benign application behavior

## Recommended Next Steps
1. Review historical activity
2. Identify owning service
3. Correlate with other alerts

## Confidence
Low
```

---

## 🚀 Running the Assistant

### Requirements
- Python 3.10+
- fastapi, uvicorn

Install dependencies:

```bash
pip install fastapi uvicorn
```

Start the service:

```bash
uvicorn assistant:app --host 0.0.0.0 --port 8000
```

---

## 🔧 API Usage

**Endpoint**
```
POST /investigate
```

Example:

```bash
curl -X POST http://localhost:8000/investigate \
  -H "Content-Type: application/json" \
  -d '{
    "summary": "Outbound connection to rare IP",
    "source": "Firewall",
    "severity": "Medium"
  }'
```

---

## 🔗 Integrations

- **Wazuh** — alert source via n8n webhook
- **n8n** — orchestration and normalization
- **Ollama (optional)** — local AI reasoning refinement
- **Slack / ticketing** — analyst-facing output

---

## 🎓 Research & Educational Value

This repository supports research on:
- explainable AI in SOCs
- decision-support systems
- analyst trust in AI
- reproducible SOC workflows

---

## 📜 License

MIT

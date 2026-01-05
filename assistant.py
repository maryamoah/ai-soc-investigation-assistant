from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(title="AI SOC Investigation Assistant")


def generate_investigation(alert: dict) -> str:
    now = datetime.now(timezone.utc).isoformat()

    return f"""
# SOC Investigation Notes

## Alert Summary
{alert.get("summary", "No summary provided.")}

## Initial Observations
- Source: {alert.get("source", "Unknown")}
- Severity: {alert.get("severity", "Unknown")}

## Hypotheses
- Possible misconfiguration
- Opportunistic scanning
- Benign application behavior

## Recommended Next Steps
1. Review historical activity
2. Identify asset ownership
3. Correlate with other alerts

## Confidence
Low

_Advisory output — requires analyst validation._
_Generated at {now}_
""".strip()


@app.post("/investigate")
def investigate(alert: dict):
    report = generate_investigation(alert)
    return {
        "investigation_markdown": report
    }

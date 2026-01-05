import json
from pathlib import Path
from datetime import datetime, timezone


def generate_investigation(alert: dict) -> str:
    now = datetime.now(timezone.utc).isoformat()

    lines = [
        "# SOC Investigation Notes",
        "",
        "## Alert Summary",
        alert.get("summary", "No summary provided."),
        "",
        "## Initial Observations",
        f"- Alert source: {alert.get('source', 'Unknown')}",
        f"- Severity: {alert.get('severity', 'Unknown')}",
        "",
        "## Hypotheses",
        "- Possible misconfiguration",
        "- Opportunistic external scanning",
        "- Benign application behavior",
        "",
        "## Recommended Next Steps",
        "1. Review historical activity for this asset",
        "2. Identify owning service or application",
        "3. Correlate with authentication or process logs",
        "",
        "## Confidence",
        "Low",
        "",
        "## Analyst Note",
        "This output is advisory and requires human validation.",
        "",
        f"_Generated at {now}_"
    ]

    return "\n".join(lines)


def main():
    alert_path = Path("examples/sample_alert.json")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    alert = json.loads(alert_path.read_text())
    report = generate_investigation(alert)

    output_file = output_dir / "investigation.md"
    output_file.write_text(report, encoding="utf-8")

    print(f"[+] Investigation written to {output_file}")


if __name__ == "__main__":
    main()

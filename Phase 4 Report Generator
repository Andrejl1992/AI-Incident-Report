import os
import json
import datetime

# -----------------------------
# PHASE 4: Report Generator
# -----------------------------
# What this script does:
# - Reads timeline.json (from Phase 3)
# - Creates a simple draft incident report
# - Saves the report as incident_report.txt
# -----------------------------

TIMELINE_FILE = "timeline.json"
REPORT_FILE = "incident_report.txt"


def load_timeline():
    """
    Load the timeline entries from timeline.json.
    """
    if not os.path.exists(TIMELINE_FILE):
        print("Error: timeline.json not found. Run Phase 3 first.")
        return []

    with open(TIMELINE_FILE, "r") as f:
        return json.load(f)


def generate_report(timeline):
    """
    Turn timeline entries into a plain text draft report.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines = []
    report_lines.append("INCIDENT DRAFT REPORT")
    report_lines.append(f"Generated on: {now}")
    report_lines.append("")

    if not timeline:
        report_lines.append("No data available to generate report.")
        return "\n".join(report_lines)

    # Add each event from the timeline
    for entry in timeline:
        timestamp = entry.get("timestamp", "Unknown time")
        entry_type = entry.get("type", "Unknown")

        if entry_type == "transcript":
            content = entry.get("content", "")
            report_lines.append(f"[{timestamp}] Transcript: {content}")

        elif entry_type == "detection":
            obj = entry.get("object", "unknown object")
            action = entry.get("action", "unknown action")
            details = entry.get("details", "")
            report_lines.append(f"[{timestamp}] Detection: {obj} - {action} ({details})")

    report_lines.append("")
    report_lines.append("Note: This is an AI-generated draft. Please review before final use.")
    return "\n".join(report_lines)


def save_report(report_text):
    """
    Save the report text into incident_report.txt.
    """
    with open(REPORT_FILE, "w") as f:
        f.write(report_text)
    print(f"Incident report saved as {REPORT_FILE}")


# -----------------------------
# Example run (for testing only)
# -----------------------------
if __name__ == "__main__":
    print("Generating draft incident report...")

    timeline = load_timeline()
    report_text = generate_report(timeline)

    if report_text:
        save_report(report_text)

import os
import re

# -----------------------------
# PHASE 6: Redaction & Privacy Tools
# -----------------------------
# What this script does:
# - Reads the draft report (incident_report.txt from Phase 4)
# - Finds sensitive words (like names, addresses, or objects)
# - Replaces them with [REDACTED]
# - Saves a new copy called incident_report_redacted.txt
# -----------------------------

REPORT_FILE = "incident_report.txt"
REDACTED_FILE = "incident_report_redacted.txt"

# List of words to redact (examples, can be updated as needed)
SENSITIVE_WORDS = ["Smith", "Johnson", "Main Street", "knife"]


def load_report():
    """
    Open incident_report.txt and return its text.
    """
    if not os.path.exists(REPORT_FILE):
        print("Error: incident_report.txt not found. Run Phase 4 first.")
        return ""

    with open(REPORT_FILE, "r") as f:
        return f.read()


def redact_text(report_text):
    """
    Replace each sensitive word with [REDACTED].
    """
    redacted_text = report_text
    for word in SENSITIVE_WORDS:
        # re.IGNORECASE makes it match regardless of upper/lowercase
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        redacted_text = pattern.sub("[REDACTED]", redacted_text)
    return redacted_text


def save_redacted_report(redacted_text):
    """
    Save the new redacted report into a file.
    """
    with open(REDACTED_FILE, "w") as f:
        f.write(redacted_text)
    print(f"Redacted report saved as {REDACTED_FILE}")


# -----------------------------
# Example run (for testing only)
# -----------------------------
if __name__ == "__main__":
    print("Starting redaction process...")

    report_text = load_report()  # Step 1: Load the report

    if report_text:
        redacted_text = redact_text(report_text)  # Step 2: Redact sensitive words
        save_redacted_report(redacted_text)       # Step 3: Save new copy

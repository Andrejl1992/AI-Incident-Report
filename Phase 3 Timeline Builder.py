import os
import json
import datetime

# -----------------------------
# PHASE 3: Timeline Builder
# -----------------------------
# What this script does:
# - Reads transcript from Phase 1 (transcript.txt)
# - Reads detections from Phase 2 (detections.json)
# - Combines both into a timeline
# - Saves the result into timeline.json
# -----------------------------

TRANSCRIPT_FILE = "transcript.txt"
DETECTIONS_FILE = "detections.json"
TIMELINE_FILE = "timeline.json"


def load_transcript():
    """
    Load transcript lines and return them as timeline entries.
    Each line becomes its own entry.
    """
    if not os.path.exists(TRANSCRIPT_FILE):
        print("Error: transcript.txt not found. Run Phase 1 first.")
        return []

    with open(TRANSCRIPT_FILE, "r") as f:
        text = f.read().strip()

    if not text:
        return []

    lines = text.split("\n")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entries = []
    for line in lines:
        if line.strip():
            entries.append({
                "timestamp": now,   # Same timestamp for placeholder
                "type": "transcript",
                "content": line.strip()
            })
    return entries


def load_detections():
    """
    Load detections from detections.json and return them as entries.
    """
    if not os.path.exists(DETECTIONS_FILE):
        print("Error: detections.json not found. Run Phase 2 first.")
        return []

    with open(DETECTIONS_FILE, "r") as f:
        detections = json.load(f)

    # Mark them as detection entries
    for d in detections:
        d["type"] = "detection"
    return detections


def build_timeline(transcript_entries, detections):
    """
    Merge transcript and detection entries into one timeline.
    """
    timeline = transcript_entries + detections
    timeline.sort(key=lambda x: x.get("timestamp", ""))
    return timeline


def save_timeline(timeline):
    """
    Save the combined timeline to timeline.json.
    """
    with open(TIMELINE_FILE, "w") as f:
        json.dump(timeline, f, indent=4)
    print(f"Timeline saved as {TIMELINE_FILE}")


# -----------------------------
# Example run (testing only)
# -----------------------------
if __name__ == "__main__":
    print("Building incident timeline...")

    transcript_entries = load_transcript()
    detections = load_detections()

    if transcript_entries or detections:
        timeline = build_timeline(transcript_entries, detections)
        save_timeline(timeline)
    else:
        print("No transcript or detections found.")

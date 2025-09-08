import os
import json
import datetime

# -----------------------------
# PHASE 2: Object + Action Detection
# -----------------------------
# What this script does:
# - Takes a video file (example: body cam recording)
# - Detects people, objects, and actions (placeholder for now)
# - Saves results into detections.json
# -----------------------------

OUTPUT_FILE = "detections.json"


def analyze_video(file_path):
    """
    Pretend to analyze a video and return detections.
    Later this can be replaced with a real object/action detection model.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found - {file_path}")
        return []

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Example fake detections (for testing only)
    detections = [
        {
            "timestamp": now,
            "object": "person",
            "action": "walking",
            "details": "Civilian visible near vehicle"
        },
        {
            "timestamp": now,
            "object": "vehicle",
            "action": "stopped",
            "details": "Blue sedan parked on roadside"
        },
        {
            "timestamp": now,
            "object": "person",
            "action": "holding_object",
            "details": "Object resembles a knife"
        }
    ]
    return detections


def save_detections(detections, output_file=OUTPUT_FILE):
    """
    Save detections into a JSON file.
    """
    with open(output_file, "w") as f:
        json.dump(detections, f, indent=4)
    print(f"Detections saved as {output_file}")


# -----------------------------
# Example run (for testing only)
# -----------------------------
if __name__ == "__main__":
    # Example video file (replace with a real file later)
    test_file = "examples/sample_video.mp4"

    print("Starting object + action detection...")
    detections = analyze_video(test_file)

    if detections:
        save_detections(detections)

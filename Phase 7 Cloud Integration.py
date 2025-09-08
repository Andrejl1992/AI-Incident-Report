import os
import time
import subprocess

# -----------------------------
# PHASE 7: Cloud Integration
# -----------------------------
# What this script does:
# - Watches a folder for new files (simulates cloud upload)
# - When a new file is added, it runs Phases 1–6 in order
# - Moves the processed file to a "processed_files" folder
# -----------------------------

# Folder names
WATCH_FOLDER = "incoming_files"      # Place new files here
PROCESSED_FOLDER = "processed_files" # Files will be moved here after processing


def ensure_folders():
    """
    Make sure the watch folder and processed folder exist.
    If not, they are created.
    """
    os.makedirs(WATCH_FOLDER, exist_ok=True)
    os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def run_pipeline(file_path):
    """
    Run all the scripts from Phase 1 to Phase 6.
    This simulates the full reporting pipeline.
    """
    print(f"\nProcessing file: {file_path}\n")

    # Run each phase one after another
    subprocess.run(["python", "phase1_transcription.py"])
    subprocess.run(["python", "phase2_object_detection.py"])
    subprocess.run(["python", "phase3_timeline_builder.py"])
    subprocess.run(["python", "phase4_report_generator.py"])
    subprocess.run(["python", "phase5_export_report.py"])
    subprocess.run(["python", "phase6_redaction.py"])

    print("\nPipeline complete.\n")

    # Move the processed file to the "processed_files" folder
    new_path = os.path.join(PROCESSED_FOLDER, os.path.basename(file_path))
    os.rename(file_path, new_path)
    print(f"File moved to {new_path}\n")


def watch_folder():
    """
    Keep checking the watch folder for new files.
    When a new file appears, run the pipeline on it.
    """
    print(f"Watching folder: {WATCH_FOLDER}\n")
    watched_files = set()  # Keep track of files already processed

    while True:
        files = os.listdir(WATCH_FOLDER)
        for file in files:
            file_path = os.path.join(WATCH_FOLDER, file)

            # Only process new files (not seen before)
            if file_path not in watched_files and os.path.isfile(file_path):
                run_pipeline(file_path)
                watched_files.add(file_path)

        # Wait 5 seconds before checking again
        time.sleep(5)


# -----------------------------
# Example run (for testing only)
# -----------------------------
if __name__ == "__main__":
    ensure_folders()   # Step 1: Create folders if missing
    watch_folder()     # Step 2: Start watching for new files

import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from docx import Document

# -----------------------------
# PHASE 5: Export & Formatting
# -----------------------------
# What this script does:
# - Reads incident_report.txt (from Phase 4)
# - Makes two new copies of the report:
#       1. A PDF file
#       2. A Word (DOCX) file
# -----------------------------

REPORT_FILE = "incident_report.txt"
PDF_FILE = "incident_report.pdf"
DOCX_FILE = "incident_report.docx"


def load_report():
    """
    Read the text report from incident_report.txt.
    """
    if not os.path.exists(REPORT_FILE):
        print("Error: incident_report.txt not found. Run Phase 4 first.")
        return ""

    with open(REPORT_FILE, "r") as f:
        return f.read()


def export_to_pdf(report_text):
    """
    Turn the text report into a PDF file.
    """
    doc = SimpleDocTemplate(PDF_FILE, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add each line of the report into the PDF
    for line in report_text.split("\n"):
        if line.strip():
            elements.append(Paragraph(line.strip(), styles["Normal"]))
        elements.append(Spacer(1, 12))  # Add space between lines

    doc.build(elements)
    print(f"Report exported as {PDF_FILE}")


def export_to_docx(report_text):
    """
    Turn the text report into a Word (DOCX) file.
    """
    doc = Document()

    # Add each line of the report into the Word document
    for line in report_text.split("\n"):
        if line.strip():
            doc.add_paragraph(line.strip())

    doc.save(DOCX_FILE)
    print(f"Report exported as {DOCX_FILE}")


# -----------------------------
# Example run (for testing only)
# -----------------------------
if __name__ == "__main__":
    print("Exporting report into PDF and DOCX formats...")

    report_text = load_report()  # Step 1: Load report text

    if report_text:
        export_to_pdf(report_text)   # Step 2: Export as PDF
        export_to_docx(report_text)  # Step 3: Export as DOCX

from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()

def save_report(text, result, ai):

    filename = datetime.now().strftime(
        "reports/report_%Y%m%d_%H%M%S.pdf"
    )

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>AI Cybersecurity Awareness Report</b>", styles["Heading1"]))
    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(Paragraph(f"<b>User Input:</b><br/>{text}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Threat:</b> {result['type']}", styles["BodyText"]))
    story.append(Paragraph(f"<b>Risk Score:</b> {result['risk']}%", styles["BodyText"]))
    story.append(Paragraph(f"<b>Reason:</b> {result['reason']}", styles["BodyText"]))
    story.append(Paragraph("<br/>", styles["Normal"]))
    story.append(Paragraph("<b>AI Recommendation</b>", styles["Heading2"]))
    story.append(Paragraph(ai.replace("\n", "<br/>"), styles["BodyText"]))

    pdf.build(story)

    return filename
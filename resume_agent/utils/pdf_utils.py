
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    margin = 40
    text_width = width - 2 * margin
    textobject = c.beginText(margin, height - margin)
    textobject.setFont("Helvetica", 10)
    textobject.setTextOrigin(margin, height - margin)

    lines = text.split("\n")
    for line in lines:
        words = line.split(" ")
        wrapped_line = ""
        for word in words:
            test_line = wrapped_line + word + " "
            if c.stringWidth(test_line, "Helvetica", 10) < text_width:
                wrapped_line = test_line
            else:
                textobject.textLine(wrapped_line.strip())
                wrapped_line = word + " "
        if wrapped_line.strip():
            textobject.textLine(wrapped_line.strip())

    c.drawText(textobject)
    c.save()
    buffer.seek(0)
    return buffer

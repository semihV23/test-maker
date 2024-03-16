from fpdf import FPDF
import os
import math

"""
A python code that prepares a test quiz with 4 questions on a page.
Authot: https://github.com/semihV23
"""

with open("Header.txt", "r") as f:
    header = f.read().split("[[NewLine]]")

fileName = header[0].lower().replace("\n", "_").replace(
    " ", "_") + "_" + header[1].strip("\n") + ".pdf"

images = [f for f in os.listdir("questions")
          if os.path.isfile("questions/"+f)]

print("Found Images:", images)

pdf = FPDF()
pdf.add_page()

pdf.add_font("poppins", style="", fname="fonts/Poppins-Regular.ttf")
pdf.add_font("poppins", style="B", fname="fonts/Poppins-Bold.ttf")
pdf.add_font("poppins", style="I", fname="fonts/Poppins-Italic.ttf")
pdf.add_font("poppins", style="bi", fname="fonts/Poppins-BoldItalic.ttf")

pdf.set_font(family="Poppins", style="B", size=42)
pdf.write(text=header[0])

pdf.set_font(family="Poppins", size=15)
pdf.write(text=header[1]+"\n")

pdf.set_font(family="Poppins", size=15)
pdf.write(text=f'Soru sayısı: {len(images)}\n')
pdf.write(text=f'Sayfa sayısı: {math.ceil(len(images)/4)}\n')

pdf.set_font(family="Poppins", size=18)
pdf.write(text=header[2])


pdf.add_page()

pdf.set_line_width(0.3)
pdf.set_draw_color(r=0, g=0, b=0)
pdf.line(x1=105, y1=10, x2=105, y2=287)

for index, image in enumerate(images):
    match index % 4:
        case 0:
            pdf.image(
                "questions/"+image,
                x=10, y=10,
                w=90,
                keep_aspect_ratio=True
            )
        case 1:
            pdf.image(
                "questions/"+image,
                # x=110, y=10,
                x=10, y=160,
                w=90,
                keep_aspect_ratio=True
            )
        case 2:
            pdf.image(
                "questions/"+image,
                # x=10, y=160,
                x=110, y=10,
                w=90,
                keep_aspect_ratio=True
            )
        case 3:
            pdf.image(
                "questions/"+image,
                x=110, y=160,
                w=90,
                keep_aspect_ratio=True
            )
            if index+1 != len(images):
                pdf.add_page()
                pdf.set_line_width(0.3)
                pdf.set_draw_color(r=0, g=0, b=0)
                pdf.line(x1=105, y1=10, x2=105, y2=287)

pdf.output("PDFs/"+fileName)
print("Done. File saved as:", fileName)

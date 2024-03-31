from fpdf import FPDF
import os
import math
from PIL import Image

"""
A python code that prepares a test quiz with 4 questions on a page.
Author: https://github.com/semihV23
"""

print("Working directory:", os.getcwd())

with open("Header.txt", "r", encoding="utf-8") as f:
    header = f.read().split("[[NewLine]]")

fileName = header[0].lower().replace("\n", "_").replace(
    " ", "_") + "_" + header[1].strip("\n") + ".pdf"

images = [f for f in os.listdir("questions")
          if os.path.isfile("questions/"+f) and f.lower().endswith((".jpg", ".png"))]

print("Found Images:", images)

pdf = FPDF()
pdf.add_page()
pdf.set_text_shaping(True)

pdf.add_font("Poppins", style="", fname="./fonts/Poppins/Poppins-Regular.ttf")
pdf.add_font("Poppins", style="B", fname="./fonts/Poppins/Poppins-Bold.ttf")
pdf.add_font("Poppins", style="I", fname="./fonts/Poppins/Poppins-Italic.ttf")
pdf.add_font("Poppins", style="bi",
             fname="./fonts/Poppins/Poppins-BoldItalic.ttf")

pdf.add_font("DejaVu", style="", fname="./fonts/DejaVu/DejaVuSansCondensed.ttf")
pdf.add_font("DejaVu", style="B",
             fname="./fonts/DejaVu/DejaVuSansCondensed-Bold.ttf")
pdf.add_font("DejaVu", style="I",
             fname="./fonts/DejaVu/DejaVuSansCondensed-Bold.ttf")
pdf.add_font("DejaVu", style="bi",
             fname="./fonts/DejaVu/DejaVuSansCondensed-BoldOblique.ttf")

defaultFontFamily = "Poppins"

pdf.set_font(family=defaultFontFamily, style="B", size=42)
pdf.write(text=header[0])

pdf.set_font(family=defaultFontFamily, size=15)
pdf.write(text=header[1]+"\n")

pdf.set_font(family=defaultFontFamily, size=15)
pdf.write(text=f'Soru sayısı: {len(images)}\n')
pdf.write(text=f'Sayfa sayısı: {math.ceil(len(images)/4)}\n')

pdf.set_font(family=defaultFontFamily, size=18)
pdf.write(text=header[2])


pdf.add_page()

pdf.set_line_width(0.3)
pdf.set_draw_color(r=0, g=0, b=0)
pdf.line(x1=105, y1=10, x2=105, y2=287)

for index, image in enumerate(images):
    q_width = 90.0
    q_height = 138.5

    i_width, i_height = Image.open("./questions/"+image).size

    if i_width/i_height > q_width/q_height:
        q_height = q_width*(i_height/i_width)

    match index % 4:
        case 0:
            pdf.image(
                "./questions/"+image,
                x=10, y=10,
                w=q_width, h=q_height,
                keep_aspect_ratio=True
            )
        case 1:
            pdf.image(
                "./questions/"+image,
                x=10, y=148.5,
                w=q_width, h=q_height,
                keep_aspect_ratio=True
            )
        case 2:
            pdf.image(
                "./questions/"+image,
                x=110, y=10,
                w=q_width, h=q_height,
                keep_aspect_ratio=True
            )
        case 3:
            pdf.image(
                "./questions/"+image,
                x=110, y=148.5,
                w=q_width, h=q_height,
                keep_aspect_ratio=True
            )
            if index+1 != len(images):
                pdf.add_page()
                pdf.set_line_width(0.3)
                pdf.set_draw_color(r=0, g=0, b=0)
                pdf.line(x1=105, y1=10, x2=105, y2=287)

pdf.output("./PDFs/"+fileName)
print("Done. File saved as:", fileName)

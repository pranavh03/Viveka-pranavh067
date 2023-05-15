# Viveka-pranavh067 
from libretranslatepy import LibreTranslateAPI

from PyPDF2 import PdfWriter,PdfReader

from fpdf import FPDF

lt = LibreTranslateAPI("https://translate.argosopentech.com/")

input_pdf = PdfReader(open('po.pdf', 'rb'))

pdf=FPDF()

output_pdf = PdfWriter()

count=0   

for page_num in range(len(input_pdf.pages)):

  count+=1

  pdf.add_page()

  pdf.set_font("Arial", size = 15)

  page = input_pdf.pages[page_num]

  mediabox = page.mediabox

  text = page.extract_text()

    

    # my_canvas = Canvas("output.pdf", pagesize = LETTER)  

    # my_canvas.setFont("Courier", 18)  

    # my_canvas.setFillColor(purple)  

    # my_canvas.drawString(10 * inch, 10 * inch, text)  

    # my_canvas.save()

    # for i in page.readline():

    #   print(i)

    

      

  translated_text=lt.translate(text,"en","de")

  pdf.multi_cell(0, 10, txt = translated_text)

    

    

    # output_pdf.merge_page(translated_text)

    # output_pdf.addPage(page)

pdf.output("output.pdf")

print(count)

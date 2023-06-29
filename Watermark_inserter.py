import PyPDF2

pdf=PyPDF2.PdfFileReader(open('combined_pdf.pdf','rb'))
watermark=PyPDF2.PdfFileReader(open('WATERMARK.pdf','rb'))
output=PyPDF2.PdfFileWriter()

for i in range(pdf.getNumPages()):
    page=pdf.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('watermarked_pdf.pdf','wb') as final_pdf:
    output.write(final_pdf) 
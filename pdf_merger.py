import PyPDF2
import sys

inputs= sys.argv[1:]

def Pdf_Merger(pdf_list):
    merger=PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('combined_pdf.pdf')

Pdf_Merger(inputs)
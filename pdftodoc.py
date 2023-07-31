pip install pdf2docx
from pdf2docx import Converter
pdf_file = 'nts.pdf'
#name of the pdf file in the program file
doc_file = 'nts.doc'
#DOC file
cv = Converter(pdf_file)      #
cv.convert(doc_file)
cv.close()

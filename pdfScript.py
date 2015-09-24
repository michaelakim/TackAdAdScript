#!/usr/bin/python

#python pdfScript.py [pdf] [ad image]

import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

from reportlab.pdfgen import canvas
from StringIO import StringIO

# PDF Writer
output = PdfFileWriter()

# Using ReportLab to insert image into PDF
imgTemp = StringIO()
imgDoc = canvas.Canvas(imgTemp)

# Draw image on Canvas and save PDF in buffer
imgPath = sys.argv[2]
imgDoc.drawImage(imgPath, 0, 0, 600, 70)
imgDoc.save()
overlay = PdfFileReader(StringIO(imgTemp.getvalue())).getPage(0)

# Use PyPDF to merge the image-PDF into the template
page = PdfFileReader(file(sys.argv[1],"rb"))
num_pages = page.getNumPages()

for num in xrange(num_pages):
	current_page =page.getPage(num)
	current_page.mergePage(overlay)
	output.addPage(current_page)

#Save the result
output.write(file(sys.argv[1].replace('.pdf','')+"-output.pdf","wb"))
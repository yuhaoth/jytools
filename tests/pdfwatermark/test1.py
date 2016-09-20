from pyPdf import PdfFileWriter, PdfFileReader
#~ file=open

output = PdfFileWriter()
input1 = PdfFileReader(open("example.pdf", "rb"))
watermark = PdfFileReader(open("watermark.pdf", "rb"))
page4=input1.getPage(0)
page4.mergePage(watermark.getPage(0))
output.addPage(page4)
# finally, write "output" to document-output.pdf
outputStream = open("document-output.pdf", "wb")
output.write(outputStream)
outputStream.close()

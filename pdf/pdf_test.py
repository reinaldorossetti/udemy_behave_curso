from PyPDF2 import PdfFileReader
inputPdf = PdfFileReader(open("ScenarioOutline.pdf", "rb"), strict=False)

# pega informações sobre o pdf.
docInfo = inputPdf.getDocumentInfo()
print(docInfo.author)
print(docInfo.creator)
print(docInfo.producer)
print(docInfo.title)
print(docInfo.subject)

page = inputPdf.getPage(0)
page_content = page.extractText()
print(page_content.encode('utf-8'))
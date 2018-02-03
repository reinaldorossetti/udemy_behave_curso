from pdfrw import PdfReader
x = PdfReader('sample.pdf')
#print(x.Info)
print(len(x.pages))
print(x.pages[0].Contents.stream)
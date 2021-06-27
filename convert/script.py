from pdf2image import convert_from_path

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

images = convert_from_path('Chiraag_Kakar_2022_CSE.pdf')

for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'
    image.save(fname, "PNG")
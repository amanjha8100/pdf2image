from django.shortcuts import redirect, render
from . models import Convert
from . forms import ConvertForm
from django.contrib import messages
from pdf2image import convert_from_path
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def converter(p):
    images = convert_from_path(f"C:/Users/91747/Desktop/Projects/pdftopng/{p}",output_folder="C:/Users/91747/Desktop/Projects/pdftopng/output_images/")

    for i, image in enumerate(images):
        fname = 'image'+str(i)+'.png'
        image.save(fname, "PNG")
        return

# Create your views here.
def task(request):
    print(os.path.join(BASE_DIR,'media' ))
    form = ConvertForm()
    if request.method == "POST":
        form = ConvertForm(request.POST,request.FILES)
        if form.is_valid():
            messages.success(request, 'File Uploaded')
            instance = form.save(commit=False)
            instance.save()
            print(instance.file.name)
            converter(instance.file.url)
            return render(request, 'index.html',{'form':form})
        else:
            messages.error(request, 'Something went wrong!')
            return render(request, 'index.html',{'form':form})
    return render(request, 'index.html',{'form':form})
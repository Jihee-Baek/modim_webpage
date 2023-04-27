from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def document_download(request):
    return render(request, 'doc_manage/document_download.html')

def book_manage(request):
    return render(request, 'book_manage.html')

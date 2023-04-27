from django.shortcuts import render
from django.views.generic import ListView
from .models import DocManage, DocAttached

class FileDownload(ListView):
    model = DocAttached
    ordering = '-doc_mng'
    template_name = './templates/document_download.html'

    def get_context_data(self, **kwargs):
        context = super(FileDownload, self).get_context_data()
        context['files'] = DocManage.objects.all()

        return context

    def get_download_link(self):
        return DocAttached.attached

def file_list(request, slug):
    pass

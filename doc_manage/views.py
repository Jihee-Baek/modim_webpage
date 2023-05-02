from django.shortcuts import render
from django.views.generic import ListView
from .models import DocManage, DocAttached

class DocAttachedList(ListView):
    model = DocAttached
    # ordering = '-pk'
    template_name = 'document_download.html'

    def get_queryset(self):
        return DocAttached.objects.order_by('doc_mng_id')[:3]


def categories(request):

    employee_info = DocAttached.objects.filter(doc_mng_id=1).order_by('-pk')[:1]
    monthly_info = DocAttached.objects.filter(doc_mng_id=2).order_by('-pk')[:1]
    weekly_info = DocAttached.objects.filter(doc_mng_id=3).order_by('-pk')[:1]

    return render(
        request,
        'document_download.html',
        {
            'employee_info': employee_info,
            'monthly_info': monthly_info,
            'weekly_info': weekly_info,
        }
    )


def per_category(request, slug):
    doc_mng_id = DocManage.objects.filter(slug=slug)
    per_info = DocAttached.objects.filter(doc_mng_id=doc_mng_id[0]).order_by('-pk')
    DocAtt = per_info[0]

    return render(
        request,
        'doc_manage/per_doc_download.html',
        {
            'per_info': per_info,
            'slug_name': slug,
            'DocAtt': DocAtt,
            'doc_mng_id': doc_mng_id[0]
        }
    )

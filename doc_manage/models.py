from django.db import models
import os

class DocManage(models.Model):
    name = models.CharField(max_length=100)         # 문서 이름
    slug = models.SlugField(allow_unicode=True)     # url slug

    def __str__(self):
        return f'{self.pk}. {self.name}'

    def get_absolute_url(self):
        return f'/downloads/{self.slug}/'

class DocAttached(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    attached = models.FileField(upload_to='uploads/file/%Y/%m/%d/')

    doc_mng = models.ForeignKey(DocManage, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.doc_mng}\t{self.name}'

    def get_file_name(self):
        return os.path.basename(self.attached.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
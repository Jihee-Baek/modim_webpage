from django.db import models

class DocManage(models.Model):
    name = models.CharField(max_length=100)         # 문서 이름

    def __str__(self):
        return f'{self.pk}. {self.name}'

class DocAttached(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    attached = models.FileField(upload_to='uploads/file/%Y/%m/%d/')

    doc_mng = models.ForeignKey(DocManage, on_delete=models.CASCADE)







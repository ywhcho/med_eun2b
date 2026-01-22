from django.db import models
from django.urls import reverse

class Medicine(models.Model):
    """의약품 정보 모델"""
    drug_name = models.CharField('약품명', max_length=200)
    ingredient = models.CharField('성분명', max_length=200)
    efficacy = models.TextField('효능')
    dosage = models.CharField('용량', max_length=200)
    precautions = models.TextField('주의사항')
    company = models.CharField('회사명', max_length=200)
    created_at = models.DateTimeField('등록일', auto_now_add=True)

    class Meta:
        ordering = ['drug_name']
        verbose_name = '의약품'
        verbose_name_plural = '의약품'

    def __str__(self):
        return self.drug_name

    def get_absolute_url(self):
        return reverse('medicine:detail', kwargs={'pk': self.pk})


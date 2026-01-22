from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    """게시판 게시글 모델"""
    title = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)
    views = models.IntegerField('조회수', default=0)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '게시글'
        verbose_name_plural = '게시글'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:detail', kwargs={'pk': self.pk})


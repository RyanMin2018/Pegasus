# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Blog Cateogry
class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='분류명')

    def __str__(self):
        return self.category_name

class Blog(models.Model):
    author         = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='등록자')
    category       = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='분류')
    title          = models.CharField(max_length=200, verbose_name='제목')
    text           = models.TextField(verbose_name='내용')
    created_date   = models.DateTimeField(default=timezone.now, verbose_name='생성일')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='공개일')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Attached Image
class AttachedImage(models.Model):
    blogid = models.ForeignKey(Blog, on_delete=models.CASCADE)
    img    = models.ImageField(blank=True, null=True, upload_to='%Y%m', verbose_name='이미지')

    def __str__(self):
        return self.img.name




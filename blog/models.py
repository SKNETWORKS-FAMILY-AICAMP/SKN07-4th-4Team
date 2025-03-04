from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


'''
Model은 데이터를 저장하기 위한 하나의 단위. 
'''

# Create your models here.

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(max_length=50)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True
    )
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d', blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def go2page(self):
        return f'/blog/{self.pk}/'

    def __str__(self):
        return f'[{self.pk}] {self.title} :: {self.author}'
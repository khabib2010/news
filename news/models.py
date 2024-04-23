from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class News(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    rasm=models.ImageField(upload_to='rasmlar/',null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    tur=models.ForeignKey(Category,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    prasmotr=models.PositiveIntegerField(default=0)
    like=models.ManyToManyField(User,related_name='likes')

    def __str__(self):
        return self.title




class Comment(models.Model):
    izoh=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    news=models.ForeignKey(News,on_delete=models.CASCADE, related_name='comments')
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.izoh[:20]



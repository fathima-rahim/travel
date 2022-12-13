from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class programmers(models.Model):
    image=models.ImageField(upload_to='pics')
    pname=models.CharField(max_length=250)
    discrp=models.TextField()

    def __str__(self):
        return self.pname
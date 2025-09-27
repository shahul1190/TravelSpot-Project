from django.db import models



class Tour(models.Model):
    Name=models.CharField(max_length=250)
    Weather=models.CharField(max_length=250)
    Location=models.CharField(max_length=2000)
    Map_link = models.URLField(blank=True)
    Tour_img=models.ImageField(upload_to='tour/')
    Description=models.CharField(max_length=5000)

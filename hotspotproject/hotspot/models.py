from django.db import models

# Create your models here.
class Hotspot(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    image=models.ImageField(upload_to='images')
    date_added=models.DateTimeField()
    year_added=models.IntegerField()

    def __str__(self):
        return self.name


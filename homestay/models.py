from django.db import models



# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=200)
    ima = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    address = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.name}'




   
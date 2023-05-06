from django.db import models
from django.core import validators
# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(5)])

    def __str__(self):
        return self.topic_name
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[validators.MaxLengthValidator(10)])
    url=models.URLField()
    Email=models.EmailField()
    
    
    def __str__(self):
        return self.name
    

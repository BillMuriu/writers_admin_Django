from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    academic_level = models.CharField(max_length=200)
    paper_type = models.CharField(max_length=200)
    discipline = models.CharField(max_length=200)
    topic = models.TextField(null=True, blank=True)
    paper_instructions = models.TextField(null=True, blank=True)
    pages = models.IntegerField(default = 0)
    #writer =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # id =

    def __str__(self):
        return self.discipline

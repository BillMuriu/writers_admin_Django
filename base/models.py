from django.db import models

# Create your models here.

class Order(models.Model):
    #client =
    #topic =
    name = models.CharField(max_length=200)
    academic_level = models.CharField(max_length=200)
    paper_type = models.CharField(max_length=200)
    discipline = models.CharField(max_length=200)
    topic = models.TextField(null=True, blank=True)
    paper_instructions = models.TextField(null=True, blank=True)
    #writer =
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

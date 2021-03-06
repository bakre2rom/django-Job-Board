from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

Job_Type = (
    ("Part Time","Part Time"),
    ("Full Time","Full Time")
)

class Job(models.Model): # table

    category = models.ForeignKey('Category',on_delete=CASCADE)
    title = models.CharField(max_length=100) #column
    # location
    job_type = models.CharField(max_length=15,choices=Job_Type,null=False,default='')
    description = models.CharField(max_length=1000,null=False)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
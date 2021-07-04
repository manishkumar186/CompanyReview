from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=250)
    founder = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    date = models.DateField()
    averageRating = models.FloatField()
    image = models.URLField(default=None,null=True)

    def __str__(self):
        return self.company_name

class Review(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username




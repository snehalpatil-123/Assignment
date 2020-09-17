from django.db import models


class Stock(models.Model):
    Name = models.CharField(max_length=50)
    EmailId = models.CharField(max_length=20)
    PhoneNo = models.IntegerField()
    Description = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


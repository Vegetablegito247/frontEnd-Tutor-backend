from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.email
    
from django.db import models

# Create your models here.
class Contacts(models.Model):
    contact_id = models.BigAutoField(primary_key=True)
    business_name = models.CharField( max_length=50)
    BUSINESS_TYPE = (
        ('R', 'Restaurant'),
        ('F', 'Farm'),
    )
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=20)
    country = models.CharField(max_length=25)


class Requests(models.Model):
    request_id = models.BigAutoField(primary_key=True)


class Orders(models.Model):
    contact_id = models.ForeignKey(
        Contacts, on_delete=models.CASCADE,
    )
    order_id = models.BigAutoField(primary_key=True)
    fulfillment_date = models.DateTimeField(auto_now=True)
    

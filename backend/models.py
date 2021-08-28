from django.db import models

# Create your models here.

def request_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / request_<id>/<filename>
    return 'request_{0}/{1}'.format(instance.id, filename)

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
    business_type = models.CharField(max_length=1, choices=BUSINESS_TYPE, default='R')


class Requests(models.Model):
    request_id = models.BigAutoField(primary_key=True)
    request_text = models.CharField(max_length=500) 
    post_date = models.DateTimeField('date posted')
    request_photo = models.ImageField(upload_to = request_directory_path)
    contact_id = models.ForeignKey(
        Contacts, on_delete=models.CASCADE,
    )


class Orders(models.Model):
    contact_id = models.ForeignKey(
        Contacts, on_delete=models.CASCADE,
    )
    order_id = models.BigAutoField(primary_key=True)
    fulfillment_date = models.DateTimeField(auto_now=True)
    
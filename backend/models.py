from django.db import models


def request_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / request_<id>/<filename>
    return 'request_{0}/{1}'.format(instance.id, filename)


class Users(models.Model):
    email_address = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=20)


class Contacts(models.Model):
    contact_id = models.BigAutoField(primary_key=True)
    business_name = models.CharField(max_length=50)
    BUSINESS_TYPE = (
        ('R', 'Restaurant'),
        ('F', 'Farm'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email_address = models.ForeignKey(
        Users, on_delete=models.CASCADE,
    )
    phone_number = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    zip = models.CharField(max_length=20)
    country = models.CharField(max_length=25)
    business_type = models.CharField(max_length=1, choices=BUSINESS_TYPE, default='R')


class Requests(models.Model):
    request_id = models.BigAutoField(primary_key=True)
    request_item = models.CharField(max_length=500)
    request_amount = models.DecimalField()
    requested_total_price = models.DecimalField()
    requested_expense = models.CharField()
    request_urgency = models.CharField()
    post_date = models.DateTimeField('date posted')
    request_photo = models.ImageField(upload_to=request_directory_path)
    contact_id = models.ForeignKey(
        Contacts, on_delete=models.CASCADE,
    )


class Orders(models.Model):
    contact_id = models.ForeignKey(
        Contacts, on_delete=models.CASCADE,
    )
    order_id = models.BigAutoField(primary_key=True)
    fulfillment_date = models.DateTimeField(auto_now=True)

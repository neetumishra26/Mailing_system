from django.db import models

# Create your models here.

class Email(models.Model):
    to_email_id = models.EmailField()
    from_email_id = models.EmailField()
    subject = models.TextField()
    content = models.TextField()

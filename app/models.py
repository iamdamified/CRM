from django.db import models

# Create your models here.
SERVICE_CHOICES = (
    ("CARDIOLOGY", "CARDIOLOGY"),
    ("DIAGNOSIS", "DIAGNOSIS"),
    ("SURGERY", "SURGERY"),
    ("FIRST AID", "FIRST AID"),
    ("INTENSIVE CARE", "INTENSIVE CARE"),
    ("GYNAECOLOGY", "GYNAECOLOGY"),
    ("NURSING", "NURSING"),
    ("PHARMACY", "PHARMACY"),
    ("DIALYSIS", "DIALYSIS"),
    ("ORTHOPAEDICS", "ORTHOPAEDICS")
)



class Department(models.Model):
    service = models.CharField(choices=SERVICE_CHOICES, max_length=25)
    image = models.ImageField(upload_to='service_image')
    description = models.TextField()

    def __str__(self):
        return self.service
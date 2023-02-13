from django.db import models

# Create your models here.
class Togri(models.Model):
    soz=models.CharField(max_length=50)
    def __str__(self):
        return self.soz
class Xato(models.Model):
    notogri=models.CharField(max_length=50)
    t_soz=models.ForeignKey(Togri,on_delete=models.CASCADE)
    def __str__(self):
        return self.notogri
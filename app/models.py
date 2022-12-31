from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Role(models.Model):
    
    
    ROLE_CHOICES = (
      (1, ' staff'),
      (2, ' doctor'),
      (3, ' nurse'),
      (4, 'manager'),
      (5, 'admin'),
  )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)  
   
    def __str__(self):
      return self.get_id_display()
class User(models.Model):
    roles = models.ForeignKey(Role, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
         return self.roles
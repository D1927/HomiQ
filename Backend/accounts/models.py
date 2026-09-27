from django.contrib.auth.models import AbstractUser
from django.db import models

# To create user along with mentioning roles
class User(AbstractUser):
    class Role(models.TextChoices):
        # To create choices for role
        TENANT = "TENANT" , "Tenant"
        OWNER = "OWNER" , "Owner" 
        PROVIDER = "PROVIDER" , "Service Provider"

    # Adding that feature for module
    role = models.CharField(
        max_length = 20 ,
        choices = Role.choices ,
        default = Role.TENANT
    )    

    def __str__ (self):
        return f"{self.username} is a {self.role}"


from django.db import models
from django.contrib.auth import get_user_model
import random
import string


User = get_user_model()


class Invoice(models.Model):
    def random_unique_code():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=45))
    
    unique_code = models.CharField(max_length=45, unique=True, default=random_unique_code)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

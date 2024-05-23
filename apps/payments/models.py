from django.db import models
from django.contrib.auth.models import User 
from apps.user.models import User
from django.db import models

# Your other imports and code
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Payment(models.Model):
    account = models.ForeignKey(
        'user.UserAccount',  # Use app_label.ModelName format for the ForeignKey
        on_delete=models.CASCADE,
        related_name="payments"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=256, null=True)
    finalized = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)









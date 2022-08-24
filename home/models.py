from plistlib import UID
from statistics import mode
import uuid
from django.db import models



class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now_add=True)
    



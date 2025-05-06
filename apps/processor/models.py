from django.db import models
import os
from datetime import datetime

def upload_to(instance, filename):
    now = datetime.now()
    return os.path.join('processed', f"{now.strftime('%Y%m%d_%H%M%S')}_{filename}")


from django.db import models

class ProcessedFile(models.Model):
    original_folder = models.CharField(max_length=255)
    master_file = models.FileField(upload_to='processed/')
    summary_file = models.FileField(upload_to='summary/', null=True, blank=True)  # <-- important!
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_folder


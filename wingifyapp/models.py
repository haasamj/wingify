from django.db import models

# Create your models here.
class wingifypass(models.Model):
    name = models.TextField()

    # created = models.DateTimeField(auto_now_add=True, editable=False)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

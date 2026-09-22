from django.db import models

class custome_model_manager(models.Manager):
    def is_active(self):
        return self.filter(is_active=True)
     
    def get_queryset(self):
        object=super().get_queryset()
        return object.filter(is_active=False)
import uuid

from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['created_at']
        abstract = True #no crea este modelo dentro de la base de datos, pues solo se usa para que los demás modelos hereden de este
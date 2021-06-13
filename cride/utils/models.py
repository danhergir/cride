"""Django models utilities"""

#Django
from django.db import models
from django.db.models.base import Model

class CRideModel(models.Model):
    """
     Acts as an abstract class from wich every other
     model in the project will inherit. This class provides
     every table with the following attributes:
        + created (DateTime)
        + modified (DateTime)
    """

    created = models.DateTimeField(
        'created_at',
        auto_now_add=True,
        help_text="Date time on which the object was created"
    )

    modified = models.DateTimeField(
        'modified_at',
        auto_now_add=True,
        help_text="Date time on which the object was last modified"
    )

    class Meta: 
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']

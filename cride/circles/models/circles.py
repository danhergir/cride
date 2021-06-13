from django.db import models

# Utilities
from cride.utils.models import CRideModel

class Circle(CRideModel):
    """
    A circle private where rides are offered.
    """

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='circles/pictures', blank=True, null=True)
    
    members = models.ManyToManyField('users.User', 
        through='circles.Membership',
        through_fields=('circle', 'user')
    )

    # Stats
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are also known as official communities'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Circles can be private or public'
    )

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to fixed number of members'
    )

    members_limit = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.name

    class Meta(CRideModel.Meta): 
        ordering = ['-rides_taken', '-rides_offered']
from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import User

class Feed(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return f'{self.id}'

    def get_absolute_url(self):
        return f'/{self.id}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

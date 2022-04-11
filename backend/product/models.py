from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE


class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='uploads/profile', blank=True, null=True)
    profile_thumbnail = models.ImageField(upload_to='uploads/profile', blank=True, null=True)

    #
    REQUIRED_FIELDS = ['nickname', 'get_profile_thumbnail', 'first_name', 'last_name']

    def __str__(self):
        return f'{self.nickname}'

    def get_absolute_url(self):
        return f'/{self.nickname}/{self.id}/'

    def get_profile_thumbnail(self):
        if self.profile_thumbnail:
            return 'http://127.0.0.1:8000' + self.profile_thumbnail.url
        else:
            if self.profile_image:
                self.profile_thumbnail = self.make_profile_thumbnail(self.profile_image)
                self.save()

                return 'http://127.0.0.1:8000' + self.profile_thumbnail.url
            else:
                return ''

    def make_profile_thumbnail(self, profile_image, size=(300, 300)):
        img = Image.open(profile_image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        profile_thumbnail = File(thumb_io, name=profile_image.name)

        return profile_thumbnail

class Feed(models.Model):
    profile = models.ForeignKey(User, on_delete=CASCADE)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return f'{self.profile.nickname}: {self.description}'

    def get_absolute_url(self):
        return f'/{self.id}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''

    def get_feed_poster(self):
        poster = {
            'poster_id': self.profile.id,
            'poster_nickname': self.profile.nickname,
            'poster_thumbnail': self.profile.get_profile_thumbnail(),
        }

        return poster

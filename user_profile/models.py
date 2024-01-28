from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    tg_id = models.CharField(max_length=15, null=True, blank=True, verbose_name='ID Телеграмм')
    tg_key = models.CharField(max_length=25, null=True, blank=True, verbose_name='Ключ')
    profile_pic = models.ImageField(
        null=True,
        blank=True,
        default='default.jpg',
        upload_to="profile",
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))],
        verbose_name='Аватар',
    )
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ['user']


    def save(self):
        super().save()
        if self.profile_pic:
            img = Image.open(self.profile_pic.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_pic.path)
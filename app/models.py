from django.db import models

from django.contrib.auth.models import User
from django.views.generic import View

from django.conf import settings
from django.conf.urls.static import static

from PIL import Image
from django.urls import reverse
from django.utils import timezone

from ckeditor.fields import RichTextField

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length = 100, default='', blank=True)
    image = models.ImageField(upload_to='image', default='', blank=True)
    url_text = models.CharField(max_length = 100, default = '', blank=True)
    amount = models.CharField(max_length = 20, default = '0', blank=True)
    description = RichTextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})

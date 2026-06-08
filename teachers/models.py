from django.db import models
from django.utils.text import slugify


class Teacher(models.Model):
    full_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    role = models.CharField(max_length=200, help_text="Masalan: Python Backend o'qituvchisi")
    bio = models.TextField()
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    courses = models.ManyToManyField('courses.Course', blank=True, related_name='teachers')
    telegram = models.CharField(max_length=100, blank=True, help_text="Masalan: @username")
    linkedin = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'full_name']
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('teachers:detail', kwargs={'slug': self.slug})

    @property
    def telegram_url(self):
        if self.telegram:
            handle = self.telegram.lstrip('@')
            return f"https://t.me/{handle}"
        return None

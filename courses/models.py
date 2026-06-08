from django.db import models
from django.utils.text import slugify


class Course(models.Model):
    LEVEL_CHOICES = [
        ('boshlangich', "Boshlang'ich"),
        ('orta', "O'rta"),
        ('ilgor', "Ilg'or"),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    tagline = models.CharField(max_length=150, help_text="Qisqa, ta'sirchan bir qator")
    description = models.TextField()
    cover_image = models.ImageField(upload_to='courses/', blank=True, null=True)
    icon_emoji = models.CharField(max_length=10, default='💻', help_text="Emoji icon, masalan: 🎨")
    duration = models.CharField(max_length=50, help_text="Masalan: 3 oy")
    schedule = models.CharField(max_length=100, help_text="Masalan: Du-Cho-Ju 15:00-17:00")
    price = models.CharField(max_length=100, help_text="Masalan: Bepul yoki 450 000 so'm/oy")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='boshlangich')
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('courses:detail', kwargs={'slug': self.slug})

    @property
    def level_display(self):
        return dict(self.LEVEL_CHOICES).get(self.level, self.level)

from django.db import models


class CareerPath(models.Model):
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.CASCADE,
        related_name='career_paths'
    )
    job_title = models.CharField(max_length=200, help_text="Masalan: Python dasturchisi")
    description = models.TextField()
    avg_salary_range = models.CharField(max_length=100, help_text="Masalan: $400-800/oy")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Career Path'
        verbose_name_plural = 'Career Paths'

    def __str__(self):
        return f"{self.job_title} ({self.course})"


class CareerCompany(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='career/companies/', blank=True, null=True)
    career_path = models.ForeignKey(
        CareerPath,
        on_delete=models.CASCADE,
        related_name='companies'
    )

    class Meta:
        verbose_name = 'Career Company'
        verbose_name_plural = 'Career Companies'

    def __str__(self):
        return self.name

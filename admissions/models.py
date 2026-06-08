from django.db import models


class Application(models.Model):
    STATUS_CHOICES = [
        ('yangi', 'Yangi'),
        ('korib_chiqilmoqda', "Ko'rib chiqilmoqda"),
        ('qabul_qilindi', 'Qabul qilindi'),
        ('rad_etildi', 'Rad etildi'),
    ]

    full_name = models.CharField(max_length=200, verbose_name="To'liq ism")
    phone = models.CharField(max_length=30, verbose_name="Telefon raqam")
    course = models.ForeignKey(
        'courses.Course',
        on_delete=models.SET_NULL,
        null=True,
        related_name='applications',
        verbose_name="Kurs"
    )
    message = models.TextField(blank=True, verbose_name="Xabar (ixtiyoriy)")
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='yangi')
    admin_note = models.TextField(blank=True, verbose_name="Admin izohi (ichki)")

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return f"{self.full_name} — {self.course}"

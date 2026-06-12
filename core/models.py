from django.db import models


class SiteSettings(models.Model):
    """Singleton model for global site configuration."""

    hero_headline = models.CharField(
        max_length=200, default="AyTi olamiga birinchi qadam."
    )
    hero_sub = models.CharField(
        max_length=300,
        default="IT Park tarmog'ining Yaypandagi markazi. Kichik guruhlar. Amaliy ta'lim.",
    )
    hero_typed_words = models.CharField(
        max_length=300,
        default="Dasturlash, Backend, Grafik dizayn, Python, Sun'iy intellekt",
        help_text="Bosh sahifadagi yozilib-o'chiriladigan so'zlar, vergul bilan ajrating",
    )
    about_text = models.TextField(
        default="IT Center Yaypan — Farg'ona viloyatining Yaypan tumanida joylashgan texnologiya ta'lim markazi. IT Park tarmog'ining bir qismi sifatida faoliyat yuritamiz. Maqsadimiz — dasturlash va raqamli ko'nikmalarni hududdagi yoshlarga yetkazish."
    )
    address = models.CharField(
        max_length=300, default="Yaypan tumani, Farg'ona viloyati"
    )
    phone = models.CharField(max_length=50, default="+998 90 058 68 55")
    telegram_url = models.URLField(blank=True, default="https://t.me/itcenteryaypan")
    instagram_url = models.URLField(blank=True)
    working_hours = models.CharField(
        max_length=100, default="Dushanba-Shanba: 08:00-18:00"
    )
    google_maps_embed_url = models.URLField(blank=True, max_length=1000)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

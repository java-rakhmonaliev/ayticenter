"""
Management command to seed initial data for IT Center Yaypan.
Run: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from courses.models import Course
from teachers.models import Teacher
from career.models import CareerPath, CareerCompany
from news.models import Post
from core.models import SiteSettings
from django.utils import timezone


class Command(BaseCommand):
    help = "Seed initial data for IT Center Yaypan"

    def handle(self, *args, **options):
        self.stdout.write("Seeding data...\n")

        self._seed_site_settings()
        courses = self._seed_courses()
        self._seed_career_paths(courses)
        self._seed_news()

        self.stdout.write(self.style.SUCCESS("\n✓ Seed complete. All data created.\n"))
        self.stdout.write("  Run: python manage.py createsuperuser\n")
        self.stdout.write("  Then: python manage.py runserver\n")

    def _seed_site_settings(self):
        settings, created = SiteSettings.objects.get_or_create(pk=1)
        settings.hero_headline = "Dasturlashni o'rgan. Yerda, haqiqatda."
        settings.hero_sub = (
            "IT Park tarmog'ining Yaypandagi markazi. "
            "Kichik guruhlar, amaliy ta'lim, haqiqiy loyihalar."
        )
        settings.about_text = (
            "IT Center Yaypan — Farg'ona viloyatining Yaypan tumanida joylashgan texnologiya ta'lim markazi. "
            "IT Park tarmog'ining bir qismi sifatida faoliyat yuritamiz.\n\n"
            "Markazimiz 2023-yilda ochilgan. Maqsadimiz — dasturlash va raqamli ko'nikmalarni "
            "hududdagi yoshlarga yetkazish. Katta shaharlarga bormasdan ham, "
            "sifatli IT ta'lim olish mumkin — shu fikrdan kelib chiqib ish boshladik.\n\n"
            "Kichik guruhlar bilan ishlaymiz: maksimum 12 kishi. "
            "Shu sababli har bir o'quvchiga alohida e'tibor qarata olamiz. "
            "Dars jarayonida nazariy bilimdan ko'ra amaliy loyihalarga ko'proq urg'u beriladi."
        )
        settings.address = "Yaypan tumani, Farg'ona viloyati, O'zbekiston"
        settings.phone = "+998 73 XXX XX XX"
        settings.telegram_url = "https://t.me/itcenter_yaypan"
        settings.working_hours = "Du-Ju: 09:00-18:00, Sha: 10:00-15:00"
        settings.save()
        status = "created" if created else "updated"
        self.stdout.write(f"  ✓ SiteSettings {status}")

    def _seed_courses(self):
        courses_data = [
            {
                "name": "Kompyuter Savodxonligi",
                "tagline": "Kompyuter bilan ishlashni noldan o'rganish.",
                "description": (
                    "Kompyuter savodxonligi kursi — hayotida birinchi marta kompyuter bilan jiddiy ishlashni "
                    "boshlamoqchi bo'lganlar uchun. Bu yerda hech narsa o'z-o'zidan tushunarli deb hisoblanmaydi.\n\n"
                    "Kursda siz Windows yoki macOS operatsion tizimi bilan ishlashni, "
                    "Microsoft Office dasturlari (Word, Excel, PowerPoint) asoslarini, "
                    "internet va elektron pochta bilan ishlashni o'rganasiz. "
                    "Bundan tashqari, fayl va papkalarni tartibli saqlash, "
                    "onlayn xavfsizlik va parollar boshqaruviga oid bilimlar ham beriladi.\n\n"
                    "Kurs oxirida siz kundalik ish va o'qish uchun zarur bo'lgan barcha asosiy "
                    "kompyuter ko'nikmalariga ega bo'lasiz."
                ),
                "icon_emoji": "💻",
                "duration": "2 oy",
                "schedule": "Du-Cho-Ju 14:00-16:00",
                "price": "350 000 so'm/oy",
                "level": "boshlangich",
                "order": 1,
            },
            {
                "name": "Foundation",
                "tagline": "IT sohasiga kirish: ingliz tili, mantiqiy fikrlash, matematik asos.",
                "description": (
                    "Foundation kursi — IT sohasiga kirishdan oldin zarur bo'lgan asos. "
                    "Bu kurs texnik bilimlarni o'rganishdan ko'ra, o'rganish qobiliyatini rivojlantirishga yo'naltirilgan.\n\n"
                    "Kursda IT ingliz tili — dasturlashda eng ko'p uchraydigan so'zlar va atamalar, "
                    "mantiqiy fikrlash va algoritmik tafakkur, matematik asos (son sistemalari, "
                    "mantiq elementlari), va terminal bilan boshlang'ich ishlash ko'nikmalariga ega bo'lasiz.\n\n"
                    "Agar dasturlashni o'rganishni istasangiz, lekin qayerdan boshlashni bilmasangiz — "
                    "Foundation siz uchun eng to'g'ri qadam. "
                    "Kurs tugagach, Python Backend yoki boshqa texnik kursga tayyor bo'lasiz."
                ),
                "icon_emoji": "🧱",
                "duration": "2 oy",
                "schedule": "Se-Pa-Sha 10:00-12:00",
                "price": "400 000 so'm/oy",
                "level": "boshlangich",
                "order": 2,
            },
            {
                "name": "Python Backend Development",
                "tagline": "Server tarafida dasturlash: Python, Django, API, ma'lumotlar bazasi.",
                "description": (
                    "Python Backend Development kursi — professional veb dasturchi bo'lishni maqsad qilganlar uchun. "
                    "Kurs davomida siz Python dasturlash tilini puxta o'rganib, "
                    "Django freymvorki asosida real veb-ilovalar yaratishni o'rganasiz.\n\n"
                    "Kurs modullariga quyidagilar kiradi: Python asoslari va ilg'or mavzular, "
                    "ma'lumotlar bazasi (PostgreSQL) bilan ishlash, Django ORM, "
                    "REST API yaratish, autentifikatsiya va ruxsatlar tizimi, "
                    "deployment — serverga chiqarish, Git va versiya nazorati.\n\n"
                    "Har oyda kamida bitta amaliy loyiha bajariladi. "
                    "Kurs oxirida portfoliongizda haqiqiy loyihalar bo'ladi."
                ),
                "icon_emoji": "🐍",
                "duration": "6 oy",
                "schedule": "Du-Cho-Ju 17:00-19:30",
                "price": "600 000 so'm/oy",
                "level": "orta",
                "order": 3,
            },
            {
                "name": "Grafik Dizayn",
                "tagline": "Figma, Adobe, brend identifikatsiyasi va UI asoslari.",
                "description": (
                    "Grafik Dizayn kursi — vizual kommunikatsiya bilan professional darajada ishlashni "
                    "o'rganmoqchi bo'lganlar uchun. Kursda ko'proq amaliy ish bo'ladi: loyihalar, brieflar, "
                    "real topshiriqlar.\n\n"
                    "Kurs davomida Adobe Photoshop va Illustrator dasturlari, Figma bilan UI dizayn, "
                    "tipografiya — harflar bilan ishlash san'ati, rang nazariyasi va kompozitsiya, "
                    "logotip va brend identifikatsiyasi yaratish, "
                    "va ijtimoiy tarmoqlar uchun dizayn qilishni o'rganasiz.\n\n"
                    "Kurs oxirida sizda to'liq portfolio bo'ladi: logotiplar, bannerlar, "
                    "UI ekranlar va brending loyihalari."
                ),
                "icon_emoji": "🎨",
                "duration": "4 oy",
                "schedule": "Se-Pa 15:00-17:30, Sha 11:00-14:00",
                "price": "500 000 so'm/oy",
                "level": "boshlangich",
                "order": 4,
            },
        ]

        created_courses = {}
        for data in courses_data:
            slug = slugify(data["name"])
            course, created = Course.objects.get_or_create(
                slug=slug,
                defaults={**data},
            )
            if not created:
                for k, v in data.items():
                    setattr(course, k, v)
                course.save()
            created_courses[data["name"]] = course
            status = "created" if created else "updated"
            self.stdout.write(f"  ✓ Course '{course.name}' {status}")

        return created_courses

    def _seed_career_paths(self, courses):
        career_data = {
            "Python Backend Development": [
                {
                    "job_title": "Python Backend Dasturchisi",
                    "description": (
                        "Veb-ilovalar uchun server tomoni logikasini yozish. "
                        "Django yoki FastAPI bilan API yaratish, ma'lumotlar bazasini boshqarish. "
                        "O'zbekistonda IT kompaniyalarda va masofaviy ish sifatida talabi yuqori."
                    ),
                    "avg_salary_range": "$400–900/oy",
                    "companies": ["Nestle UZ (IT bo'lim)", "Uzum Market", "Humans", "Upwork/Toptal"],
                },
                {
                    "job_title": "Junior Django Developer",
                    "description": (
                        "Kichik va o'rta loyihalarda Django freymvorki asosida ishlash. "
                        "Ko'pincha bitta katta jamoaning bir qismi sifatida ish boshlash mumkin."
                    ),
                    "avg_salary_range": "$300–600/oy",
                    "companies": ["Mahalliy startaplar", "IT agentliklar"],
                },
                {
                    "job_title": "Freelance Backend Developer",
                    "description": (
                        "Xorijiy va mahalliy mijozlar uchun mustaqil ishlash. "
                        "Upwork, Fiverr, Freelancer kabi platformalarda loyihalar olish mumkin. "
                        "Boshida qiyin, tajriba ortgan sari daromad o'sadi."
                    ),
                    "avg_salary_range": "$200–1500/oy",
                    "companies": ["Upwork", "Fiverr", "Freelancer"],
                },
            ],
            "Grafik Dizayn": [
                {
                    "job_title": "Grafik Dizayner",
                    "description": (
                        "Brendlar, nashriyotlar, reklama agentliklari uchun vizual materiallar yaratish. "
                        "Logotip, plakat, broshyura, ijtimoiy tarmoq kontenti."
                    ),
                    "avg_salary_range": "$250–600/oy",
                    "companies": ["Reklama agentliklari", "Media kompaniyalar", "Brendlar"],
                },
                {
                    "job_title": "UI/UX Dizayner",
                    "description": (
                        "Mobil ilovalar va veb-saytlar uchun foydalanuvchi interfeysi loyihalash. "
                        "Figma asosiy vosita. IT kompaniyalarda talab yuqori, "
                        "dasturchilar bilan jamoada ishlash zarur."
                    ),
                    "avg_salary_range": "$400–1000/oy",
                    "companies": ["IT kompaniyalar", "Startaplar", "Freelance"],
                },
                {
                    "job_title": "SMM va Kontent Dizayner",
                    "description": (
                        "Ijtimoiy tarmoqlar uchun vizual kontent yaratish. "
                        "Instagram, Telegram kanallar, korxona sahifalari uchun dizayn. "
                        "Kirishga nisbatan osonroq yo'l."
                    ),
                    "avg_salary_range": "$150–400/oy",
                    "companies": ["Mahalliy bizneslar", "Onlayn do'konlar", "Freelance"],
                },
            ],
        }

        for course_name, paths in career_data.items():
            course = courses.get(course_name)
            if not course:
                continue
            for i, path_data in enumerate(paths):
                companies = path_data.pop("companies", [])
                path, created = CareerPath.objects.get_or_create(
                    course=course,
                    job_title=path_data["job_title"],
                    defaults={**path_data, "order": i},
                )
                if not created:
                    for k, v in path_data.items():
                        setattr(path, k, v)
                    path.order = i
                    path.save()

                for company_name in companies:
                    CareerCompany.objects.get_or_create(
                        career_path=path,
                        name=company_name,
                    )

                status = "created" if created else "updated"
                self.stdout.write(f"  ✓ CareerPath '{path.job_title}' {status}")

    def _seed_news(self):
        posts_data = [
            {
                "title": "2024-yil qabul boshlandi",
                "body": (
                    "Yangi o'quv yiliga qabul rasman boshlandi. Bu yil to'rtta kurs bo'yicha o'quvchi qabul qilinadi: "
                    "Kompyuter Savodxonligi, Foundation, Python Backend Development va Grafik Dizayn.\n\n"
                    "Guruhlar kichik — maksimum 12 kishi. Shuning uchun o'rinlar cheklangan. "
                    "Ariza topshirish sahifasiga o'ting va ma'lumotlaringizni qoldiring. "
                    "Bir ish kuni ichida aloqaga chiqamiz."
                ),
                "is_published": True,
                "published_at": timezone.now(),
            },
            {
                "title": "Python kursi yangi oquv dasturi bilan boshlandi",
                "body": (
                    "Python Backend Development kursining yangi kohortiida o'quv dasturi yangilandi. "
                    "Endi kursga FastAPI ham qo'shildi — Django bilan birga ikki xil freymvork o'rganiladi.\n\n"
                    "Bundan tashqari, kurs oxirida o'quvchilar real mijoz loyihasida ishtirok etish imkoniyatiga ega bo'lishadi. "
                    "Bu tajriba portfolio uchun muhim va haqiqiy ish jarayonini his qilishga yordam beradi."
                ),
                "is_published": True,
                "published_at": timezone.now(),
            },
        ]

        for data in posts_data:
            slug = slugify(data["title"])
            post, created = Post.objects.get_or_create(
                slug=slug,
                defaults={**data},
            )
            status = "created" if created else "exists"
            self.stdout.write(f"  ✓ Post '{post.title}' {status}")

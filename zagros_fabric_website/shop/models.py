from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.


class Material(models.Model):
    name = models.CharField(max_length=100, verbose_name="جنس پارچه")
    first_page = models.BooleanField(default=False, verbose_name="نمایش در صفحه اول")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "جنس پارچه"
        verbose_name_plural = "جنس های پارچه"


class Pattern(models.Model):
    name = models.CharField(max_length=100, verbose_name="طرح پارچه")
    first_page = models.BooleanField(default=False, verbose_name="نمایش در صفحه اول")
    original_image = models.ImageField(upload_to='pattern_images', blank=True, null=True, verbose_name='تصویر')
    
    thumbnail_small = ImageSpecField(
        source="original_image",
        processors=[ResizeToFill(100, 100)],
        format="WEBP",
        options={"quality": 90},
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "طرح پارچه"
        verbose_name_plural = "طرح های پارچه"


class Usage(models.Model):
    name = models.CharField(max_length=150, verbose_name="کاربرد پارچه")
    first_page = models.BooleanField(default=False, verbose_name="نمایش در صفحه اول")
    original_image = models.ImageField(upload_to='usage_images', blank=True, null=True, verbose_name='تصویر')
    
    thumbnail_small = ImageSpecField(
        source='original_image',
        processors=[ResizeToFill(100, 100)],
        format="WEBP",
        options={"quality": 90},
    )
    
    thumbnail_medium = ImageSpecField(
        source="original_image",
        processors=[ResizeToFill(360, 240)],
        format="WEBP",
        options={"quality": 80},
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "کاربرد پارچه"
        verbose_name_plural = "کاربردهای پارچه"
        
    

class Color(models.Model):
    name = models.CharField(max_length=100, verbose_name="رنگ پارچه")
    hex_code = models.CharField(max_length=7, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "رنگ پارچه"
        verbose_name_plural = "رنگ های پارچه"


class Width(models.Model):
    name = models.IntegerField(verbose_name="عرض پارچه")

    def __str__(self):
        return f"{self.name} سانتی‌متر"

    class Meta:
        verbose_name = "عرض پارچه"
        verbose_name_plural = "عرض های پارچه"


class Fabric(models.Model):
    THICKNESS_CHOICES = [
        ("thin", "نازک"),
        ("normal", "معمولی"),
        ("thick", "ضخیم"),
    ]
    name = models.CharField(max_length=200, verbose_name="عنوان")
    thickness = models.CharField(
        max_length=10, choices=THICKNESS_CHOICES, verbose_name="ضخامت پارچه"
    )
    inventory = models.FloatField(default=0, verbose_name="مقدار موجودی پارچه")
    price = models.IntegerField(verbose_name="قیمت")

    material = models.ForeignKey(
        Material, on_delete=models.PROTECT, verbose_name="جنس پارچه"
    )
    pattern = models.ForeignKey(
        Pattern, on_delete=models.PROTECT, verbose_name="طرح پارچه"
    )
    usage = models.ManyToManyField(Usage, verbose_name="کاربرد پارچه")
    color = models.ManyToManyField(Color, verbose_name="رنگ پارچه")
    width = models.ForeignKey(
        Width, related_name="fabric", on_delete=models.PROTECT, verbose_name="عرض پارچه"
    )
    first_page = models.BooleanField(default=False, verbose_name="نمایش در صفحه اول")

    class Meta:
        verbose_name = "پارچه"
        verbose_name_plural = "پارچه ها"

    def __str__(self):
        return self.name


class FabricImages(models.Model):
    original_image = models.ImageField(
        upload_to="fabric_images", blank=True, null=True, verbose_name="تصویر"
    )
    fabric = models.ForeignKey(
        Fabric, on_delete=models.CASCADE, related_name="images", verbose_name="پارچه"
    )

    thumbnail_small = ImageSpecField(
        source="original_image",
        processors=[ResizeToFill(100, 100)],
        format="WEBP",
        options={"quality": 90},
    )

    thumbnail_medium = ImageSpecField(
        source="original_image",
        processors=[ResizeToFill(240, 240)],
        format="WEBP",
        options={"quality": 80},
    )

    thumbnail_large = ImageSpecField(
        source="original_image",
        processors=[ResizeToFill(500, 500)],
        format="WEBP",
        options={"quality": 75},
    )

    class Meta:
        verbose_name = "تصویر"
        verbose_name_plural = "تصاویر"

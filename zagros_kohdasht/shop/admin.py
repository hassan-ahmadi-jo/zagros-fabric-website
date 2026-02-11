from django.contrib import admin
from django.utils.html import format_html
from . import models
from django import forms
from django.forms.widgets import ColorInput
from django.utils.html import format_html

# Register your models here.

class FabricImagesInline(admin.TabularInline):
    model = models.FabricImages
    extra = 3
    fields = ['image']

class FabricAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_page', 'material', 'inventory', 'price', 'image_existence']
    list_filter = ['inventory', 'first_page']
    list_editable = ['inventory', 'first_page']
    inlines = [FabricImagesInline]
    def image_existence(self, obj):
        if obj.images.count() > 0:
            color = 'green'
            text = 'موجود'
        else:
            color = 'red'
            text = 'ناموجود'
        return format_html(f'<span style="background-color: {color}; color: white; padding: 3px 10px; border-radius: 5px;">{text}</span>')
    
    image_existence.short_description = 'آیا تصویر وجود دارد؟'

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_page']
    list_filter = ['first_page']
    list_editable = ['first_page']
    
class PatternAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_page', 'image_existence']
    list_filter = ['first_page']
    list_editable = ['first_page']
    
    def image_existence(self, obj):
        if obj.thumbnail_small:
            color = 'green'
            text = 'موجود'
        else:
            color = 'red'
            text = 'ناموجود'
        return format_html(f'<span style="background-color: {color}; color: white; padding: 3px 10px; border-radius: 5px;">{text}</span>')
    image_existence.short_description = 'آیا تصویر وجود دارد؟'
    
class UsageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_page', 'image_existence']
    list_filter = ['first_page']
    list_editable = ['first_page']
    
    def image_existence(self, obj):
        if obj.thumbnail_small:
            color = 'green'
            text = 'موجود'
        else:
            color = 'red'
            text = 'ناموجود'
        return format_html(f'<span style="background-color: {color}; color: white; padding: 3px 10px; border-radius: 5px;">{text}</span>')
    image_existence.short_description = 'آیا تصویر وجود دارد؟'
    
class ColorAdminForm(forms.ModelForm):
    class Meta:
        model = models.Color
        fields = "__all__"
        widgets = {
            "hex_code": ColorInput(attrs={"type": "color"}),
        }

class ColorAdmin(admin.ModelAdmin):
    form = ColorAdminForm


admin.site.register(models.Material, MaterialAdmin)
admin.site.register(models.Pattern, PatternAdmin)
admin.site.register(models.Usage, UsageAdmin)
admin.site.register(models.Color, ColorAdmin)
admin.site.register(models.Width)
admin.site.register(models.Fabric, FabricAdmin)
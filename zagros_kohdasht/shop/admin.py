from django.contrib import admin
from . import models
from django import forms
from django.forms.widgets import ColorInput

class ColorAdminForm(forms.ModelForm):
    class Meta:
        model = models.Color
        fields = "__all__"
        widgets = {
            "hex_code": ColorInput(attrs={"type": "color"}),
        }

class ColorAdmin(admin.ModelAdmin):
    form = ColorAdminForm

# Register your models here.

class FabricAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_page', 'material', 'inventory', 'price']
    list_filter = ['inventory', 'first_page']
    list_editable = ['inventory', 'first_page']

class MaterialAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_page']
    list_filter = ['first_page']
    list_editable = ['first_page']
    
class PatternAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_page']
    list_filter = ['first_page']
    list_editable = ['first_page']

class UsageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'first_page']
    list_filter = ['first_page']
    list_editable = ['first_page']


admin.site.register(models.Material, MaterialAdmin)
admin.site.register(models.Pattern, PatternAdmin)
admin.site.register(models.Usage, UsageAdmin)
admin.site.register(models.Color, ColorAdmin)
admin.site.register(models.Width)
admin.site.register(models.Fabric, FabricAdmin)
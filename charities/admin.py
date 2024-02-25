from django.contrib import admin
from .models import Charity, Category

# Register your models here.

admin.site.register(Charity)
admin.site.register(Category)
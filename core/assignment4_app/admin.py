from django.contrib import admin
from assignment4_app import models
# Register your models here.
admin.site.register(models.Tags)
admin.site.register(models.Category)
admin.site.register(models.Product)
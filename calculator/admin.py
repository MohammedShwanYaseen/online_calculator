from django.contrib import admin
from calculator import models

admin.site.register(models.UserProfile)
admin.site.register(models.Category)
admin.site.register(models.Course)
admin.site.register(models.Article)
admin.site.register(models.Partner)

#admin.site.register(models.student)
#admin.site.register(models.Grade)
# Register your models here.

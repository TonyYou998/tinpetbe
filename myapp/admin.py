from django.contrib import admin
from .models import Pet,UserFavourite,Comment

# Register your models here.
# admin.site.register(demo)
admin.site.register(Pet)
admin.site.register(UserFavourite)
admin.site.register(Comment)
# admin.site.register(Product)
from django.contrib import admin
from . models import Category, Designer, Asset, Download, Favorites

admin.site.register(Category)
admin.site.register(Designer)
admin.site.register(Asset)
admin.site.register(Download)
admin.site.register(Favorites)
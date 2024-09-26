from django.db import models
from django.utils import timezone
import datetime

#Categories of assets
class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

#User/designers details
class Designer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=10,  null=True, blank=True)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=100, null=True, blank=True)
    password2 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.username}'

#All assets details
class Asset(models.Model):
    asset_name = models.CharField(max_length=50)
    asset_description = models.CharField(max_length=250, default='', blank=True, null=True)
    filetype = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    uploaddate = models.DateTimeField(default=timezone.now)  # Automatically set when the asset is uploaded
    assettype = models.CharField(max_length=50)
    asset_image = models.ImageField(upload_to='uploads/assets/')  

    def __str__(self):
        return self.asset_name

# Asset downloads
class Download(models.Model):
    file_name = models.CharField(max_length=50)
    timestamp = models.DateField(default = datetime.datetime.today)
    downloadstatus = models.BooleanField(default = False)
    designer = models.ForeignKey(Designer, on_delete = models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete = models.CASCADE,  null=True, blank=True)

    def __str__(self):
        return self.assets

#Favroite assets
class Favorites(models.Model):
    designer = models.ForeignKey(Designer, on_delete = models.CASCADE)
    assets = models.ForeignKey(Asset, on_delete = models.CASCADE)

    def __str__(self):
        return self.assets

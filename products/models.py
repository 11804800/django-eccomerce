from django.db import models
from django.utils.text import slugify

class Products(models.Model):
    preview=models.JSONField()
    name=models.CharField(unique=True,blank=True,max_length=255)
    fullname=models.CharField(blank=True,null=True)
    featured=models.BooleanField(default=False)
    prime=models.BooleanField(default=False)
    certified=models.BooleanField(default=False)
    os=models.CharField(blank=True,null=True)
    processor=models.CharField(blank=True,null=True)
    modal=models.CharField(blank=True,null=True)
    category=models.CharField(blank=True,null=True)
    brand=models.CharField(blank=True,null=True)
    sellertype=models.CharField(blank=True,null=True)
    seller=models.CharField(blank=True,null=True)
    charge=models.CharField(blank=True,null=True)
    label=models.CharField(blank=True,null=True)
    weight=models.CharField(blank=True,null=True)
    color=models.CharField(blank=True,null=True)
    size=models.CharField(blank=True,null=True)
    price=models.PositiveIntegerField(default=0)
    cprice=models.IntegerField(blank=True,null=True)
    description=models.CharField(blank=True,null=True)
    slug=models.SlugField(blank=True)
    quantity=models.PositiveIntegerField(default=10)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

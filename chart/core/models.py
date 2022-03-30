from django.db import models


class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
    
    name = models.CharField(max_length=50)
    daromadi = models.IntegerField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        verbose_name = "Field"
        verbose_name_plural = "Field"
    
    name = models.CharField(max_length=50)
    daromadi = models.IntegerField()
    
    def __str__(self):
        return self.name 

class Post(models.Model):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Custome"
    
    name = models.CharField(max_length=50)
    daromadi = models.IntegerField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Section"
    
    name = models.CharField(max_length=50)
    daromadi = models.IntegerField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        verbose_name = "Copy"
        verbose_name_plural = "Copy"
    
    name = models.CharField(max_length=50)
    daromadi = models.IntegerField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    class Meta:
        verbose_name = "Information"
        verbose_name_plural = "Information"
    
    name = models.CharField(max_length=50)
    daromadi = models.IntegerField()
    
    def __str__(self):
        return self.name
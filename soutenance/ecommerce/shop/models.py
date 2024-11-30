from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now = True)
    class Meta:
        ordering = ['-date_added']
    def  __str__(self):
        return self.name
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category , related_name = 'categorie', on_delete = models.CASCADE)
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now= True)
    class Meta:
        ordering = ['-date_added']
    def  __str__(self):
        return self.title
class Commander(models.Model):
    items = models.CharField(max_length=200)
    total= models.CharField(max_length=200)
    nom = models.CharField(max_length=20)
    email = models.EmailField()
    adresse = models.EmailField(max_length=200)
    ville = models.CharField( max_length=200)
    pays = models.CharField( max_length=200)
    zipcode = models.CharField(max_length=200)
    date_commander = models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ['-date_commander']

    def __str__(self):
        return self.nom
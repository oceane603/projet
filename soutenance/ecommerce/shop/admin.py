from django.contrib import admin
from .models import Category , Product , Commander
# Register your models here.

admin.site.site_header = "E-commerce"
admin.site.site_title = "SBC shop"
admin.site.index_title = "Manager"


class AdminCategorie(admin.ModelAdmin):
    list_display = ('name','date_added')

class AdminProduct(admin.ModelAdmin):
    list_display = ('title','price', 'category' ,'date_added')
    search_fields = ('title',)
    list_editable = ('price',)

class AdminCommander(admin.ModelAdmin):
    list_display = ('items','nom','email', 'adresse' ,'ville' ,'pays' ,'total', 'date_commander')

admin.site.register(Product, AdminProduct)
admin.site.register(Category ,AdminCategorie)
admin.site.register(Commander,AdminCommander)


from django.contrib import admin
from .models import Category, Item, Stock, Transaction

class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]
admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Item._meta.fields]
admin.site.register(Item, ItemAdmin)

class StockAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Stock._meta.fields]
admin.site.register(Stock, StockAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Transaction._meta.fields]
admin.site.register(Transaction, TransactionAdmin)
# Register your models here.

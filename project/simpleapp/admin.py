from django.contrib import admin
from .models import Category, New


# создаём новый класс для представления новостей в админке
class NewAdmin(admin.ModelAdmin):
    # list_display - это список или кортеж со всеми полями, которые вы хотите видеть в таблице с новостями
    list_display = ('name', 'date_pub', 'category')
    list_filter = ('date_pub', 'category')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('name', 'category')  # тут всё очень похоже на фильтры из запросов в базу

# Register your models here.

admin.site.register(Category)
admin.site.register(New, NewAdmin)

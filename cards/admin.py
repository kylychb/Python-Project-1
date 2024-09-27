from django.contrib import admin

from .models import Category, Item, ItemImages


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

class ItemImagesInline(admin.StackedInline):
    model = ItemImages
    extra = 0

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = (ItemImagesInline,)

@admin.register(ItemImages)
class ItemImagesAdmin(admin.ModelAdmin):
    pass

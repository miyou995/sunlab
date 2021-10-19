from django.contrib import admin
from .models import Product, SubCategory, Category, ContactForm,  Gamme, PhotoProduct
from django.contrib.auth.models import Group, User
from django.utils.html import format_html

admin.autodiscover()
admin.site.enable_nav_sidebar = False
admin.site.unregister(Group)

class SubCategoryLinesAdmin(admin.TabularInline):
    model = SubCategory
    readonly_fields = ('name','slug')

class PhotosLinesAdmin(admin.TabularInline):
    def image_tag(self):
        return format_html('<img src="{}" height="150"  />'.format(self.photo.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    model = PhotoProduct
    readonly_fields= (image_tag,)
    # readonly_fields = ('photo',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'actif')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name')
    list_per_page = 40
    list_editable = ['actif']
    search_fields = ('id', 'name',)
    exlude = ['slug']
    inlines = [SubCategoryLinesAdmin,]



class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'actif')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 40
    list_filter = ('category',)
    list_editable = [ 'category', 'actif']
    search_fields = ('name',)
    exlude = ['slug']
    


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sous_category', 'old_price', 'price', 'new', 'top', 'actif', 'volume', 'gamme', 'status')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('id','name' )
    list_per_page = 40
    list_filter = ('name', 'sous_category','price', 'new')
    list_editable = ['sous_category', 'price', 'new', 'top', 'actif', 'old_price', 'status']
    search_fields = ('name',)
    exlude = ['slug']
    inlines = [PhotosLinesAdmin]
    save_as= True
    


# Contact
class GammeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id','name')
    list_per_page = 40
    search_fields = ('id', 'name')

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    list_per_page = 40
    list_filter = ('name', 'phone', 'email',)
    search_fields = ('id', 'phone', 'email')




class PhotosAdmin(admin.ModelAdmin):
    def image_tag(self):
        return format_html('<img src="{}" height="150"  />'.format(self.big_slide.url))
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    list_display = ('id', image_tag, 'actif', 'is_big', 'is_small', 'big_slide')
    list_editable = ['actif', 'is_big', 'is_small', 'big_slide']
    list_display_links = ('id',image_tag)
    list_per_page = 40


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Gamme, GammeAdmin)

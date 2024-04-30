from django.contrib import admin
from .import models
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'added_by','slug','add_time', 'image']
    prepopulated_fields = {"slug": ("name",)}

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name','phone','problem']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display=['reviewer_name','recipe_name','rating']
    
    def reviewer_name(self,obj):
        return obj.user.first_name
    
    def recipe_name(self,obj):
        return obj.recipe.name
    
class FavouriteAdmin(admin.ModelAdmin):
    list_display=['user','recipe_name']
    
    def user(self,obj):
        return obj.user.first_name
    
    def recipe_name(self,obj):
        return obj.recipe.name
    
    
    
admin.site.register(models.RecipeModel,RecipeAdmin)
admin.site.register(models.ContactUs,ContactUsAdmin)
admin.site.register(models.Review,ReviewAdmin)
admin.site.register(models.Favourite,FavouriteAdmin)


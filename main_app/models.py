from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RecipeModel(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False,unique=True)
    description = models.TextField()
    ingredients = models.TextField(blank=True)
    recipe = models.TextField()
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Recipe/")
    
    def __str__(self):
        return self.name
    
    
class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    problem = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Contact Us'
        
        
class Favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeModel,on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ["user","recipe"]
    
    def __str__(self):
        return f"Favourite For {self.recipe.name}"
        
ratings = [
    ("⭐","⭐"),
    ("⭐⭐","⭐⭐"),
    ("⭐⭐⭐","⭐⭐⭐"),
    ("⭐⭐⭐⭐","⭐⭐⭐⭐"),
    ("⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐")
]
class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    recipe = models.ForeignKey(RecipeModel,on_delete=models.CASCADE)
    body = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(choices=ratings, max_length=20,verbose_name="Rating")   
    
    class Meta :
        unique_together = ['user','recipe']
        
    @property
    def reviewer_name(self):
        return self.user.first_name  # Assuming 'username' is the field containing the user's name

    @property
    def recipe_name(self):
        return self.recipe.name

    def __str__(self) -> str:
        return f"Reviewer {self.reviewer_name}; Recipe {self.recipe_name}"

from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = "__all__"
        
class DoContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = "__all__"
        
class RecipeSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.RecipeModel
        fields = "__all__"
        
        
class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.RecipeModel
        fields = "__all__"

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password1 = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password1 != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists"})
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        print(account)
        account.set_password(password1)
        account.save()
        return account
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    
class UserSerializer(serializers.ModelSerializer):
    added_recipes = serializers.SerializerMethodField()

    class Meta:     
        model = User
        fields = ["id", "username", 'first_name', 'last_name', "email", "added_recipes"]

    def get_added_recipes(self,user):
        recipes = models.RecipeModel.objects.filter(added_by=user)
        recipe_serializer = RecipeSerializer(recipes, many=True)
        return recipe_serializer.data
        
        
class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.ReadOnlyField(source='user.first_name')
    recipe_name = serializers.ReadOnlyField(source='recipe.name')

    class Meta:
        model = models.Review
        fields = '__all__'
        
class CreateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ['id', 'reviewer_name', 'recipe_name', 'body', 'rating']
        
class FavouriteSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.Favourite
        fields = '__all__'

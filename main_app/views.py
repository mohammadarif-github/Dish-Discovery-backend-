from django.shortcuts import render,redirect
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework import generics,filters
from django.utils.text import slugify


class ContactUsViewset(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer
    
class RecipeViewset(viewsets.ModelViewSet):
    queryset = models.RecipeModel.objects.all()
    serializer_class = serializers.RecipeSerializer
    
class RegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data) 
        
        if serializer.is_valid(): 
            user = serializer.save()
            return redirect("login")
        return Response(serializer.errors)
    
from rest_framework.authtoken.models import Token


class LoginApiView(APIView):
    def post(self, request):
        serializer = serializers.LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error' : "Invalid Credential"})
        return Response(serializer.errors)

class LogoutApiView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    
    
class FavouriteViewSet(viewsets.ModelViewSet):
    queryset = models.Favourite.objects.all()
    serializer_class = serializers.FavouriteSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
class RecipeFilter(generics.ListAPIView):
    queryset = models.RecipeModel.objects.all()
    serializer_class = serializers.RecipeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name','description','slug']
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     search_text = self.request.query_params.get('search', None)
    #     if search_text:
    #         # Convert the search text into a slug format
    #         slugified_search_text = slugify(search_text)
    #         # Apply the search filter with the slugified text
    #         queryset = queryset.filter(slug__icontains=slugified_search_text)
    #     return queryset
    
        

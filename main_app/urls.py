from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router For Contact Us MODEL
contact_router = DefaultRouter()
contact_router.register('', views.ContactUsViewset)

# Router For Recipe MODEL
recipe_router = DefaultRouter()
recipe_router.register('', views.RecipeViewset)

#Router For User MODEL
user_router = DefaultRouter()
user_router.register("",views.UserViewSet)


#Router For Favourite MODEL
favourite_router = DefaultRouter()
favourite_router.register("",views.FavouriteViewSet)

#Router For Review MODEL 
review_router = DefaultRouter()
review_router.register('',views.ReviewViewSet)

urlpatterns = [
    path('contact_us/', include(contact_router.urls)),
    path('recipe/', include(recipe_router.urls)),
    path('register/', views.RegistrationApiView.as_view(),name="registration"),
    path('login/', views.LoginApiView.as_view(),name="login"),
    path('logout/', views.LogoutApiView.as_view(),name="logout"),
    path("user/",include(user_router.urls)),
    path("favourite/",include(favourite_router.urls)),
    path("review/",include(review_router.urls)),
    path("recipes/",views.RecipeFilter.as_view(),name="recipe_filter"),
]

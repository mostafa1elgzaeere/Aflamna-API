from django.urls import path,include
from aflamna.api.views import All_films, AllUsers, New_films, SelectedComments, Trends_films, one_user, watch_film , Signup
from rest_framework.authtoken.views import obtain_auth_token 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)



urlpatterns = [
    # path("films_api/",films_api,name="films_api"),
    # path("films_api/<int:id>/",edit_film,name="edit_film"),
    # path("comments_api/",comments_api,name="comments_api"),
    
    path("all_films/",All_films.as_view(),name="all_films"),
    path("new_films/",New_films.as_view(),name="new_films"),
    path("trend_films/",Trends_films.as_view(),name="trend_films"),



    path("all_films/<int:pk>/",watch_film.as_view(),name="watch_film"),
    path("comments/",SelectedComments.as_view(),name="selectedcomments"),

    path('all_users/',AllUsers.as_view(),name="allusers"),
    path("all_users/<int:pk>/",one_user.as_view(),name="get_one_user"),


    path('signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/',Signup.as_view(),name="signup"),
    
    
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path("rest-auth/logout/",include("rest_framework.urls")),
    # path('rest-auth-token',obtain_auth_token),
    



   
]

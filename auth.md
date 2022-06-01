Authentication :
            1- BasicAuthenticated
            2- TokenAuthenticated


Permessions :
            1- AllowAny
            2- IsAuthenticated
            3- IsAuthenticatedOrReadOnly
            4- IsAdminUser 


ways to write :
            1- Global ( in setting for all views )
            2- Privet ( in views )



Global :
        in settings.py :
                        REST_FRAMEWORK = {
                            'DEFAULT_AUTHENTICATION_CLASSES':['rest_framework.authentication.BasicAuthentication'],
                            'DEFAULT_PERMESSION_CLASSES':['rest_framework.permessions.AllowAny']
                        }


        if i didn`t use any api urls to authentication :
                    the user and password will adding in ( alert , confirm )
        
        to use auth gui 
        in urls.py  :
                    path('api-auth',include('rest_framework.urls'))



Privet :
        in views.py :
            from rest_framework.authentication import BasicAuthentication , TokenAuthentication
            from rest_framework.permissions import IsAuthenticated , AllowAny , IsAuthenticatedOrReadOnly


        class FilmList(generics.ListCreateAPIView):
                queryset=Film.objects.all()
                serializer_class=FilmSerializer
                authentication_classes=[BasicAuthentication]
                permission_classes=[IsAuthenticatedOrReadOnly]




*** Token Authentication ***
    in settings.py :
        1- add 'rest_framework.authtoken'  in installed apps
        2- REST_FRAMEWORK={'DEFAULT_AUTHENTICATION_CLASSES':'rest_framework.authintication.TokenAuthentication'}
        
    in models.py :
        1- from django.db.models.signals impost post_save  
        2- from django.dispatch import receiver
        3- from django.conf import settings
        4- from rest_framework.authtoken.models import Token

        5- @receiver(post_save,sender=settings.AUTH_USER_MODEL)
           def CreateToken(sender,instance,created,**kewargs):
                if created:
                    Token.objects.create(user=instance)


    in urls.py :
        1- from rest_framework.authtoken.views import obtain_auth_token
        2- path('api-auth-token',obtain_auth_token) 


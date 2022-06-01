from django.db.models import *

# Create your models here.
from django.db.models import *
from django.contrib.auth.models import User , AbstractUser
# Create your models here.


# post_save , receiver , Token , settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.utils.translation import activate
from rest_framework.authtoken.models import Token
from rest_framework.fields import ChoiceField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def CreateToken(sender,created,instance,**kewargs):
    if created:
        Token.objects.create(user=instance)



FilmsType =(
        ("New", "New"),
        ("Trend", "Trend"),
    )

Genders=(
    ("Male","Male"),("Female","Female"),
    )    

class Film(Model):

    title=CharField(max_length=100)
    image=ImageField(upload_to="static\images", height_field=None, width_field=None, max_length=None,default="",null=True, blank=True)
    description=TextField(max_length=600)
    rate=PositiveIntegerField()

    
    video=URLField(max_length=500)
    trailer = URLField(max_length=500)
    Type=CharField(choices=FilmsType,max_length=100)
    # video= FileField(upload_to='media/',null=True ,blank=True)


    def __str__(self):
        return self.title




class Comment(Model):
    writer     = ForeignKey(User, on_delete=CASCADE , related_name="comments")
    content    = TextField(max_length=400)
    film       = ForeignKey(Film,on_delete=CASCADE , related_name="comments",null=True,blank=True)        
    
    


    def __str__(self):
        return f" {self.writer} is commented at {self.film} "



    


class CustomUser(Model):
    user_name =CharField(max_length=100)
    email=EmailField()
    phone_number = CharField(max_length=20)
    gender=CharField(choices=Genders,max_length=100)
    Age=IntegerField()
    address=CharField(max_length=200,default="",null=True)

    def __str__(self):
        return self.user_name
from django.db.models import fields
from django.db.models.fields import PositiveIntegerField, PositiveSmallIntegerField, TextField
from django.utils.translation import activate
from rest_framework.serializers import *
from aflamna.models import Comment, Film , CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



class CommentSerializer(ModelSerializer):

	class Meta:
		model=Comment
		fields="__all__"




class FilmSerializer(ModelSerializer):
	comments=CommentSerializer(many=True,read_only=True)

	class Meta:
		model = Film
		fields="__all__"





class UserSerialize(ModelSerializer):
	password = CharField(
		write_only=True,
		required=True,
		style={'input_type': 'password', 'placeholder': 'Password'}
	)
	
	class Meta:
		model=User
		fields=('first_name','last_name','username','password')

	def create(self, validated_data):
		validated_data['password'] = make_password(validated_data.get('password'))
		return super().create(validated_data)








# class FilmSerializer(Serializer):
#     id=ReadOnlyField()
#     title=CharField(max_length=100)
#     video=URLField(max_length=500)
#     trailer=URLField(max_length=500)
#     image=ImageField()
#     rate=IntegerField()
#     description=CharField()

#     def create(self, validated_data):
#         return Film.objects.create(**validated_data)



#     def update(self, instance, validated_data):

#         instance.title       = validated_data.get("title",instance.title)
#         # instance.image       = validated_data.get("image",instance.image)
#         instance.description = validated_data.get("description",instance.description)
#         instance.rate        = validated_data.get("rate",instance.rate)
#         instance.video       = validated_data.get("video",instance.video)
#         instance.trailer     = validated_data.get("trailer",instance.trailer)     

#         instance.save()
#         return instance        
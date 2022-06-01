from typing import Type
from django.db import models
from django.utils.translation import activate
from rest_framework import serializers, status
import rest_framework 
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from aflamna.models import Comment, CustomUser, Film
from aflamna.api.serilaizers import CommentSerializer, FilmSerializer, UserSerialize
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication
from django.contrib.auth.models import User


from rest_framework import generics,mixins




# #fbv
# @api_view(["GET","POST"])
# def films_api(request):
#     if request.method=="GET":
#         films=Film.objects.all()
#         serializering=FilmSerializer(films,many=True)
#         return Response(serializering.data)

#     elif request.method=="POST":
#         serializering=FilmSerializer(data=request.data)  
#         if serializering.is_valid():
#             serializering.save()
#             return Response(serializering.data,status=status.HTTP_201_CREATED) 
#         return Response(serializering.error_messages,status=status.HTTP_404_NOT_FOUND)    

  
# @api_view(["GET","PUT","DELETE"])
# def edit_film(request,id):
#     film=Film.objects.get(id=id)
#     if request.method=="GET":
#         serializering=FilmSerializer(film)
#         return Response(serializering.data)

#     elif request.method=="PUT":
#         serializering=FilmSerializer(film,data=request.data)
#         if serializering.is_valid():
#             serializering.save()
#             return Response(serializering.data,status=status.HTTP_201_CREATED) 
#         return Response(serializering.error_messages,status=status.HTTP_404_NOT_FOUND)

#     elif request.method=="DELETE":
#         film.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




# @api_view(["GET","POST"])
# def comments_api(request):
#     comments=Comment.objects.all()
#     if request.method=="GET":
#         serializering=CommentSerializer(comments,many=True)
#         return Response(serializering.data)
#     elif request.method=="POST":
#         serializering=CommentSerializer(data=request.data)
#         if serializering.is_valid():
#             serializering.save()
#         return Response(serializering.error_messages,status=status.HTTP_500_INTERNAL_SERVER_ERROR)    









#generics
class All_films(generics.ListCreateAPIView):
    def get_queryset(self):
            return Film.objects.all()

    serializer_class=FilmSerializer



class Trends_films(generics.ListAPIView):
    def get_queryset(self):
            return Film.objects.filter(Type="Trend")

    serializer_class=FilmSerializer

class New_films(generics.ListAPIView):
    def get_queryset(self):
            return Film.objects.filter(Type="New")
    
    serializer_class=FilmSerializer


class watch_film(generics.RetrieveUpdateDestroyAPIView):
    
    queryset=Film.objects.all()
    serializer_class=FilmSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]


#generics
class SelectedComments(generics.ListCreateAPIView):
    def get_queryset(self):
            # film=Film.objects.get(pk=id)
            # return film.comments.filter(film=film)
            return Comment.objects.all()
    
    serializer_class=CommentSerializer



class AllUsers(generics.ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerialize

class one_user(generics.RetrieveUpdateDestroyAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerialize

#cbv
'''
    if request.method=="GET":
        films=Film.objects.all()
        serilaizering=Filmserializer(films,many=True)
        return Response(serilaizering.data)


    elif request.method=="POST":
        serilaizering=Filmserializer(data=request.data)
        if serilaizering.is_valid():
            serilaizering.save()
            return Response (serilaizering,status=status.HTTP_201_CREATED)

    elif request.method=="PUT":
        film=Film.objects.get(id=id)
        serilaizering=FilmSerilaizer(film,data=request.data)
        if serilaizering.is_valid():
           serilaizering.save()
           return Response (serilaizering,status=status.HTTP_201_CREATED)

    elif request.method=="DELETE":
        film.delete()


'''





#mixins
# class films_list(generics.CreateAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
#     queryset=Film.objects.all()
#     serializer_class=FilmSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)    


#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



# class films_list_edit(generics.RetrieveAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     queryset=Film.objects.all()
#     serializer_class=FilmSerializer
    
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


class Signup(generics.CreateAPIView):
    serializer_class=UserSerialize
    queryset=User.objects.all()


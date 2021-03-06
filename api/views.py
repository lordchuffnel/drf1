from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class MovieViewSet(viewsets.ModelViewSet):
  queryset = Movie.objects.all()
  serializer_class = MovieSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated)

  # useless action.....
  @action(detail=True, methods=['POST'])
  def rate_movie(self, request, pk=None):
    if 'stars' in request.data:
      movie = Movie.objects.get(id=pk)
      stars = request.data['stars']
      user = request.user

      try:
        rating = Rating.objects.get(user=user.id, movie=movie.id)
        rating.stars = stars
        rating.save()
        serializer = RatingSerializer(rating, many=False)
        message = {'message': 'Rating updated', 'result': serializer.data}
        return Response(message, status=status.HTTP_200_OK)
      except:
        rating = Rating.objects.create(user=user, movie=movie, stars=stars)
        serializer = RatingSerializer(rating, many=False)
        message = {'message': 'Rating created', 'result': serializer.data}
        return Response(message, status=status.HTTP_200_OK)

      message = {'message', 'its working'}
      return Response(message, status=status.HTTP_200_OK)
    else:
      message = {'message': 'you ndeed to provide stars'}
      return Response(message, status=status.HTTP_400_BAD_REQUEST)
    

class RatingViewSet(viewsets.ModelViewSet):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer
  authentication_classes = (TokenAuthentication, )
  permission_classes = (IsAuthenticated)

  def update(self, request, *args, **kwargs):
    message = {'message': 'Cannot update rating like that'}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)

  def create(self, request, *args, **kwargs):
    message = {'message': 'Cannot create rating like that'}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)
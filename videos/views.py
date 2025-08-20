from rest_framework import generics, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Video, Comment, Favorite
from .serializers import VideoSerializer, CommentSerializer, FavoriteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.conf import settings
from django.db import IntegrityError

class IsCreator(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_creator)

class VideoListCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True, context={'request': request})
        return Response({
                "message": "Videos fetched successfully.",
                "data": serializer.data,
                "status": "200"
            }, status=status.HTTP_200_OK)
    

    def post(self, request):
        if not request.user.is_authenticated or not request.user.is_creator:
            return Response({'detail': 'Only creators can upload.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = VideoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VideoDetailView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk):
        try:
            vid = Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = VideoSerializer(vid, context={'request': request})
        return Response({
            "message": "Video retrieved successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

### COMMENTS & RATINGS ###

class CommentCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FavoriteCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                favorite = serializer.save(user=request.user)
                return Response({
                    "message": "Video marked as favorite successfully.",
                    "data": FavoriteSerializer(favorite).data
                }, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response({
                    "error": "You have already marked this video as favorite."
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "error": "Invalid data.",
            "details": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class FavoriteDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            favorite = Favorite.objects.get(pk=pk, user=request.user)
        except Favorite.DoesNotExist:
            return Response({
                "error": "Favorite not found.",
                "message": "The specified favorite does not exist or does not belong to you."
            }, status=status.HTTP_404_NOT_FOUND)

        favorite.delete()
        return Response({
            "message": "Video removed from favorites successfully.",
            "favorite_id": pk,
            "status": "200"
        }, status=status.HTTP_200_OK)
    

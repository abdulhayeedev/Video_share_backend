from rest_framework import serializers
from .models import Video, Comment, Favorite

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'video', 'user', 'user_name', 'text', 'is_shared', 'created_at']
        read_only_fields = ['user','user_name', 'created_at']

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'video', 'user', 'is_favorite', 'created_at']
        read_only_fields = ['user', 'created_at']


class VideoSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    favorites = FavoriteSerializer(many=True, read_only=True)
    video = serializers.FileField()  
    uploaded_by = serializers.CharField(source='uploaded_by.username', read_only=True)



    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'video', 'uploaded_by', 'uploaded_at', 'comments', 'favorites']
        read_only_fields = ['uploaded_by', 'uploaded_at']

    def get_video(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.video.url) if obj.video else None
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get('request')
        if instance.video:
            rep['video'] = request.build_absolute_uri(instance.video.url)
        return rep


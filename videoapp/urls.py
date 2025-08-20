from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.views import RegisterView, ProfileView, LoginView
from videos.views import VideoListCreateView, VideoDetailView, CommentCreateView, FavoriteCreateView, FavoriteDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    path('api/videos/', VideoListCreateView.as_view(), name='video-list'),
    path('api/videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('api/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('api/favorites/', FavoriteCreateView.as_view(), name='favorite-create'),
    path('api/favorites/<int:pk>/', FavoriteDeleteView.as_view(), name='favorite-delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


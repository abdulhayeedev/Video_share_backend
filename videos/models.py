from django.db import models
from users.models import CustomUser

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='videos/')  # <-- store in local /media/videos/
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    is_shared = models.BooleanField(default=False)  # ✅ new field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.video}"


class Favorite(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='favorites')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=True)  # Optional toggle
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('video', 'user')  

    def __str__(self):
        return f"{self.user} favorited {self.video}"


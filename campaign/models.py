from django.db import models


class SocialMediaPlatform(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    social_media_platoform = models.ForeignKey(
        SocialMediaPlatform, on_delete=models.CASCADE, null=True
    )


class Campaign(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

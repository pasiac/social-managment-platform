from rest_framework import viewsets

from campaign.models import Campaign, Post, SocialMediaPlatform
from campaign.serializers import (
    CampaignSerializer,
    PostSerializer,
    SocialMediaPlatformSerializer,
)


class SocialMediaPlatformViewSet(viewsets.ModelViewSet):
    queryset = SocialMediaPlatform.objects.all()
    serializer_class = SocialMediaPlatformSerializer
    permission_classes = []


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = []


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = []

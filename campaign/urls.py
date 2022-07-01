# modelviewset router for campaign
from rest_framework import routers

from campaign.views import CampaignViewSet, PostViewSet, SocialMediaPlatformViewSet

router = routers.DefaultRouter()
router.register(r"campaigns", CampaignViewSet, basename="campaign")
router.register(r"posts", PostViewSet, basename="post")
router.register(
    r"social_media_platforms",
    SocialMediaPlatformViewSet,
    basename="social_media_platform",
)
urlpatterns = router.urls

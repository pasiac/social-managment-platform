from rest_framework.test import APITestCase

from campaign.models import Campaign, Post, SocialMediaPlatform


class PostTest(APITestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create(title="Test Post", text="Test")

    def test_posts_list(self):
        response = self.client.get("/api/posts/")
        self.assertContains(response, "Test Post")
        self.assertEqual(response.status_code, 200)

    def test_posts_detail(self):
        response = self.client.get("/api/posts/1/")
        self.assertContains(response, "Test Post")
        self.assertEqual(response.status_code, 200)

    def test_posts_create(self):
        response = self.client.post("/api/posts/", {"title": "Test", "text": "Test"})
        self.assertEqual(response.status_code, 201)

    def test_posts_update(self):
        response = self.client.put(
            "/api/posts/1/",
            {"title": "Updated Test title", "text": "Updated Test text"},
        )
        self.assertEqual(response.status_code, 200)

    def test_posts_delete(self):
        response = self.client.delete("/api/posts/1/")
        self.assertEqual(response.status_code, 204)


class SocialMediaPlatformTest(APITestCase):
    def setUp(self) -> None:
        self.social_media_platform = SocialMediaPlatform.objects.create(
            name="Test name", url="http://test.com"
        )

    def test_social_media_platform_list(self):
        response = self.client.get("/api/social_media_platforms/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test name")

    def test_social_media_platform_detail(self):
        response = self.client.get("/api/social_media_platforms/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test name")

    def test_social_media_platform_create(self):
        response = self.client.post(
            "/api/social_media_platforms/", {"name": "Test", "url": "http://test.com"}
        )
        self.assertEqual(response.status_code, 201)

    def test_social_media_platform_update(self):
        response = self.client.put(
            "/api/social_media_platforms/1/",
            {"name": "Updated Test", "url": "http://updated.com"},
        )
        self.assertEqual(response.status_code, 200)

    def test_social_media_platform_delete(self):
        response = self.client.delete("/api/social_media_platforms/1/")
        self.assertEqual(response.status_code, 204)


class CampaignTest(APITestCase):
    def setUp(self) -> None:
        self.post = Post.objects.create(title="Test Post", text="Test")
        self.campaign = Campaign.objects.create(post=self.post)

    def test_campaign_list(self):
        response = self.client.get("/api/campaigns/")
        self.assertEqual(response.status_code, 200)

    def test_campaign_detail(self):
        response = self.client.get("/api/campaigns/1/")
        self.assertEqual(response.status_code, 200)

    def test_campaign_create(self):
        response = self.client.post("/api/campaigns/", {"post": 1})
        self.assertEqual(response.status_code, 201)

    def test_campaign_update(self):
        response = self.client.put("/api/campaigns/1/", {"post": 1})
        self.assertEqual(response.status_code, 200)

    def test_campaign_delete(self):
        response = self.client.delete("/api/campaigns/1/")
        self.assertEqual(response.status_code, 204)

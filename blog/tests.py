from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth import get_user_model

from blog.models import PostModel, Category
from blog.views import CreatePost


class BlogTestCase(TestCase):
    def setUp(self) -> None:
        user_model = get_user_model()
        self.user = user_model.objects.create(email="test_user@test.ru", password="Aa123456")
        self.category = Category.objects.create(name="it", slug="it")
        image = SimpleUploadedFile("test_post_image.jpg", content=b"", content_type="image/jpg")
        self.post = PostModel.objects.create(
            author="Test_author",
            title="Test_title",
            text="Test_text",
            # slug="test-post",
            image=image,
            category=self.category,
        )

    def test_add_post(self):
        self.assertIn(self.post, PostModel.objects.all())
        self.assertEqual(PostModel.objects.count(), 1)

    def test_add_post_slug(self):
        self.assertEqual(self.post.slug, "test_title")

    def test_anonym_access(self):
        client = Client()
        response = client.get("/blog/create")
        # print(response.url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/blog/login?next=/blog/create")

    def test_exist_user_create(self):
        rf = RequestFactory()
        request = rf.get("")
        request.user = self.user
        response = CreatePost.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_add_post_by_existing_user(self):
        rf = RequestFactory()
        request = rf.post("")
        request.user = self.user
        request.POST["csrf_token"] = "..."
        request.POST["author"] = "author2"
        request.POST["title"] = "title_test_3"
        request.POST["text"] = "text_test_3"
        request.POST["category"] = "category_test_3"
        response = CreatePost.as_view()(request)
        posts = PostModel.objects.all()
        self.assertEqual(PostModel.objects.count(), 2)

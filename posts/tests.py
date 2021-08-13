from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from posts.models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testUser1 = User.objects.create_user(username= 'testUser1', password='abc123')
        testUser1.save()

        # create a blog post

        test_post = Post.objects.create(
            author = testUser1, title='Blog title', body= 'body content',
        )
        test_post.save()

    def test_blog_contnet(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testUser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'body content')

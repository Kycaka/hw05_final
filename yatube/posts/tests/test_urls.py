from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import Client, TestCase
from django.urls import reverse

from ..models import Group, Post

User = get_user_model()


class PostsUrlsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Тестовое название',
            slug='slug',
            description='Тестовое описание',
        )
        cls.author = User.objects.create_user(username='Тестовый пользователь')
        cls.no_author = User.objects.create_user(
            username='Не авторизованый пользователь'
        )
        cls.post = Post.objects.create(
            author=cls.author,
            text='Тестовый пост',
        )
        cls.templates_url_names_public = {
            'posts/index.html': reverse('posts:index'),
            'posts/group_list.html': reverse(
                'posts:group_list',
                kwargs={'slug': cls.group.slug},
            ),
            'posts/profile.html': reverse(
                'posts:profile',
                kwargs={'username': cls.author.username},
            ),
        }

        cls.templates_url_names_private = {
            'posts/create_post.html': reverse('posts:create')
        }

        cls.templates_url_names = {
            'posts/group_list.html': reverse(
                'posts:group_list',
                kwargs={'slug': cls.group.slug},
            ),
            'posts/profile.html': reverse(
                'posts:profile',
                kwargs={'username': cls.author.username},
            ),
            'posts/create_post.html': reverse('posts:create'),
            'posts/index.html': reverse('posts:index'),
        }

    def setUp(self):
        self.guest_client = Client()

        self.authorized_client = Client()
        self.authorized_client.force_login(self.author)

        self.no_author_client = Client()
        self.no_author_client.force_login(self.no_author)

    def test_urls_guest_user_private(self):
        """
        Проверка на доступнотсь ссылок гостевому пользователю и редирект
        недоступных страниц.
        """
        for template, reverse_name in self.templates_url_names_private.items():
            with self.subTest():
                response = self.guest_client.get(reverse_name)
                self.assertEqual(response.status_code, HTTPStatus.FOUND)
        response = self.guest_client.get(
            reverse(
                'posts:edit',
                kwargs={'post_id': self.post.id},
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_urls_guest_user_public(self):
        """
        Проверка на доступнотсь ссылок гостевому пользователю и редирект
        доступных страниц.
        """
        for template, reverse_name in self.templates_url_names_public.items():
            with self.subTest():
                response = self.guest_client.get(reverse_name)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_urls_authorized_user(self):
        """Проверка ссылок авторизованному пользователю - автору поста."""
        for template, reverse_name in self.templates_url_names.items():
            with self.subTest():
                response = self.authorized_client.get(reverse_name)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_urls_no_authorized_user(self):
        """Проверка ссылок авторизованному пользователю - не автору поста."""
        for template, reverse_name in self.templates_url_names.items():
            with self.subTest():
                response = self.guest_client.get(
                    reverse(
                        'posts:edit',
                        kwargs={'post_id': self.post.id},
                    )
                )
                self.assertEqual(response.status_code, HTTPStatus.FOUND)

    def test_urls_no_authorized_user_2(self):
        """Проверка ссылок авторизованному пользователю - не автору поста 2."""
        for template, reverse_name in self.templates_url_names.items():
            with self.subTest():
                response = self.no_author_client.get(reverse_name)
                self.assertEqual(response.status_code, HTTPStatus.OK)

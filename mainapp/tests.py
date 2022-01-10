from django.test import TestCase
from django.contrib.gis.geos import Point
from django.urls import reverse
from .models import Memories
from django.contrib.auth.models import User


class PlaceModelTest(TestCase):

    def test_create_memories(self):
        user = User.objects.create_user('Иван', 'ваня@иванушки.com', 'ваня')
        Memories.objects.create(author=user, title='Америка', comment='144', location=Point(10, 213))

        field_label = Memories._meta.get_field('title').verbose_name
        self.assertEquals('Введите воспоминание', field_label)

        field_label_2 = Memories._meta.get_field('location').verbose_name
        self.assertEquals('Местоположение', field_label_2)

        field_label_3 = Memories._meta.get_field('comment').verbose_name
        self.assertEquals('Введите комментарий', field_label_3)

        max_length = Memories._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)


class ListPlaceViewTest(TestCase):
    @classmethod
    def setUpData(cls):
        user = User.objects.create_user('Иван', 'ваня@иванушки.com', 'ваня')
        number_of_memories = 4
        for i in range(number_of_memories):
            Memories.objects.create(author=user, title='Иван' % i, location=Point(i, i * 2))

    def test_url_exists(self):
        first_resp = self.client.get('/')
        second_resp = self.client.get('/home/')
        self.assertEqual(first_resp.status_code, 200)
        self.assertEqual(second_resp.status_code, 302)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 302)


class LoginTest(TestCase):
    @classmethod
    def setUp(cls):
        test_user_1 = User.objects.create_user('Иван', 'иван@mail.com', 'ваня').save()
        test_user_2 = User.objects.create_user('Максим', 'максим@mail.com', 'макс').save()
        test_user_3 = User.objects.create_user('Владислав', 'владислав@mail.com', 'влад').save()
        test_user_4 = User.objects.create_user('Николай', 'николай@mail.com', 'коля').save()

        Memories.objects.create(author=test_user_1, title='user_1_title', comment='1234',
                                location=Point(30, 4), author_id='1')
        Memories.objects.create(author=test_user_2, title='user_2_title', comment='2234',
                                location=Point(50, 8), author_id='2')
        Memories.objects.create(author=test_user_3, title='user_3_title', comment='3234',
                                location=Point(100, 22), author_id='3')
        Memories.objects.create(author=test_user_4, title='user_4_title', comment='4234',
                                location=Point(200, 44), author_id='4')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='Иван', password='ваня')
        resp = self.client.get(reverse('home'))
        self.assertEqual(str(resp.context['user']), 'Иван')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

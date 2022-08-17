from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTests(APITestCase):

    def setUp(self):
        User.objects.create_user(
            username='testing_user',
            email='user_testing@gmail.com',
            password='@test123'
        )

    def test_login(self):
        response = self.client.post(
            path='/login/',
            data={
                "username": 'testing_user',
                "password": '@test123'
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data.get('Token'), None)

    def test_signup(self):
        response = self.client.post(
            path='/signup/',
            data={
                "username": "testing_user1",
                "first_name": "test_first",
                "last_name": "test_last",
                "password": "@Test123",
                "password2": "@Test123",
                "email": "test1@gmail.com"
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from users.models import User


class AccountTests(APITestCase):

    def setUp(self):
        user = User.objects.create_user(
            username='saadsh18',
            email='test@gmail.com',
            password='@saadsh18',
            is_artist=True
        )
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token}')



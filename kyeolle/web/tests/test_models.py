from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):

    def test_유저_모델과_이메일을_생성한다(self):
        """
        새로운 유저와 이메일을 같이 생성합니다
        """
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_새로운_유저의_이메일을_정규화한다(self):
        """
        새로운 유저의 이메일을 정규화합니다
        """
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_새로운_유저의_이메일이_없다(self):
        """
        새로운 유저의 이메일이 없으면 에러를 일으킵니다
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_슈퍼유저를_생성한다(self):
        """
        슈퍼유저를 생성합니다
        """
        user = get_user_model().objects.create_superuser(
            'test@gmail.com', 'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

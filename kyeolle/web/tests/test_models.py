from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTestCase(TestCase):

	def test_사용자와_이메일을_생성한다(self):
		"""
		새로운 유저와 이메일을 같이 생성합니다
		"""
		email = "test@gmail.com"
		password = "testpass123"
		user = get_user_model().objects.create_user(
			email=email,
			password=password
		)

		self.assertEqual(user.email, email)
		self.assertEqual(user.check_password(password))
		

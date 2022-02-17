from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTestCase(TestCase):

    def setUp(self):
        """
        임의의 어드민 유저, 일반 유저를 생성합니다
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='test@gmail.com',
            password='test123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='usertest@gmail.com',
            password='test123',
            name='Test user full name'
        )

    def test_유저가_리스트업_된다(self):
        """
        어드민 페이지에 유저가 리스트로 나열되는지 확인합니다
        """
        url = reverse('admin:web_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_유저_변경_페이지의_작동을_확인한다(self):
        """
        유저 변경 페이지 작동을 확인합니다
        """
        url = reverse('admin:web_user_change', args=[self.user.id])
        # /admin/web/user/1
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_유저_생성_페이지의_작동을_확인한다(self):
        """
        유저 생성 페이지의 작동을 확인합니다
        """
        url = reverse('admin:web_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

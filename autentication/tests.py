from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    def test_login_view(self):
        response = self.client.post(reverse('account_login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirección después del inicio de sesión
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_signup_view(self):
        response = self.client.post(reverse('account_signup'), {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # Redirección después del registro
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)  # Redirección después del cierre de sesión
        self.assertFalse(response.wsgi_request.user.is_authenticated)
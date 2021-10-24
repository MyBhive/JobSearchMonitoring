from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model


User = get_user_model()


class TestUrls(TestCase):

    def setUp(self):
        user = User.objects.create(
            email='try@bob.fr'
        )
        user.set_password('azerty123')
        user.save()

    def test_login_url_is_linked_to_good_url(self):
        self.assertEqual(reverse('login'), '/login/')
        self.assertEqual(resolve('/login/')._func_path,
                         'useraccount.views.log_in'
                         )

    def test_sign_in_url_is_linked_to_good_url(self):
        self.assertEqual(reverse('sign_in'), '/sign_in/')
        self.assertEqual(resolve('/sign_in/')._func_path,
                         'useraccount.views.sign_in'
                         )

    def test_logout_url_is_linked_to_good_url(self):
        self.assertEqual(reverse('log_out'), '/log_out/')
        self.assertEqual(resolve('/log_out/')._func_path,
                         'useraccount.views.log_out'
                         )

    def test_my_account_is_linked_to_good_url(self):
        self.assertEqual(reverse('my_account'), '/my_account/')
        self.assertEqual(resolve('/my_account/')._func_path,
                         'useraccount.views.my_account'
                         )

    def test_password_reset_is_linked_to_good_url(self):
        self.assertEqual(reverse('password_reset'), '/password_reset/')
        self.assertEqual(resolve('/password_reset/')._func_path,
                         'django.contrib.auth.views.PasswordResetView')

    def test_password_reset_done_is_linked_to_good_url(self):
        self.assertEqual(reverse('password_reset', ), '/password_reset/')
        self.assertEqual(resolve('/password_reset/done/')._func_path,
                         'django.contrib.auth.views.PasswordResetDoneView')

    def test_password_reset_confirm_is_linked_to_good_url(self):
        self.assertEqual(reverse(
            'password_reset_confirm', args=['uidb64', 'token']),
            '/password_reset_confirm/uidb64/token/'
        )
        self.assertEqual(resolve
                         ('/password_reset_confirm/uidb64/token/')._func_path,
                         'django.contrib.auth.views.PasswordResetConfirmView')

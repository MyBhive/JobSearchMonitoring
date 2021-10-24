from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()


class RegisterViewTestCase(TestCase):

    def setUp(self):
        user = User(
            first_name='bob',
            last_name='johnson',
            email='bob.johnson@email.com',
            password='Cornichon23!',
            date_of_birth='1978-10-10'
        )
        user.name = True
        user.is_superuser = True
        user.set_password('Cornichon23!')
        user.save()

    def test_sign_in_success(self):
        response = self.client.post('/sign_in/',
                                    {'first_name': 'nico2',
                                     'last_name': 'johnson',
                                     'email': "nico2@gmail.com",
                                     'password1': '123nousironsaubois!',
                                     'password2': '123nousironsaubois!',
                                     'date_of_birth': '1978-10-10'})

        self.assertEquals(response.status_code, 302)
        self.assertEqual(len(User.objects.filter(email='nico2@gmail.com')), 1)

    def test_sign_in_email_already_exist(self):
        response = self.client.post('/sign_in/',
                                    {'first_name': 'nico',
                                     'last_name': 'bob',
                                     'email': "bob.johnson@email.com",
                                     'password1': 'achtung1!',
                                     'password2': 'achtung1!',
                                     'date_of_birth': '1978-10-10'})
        self.assertEqual(response.context['form'].errors['email'][0],
                         'User with this Email address already exists.')
        self.assertEqual(response.status_code, 200)

    def test_sign_in_error_password(self):
        response = self.client.post('/sign_in/',
                                    {'first_name': 'nico2',
                                     'last_name': 'johnson',
                                     'email': "nico2@gmail.com",
                                     'password1': '123nousironsaubois!',
                                     'password2': '12nousironsaubois!',
                                     'date_of_birth': '1978-10-10'})
        self.assertEqual(response.context['form'].errors['password2'][0],
                         'The two password fields didn’t match.')


class LoginViewTestCase(TestCase):

    def setUp(self):
        self.u = User.objects.create(email='boby@bob.fr')
        self.u.set_password('azerty123')
        self.u.save()

    def test_login_success(self):
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            False
        )
        self.client.post('/login/',
                         {'email': 'boby@bob.fr',
                          'password': 'azerty123'})
        self.assertEqual(self.client.session['_auth_user_id'],
                         str(self.u.pk
                             ))

    def test_login_password_wrong(self):
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            False
        )
        response = self.client.post('/login/',
                                    {'email': 'boby@bob.fr',
                                     'password': 'azerty123!'}
                                    )
        self.assertContains(response,
                            'email or password incorrect'
                            )
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            False
        )

    def test_log_out_redirect(self):
        self.client.login(email='boby@bob.fr', password='azerty123')
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            str(self.u.pk)
        )
        response = self.client.get('/log_out/', follow=True)
        self.assertEqual(self.client.session.get(
            '_auth_user_id', False),
            False
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertTemplateUsed(response, 'pages/head_foot_nav.html')

    def test_my_account_view_success(self):
        response = self.client.get(reverse('my_account'))
        self.assertEquals(response.status_code, 302)

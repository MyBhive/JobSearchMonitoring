from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib import messages

from jobsearch.models import Categories, \
    Status, \
    TypeOfContract, \
    StyleOfContract, \
    JobOffer
from useraccount.models import CustomUser
from jobsearch.views import delete_category, job_offers_views

User = get_user_model()


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.bob = CustomUser.objects.create_user(
            email='bob@gmail.com'
        )
        self.bob.set_password('azerty123')
        self.bob.save()

        self.legal_notices_url = reverse('legal_notices')
        self.contact_url = reverse('contact')

        self.category_to_delete = Categories.objects.create(
            name_category='consultant',
            user=self.bob
        )
        self.category = Categories.objects.create(
            name_category='programming',
            user=self.bob
        )

        self.status = Status.objects.create(
            advanced='CV sent'
        )
        self.type = TypeOfContract.objects.create(
            type='Permanent'
        )
        self.style = StyleOfContract.objects.create(
            style='Full time'
        )
        self.job = JobOffer.objects.create(
            title='dev',
            company_name='Oc',
            url='https://github.com/MyBhive/NutellaLovers',
            salary='125000',
            comments='arazamzam arazamzam gouligouligouli ramzamzam',
            category_id=self.category,
            user_id=self.bob,
            status_id=self.status,
            style_id=self.style,
            type_id=self.type
        )

    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/home.html')
        self.assertTemplateUsed(response, 'pages/head_foot_nav.html')

    def test_legal_notices_view(self):
        response = self.client.get(self.legal_notices_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/legal_notices.html')

    def test_contact_view(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/contact.html')

    def test_add_category_success(self):
        pre_number_category = len(Categories.objects.filter(
            name_category=self.category)
        )
        self.assertEqual(pre_number_category, 1)
        category_created = 'consultant'
        request = self.client.get(
            '/add_categories',
            data={'add_categories': category_created}
        )
        request.user = self.bob
        self.assertEqual(pre_number_category + 1, 2)

    def test_see_categories_success(self):
        response = self.client.get(reverse('see_categories'))
        self.assertEquals(response.status_code, 302)

    def test_enter_category_views(self):
        response = self.client.get(
            f'/enter_category/{self.category.id}/'
        )
        self.assertEquals(response.status_code, 302)

    def test_delete_category_success(self):

        request = self.factory.get(
            f'/delete_category/'
            f'{self.category_to_delete.id}/')
        request.user = self.bob
        request._messages = messages.storage.default_storage(request)
        pre_number_category = len(Categories.objects.filter(
            name_category=self.category_to_delete)
        )
        self.assertEqual(pre_number_category, 1)
        delete_category(request, self.category_to_delete.id)
        after_number_category = len(Categories.objects.filter(
            name_category=self.category_to_delete)
        )
        self.assertEqual(after_number_category, 0)

    def test_delete_category_fail(self):
        request = self.factory.get(
            f'/delete_category/{self.category.id}/'
        )
        request.user = self.bob
        request._messages = messages.storage.default_storage(request)
        pre_number_category = len(Categories.objects.filter(
            name_category=self.category)
        )
        self.assertEqual(pre_number_category, 1)
        delete_category(request, self.category.id)
        after_number_category = len(Categories.objects.filter(
            name_category=self.category)
        )
        self.assertEqual(after_number_category, 1)

    def test_delete_category_fail_status_code_404(self):
        response = self.client.get(
            f'/delete_category/{self.category.id}/'
        )
        self.assertEqual(response.status_code, 404)

    def test_job_offers_views(self):
        request = self.factory.get(
            f'/job_description/{self.category.id}'
        )
        request.user = self.bob
        response1 = job_offers_views(request, self.category.id)
        self.assertEquals(response1.status_code, 200)

    def test_JobOfferDetailView_render_correctly(self):
        response = self.client.get(f'/job_detail/{self.job.id}')
        self.assertEqual(response.status_code, 200)

    def test_CreateJobOffer_render_correctly(self):
        response = self.client.get(reverse('add_job'))
        self.assertEquals(response.status_code, 302)

    def test_UpdateJobOffer_render_correctly(self):
        response = self.client.get(
            f'/job_detail/edit/{self.job.id}'
        )
        self.assertEqual(response.status_code, 302)

    def test_DeleteJobOffer_render_correctly(self):
        response = self.client.get(
            f'/job_detail/edit/{self.job.id}'
        )
        self.assertEqual(response.status_code, 302)

    def test_select_status_render_correctly(self):
        response = self.client.get(
            f'/status/{self.status.id}/{self.category.id}'
        )
        self.assertEqual(response.status_code, 302)

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from jobsearch.views import *

User = get_user_model()


class TestUrls(SimpleTestCase):

    def test_home_is_linked_to_good_url_and_views(self):
        self.assertEqual(reverse('home'), '/')
        self.assertEqual(resolve('/')._func_path, 'jobsearch.views.home')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! wrong page! Oups.')

    def test_legal_notices_is_linked_to_good_url_and_views(self):
        self.assertEqual(reverse('legal_notices'), '/legal_notices')
        self.assertEqual(resolve('/legal_notices')._func_path,
                         'jobsearch.views.legal_notices')

    def test_contact_is_linked_to_good_url_and_views(self):
        self.assertEqual(reverse('contact'), '/contact')
        self.assertEqual(resolve('/contact')._func_path,
                         'jobsearch.views.contact')

    def test_enter_category_is_linked_to_good_url_and_views(self):
        url = reverse("enter_category", args=['id_cat'])
        self.assertEquals(resolve(url).func, enter_category)

    def test_delete_category_is_linked_to_good_url_and_views(self):
        url = reverse("delete_category", args=['cat_id'])
        self.assertEquals(resolve(url).func, delete_category)

    def test_add_category_is_linked_to_good_url_and_views(self):
        self.assertEqual(reverse('add_categories'), '/add_categories')
        self.assertEqual(resolve('/add_categories')._func_path,
                         'jobsearch.views.add_category')

    def test_see_categories_is_linked_to_good_url_and_views(self):
        self.assertEqual(reverse('see_categories'), '/see_categories')
        self.assertEqual(resolve('/see_categories')._func_path,
                         'jobsearch.views.see_categories')


# add_job_offer
# modify_job_offer
# select_status ( status_id))
# see_job_offer
# delete_job_offer (job_id)
    # def test_product_info_url_resolves(self):
      #  url = reverse("product_info", args=['description'])
      #  self.assertEquals(resolve(url).func, product_info)
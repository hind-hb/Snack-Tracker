from django.test import TestCase
from django.urls import reverse



class ThingsToTest(TestCase):
    def test_home_page_status(self):
        url = reverse('Snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    

    def test_base_page_template(self):
        url = reverse('Snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')

     
    def test_snack_list_template(self):
        url = reverse('Snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'Snack_list.html')

        
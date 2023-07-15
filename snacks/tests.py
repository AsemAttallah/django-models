from django.test import TestCase
from django.urls import reverse

# Create your tests here.
# class TestHome(TestCase):
#     def test_status_code(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)

#     def test_home_page_template(self):
#         url = reverse('home')
#         response = self.client.get(url)
#         self.assertTemplateUsed(response, 'home.html')

class TestSnackList(TestCase):
    def test_status_code(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

class TestSnackDetail(TestCase):
    def test_status_code(self):
        url = reverse('snacks_details')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_snack_detail_template(self):
    #     url = reverse('snacks_details')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, 'snack_detail.html')
from django.test import TestCase
from rest_framework.test import APIClient
from Restaurant.models import Menu


class MenuViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

        Menu.objects.create(
            title="Pizza",
            price=20,
            inventory=10
        )

        Menu.objects.create(
            title="Burger",
            price=15,
            inventory=5
        )

    def test_get_all_menu_items(self):
        response = self.client.get("/restaurant/menu/items/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
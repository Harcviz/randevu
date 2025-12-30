from django.test import SimpleTestCase


class HomeViewTests(SimpleTestCase):
    def test_home_returns_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ay görünümü")
        self.assertContains(response, "Günlük döküm")
        self.assertContains(response, "Hoca seç")
        self.assertContains(response, "15 dk")

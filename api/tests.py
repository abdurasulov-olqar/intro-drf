from django.test import TestCase

class MainViewTestCase(TestCase):
    def test_name(self):
        name = 'ali'
        url = f'/api/home/?name={name}'

        response = self.client.get(url)

        self.assertEqual(response.json(), {"name": name})


class SumViewTestCase(TestCase):
    def test_get(self):
        a = 2
        b = 4

        url = f'/api/sum/?a={a}&b={b}'

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'sum': 6})

    def test_post(self):
        data = {
            "a": 1,
            "b": 3
        }

        url = f'/api/sum/'

        response = self.client.post(url, data, 'application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'sum': 4})
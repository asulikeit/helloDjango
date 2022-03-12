from rest_framework import status
from rest_framework.test import APITestCase

class JustTest(APITestCase):

    def test01_no_addr(self):
        people_list = [
            {'name': 'chulsu', 'description': 'Kim Chul-su'},
        ]

        data = { 'peoples': people_list }
        resp = self.client.post("/peoples", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test02_address(self):
        people_list = [
            {'name': 'chulsu', 'description': 'Kim Chul-su', 'profile': {'address': 'Seoul'}},
        ]

        data = { 'peoples': people_list }
        resp = self.client.post("/peoples", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        req_id = str(resp.data[0])

        resp = self.client.get(f"/peoples/{req_id}/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('profile').get('address'), 'Seoul')
        
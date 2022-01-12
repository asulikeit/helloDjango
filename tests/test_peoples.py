from rest_framework import status
from rest_framework.test import APITestCase

class JustTest(APITestCase):

    def setUp(self) -> None:
        return super().setUp()

    def test01_peoples(self):
        people_list = [
            {'name': 'chulsu', 'description': 'Kim Chul-su'},
            {'name': 'yunghui', 'description': 'Lee Young-hui'},
        ]
        resp = self.client.post("/peoples", people_list, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

        data = { 'peoples': people_list }
        resp = self.client.post("/peoples", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(resp.data), 2)

        req_id = str(resp.data[0])
        resp = self.client.get(f"/peoples/{req_id}/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('name'), 'chulsu')

        resp = self.client.get("/peoples/0/")
        self.assertEqual(resp.status_code, status.HTTP_404_NOT_FOUND)

        resp = self.client.get("/peoples/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)

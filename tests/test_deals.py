from rest_framework import status
from rest_framework.test import APITestCase

class ApiTest(APITestCase):

    def setUp(self):
        return super().setUp()

    def test01_deals(self):
        people_list = [
            {'name': 'chulsu', 'description': 'Kim Chul-su'},
            {'name': 'yunghui', 'description': 'Lee Young-hui'},
            {'name': 'mansu', 'description': 'Park Man-su'},
        ]
        data = { 'peoples': people_list }
        resp = self.client.post("/peoples/", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(resp.data), 3)

        people_ids = resp.data
        data = {
            'sender': people_ids[0],
            'receiver': people_ids[1],
        }
        resp = self.client.post("/deals/", data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        deal_id = str(resp.data)

        resp = self.client.get(f"/deals/{deal_id}/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('sender').get('name'), 'chulsu')

        data = {
            'sender': people_ids[0],
            'receiver': people_ids[2],
        }
        resp = self.client.post("/deals", data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        deal_id = str(resp.data)

        resp = self.client.get(f"/deals/{deal_id}")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data.get('receiver').get('name'), 'mansu')

        resp = self.client.get("/deals/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)

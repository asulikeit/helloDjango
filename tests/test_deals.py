from rest_framework import status
from rest_framework.test import APITestCase

class ApiTest(APITestCase):

    def setUp(self):
        return super().setUp()

    def test01_deals(self):
        people_list = [
            {'name': 'chulsu', 'description': 'Kim Chul-su'},
            {'name': 'yunghui', 'description': 'Lee Young-hui'},
        ]
        data = { 'peoples': people_list }
        resp = self.client.post("/peoples/", data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(resp.data), 2)

        people_ids = resp.data
        data = {
            'sender': people_ids[0],
            'receiver': people_ids[1],
        }
        resp = self.client.post("/deals/", data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        deal_id = str(resp.data)

        resp = self.client.get("/deals/" + deal_id + "/")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)      

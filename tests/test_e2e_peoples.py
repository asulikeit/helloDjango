from rest_framework import status
from rest_framework.test import APITestCase

class JustTest(APITestCase):

    def test01_peoples(self):
        people_list = [
            {'name': 'chulsu', 'description': 'Kim Chul-su'},
            {'name': 'yunghui', 'description': 'Lee Young-hui'},
        ]

        # Step.1
        data = { 'peoples': people_list }
        resp = self.client.post("/peoples/signup/", data, follow=True, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        # Step.2
        resp = self.client.get("/peoples/signup/", follow=True, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)

        # Step.3
        resp = self.client.post("/peoples/signup/confirm", follow=True)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
